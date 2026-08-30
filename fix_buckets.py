import json
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Read existing report
with open('thread_1nugs0l_analysis.md', 'r') as f:
    report = f.read()

# Find the TOP COMMENTS section
top_start = report.find('# TOP COMMENTS')
original_start = report.find('# ORIGINAL POST')

# Sort comments by score
sorted_comments = sorted(real, key=lambda x: x['score'], reverse=True)

# Proper bucket ranges (non-overlapping)
buckets = [
    (200, 299, '200+'),
    (100, 199, '100+'),
    (90, 99, '90+'),
    (80, 89, '80+'),
    (70, 79, '70+'),
    (60, 69, '60+'),
    (50, 59, '50+'),
    (40, 49, '40+'),
    (30, 39, '30+'),
    (20, 29, '20+'),
    (10, 19, '10+'),
]

used_scores = set()
top_comments = []
for low, high, label in buckets:
    candidates = [c for c in sorted_comments if low <= c['score'] <= high and c['score'] not in used_scores]
    if candidates:
        top = candidates[0]
        used_scores.add(top['score'])
        url = f"https://www.reddit.com{top['permalink']}"
        top_comments.append(f"## {label}\n\nu/{top['author']}\n\n\"{top['body']}\" ({top['score']} Upvotes) - {url}\n")

# Replace TOP COMMENTS section
new_report = report[:top_start] + '# TOP COMMENTS\n\n' + '\n'.join(top_comments) + '\n\n' + report[original_start:]

with open('thread_1nugs0l_analysis.md', 'w') as f:
    f.write(new_report)

print("Fixed TOP COMMENTS buckets")
print(f"Top comments included: {len(top_comments)}")
for low, high, label in buckets:
    candidates = [c for c in sorted_comments if low <= c['score'] <= high]
    if candidates:
        top = max(candidates, key=lambda x: x['score'])
        print(f"  {label}: {top['author']} ({top['score']})")
