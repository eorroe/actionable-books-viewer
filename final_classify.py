import json
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Comprehensive keyword sets
pro_rebase = [
    'rebase is better', 'rebase is the', 'rebase is king', 'always rebase', 'only rebase',
    'prefer rebase', 'i rebase', 'rebase team', 'rebasing is', 'rebase and merge',
    'rebase +', 'rebase before', 'rebase onto', 'rebase local', 'rebase feature',
    'rebase fast', 'rebase --', 'rebase onto main', 'rebase onto dev', 'linear history',
    'clean history', 'clean commit', 'squash is', 'squash and rebase', 'ff merge',
    'fast forward', 'rebase fast forward', 'rebase is nice', 'rebase is easier',
    'rebase is cleaner', 'rebase is simpler', '100% agree', 'agree with', 'totally agree',
    'absolutely agree', 'same side', 'same boat', 'rebase is our friend',
    'rebase should not be feared', 'rebase is the only way', 'only way to',
    'rebase is the way', 'rebase is awesome', 'rebase is great', 'rebase is best',
    'rebase is my tool', 'rebase is the only way', 'rebasing is the king',
    'rebase is king', 'rebase all the time', 'rebase is my go',
    'never go back', 'never looked back', 'switched to rebase', 'only using rebase',
    'strictly rebase', 'rebase only', 'rebase everything', 'rebase all',
    'rebase is preferred', 'rebase is preferred for', 'rebase is preferred when',
]

pro_merge = [
    'prefer merge', 'always merge', 'merge is better', 'merge is safer', 'merge commits',
    'never rebase', 'hate rebase', 'dislike rebase', 'rebasing is bad', 'rewriting history is bad',
    'force push is bad', 'rebasing sucks', 'rebasing is dangerous', 'merge only', 'never merge',
    'merge is the', 'merge is default', 'merge preserves', 'history is important', 'raw log',
    'forensic', 'security camera', 'git tree', 'not a skyscraper', 'merge is standard',
    'merge is the standard', '99.9%', '99%', 'rebasing loses', 'rebasing loses information',
    'merge retains', 'merge retains history', 'rebasing is a noob', 'noob trap',
    'rebasing is riskier', 'rebasing is always riskier', 'never touch shared',
    'never rebase shared', 'rebasing shared is bad', 'do not rebase shared',
    'merge is simpler', 'merge is easier', 'merge is safer', 'merge is the default',
    'merge is always', 'merge is the standard way', 'merge covers', 'merge is safe',
    'merge is the safe', 'merge is the safer', 'merge is the better',
    'squash merge', 'squash and merge', 'squash when merging', 'merge squash',
]

nuanced = [
    'depends on', 'both have', 'different tools', 'different use cases', 'it depends',
    'context matters', 'situations where', 'tradeoff', 'trade-off', 'pros and cons',
    'use case', 'rebase for', 'merge for', 'rebase in some', 'merge in some',
    'both are', 'each have', 'their own', 'appropriate for', 'different jobs',
    'different purposes', 'different sides', 'co-exist', 'complementary', 'toolbox',
    'as usual', 'it depends on the', 'rebase when', 'merge when', 'rebase if',
    'merge if', 'rebase for feature', 'merge for shared', 'rebase for local',
    'merge for public', 'rebase for private', 'merge for shared branch',
    'rebase for personal', 'merge for team', 'rebase for solo', 'merge for group',
    'rebase for individual', 'merge for collaborative', 'rebase for own',
    'merge for others', 'rebase for yourself', 'merge for everyone',
    'rebase for private branch', 'merge for public branch', 'rebase for feature branch',
    'merge for main branch', 'rebase for dev branch', 'merge for master branch',
]

practical = [
    'git pull', 'git commit', 'git merge', 'git rebase', 'git push', 'git fetch',
    'git checkout', 'git branch', 'workflow', 'ci ', 'cd ', 'pipeline', 'github',
    'gitlab', 'bitbucket', 'azure', 'pr ', 'mr ', 'pull request', 'merge request',
    'feature branch', 'main branch', 'master branch', 'dev branch', 'trunk',
    'conflict', 'force push', '--squash', '--ff-only', '--no-ff', 'rebase --',
    'merge --', 'squash', 'ff merge', 'fast forward', 'branch protection', 'monorepo',
    'trunk based', 'gitflow', 'github flow', 'gitlab flow', 'rebase --interactive',
    'git rebase -i', 'git pull --rebase', 'git merge --squash', 'git merge --no-ff',
    'git merge --ff-only', 'force-with-lease', 'force push --with-lease',
    'git push --force', 'git push -f', 'reflog', 'bisect', 'cherry-pick',
    'gerrit', 'reviewboard', 'azure devops', 'git extensions', 'tbd',
    'trunk-based development', 'feature flag', 'short-lived branch',
    'long-lived branch', 'merge train', 'merge queue', 'rebase onto',
    'merge into', 'squash merge', 'squash and merge', 'rebase and merge',
    'rebase then merge', 'merge then rebase', 'rebase first', 'merge first',
]

review = [
    'review', 'comments on', 'approval', 'changes since', 'reviewer', 'approve',
    'code review', 'pr review', 'mr review', 'review process', 'approval process',
    'merge conflict resolution', 'conflict resolution', 'review feedback',
    're-review', 'changes since your last', 'changes since last review',
    'reset the times', 'commit hashes change', 'hash change',
    'github review', 'gitlab review', 'bitbucket review',
    'pull request', 'merge request',
]

def classify(c):
    body = c['body'].lower()
    score = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    
    # Questions: has ? and is not just rhetorical
    if '?' in body and len(body) < 500:
        score[6] += 2
    
    # Short reactions
    if len(body) < 60 and '?' not in body:
        score[7] += 3
    
    # Keyword scoring
    for kw in pro_rebase:
        if kw in body:
            score[1] += 2
    
    for kw in pro_merge:
        if kw in body:
            score[2] += 2
    
    for kw in nuanced:
        if kw in body:
            score[3] += 2
    
    for kw in practical:
        if kw in body:
            score[4] += 1
    
    for kw in review:
        if kw in body:
            score[5] += 2
    
    # Boost review score if multiple review keywords
    review_count = sum(1 for kw in review if kw in body)
    if review_count >= 3:
        score[5] += 3
    
    # Boost practical score if multiple practical keywords
    practical_count = sum(1 for kw in practical if kw in body)
    if practical_count >= 4:
        score[4] += 3
    
    # Priority: questions and short reactions first, then highest score
    if score[6] >= 2:
        return 6
    
    if score[7] >= 3:
        return 7
    
    max_score = max(score.values())
    if max_score == 0:
        return 3  # Default to nuanced
    
    max_cats = [k for k, v in score.items() if v == max_score and k not in (6, 7)]
    if not max_cats:
        return 3
    
    # Priority order: Pro-Rebase > Pro-Merge > Nuanced > Practical > Code Review
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

# Verify top comments are in reasonable clusters
print("\nTop 10 comments by score:")
top10 = sorted(real, key=lambda x: x['score'], reverse=True)[:10]
for c in top10:
    cl = results[c['id']]
    print(f"  [{cl}] {c['author']} ({c['score']}): {c['body'][:100]}")
