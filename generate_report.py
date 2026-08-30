import json
import re
from collections import defaultdict, Counter
from datetime import datetime

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

with open('data/1nugs0l/initial_raw.json') as f:
    initial = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Classification (same as before)
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
    
    if '?' in body and len(body) < 500:
        score[6] += 2
    
    if len(body) < 60 and '?' not in body:
        score[7] += 3
    
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
    
    review_count = sum(1 for kw in review if kw in body)
    if review_count >= 3:
        score[5] += 3
    
    practical_count = sum(1 for kw in practical if kw in body)
    if practical_count >= 4:
        score[4] += 3
    
    if score[6] >= 2:
        return 6
    
    if score[7] >= 3:
        return 7
    
    max_score = max(score.values())
    if max_score == 0:
        return 3
    
    max_cats = [k for k, v in score.items() if v == max_score and k not in (6, 7)]
    if not max_cats:
        return 3
    
    priority = [1, 2, 3, 4, 5]
    for p in priority:
        if p in max_cats:
            return p
    
    return max_cats[0]

cluster_names = {
    1: 'Rebase Advocacy',
    2: 'Merge Advocacy', 
    3: 'Balanced Perspective',
    4: 'Practical Git Workflows',
    5: 'Code Review & Collaboration',
    6: 'Questions',
    7: 'Brief Reactions & Humor'
}

results = {c['id']: classify(c) for c in real}

# Post-process: fix known misclassifications
results['nh0yja4'] = 2  # FlipperBumperKickout main comment - pro-merge
results['nh0xx1i'] = 2  # homezlice - pro-merge
results['nh0zlvw'] = 2  # ars0nisfun - pro-merge

# Count clusters
counts = defaultdict(int)
scores_sum = defaultdict(int)
cluster_comments = defaultdict(list)

for c in real:
    cl = results[c['id']]
    counts[cl] += 1
    scores_sum[cl] += c['score']
    cluster_comments[cl].append(c)

# Sentiment analysis
positive_words = ['agree', 'love', 'great', 'awesome', 'best', 'good', 'nice', 'yes', 'totally', 'absolutely', '100%', '💯', '💪', '🥰', '🙌', 'sensei', 'unicorn', 'welcome', 'valid', 'good point']
negative_words = ['disagree', 'hate', 'bad', 'wrong', 'noob', 'trap', 'dangerous', 'risk', 'sucks', 'terrible', 'awful', 'nightmare', 'problem', 'issue', 'confusing', 'annoying', 'hate', 'dislike']
neutral_words = ['depends', 'context', 'situation', 'case', 'both', 'each', 'different', 'tool', 'use', 'workflow']

def get_sentiment(c):
    body = c['body'].lower()
    pos = sum(1 for w in positive_words if w in body)
    neg = sum(1 for w in negative_words if w in body)
    neu = sum(1 for w in neutral_words if w in body)
    
    if pos > neg and pos > neu:
        return 'Positive'
    elif neg > pos and neg > neu:
        return 'Negative'
    else:
        return 'Neutral'

sentiments = [get_sentiment(c) for c in real]
sentiment_counts = Counter(sentiments)
total = len(real)
pos_pct = sentiment_counts.get('Positive', 0) / total * 100
neu_pct = sentiment_counts.get('Neutral', 0) / total * 100
neg_pct = sentiment_counts.get('Negative', 0) / total * 100

# Keyword extraction
all_text = ' '.join(c['body'] for c in real).lower()
stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare', 'ought', 'used', 'it', 'its', 'this', 'that', 'these', 'those', 'a', 'an', 'i', 'you', 'he', 'she', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'who', 'whom', 'whose', 'which', 'what', 'where', 'when', 'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'because', 'but', 'and', 'or', 'if', 'while', 'although', 'though', 'even', 'also', 'then', 'now', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'every', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'don', 'now', 're', 've', 'll', 'd', 'm', 'o', 'ma', 'might', 'much', 'like', 'get', 'got', 'one', 'two', 'make', 'made', 'way', 'thing', 'things', 'something', 'anything', 'everything', 'nothing'}

words = re.findall(r'\b[a-z]{3,}\b', all_text)
word_freq = Counter(words)
keywords = [(w, c) for w, c in word_freq.most_common(50) if w not in stop_words and len(w) > 3]
top_keywords = keywords[:15]

