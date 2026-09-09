---
name: book-to-action
description: Create Book Action Markdown File Based Of YouTube Video Book
---

# Requirements / Mandatory
1. Use powershell "Get-ChildItem" or "grep" never "glob" to find files.
2. Must use PyPDF2 library to parse PDFs. (Install if not installed)
3. Only use sub agents and edit tools or powershell to update ambiguities found.

## Tool Calls
1. Avoid any use of '&&' when running shell commands as it usually fails. Just execute commands sequentially.
2. Use write tool to create BOOK.md.

## Using Agents
1. All tool calls must run using sub agents.
2. Each agent must only write to 1 file (multiple writes but only ever 1 file).
3. Agents may read from multiple files but never write to more than 1 file.
4. Must never with no exception perform any tool call like reads, edits or updates on Main agent.
5. Even small edits like 1 line of code changes must run on sub agent separate from Main Agent.
6. Only use Main Agent for communicating and orchestrating with sub agents and communicating with user.

## Created BOOK.md Files
1. All Books must follow and have a minium of all sections of the "book-template.md" file. Use the provided template exactly as provided. Never create own template.
2. Only 1 sub agent must write the 1 BOOK.md file.
3. All Glossary / Index must be sorted alphabetically.

# Expected Prompt Arguments
1. Single PDF file
2. Directory of PDF files
3. Text File With List of PDF files
4. Text File With Text To Convert To Book

# Naming Book Directory
1. Use Book Name Title Case Initials as prefix
2. Use actionable text derived from pdf or pdf description for 2nd part / rest of book name (suffix) using "TEXT-TEXT-TEXT" convention

Examples:

When Book Name: BookTitle

Final Book Name: BT-TEXT-TEXT-TEXT


# Agent Mode Classification

Before processing, classify the source material into one of two modes:

## Mode A: Literary-Analysis / Narrative / Thematic Books

Books whose value comes from cross-chapter patterns, character arcs, thematic throughlines, or narrative synthesis.

Examples:
- Novels, memoirs, biographies, essays
- Self-help books built around a central thesis
- Philosophy or psychology books with unifying arguments
- Any book where chapters are interdependent and must be understood together

**Rule: Use a single shared-context agent for the entire book.**

Rationale:
- Thematic synthesis requires seeing the whole work.
- Character arcs and argument development span multiple chapters.
- A glossary/index must be built from the complete text.
- Isolated chapter context risks losing throughlines and producing disjointed output.
- Merge overhead from multiple chapter agents usually exceeds any parallelization benefit.

Workflow for Mode A:
1. Extract full text from PDF.
2. Analyze the complete work in one context.
3. Identify actionable lessons, step-by-step instructions, and glossary terms from the whole book.
4. Read book-template.md and write BOOK.md directly.
5. Run verification and ambiguity-resolution loops on the single output.


## Mode B: Reference / Technical / Self-Contained Books

Books whose chapters are largely independent units, where each chapter functions as a standalone reference.

Examples:
- Technical manuals, API references, cookbooks, textbooks
- Standards documents, legal codes, product documentation
- Instructional guides where Chapter 3 does not depend on Chapter 2
- Any book designed to be read non-sequentially or consulted by topic

**Rule: Use one sub agent per chapter, with no chapter managed by more than one sub agent.**

Rationale:
- Chapter isolation preserves context boundaries and prevents bleed.
- Parallel processing of independent chapters reduces wall-clock time.
- Each subagent can specialize in its chapter's domain without noise from other sections.
- Glossary/index construction should be delegated to a final dedicated subagent that reads all chapter outputs.

Workflow for Mode B:
1. Extract full text from PDF.
2. Identify chapter boundaries.
3. Spawn parallel sub agents, one per chapter, to extract actionable lessons and steps.
4. Spawn one additional subagent to build the unified Glossary / Index from all chapter outputs.
5. Spawn one final subagent to read book-template.md and assemble BOOK.md from chapter results and glossary.
6. Run verification and ambiguity-resolution loops on the assembled output.


## Decision Heuristics

When classification is ambiguous, apply these tests:

| Test | If YES → Mode A | If NO → Mode B |
|------|-----------------|----------------|
| Can chapters be read independently without losing meaning? | No | Yes |
| Does the book's central thesis require cumulative evidence across chapters? | Yes | No |
| Are chapters organized by topic rather than by narrative progression? | No | Yes |
| Does the glossary/index require understanding relationships across chapters? | Yes | No |
| Is the book primarily a story, argument, or unified framework? | Yes | No |
| Would removing one chapter leave the rest largely intact? | No | Yes |

If tests are mixed, default to Mode A unless the book is explicitly designed as a reference work.


# Creating Books

## Single PDF file

1. Identify Book Name and Description.
2. Create folder directory following "Naming Book Directory" above.
3. Analyze full PDF text.
4. Classify the book into Mode A or Mode B using the criteria above.
5. Execute the corresponding workflow (Mode A or Mode B).
6. Update BOOK.md file with duplicate parts of the template that make sense to have duplicate sections for different parts of the actionable identified parts of PDF text.

## Directory of PDF files

1. Classify each PDF independently using the criteria above.
2. For Mode A PDFs: run single shared-context agents.
3. For Mode B PDFs: run parallel sub agents for every chapter within each PDF, following the Mode B workflow.
4. Aggregate results per PDF.

## Text File With List of PDF files

1. Classify each PDF independently.
2. Execute the corresponding workflow per PDF in parallel where possible.

## Text File With Text To Convert To Book

1. Classify the text by its structure.
2. If narrative/thematic → Mode A single agent.
3. If reference/self-contained → Mode B chapter agents.


# Verifying Books (Loop)
1. Scan created BOOK.md file and compare it section-by-section against the template file, update file to make sure has all sections from "book-template.md" file. Only proceed when created file has all sections and follows template with 0 discrepancies.
2. Scan created BOOK.md file and find all ambiguious text (Define "ambiguious" yourself).
3. Without using scripts only sub agents and edit tool update BOOK.md files with rewrite of found ambiguious text to be explicit.
4. Loop scanning and updating BOOK.md until find 0 ambiguious text upon each scan execution. Report 0 ambiguity found after reapeatedly scanning and updating the BOOK.md file.

# Identifying Duplicate Books
Not all Files are named "BOOK.md" must search all ".md" files.

1. Run parallel sub agents to read and analyze all .md files (Most likely renamed .md files) with "book-template.md" structure.
2. Check for existing "Duplicate-Books.md" markdown file.
3. Append to existing or create markdown file "Duplicate-Books.md" populated with list of book that have similar content to other created .md files (Most likely renamed .md files).
4. Populate the "Duplicate-Books.md" file with table formatted group of duplicate book with their differences so user can easily decide whether to keep duplicates or remove duplicate book.

# Behavior
1. Analyze prompt arguments
2. Identify prompt arguments for Expected Prompt Arguments.
3. Classify each book into Mode A or Mode B.
4. For Mode A books: run single shared-context agent to follow "Creating Books" Instructions.
5. For Mode B books: run parallel agents to follow "Creating Books" Instructions.
6. For every book created run parallel agents to follow "Verifying Books Loop" Instructions.
7. Follow "Identifying Duplicate Books" Instructions.
8. Report To User and Standby For Instructions.
