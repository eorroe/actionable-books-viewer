import json
import re
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Keyword sets with scores
pro_rebase_kw = {
    'rebase is better': 3, 'rebase is the': 2, 'rebase is king': 3, 'always rebase': 3,
    'only rebase': 3, 'prefer rebase': 2, 'i rebase': 2, 'rebase team': 2,
    'rebasing is': 1, 'rebase and merge': 2, 'rebase +': 1, 'rebase before': 1,
    'rebase onto': 2, 'rebase local': 2, 'rebase feature': 2, 'rebase fast': 2,
    'rebase --': 1, 'rebase onto main': 3, 'rebase onto dev': 3, 'linear history': 2,
    'clean history': 2, 'clean commit': 1, 'squash is': 1, 'squash and rebase': 2,
    'ff merge': 2, 'fast forward': 2, 'rebase fast forward': 3, 'rebase is nice': 2,
    'rebase is easier': 2, 'rebase is cleaner': 2, 'rebase is simpler': 2,
    '100% agree': 2, 'agree with': 1, 'totally agree': 2, 'absolutely agree': 2,
    'same side': 1, 'same boat': 1, 'rebase is our friend': 2, 'rebase should not be feared': 3,
    'rebase is the king': 3, 'rebase is king': 3, 'rebase is the way': 2,
    'rebase is awesome': 2, 'rebase is great': 2, 'rebase is best': 2,
    'rebase is my tool': 2, 'rebase is the only way': 3, 'only way to': 1,
}

pro_merge_kw = {
    'prefer merge': 3, 'always merge': 3, 'merge is better': 3, 'merge is safer': 3,
    'merge commits': 2, 'never rebase': 3, 'hate rebase': 3, 'dislike rebase': 3,
    'rebasing is bad': 3, 'rewriting history is bad': 3, 'force push is bad': 3,
    'rebasing sucks': 3, 'rebasing is dangerous': 3, 'merge only': 2, 'never merge': 3,
    'merge is the': 1, 'merge is default': 2, 'merge preserves': 2, 'history is important': 2,
    'raw log': 1, 'forensic': 1, 'security camera': 1, 'git tree': 1, 'not a skyscraper': 1,
    'merge is standard': 2, 'merge is the standard': 3, '99.9%': 1, '99%': 1,
    'rebasing loses': 2, 'rebasing loses information': 3, 'merge retains': 2,
    'merge retains history': 3, 'rebasing is a noob': 3, 'noob trap': 3,
    'rebasing is riskier': 2, 'rebasing is always riskier': 3, 'never touch shared': 3,
    'never rebase shared': 3, 'rebasing shared is bad': 3, 'do not rebase shared': 3,
    'merge is simpler': 2, 'merge is easier': 2, 'merge is safer': 2,
}

nuanced_kw = {
    'depends on': 2, 'both have': 2, 'different tools': 2, 'different use cases': 2,
    'it depends': 2, 'context matters': 2, 'situations where': 1, 'tradeoff': 2,
    'trade-off': 2, 'pros and cons': 2, 'use case': 1, 'rebase for': 1, 'merge for': 1,
    'rebase in some': 1, 'merge in some': 1, 'both are': 1, 'each have': 1,
    'their own': 1, 'appropriate for': 1, 'different jobs': 2, 'different purposes': 2,
    'different sides': 2, 'co-exist': 1, 'complementary': 2, 'toolbox': 1,
    'as usual': 1, 'it depends on the': 2, 'rebase when': 1, 'merge when': 1,
    'rebase if': 1, 'merge if': 1, 'rebase for feature': 2, 'merge for shared': 2,
    'rebase for local': 2, 'merge for public': 2, 'rebase for private': 2,
}

