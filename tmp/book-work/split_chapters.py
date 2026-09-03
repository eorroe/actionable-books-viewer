import re
import os

input_path = '/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_82683db9-2987-4e71-b3a9-2b587805f9ea/tmp/book-work/full-text.txt'
output_dir = '/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_82683db9-2987-4e71-b3a9-2b587805f9ea/tmp/book-work/chapters'
os.makedirs(output_dir, exist_ok=True)

with open(input_path, 'r') as f:
    content = f.read()

# Find actual chapter headers in the body (not TOC)
# Pattern: CHAPTER X\n followed by title
pattern = r'\n--- Page \d+ ---\n.*?\nCHAPTER (\d+)\n(.+?)(?=\n--- Page \d+ ---\n|\Z)'
matches = list(re.finditer(pattern, content, re.DOTALL))

if not matches:
    # Fallback: look for CHAPTER followed by number
    pattern = r'CHAPTER (\d+)\n([^\n]+)'
    matches = list(re.finditer(pattern, content))

chapter_names = [
    'Introduction',
    'Desire',
    'Faith',
    'Auto-Suggestion',
    'Specialized-Knowledge',
    'Imagination',
    'Organized-Planning',
    'Decision',
    'Persistence',
    'Power-of-the-Master-Mind',
    'The-Mystery-of-Sex-Transmutation',
    'The-Subconscious-Mind',
    'The-Brain',
    'The-Sixth-Sense',
    'How-to-Outwit-the-Six-Ghosts-of-Fear'
]

print(f'Found {len(matches)} chapters')

# Get line numbers for each chapter
with open(input_path, 'r') as f:
    lines = f.readlines()

chapter_lines = []
for i, line in enumerate(lines):
    if re.match(r'^CHAPTER \d+$', line.strip()):
        # Verify next line is title (not dots)
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line and not re.match(r'^\.+', next_line):
                chapter_lines.append(i)

print(f'Chapter start lines: {chapter_lines}')

for idx, start in enumerate(chapter_lines):
    end = chapter_lines[idx + 1] if idx + 1 < len(chapter_lines) else len(lines)
    chapter_text = ''.join(lines[start:end])
    filename = f'{idx+1:02d}_{chapter_names[idx]}.txt'
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(chapter_text)
    print(f'Created {filename} ({end - start} lines)')

print(f'\nTotal chapters created: {len(chapter_lines)}')
