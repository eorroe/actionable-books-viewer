import json
import re
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Define cluster keywords
pro_rebase = ['rebase is better', 'rebase is the', 'rebase is king', 'always rebase', 'only rebase', 
              'prefer rebase', 'i rebase', 'rebase team', 'rebasing is', 'rebase and merge', 
              'rebase +', 'rebase before', 'rebase onto', 'rebase local', 'rebase feature', 
              'rebase fast', 'rebase --', 'rebase onto main', 'rebase onto dev', 'linear history',
              'clean history', 'clean commit', 'squash is', 'squash and rebase', 'ff merge']

pro_merge = ['prefer merge', 'always merge', 'merge is better', 'merge is safer', 'merge commits',
             'never rebase', 'hate rebase', 'dislike rebase', 'rebasing is bad', 'rewriting history is bad',
             'force push is bad', 'rebasing sucks', 'rebasing is dangerous', 'merge only', 'never merge',
             'merge is the', 'merge is default', 'merge preserves', 'history is important', 'raw log']

nuanced = ['depends on', 'both have', 'different tools', 'different use cases', 'it depends',
           'context matters', 'situations where', 'tradeoff', 'trade-off', 'pros and cons',
           'use case', 'rebase for', 'merge for', 'rebase in some', 'merge in some',
           'both are', 'each have', 'their own', 'appropriate for']

practical = ['git pull', 'git commit', 'git merge', 'git rebase', 'git push', 'git fetch',
             'git checkout', 'git branch', 'workflow', 'ci ', 'cd ', 'pipeline', 'github',
             'gitlab', 'bitbucket', 'azure', 'pr ', 'mr ', 'pull request', 'merge request',
             'feature branch', 'main branch', 'master branch', 'dev branch', 'trunk',
             'conflict', 'force push', '--squash', '--ff-only', '--no-ff', 'rebase --',
             'merge --', 'squash', 'ff merge', 'fast forward', 'branch protection', 'monorepo',
             'trunk based', 'gitflow', 'github flow', 'gitlab flow']

review = ['review', 'comments on', 'approval', 'changes since', 'reviewer', 'approve',
          'code review', 'pr review', 'mr review', 'review process', 'approval process',
          'merge conflict resolution', 'conflict resolution', 'review feedback']

question_words = ['why do', 'why is', 'what is', 'what are', 'how do', 'how does', 'when do',
                  'can you', 'could you', 'is it', 'does it', 'do you', 'i am not', 
                  "i don't", 'i have a', 'question', '?', 'help me', 'explain', 'clarify']

def classify(c):
    body = c['body'].lower()
    author = c['author']
    score = c['score']
    
    # Short reactions (very short, no questions, mostly emojis or one word)
    if len(body) < 60:
        if '?' not in body:
            return 7  # Short Reactions
    
    # Questions (has question mark and not just rhetorical)
    if '?' in body and len(body) < 500:
        q_count = body.count('?')
        if q_count >= 1:
            # Check if it's primarily a question
            question_ratio = sum(1 for w in question_words if w in body)
            if question_ratio >= 1:
                return 6
    
    # Code review specific
    review_score = sum(1 for w in review if w in body)
    if review_score >= 2:
        return 5
    
    # Practical workflow
    practical_score = sum(1 for w in practical if w in body)
    if practical_score >= 3:
        return 4
    
    # Pro-rebase
    pro_rebase_score = sum(1 for w in pro_rebase if w in body)
    if pro_rebase_score >= 1:
        return 1
    
    # Pro-merge
    pro_merge_score = sum(1 for w in pro_merge if w in body)
    if pro_merge_score >= 1:
        return 2
    
    # Nuanced
    nuanced_score = sum(1 for w in nuanced if w in body)
    if nuanced_score >= 1:
        return 3
    
    # Default based on length
    if len(body) > 300:
        return 4  # Practical
    
    return 3  # Default to nuanced

# Classify all
results = {c['id']: classify(c) for c in real}

# Count
counts = defaultdict(int)
scores = defaultdict(int)
names = {1: 'Pro-Rebase/Agreement', 2: 'Pro-Merge/Disagreement', 3: 'Nuanced/Balanced', 
         4: 'Practical Workflows', 5: 'Code Review/Collaboration', 6: 'Questions', 7: 'Short Reactions'}

for c in real:
    cl = results[c['id']]
    counts[cl] += 1
    scores[cl] += c['score']

print("Cluster distribution:")
total = 0
for i in range(1, 8):
    print(f"  {names[i]}: {counts[i]} comments, {scores[i]} upvotes")
    total += counts[i]
print(f"Total: {total}")

# Show some examples from each cluster
for i in range(1, 8):
    print(f"\n--- {names[i]} examples ---")
    examples = [c for c in real if results[c['id']] == i][:3]
    for c in examples:
        print(f"  {c['author']}: {c['body'][:120]}")