practical_kw = {
    'git pull': 1, 'git commit': 1, 'git merge': 1, 'git rebase': 1, 'git push': 1,
    'git fetch': 1, 'git checkout': 1, 'git branch': 1, 'workflow': 1, 'ci ': 1,
    'cd ': 1, 'pipeline': 1, 'github': 1, 'gitlab': 1, 'bitbucket': 1, 'azure': 1,
    'pr ': 1, 'mr ': 1, 'pull request': 1, 'merge request': 1, 'feature branch': 1,
    'main branch': 1, 'master branch': 1, 'dev branch': 1, 'trunk': 1, 'conflict': 1,
    'force push': 1, '--squash': 2, '--ff-only': 2, '--no-ff': 2, 'rebase --': 1,
    'merge --': 1, 'squash': 1, 'ff merge': 2, 'fast forward': 2, 'branch protection': 2,
    'monorepo': 1, 'trunk based': 2, 'gitflow': 1, 'github flow': 2, 'gitlab flow': 2,
    'rebase --interactive': 2, 'git rebase -i': 2, 'git pull --rebase': 2,
    'git merge --squash': 2, 'git merge --no-ff': 2, 'git merge --ff-only': 2,
    'force-with-lease': 2, 'force push --with-lease': 2, 'git push --force': 1,
    'git push -f': 1, 'reflog': 1, 'bisect': 1, 'cherry-pick': 1,
    'gerrit': 1, 'reviewboard': 1, 'azure devops': 2, 'git extensions': 1,
}

review_kw = {
    'review': 1, 'comments on': 1, 'approval': 1, 'changes since': 2,
    'reviewer': 1, 'approve': 1, 'code review': 2, 'pr review': 2, 'mr review': 2,
    'review process': 2, 'approval process': 2, 'merge conflict resolution': 2,
    'conflict resolution': 1, 'review feedback': 1, 're-review': 2,
    'changes since your last': 3, 'changes since last review': 3,
    'reset the times': 2, 'commit hashes change': 2, 'hash change': 1,
    'github review': 2, 'gitlab review': 2, 'bitbucket review': 2,
    'pull request': 1, 'merge request': 1, 'pr ': 1, 'mr ': 1,
}

def score_comment(body):
    body_lower = body.lower()
    scores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    
    # Short reactions (length-based)
    if len(body_lower) < 50 and '?' not in body_lower:
        scores[7] = 2
    
    # Questions
    if '?' in body_lower and len(body_lower) < 500:
        scores[6] = 1
    
    # Pro-rebase keywords
    for kw, pts in pro_rebase_kw.items():
        if kw in body_lower:
            scores[1] += pts
    
    # Pro-merge keywords
    for kw, pts in pro_merge_kw.items():
        if kw in body_lower:
            scores[2] += pts
    
    # Nuanced keywords
    for kw, pts in nuanced_kw.items():
        if kw in body_lower:
            scores[3] += pts
    
    # Practical keywords
    for kw, pts in practical_kw.items():
        if kw in body_lower:
            scores[4] += pts
    
    # Review keywords
    for kw, pts in review_kw.items():
        if kw in body_lower:
            scores[5] += pts
    
    return scores

def classify(c):
    body = c['body']
    scores = score_comment(body)
    
    # Priority order: questions, short reactions, then highest score
    # But questions only if clearly a question
    if scores[6] >= 2 and '?' in body:
        return 6
    
    if scores[7] >= 2 and len(body) < 50:
        return 7
    
    # Find max score
    max_score = max(scores.values())
    if max_score == 0:
        return 3  # Default to nuanced
    
    # Get categories with max score
    max_cats = [k for k, v in scores.items() if v == max_score and k not in (6, 7)]
    
    if not max_cats:
        return 3
    
    # Priority: Pro-Rebase > Pro-Merge > Nuanced > Practical > Code Review
    priority = [1, 2, 3, 4, 5]
    for p in priority:
        if p in max_cats:
            return p
    
    return max_cats[0]

results = {c['id']: classify(c) for c in real}

# Count
counts = defaultdict(int)
scores_sum = defaultdict(int)
names = {1: 'Pro-Rebase/Agreement', 2: 'Pro-Merge/Disagreement', 3: 'Nuanced/Balanced', 
         4: 'Practical Workflows', 5: 'Code Review/Collaboration', 6: 'Questions', 7: 'Short Reactions'}

for c in real:
    cl = results[c['id']]
    counts[cl] += 1
    scores_sum[cl] += c['score']

print("Cluster distribution:")
total = 0
for i in range(1, 8):
    print(f"  {names[i]}: {counts[i]} comments, {scores_sum[i]} upvotes")
    total += counts[i]
print(f"Total: {total}")

# Show some examples from each cluster
for i in range(1, 8):
    print(f"\n--- {names[i]} examples ---")
    examples = [c for c in real if results[c['id']] == i][:3]
    for c in examples:
        print(f"  {c['author']} ({c['score']}): {c['body'][:120]}")
