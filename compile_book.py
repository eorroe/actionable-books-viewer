#!/usr/bin/env python3
import os
import re

BASE_DIR = "R-BUILD-RUN-BUSINESS-SMART"
TEMPLATE_PATH = "/home/agent_d1f179cd-cdae-431e-82db-56c79d56bcc4/.kilocode/skills/book-to-action/book-template.md"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Read template
template = read_file(TEMPLATE_PATH)

# Read all chapter files
chapter_files = sorted([f for f in os.listdir(BASE_DIR) if f.startswith('chapter_') and f.endswith('.md')])

# Build glossary from all chapters
all_terms = {}
for cf in chapter_files:
    content = read_file(os.path.join(BASE_DIR, cf))
    in_key_terms = False
    for line in content.split('\n'):
        if '**Key Terms:**' in line:
            in_key_terms = True
            continue
        if in_key_terms:
            if line.startswith('### ') or line.startswith('---'):
                in_key_terms = False
                continue
            if line.strip().startswith('- '):
                term_line = line.strip()[2:]
                if ':' in term_line:
                    term, definition = term_line.split(':', 1)
                    term = term.strip()
                    definition = definition.strip()
                    if term not in all_terms:
                        all_terms[term] = {'definition': definition, 'pages': []}
                    chapter_num = cf.split('_')[1]
                    all_terms[term]['pages'].append(chapter_num)

sorted_terms = sorted(all_terms.items())

glossary_md = "|Term|Definition|Index Pages|\n|----|----------|-----------|\n"
for term, data in sorted_terms:
    pages = ','.join(data['pages'])
    glossary_md += f"|{term}|{data['definition']}|{pages}|\n"

lessons_md = ""
for cf in chapter_files:
    content = read_file(os.path.join(BASE_DIR, cf))
    chapter_title = ""
    for line in content.split('\n'):
        if line.startswith('# '):
            chapter_title = line.replace('# ', '').strip()
            break
    
    lessons = re.split(r'### Lesson \d+:', content)
    if len(lessons) > 1:
        for i, lesson in enumerate(lessons[1:], 1):
            lines = lesson.strip().split('\n')
            lesson_title = lines[0].strip() if lines else f"Lesson {i}"
            
            context = ""
            examples = []
            steps = []
            best_practices = []
            keep_in_mind = []
            security_notes = []
            pitfalls = []
            
            current_section = None
            for line in lines[1:]:
                line_stripped = line.strip()
                if line_stripped.startswith('**Context:**'):
                    current_section = 'context'
                    context = line_stripped.replace('**Context:**', '').strip()
                elif line_stripped.startswith('**Examples:**'):
                    current_section = 'examples'
                elif line_stripped.startswith('**Steps:**'):
                    current_section = 'steps'
                elif line_stripped.startswith('**Best Practices:**'):
                    current_section = 'best_practices'
                elif line_stripped.startswith('**Keep In Mind:**'):
                    current_section = 'keep_in_mind'
                elif line_stripped.startswith('**Security'):
                    current_section = 'security'
                elif line_stripped.startswith('**Common Pitfalls:**'):
                    current_section = 'pitfalls'
                elif line_stripped.startswith('**Key Terms:**'):
                    current_section = None
                elif line_stripped.startswith('- ') or line_stripped.startswith(('1. ', '2. ', '3. ', '4. ', '5. ')):
                    if current_section == 'examples':
                        examples.append(line_stripped[2:])
                    elif current_section == 'steps':
                        steps.append(line_stripped)
                    elif current_section == 'best_practices':
                        best_practices.append(line_stripped[2:])
                    elif current_section == 'keep_in_mind':
                        keep_in_mind.append(line_stripped[2:])
                    elif current_section == 'security':
                        security_notes.append(line_stripped[2:])
                    elif current_section == 'pitfalls':
                        pitfalls.append(line_stripped[2:])
            
            lesson_md = f"### {lesson_title}\n\n"
            if context:
                lesson_md += f"**Context:** {context}\n\n"
            
            if examples:
                lesson_md += "#### Examples\n\n"
                for ex in examples[:3]:
                    lesson_md += f"##### Example: {ex[:60]}...\n\n{ex}\n\n"
            
            if steps:
                lesson_md += "#### Steps\n\n"
                for step in steps:
                    lesson_md += f"{step}\n"
                lesson_md += "\n"
            
            if best_practices:
                lesson_md += "#### Best Practices\n\n"
                for bp in best_practices[:4]:
                    lesson_md += f"- {bp}\n"
                lesson_md += "\n"
            
            if keep_in_mind:
                lesson_md += "#### Keep In Mind\n\n"
                for kim in keep_in_mind[:2]:
                    lesson_md += f"- {kim}\n"
                lesson_md += "\n"
            
            if security_notes:
                lesson_md += "#### Security & Safety Notes\n\n"
                for sn in security_notes:
                    lesson_md += f"- {sn}\n"
                lesson_md += "\n"
            else:
                lesson_md += "#### Security & Safety Notes\n\n- No specific security or safety concerns apply to this lesson.\n\n"
            
            if pitfalls:
                lesson_md += "#### Common Pitfalls\n\n"
                for pit in pitfalls[:2]:
                    if '**Problem:**' in pit:
                        parts = pit.split('**Solution:**')
                        if len(parts) == 2:
                            lesson_md += f"- **Problem:** {parts[0].replace('**Problem:**', '').strip()}\n"
                            lesson_md += f"  **Solution:** {parts[1].strip()}\n\n"
            
            lessons_md += lesson_md

book_md = f"""# Rework

## Overview

Rework is a practical business manifesto by 37signals that challenges conventional wisdom about what it takes to build and run a successful company. Drawing from over a decade of real operating experience through multiple economic cycles, the authors argue that most business "requirements"—massive funding, large teams, five-year plans, and workaholic culture—are optional. Instead, they advocate for staying small, bootstrapping, launching quickly, and building products that solve real problems with less overhead than most people think is possible.

## When to Follow Book Teachings

- When starting or running a small business, bootstrapped startup, or side project and want to avoid unnecessary overhead
- When you feel pressure to grow headcount, raise funding, or adopt traditional business rituals that don't fit your situation
- When you need practical, experience-tested counterpoints to conventional business advice about planning, hiring, and productivity

## Lessons From Book

{lessons_md}

## Glossary / Index

{glossary_md}
"""

write_file(os.path.join(BASE_DIR, "BOOK.md"), book_md)
print(f"BOOK.md created successfully with {len(sorted_terms)} glossary terms and lessons from {len(chapter_files)} chapters.")
