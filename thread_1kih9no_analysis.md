# REDDIT POST ANALYSIS

A user in r/git asked the community whether git is a complex tool, noting that many people struggle with it because it is "too complex" even though basic use should be simple. The post, made by u/ExcellentRuin8115, received 186 upvotes and sparked 248 comments. The author wanted to hear honest opinions on whether git's complexity is justified or if it could be easier to use, especially for everyday tasks.

# REDDIT COMMENTS ANALYSIS

Basic vs Advanced Complexity (43 Comments - 190 Upvotes)
Most commenters felt that git is perfectly manageable for basic tasks like pulling, committing, and pushing, but becomes confusing when you need advanced features. Many described it as "easy to use, hard to master" and pointed out that the rare tasks—like rebasing or resolving tricky merge issues—are where the real pain shows up. Some said the 99% of normal work is fine, but the remaining 1% can feel overwhelming and often requires looking up commands.

Rebasing and Merging Strategies (21 Comments - 84 Upvotes)
A large chunk of the discussion revolved around how to handle rebasing and merging. Some users shared rules of thumb, like using rebase for personal branches and merge for shared ones, while others avoided rebasing completely. There was also talk about cherry-picking, squash merging, and how to deal with repeated conflicts when rebasing onto an active main branch. A few recommended tools like git rerere to reduce repetitive conflict resolution.

Edge Cases and Horror Stories (14 Comments - 60 Upvotes)
Several commenters recounted specific situations where git turned into a nightmare. These included accidentally merging the wrong branch, reverting a merge that caused missing changes later, and issues with LFS or detached HEAD states. One person told a story about a bad merge that went undetected for weeks because the pull request diff looked tiny when it actually touched every file. The general message was that git is wonderful when everything goes right, but mistakes or unusual situations can become very difficult to fix.

Alternative Tools and GUIs (30 Comments - 91 Upvotes)
Many users recommended graphical tools and alternative version control systems to sidestep git's CLI complexity. Popular suggestions included jj, lazygit, GitKraken, GitHub Desktop, git-fork, SmartGit, and Emacs Magit. Several people who tried jj praised it for being more intuitive and removing friction from common workflows. Others argued that GUIs are a simple solution and that there is no need to suffer through the command line for everyday tasks. A few also mentioned using AI assistants to generate git commands.

Learning Curve and Education (32 Comments - 49 Upvotes)
There was broad consensus that git has a steep learning curve, especially for beginners. Many blamed poor teaching methods or people memorizing commands without understanding core concepts like the DAG structure of commits. Some noted that the basics can be picked up in a day, but true proficiency takes much longer. A few experienced developers admitted they sometimes forget how hard it was to learn initially, which can sound dismissive to those still struggling.

CLI UX and Terminology (25 Comments - 22 Upvotes)
A number of users criticized git's command-line interface as inconsistent and unintuitive. Complaints focused on confusing terminology such as "detached HEAD," the overloaded git checkout command, and the fact that even simple tasks sometimes require arcane knowledge. Some defended the CLI by saying it is powerful and that struggles usually come from avoiding it. Others wished for better documentation and more logical command names, with one person comparing it to "ants lost in the watch."

Source Control is Inherently Complex (19 Comments - 59 Upvotes)
Several commenters argued that the underlying problem of version control is difficult by nature, not just git. They explained that when multiple people edit the same file, someone must decide which change comes first, and that complexity cannot be removed—only shifted. Some compared git to older systems like CVS, SVN, and Mercurial, noting that git became dominant because of speed and GitHub rather than being easier to learn. One person summarized it as "flexibility == complexity."

Personal Experience and Anecdotes (10 Comments - 16 Upvotes)
A handful of users shared personal stories about their own git journeys. These included struggles with setting up git across multiple computers, years of practice making the tool feel natural, and memorable first encounters with confusing concepts like detached HEAD. One developer who spent five years integrating work from 20 teams said git felt second nature, while another recalled that helping a beginner on Windows reminded them how steep the learning curve really is.

