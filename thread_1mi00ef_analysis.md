# REDDIT POST ANALYSIS

The post "What are some lesser known features of Git that more people should know?" by u/surveypoodle sparked a lively discussion in r/git about Git features that many developers wish they had learned sooner. With 203 upvotes and 228 comments, the thread drew a wide range of experienced Git users sharing their favorite underrated commands and workflows. The original poster asked for "relatively lesser-known features that more people should know about," and the community delivered with tips covering everything from worktree management to safe force-pushing, undo tools, and the ever-present debate over rebase versus merge.

# REDDIT COMMENTS ANALYSIS

[Worktree Discussion] (36 Comments - 185 Upvotes)
The largest conversation centered on git worktree, with 36 comments and 185 upvotes. Many users praised it as a game-changing way to keep multiple branches checked out simultaneously in separate folders without the overhead of full clones. One user noted it's especially valuable when branch checkouts take a long time or when projects involve local services and databases. Others remained skeptical, arguing that simply cloning the repository multiple times achieves the same result, though several pointed out that worktree saves disk space and avoids redundant git operations. The thread included practical use cases like reviewing someone else's branch while keeping current work intact.

[Safe Force Push] (16 Comments - 121 Upvotes)
This cluster of 16 comments and 121 upvotes focused on the --force-with-lease flag as a safer alternative to plain git push --force. Users explained that it prevents accidentally overwriting someone else's commits by checking that the remote branch is still at the expected state. Several commenters shared their own aliases and configurations, including combining --force-with-lease with --force-if-includes for extra safety. A lively side discussion clarified the difference between git's background prefetch operations and regular fetch, noting that prefetch does not update remote refs.

[Reflog & Undo Tools] (15 Comments - 67 Upvotes)
15 comments and 67 upvotes celebrated git reflog as the ultimate safety net for recovering lost work. Users described it as a lifesaver when branches or commits go missing, with one calling it "literally goated" and another saying it made them feel like a "friggin god." Tips included using gitk --reflog for visual browsing and the @HEAD shorthand to reference commits. The cluster also touched on related recovery tools like git checkout - for switching back to the previous branch.

[Rerere] (3 Comments - 58 Upvotes)
3 comments and 58 upvotes highlighted git rerere (reuse recorded resolution) as a hidden gem. The top comment simply linked to the rerere documentation, while others expressed interest in trying it. One user noted it was mentioned earlier in the thread as a solution to recurring merge conflicts during rebasing.

[Bisect] (6 Comments - 53 Upvotes)
6 comments and 53 upvotes covered git bisect as a powerful debugging tool for tracking down when a bug was introduced. Users described automating the process with test scripts and using git stash apply instead of repeatedly popping stashes. One commenter shared a link to an article about bisect, while another mentioned git bisect run as a way to find regression causes automatically.

[Fixup & Autosquash] (9 Comments - 48 Upvotes)
9 comments and 48 upvotes discussed git commit --fixup and git rebase --autosquash as ways to clean up commit history without manual interactive rebase. Users explained how fixup commits automatically get squashed into their target commits during rebase. Several mentioned git-absorb as an external tool that automates this even further, with one user calling it the most exciting Git tool they had learned in years.

[Rebase vs Merge] (68 Comments - 198 Upvotes)
The largest cluster at 68 comments and 198 upvotes was a heated debate about whether to rebase or merge. Pro-rebase users argued it keeps history clean and makes bisecting easier, while pro-merge users valued the explicit record of when branches were integrated. Several commenters advocated for a middle ground: rebasing feature branches locally and then merging with --no-ff to preserve both clean history and merge context. The discussion touched on team size, CI pipelines, and the importance of not rebasing shared branches.

[Stash] (4 Comments - 21 Upvotes)
4 comments and 21 upvotes covered git stash basics and advanced usage. Users noted that many developers don't know about stashing, and one explained that you can have multiple named stashes and apply them selectively rather than treating stash as a single stack.

[Switch/Restore vs Checkout] (1 Comments - 6 Upvotes)
1 comment and 6 upvotes recommended switching from git checkout to git switch and git restore for better safety and clearer intent, since checkout can be ambiguous when branch names overlap with filenames.

[Learning Resources] (11 Comments - 38 Upvotes)
11 comments and 38 upvotes shared recommendations for learning Git, including MIT's Missing Semester course, learngitbranching.js.org, the Git Parable article, and a Pluralsight course. Users praised these resources for helping new team members understand version control.

[CLI vs GUI/IDE Debate] (12 Comments - 15 Upvotes)
12 comments and 15 upvotes argued about whether developers should learn Git commands or rely on GUI tools and AI assistants. One user sparked controversy by saying they let AI handle complex Git tasks because they're too lazy to learn the commands. Others pushed back, arguing that understanding the command line is essential for debugging and that most GUIs hide important functionality. The thread included jokes about corporate culture and senior developers who can't distinguish Git from GitHub.

[Other Git Features & Tips] (40 Comments - 107 Upvotes)
40 comments and 107 upvotes covered a grab bag of additional tips including git add -p for partial staging, git format-patch and git apply for moving changes between repos, autoSetupRemote for automatic tracking branches, .git/info/exclude for private ignore rules, git notes for annotating commits, git hooks for automation, git log --follow for tracking file history, and git clone --depth for shallow clones. Users also shared custom aliases and workflows for juggling multiple branches.

(Total: 221 Comments - 917 Upvotes)

# TOP COMMENTS

## 100+

u/Cool-Walk5990

"worktree" (106 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n703w3q/

## 70+

u/PitrPi

"`--force-with-lease` allows you to force push, but only if upstream is in state that your local git expects, i. e. it will not overwrite someone else's commit. If you have to force, force with lease" (76 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n70i8c6/

## 50+

u/This-Willingness-762

"[rerere](https://git-scm.com/book/en/v2/Git-Tools-Rerere)" (54 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n704ok0/

## 30+

u/TheBigGambling

"Bisect" (39 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n70484m/

## 20+

u/drone-ah

"git commit --fixup blew my mind" (26 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n70bbe2/

## 10+

u/NotSelfAware

"`autoSetupRemote = true` in your `$HOME/.gitconfig` prevents exactly that. It basically tells Git to automatically create a tracking relationship between your local branch and the remote branch with that name when you push for the first time." (18 Upvotes) - https://www.reddit.com/r/git/comments/1mi00ef/what_are_some_lesser_known_features_of_git_that/n70fq2v/

# ORIGINAL POST

"What are some lesser known features of Git that more people should know?"

"Every once in a while when I look at Git documentation, I notice something and think "I wish I knew about this earlier.". So I'm wondering what are some relatively lesser-known features that more people should know about?"