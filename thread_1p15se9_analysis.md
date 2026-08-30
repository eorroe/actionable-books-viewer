# REDDIT POST ANALYSIS

A junior developer who has been coding for about a year asked the r/git community for advice on how to actually get comfortable with Git. The original poster, u/Aggravating_War_9292, wrote that they are "starting to get pretty good at coding, but I still struggle with Git" and often finds themselves "not really sure what I'm doing and just hope everything works out." They wanted to know whether most people learned through videos or through real-world, hands-on practice. The post earned 146 upvotes and sparked 167 real comments (with a few deleted or removed ones mixed in), showing that this is a very common pain point for new developers.

# REDDIT COMMENTS ANALYSIS

**Command Line / CLI Advice** (21 Comments - 189 Upvotes)
This cluster is the biggest and most popular, with the top comment of the entire thread (116 upvotes) falling here. People shared concrete tips like never copy-pasting commands, always typing them out until it becomes second nature, and using tab completion constantly. One commenter noted that "If you press tab and nothing happens, you know you've fucked something up," while another suggested avoiding "git add ." and instead staging changes carefully one file at a time. The overall message was that building muscle memory on the command line is the fastest way to stop feeling lost with Git.

**GUI / Visual Tools** (37 Comments - 112 Upvotes)
A large group of commenters argued that using visual tools is totally fine and can actually help beginners understand Git better. They mentioned tools like SourceTree, SmartGit, VS Code, Lazygit, and IntelliJ IDEA, saying that seeing branches and commits visually makes the concepts click. One person wrote that GUI clients can be "particularly useful for writing and crafting commits" because they let you pick exactly what to stage. Another said, "Use a GUI. We aren't living in the 80s, there is no reason to not use modern tools."

**Learning by Doing / Practice** (18 Comments - 25 Upvotes)
Many replies emphasized that the only real way to get comfortable is to use Git constantly and make mistakes on purpose. People suggested creating throwaway repositories, intentionally causing merge conflicts, and experimenting with rebasing and cherry-picking in a safe environment. One commenter said, "Create a dummy repo, and then just go nuts. If it breaks, delete and go again." Another noted that you should "just use it. Like anything eventually you just kind of know how to do the main things."

**Understanding Internals / Mental Model** (14 Comments - 22 Upvotes)
Several users stressed that Git becomes much less scary once you understand what it is actually doing under the hood. They recommended looking inside the .git folder, learning that branches are just pointers, and realizing that every commit is a complete snapshot. One person wrote, "The key to understanding git is to remove the black box magic and try to understand how incredibly simplistic it actually is." Another added that learning about "git reflog" and using it whenever you mess up can save you a lot of panic.

**Specific Resources** (14 Comments - 21 Upvotes)
Commenters shared a handful of highly recommended resources, with learngitbranching.js.org being mentioned multiple times. Others pointed to the official Pro Git book, Scott Chacon's introductory video, Atlassian's tutorials, and even ChatGPT as a coach. One person said, "My standard tip for anyone wanting to understand Git is Scott Chacon's introduction," while another recommended using learngitbranching.js.org to "get started using git on the command line confidently."

**Books and Documentation** (9 Comments - 10 Upvotes)
A smaller but enthusiastic group strongly recommended reading the free Pro Git book, which is available at git-scm.com. One user said, "Read the Pro Git book OP: That's it. I literally just made time to finally read that book and followed the exercises on my computer. I became so much more confident afterwards." Another called it "solid resource for at least 19 years" and listed chapters as required reading before giving developers access to Git at their company.

**Agreement / Support** (32 Comments - 65 Upvotes)
A large number of short replies simply agreed with earlier comments, thanked people for tips, or offered brief encouragement. Examples include "Absolutely," "Totally agree," "100% agree," "Good luck on your journey!," and "Thank you for the tip!" These replies didn't add new advice but showed that the community broadly agrees on the main strategies for learning Git.

**Questions / Clarifications** (12 Comments - 21 Upvotes)
Several people asked follow-up questions or sought clarification on specific points. The original poster asked whether people used personal projects or professional work to practice. Others asked if tab-completion advice applied to non-Git commands, whether force-pushing after a rebase is safe, and why anyone would bother with the command line when GUIs exist. One person asked, "Does this hold for Java or other non git commands too?"

**Personal Experience / Anecdotes** (3 Comments - 3 Upvotes)
A few commenters shared brief personal stories about their own Git journeys, such as teaching a seminar to new starters, using "git apply --cached -F -" to stage changes, or being thrown into Git at a job and learning by repetition. These stories were relatively short but added real-world color to the discussion.

**Humor / Off-topic** (1 Comments - 1 Upvotes)
One user launched into a colorful rant calling Git "a piece of shit" and complaining about permission errors when cloning repos. This comment stood out from the otherwise constructive tone of the thread.

**Deleted / Removed / Unclear** (6 Comments - 4 Upvotes)
A handful of comments were removed or posted by deleted accounts, leaving only placeholders or low-score remnants. These included a brief deleted reply and a removed comment that no longer contributes to the discussion.

(Total: 167 Comments - 473 Upvotes)

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 100+ Upvotes

u/craig1f
"This doesn't answer your question, but the advice I give to junior devs on using the command line is:

Never copy paste commands. Always type, until it gets to the point that typing doesn't feel like it takes a lot of energy. Once you get to that point, copy paste is ok. 

Don't lean on VSC too much. At a minimum, be comfortable with clone, pull, push, creating a branch, changing branch, deleting a branch, and stashing. 

Once you have the basics, learn about rebase. 

Edit: As @whattteva says, and I agree with, the ONE thing that I would use VSC for instead of the command line is for staging one file at a time instead of using `git add`." (116 Upvotes) - https://www.reddit.com/r/git/comments/1p15se9/how_did_you_actually_get_comfortable_with_git/npnmk68/

## 20+ Upvotes

u/rednets
"I would add: DO lean on tab completion.

This is great advice on using the command line in general. Hammer that tab key!" (29 Upvotes) - https://www.reddit.com/r/git/comments/1p15se9/how_did_you_actually_get_comfortable_with_git/nporqpg/

## 10+ Upvotes

u/Danny_Gray
"Absolutely. If you press tab and nothing happens, you know you've fucked something up." (13 Upvotes) - https://www.reddit.com/r/git/comments/1p15se9/how_did_you_actually_get_comfortable_with_git/npq753o/

# ORIGINAL POST

"How did you actually get comfortable with Git?

Hey everyone! I've been working as a junior developer for a year and I'm starting to get pretty good at coding, but I still struggle with Git. Most of the time I'm not really sure what I'm doing and just hope everything works out. I'm curious how other people got comfortable with Git. Did you mostly watch videos or was it more of a learn-by-doing, real-world kind of thing? Any advice would be really appreciated!"