Humor and Off-topic (32 Comments - 35 Upvotes)
The thread had plenty of lighthearted jokes and tangents. Comments ranged from comparing git to C++ and tax codes to quips about "multiversal timelines" and "detached HEAD" being a big WTF moment. One user joked that the first hundred comments were already about rebasing strategy, while another said git is like Jason Voorhees—simple until a problem appears, then it keeps coming back. A few off-topic remarks wondered if AI would make git obsolete.

Distributed vs Centralized Debate (8 Comments - 9 Upvotes)
A smaller group debated whether git's distributed nature is useful or overrated. Some argued that in corporate settings, everyone pushes to a central repo anyway, so the distributed aspect doesn't matter much. Others defended local commits as helpful for experiments and rollbacks before sharing work. There was also nostalgia for older centralized systems with simple global revision numbers, and concern that git allows people to work for months without pushing, risking lost work.

(Total: 234 Comments - 615 Upvotes)

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 100+ Upvotes

u/TheRedWon
"The problem is 99% of the time I am pulling, checking out a branch, adding, committing, pushing. It's not that it's complicated, but when I have to do the 1% cherry pick or rebase or whatever I have to look it up and it feels confusing because I rarely do it." (121 Upvotes) - https://www.reddit.com/r/git/comments/1kih9no/how_many_of_you_think_git_is_a_complex_tool/mrf8b2y/

## 30+ Upvotes

u/AceDecade
"Do it more often; rebasing and cherry-picking are both super handy. Cherry-picking is just grabbing work (changes in one commit) you performed on the codebase on one branch, and moving it somewhere else. Rebasing is just doing the same thing with a stack of commits.

Merging is the most straightforward strategy to use, because you don't have to think about history, you just say "here's state A, and here's state B, and if we smush them together we get state C, and anywhere the smushing produces incompatible changes the developer has to deal with all at once"

Rebasing is more complicated, but produces a nicer history. It essentially lets you change the work you did into "the work I *would have done* if I'd started working from this other state all along." Sure, each commit has the opportunity to find conflicts in its new home, rather than dealing with them all at once, but personally I find resolving merge conflicts much, much easier when in the context of "here's the change I made in this one commit, and here's the bit where the commit is no longer compatible and needs to be adapted", at most once for each commit I'm rebasing, than to tackle the merge conflicts all at once with no context" (32 Upvotes) - https://www.reddit.com/r/git/comments/1kih9no/how_many_of_you_think_git_is_a_complex_tool/mrfp5ln/

## 20+ Upvotes

u/Cinderhazed15
"The complexity isn’t in the perfectly executed workflow, it’s in the edge cases. 

One example that comes to mind is merging a branch ‘accidentally’ , then reverting the merge commit, then when your merge is ‘ready’ and you merge to main again, “some of our stuff is missing”.


This was because the merge commit pulled in all the commits from their branch prior to the accidental merge, and reverting made the merge commit not apply in the main branch.  The later merge saw that main already had the pre-bad-merge commits in history (even though they didn’t affect state) and only merged the commits after it." (24 Upvotes) - https://www.reddit.com/r/git/comments/1kih9no/how_many_of_you_think_git_is_a_complex_tool/mresue0/

## 10+ Upvotes

u/bothunter
"My rule is, use rebase for my own branches and merge for any shared branches.


Also get in the habit of making sure your code at least compiles with each commit, and then merge conflicts become much easier to do.  Basically, once you resolve the conflicts, run a build as a quick sanity check to make sure you did it right before running "git rebase --continue"" (18 Upvotes) - https://www.reddit.com/r/git/comments/1kih9no/how_many_of_you_think_git_is_a_complex_tool/mrfx8db/

# ORIGINAL POST

"How many of you think git is a complex tool

Well, after a while I realized that many people struggle with git because it is "too complex" (under the hood yes, it is kind of complex) but if you just want to do the basis then it shouldn't be that complex. So I would like to hear what you guys think about it and if you think it is too complex or not. Thanks before hand 😄"