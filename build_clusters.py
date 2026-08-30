import json

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Build a lookup by ID
by_id = {c['id']: c for c in real}

# Print all IDs in order so I can reference them
for i, c in enumerate(real, 1):
    print(f"{i:03d}|{c['id']}|{c['score']:4d}|{c['author']}")
