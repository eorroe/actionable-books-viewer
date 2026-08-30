import json
import re

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Pro-rebase keywords
pro_rebase_keywords = ['rebase is better', 'rebase is the', 'rebase is king', 'always rebase', 'only rebase', 'prefer rebase', 'i rebase', 'rebase team', 'rebasing is', 'rebase and merge', 'rebase +', 'rebase before', 'rebase onto', 'rebase local', 'rebase feature', 'rebase fast', 'rebase --']
pro_merge_keywords = ['prefer merge', 'always merge', 'merge is better', 'merge is safer', 'merge commits', 'never rebase', 'hate rebase', 'dislike rebase', 'rebasing is bad', 'rewriting history is bad', 'force push is bad', 'rebasing sucks', 'rebasing is dangerous', 'merge only', 'never merge']
nuanced_keywords = ['depends on', 'both have', 'different tools', 'different use cases', 'it depends', 'context matters', 'situations where', 'tradeoff', 'trade-off', 'pros and cons', 'use case', 'use-case', 'rebase for', 'merge for']
practical_keywords = ['git pull', 'git commit', 'git merge', 'git rebase', 'git push', 'git fetch', 'git checkout', 'git branch', 'workflow', 'ci', 'cd', 'pipeline', 'github', 'gitlab', 'bitbucket', 'azure', 'pr ', 'mr ', 'pull request', 'merge request', 'feature branch', 'main branch', 'master branch', 'dev branch', 'trunk', 'conflict', 'force push', '--squash', '--ff-only', '--no-ff', 'rebase --', 'merge --', 'squash']
review_keywords = ['review', 'pr ', 'mr ', 'comment', 'github', 'gitlab', 'bitbucket', 'approval', 'changes since', 'reviewer', 'approve']
question_keywords = ['?', 'how do', 'how does', 'why do', 'why is', 'what is', 'what are', 'when do', 'can you', 'could you', 'is it', 'does it', 'do you', 'i am not', "i don't", 'i have a', 'question']

def classify(comment):
    body = comment['body'].lower()
    author = comment['author']
    
    # Check for humor/short reactions first
    if len(body) < 50 and not any(k in body for k in question_keywords):
        if any(word in body for word in ['lol', 'haha', '😂', '🤣', '🤪', '🦄', '🥋', '💪', '👌', '🙌', '🥰', '😎', 'sensei', 'unicorn', 'both!', 'yep', 'nope', 'agreed', 'agree', 'yes!', 'no!']):
            return 'Short Reactions'
    
    # Check for questions
    if '?' in body and len(body) < 300:
        # Count question marks
        q_count = body.count('?')
        if q_count >= 1:
            return 'Questions'
    
    # Check for code review specific
    if any(k in body for k in review_keywords):
        return 'Code Review & Tooling'
    
    # Check for practical workflow
    if any(k in body for k in practical_keywords):
        return 'Practical Workflows'
    
    # Check for pro-rebase
    if any(k in body for k in pro_rebase_keywords):
        return 'Pro-Rebase'
    
    # Check for pro-merge
    if any(k in body for k in pro_merge_keywords):
        return 'Pro-Merge'
    
    # Check for nuanced
    if any(k in body for k in nuanced_keywords):
        return 'Nuanced Views'
    
    # Default based on length and content
    if len(body) > 200:
        return 'Practical Workflows'
    
    return 'Other'

clusters = {}
for c in real:
    clusters[c['id']] = classify(c)

# Count
from collections import defaultdict
counts = defaultdict(int)
scores = defaultdict(int)
for c in real:
    cl = clusters[c['id']]
    counts[cl] += 1
    scores[cl] += c['score']

print("Cluster distribution:")
total = 0
for cl in sorted(counts.keys()):
    print(f"  {cl}: {counts[cl]} comments, {scores[cl]} upvotes")
    total += counts[cl]
print(f"Total: {total}")

# Print unassigned if any