# Post metadata - use flat.json post info or extract from initial_raw
post_data = initial[0]['data']['children'][0]['data']
post_title = post_data['title']
post_author = post_data['author']
post_score = post_data['score']
post_body = post_data['selftext']
post_subreddit = post_data['subreddit']
post_created = datetime.fromtimestamp(post_data['created_utc'])
post_num_comments = post_data['num_comments']

# Generate report
report = []
report.append("# REDDIT POST ANALYSIS\n")

report.append(f"A discussion in r/{post_subreddit} sparked by u/{post_author}'s post titled \"{post_title}\" gathered {post_score} upvotes and {post_num_comments} comments. The author argued that \"Rebase is better then Merge\" and listed four main reasons: avoiding local merge commits, achieving linear history, better CI integration by testing feature branches with the latest dev changes, and the ability to rewrite history for cleaner commits. The post explicitly warned that \"Rebase on shared branches is BAD\" and asked the community for their perspectives on when to use rebase versus merge.\n")

report.append("# REDDIT COMMENTS ANALYSIS\n")

total_comments = 0
total_upvotes = 0

for cl_id in range(1, 8):
    cl_name = cluster_names[cl_id]
    cl_count = counts[cl_id]
    cl_score = scores_sum[cl_id]
    total_comments += cl_count
    total_upvotes += cl_score
    
    report.append(f"## {cl_name} ({cl_count} Comments - {cl_score} Upvotes)\n")
    
    if cl_id == 1:
        report.append("Many commenters agreed with the original post, emphasizing that rebase excels for personal or feature branches where you're the only one working on the code. They highlighted how rebase keeps local history clean, avoids unnecessary merge commits, and makes it easier to test changes against the latest upstream code. As one user put it, \"You use rebase to keep a branch that nobody is pulling from cleanly following its upstream branch.\" Others noted that rebase is particularly valuable for squashing messy work-in-progress commits before merging, with one commenter stating, \"You rewrite your history as part of writing a merge request. That's just basic hygiene!\" The consensus in this group was that rebase is a powerful tool for individual developers who want a tidy commit history.\n")
    elif cl_id == 2:
        report.append("A significant number of commenters pushed back against the pro-rebase stance, arguing that merge is safer and preserves valuable historical context. They warned that rebasing rewrites history, which can cause problems when multiple people work on the same branch or when you need to understand what actually happened during development. One critic wrote, \"Rebase is kind of a noob trap. Rather than learn about git it seems to magically solve your problem. However the force-pushing should be a red flag that it's not ideal.\" Others pointed out that merge commits serve a purpose by showing when and how branches were integrated, with one user noting, \"I care about the immediate history whilst developing a feature\" and preferring to see the full development process preserved.\n")
    elif cl_id == 3:
        report.append("The largest group of commenters took a balanced, context-dependent approach, arguing that both rebase and merge are valid tools for different situations. The top-voted comment in the entire thread (233 upvotes) captured this sentiment well: \"You use rebase to keep a branch that nobody is pulling from cleanly following its upstream branch. You use merge to get those changes into an upstream branch that many people are pulling from.\" Others echoed this, with one writing, \"Rebase is 'better' for a branch that only you are working on. Merge is 'better' for a branch that multiple people are working on.\" This cluster viewed the debate as a false dichotomy, emphasizing that the right choice depends on team size, branch ownership, and workflow requirements.\n")
    elif cl_id == 4:
        report.append("Many commenters shared specific git workflows and commands they use in their daily work. Popular patterns included rebasing feature branches onto the latest main before opening a PR, using \"git merge --squash\" to create a single clean commit on main, and employing \"git pull --rebase\" to keep local branches up to date. One user described their workflow: \"We rebase main branches into feature branches. Subsequently, we merge feature branches onto the main branches.\" Another shared a streamlined approach: \"merge main/master into your feature or rebase your f-b on main; merge squash your feature branch into main. One 'revert' if it's going wrong.\" These practical contributions showed that most teams use a hybrid approach rather than strictly rebasing or merging everything.\n")
    elif cl_id == 5:
        report.append("Several commenters discussed how the choice between rebase and merge affects code reviews and team collaboration. A major concern was that rebasing changes commit hashes, which can break tools like GitHub's \"Changes since your last review\" feature and make it harder for reviewers to track what changed. One reviewer wrote, \"If I am reviewing your PR and you are using a rebase workflow I automatically hate you. It makes it much more difficult to re-review to see if you have actually addressed my comments.\" Others noted that merge conflict resolutions are more visible in merge commits, making it easier for teams to understand how conflicts were resolved. The debate highlighted that code review tools are often built around merge-based workflows, and rebasing can create friction in collaborative environments.\n")
    elif cl_id == 6:
        report.append("A number of commenters asked clarifying questions about specific aspects of rebase and merge workflows. Questions ranged from basic inquiries like \"What's wrong with 'git pull --rebase'?\" to more nuanced ones about how rebase affects git bisect and whether squash commits preserve history. One new developer asked about handling rebase when a PR is already open on a staging branch, seeking advice on conflict resolution strategies. Others sought clarification on corporate workflows, asking how teams handle rebasing when multiple people work on the same feature branch. These questions revealed that many developers are still learning the trade-offs and seeking guidance on best practices.\n")
    elif cl_id == 7:
        report.append("The thread included many short, humorous, and off-topic reactions. Comments like \"BOTH!\", \"Sensei 🥋\", \"Unicorn 🦄\", and \"Yes. It's called a git tree, not a git skyscraper\" added levity to the discussion. Some commenters made jokes about rebasing being a \"noob trap\" or about developers who never rebase being \"unicorns.\" One user quipped, \"After reading all the conversations here, you're all wrong. I'm going to just cherry-pick into main from now on.\" These brief reactions showed that while the topic is serious, many in the git community approach it with humor and a recognition that there's no one-size-fits-all answer.\n")

report.append(f"(Total: {total_comments} Comments - {total_upvotes} Upvotes)\n")

report.append("# TOP COMMENTS\n")

# Sort comments by score
sorted_comments = sorted(real, key=lambda x: x['score'], reverse=True)

# Threshold buckets
buckets = [
    (1000000, '1M+'),
    (900000, '900k+'),
    (800000, '800k+'),
    (700000, '700k+'),
    (600000, '600k+'),
    (500000, '500k+'),
    (400000, '400k+'),
    (300000, '300k+'),
    (200000, '200k+'),
    (100000, '100k+'),
    (90000, '90k+'),
    (80000, '80k+'),
    (70000, '70k+'),
    (60000, '60k+'),
    (50000, '50k+'),
    (40000, '40k+'),
    (30000, '30k+'),
    (20000, '20k+'),
    (10000, '10k+'),
    (9000, '9k+'),
    (8000, '8k+'),
    (7000, '7k+'),
    (6000, '6k+'),
    (5000, '5k+'),
    (4000, '4k+'),
    (3000, '3k+'),
    (2000, '2k+'),
    (1000, '1k+'),
    (900, '900+'),
    (800, '800+'),
    (700, '700+'),
    (600, '600+'),
    (500, '500+'),
    (400, '400+'),
    (300, '300+'),
    (200, '200+'),
    (100, '100+'),
    (90, '90+'),
    (80, '80+'),
    (70, '70+'),
    (60, '60+'),
    (50, '50+'),
    (40, '40+'),
    (30, '30+'),
    (20, '20+'),
    (10, '10+'),
]

used_scores = set()
for threshold, label in buckets:
    candidates = [c for c in sorted_comments if threshold <= c['score'] < threshold + 1000 and c['score'] not in used_scores]
    if candidates:
        top = candidates[0]
        used_scores.add(top['score'])
        url = f"https://www.reddit.com{top['permalink']}"
        report.append(f"## {label}\n")
        report.append(f"u/{top['author']}\n")
        report.append(f'"{top["body"]}" ({top["score"]} Upvotes) - {url}\n')

report.append("\n# ORIGINAL POST\n")
report.append(f'"{post_title}"\n\n')
report.append(f'"{post_body}"\n')

# Write report
with open('thread_1nugs0l_analysis.md', 'w') as f:
    f.write('\n'.join(report))

print("Report generated: thread_1nugs0l_analysis.md")
print(f"Total comments: {total_comments}")
print(f"Total upvotes: {total_upvotes}")
print(f"Sentiment: {pos_pct:.1f}% Positive, {neu_pct:.1f}% Neutral, {neg_pct:.1f}% Negative")
print(f"Top keywords: {', '.join(w for w, c in top_keywords)}")
