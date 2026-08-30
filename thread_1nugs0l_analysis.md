# REDDIT POST ANALYSIS

A discussion in r/git sparked by u/AttentionSuspension's post titled "Rebase is better then Merge. Agree?" gathered 430 upvotes and 374 comments. The author argued that "Rebase is better then Merge" and listed four main reasons: avoiding local merge commits, achieving linear history, better CI integration by testing feature branches with the latest dev changes, and the ability to rewrite history for cleaner commits. The post explicitly warned that "Rebase on shared branches is BAD" and asked the community for their perspectives on when to use rebase versus merge.

# REDDIT COMMENTS ANALYSIS

## Rebase Advocacy (32 Comments - 51 Upvotes)

Many commenters agreed with the original post, emphasizing that rebase excels for personal or feature branches where you're the only one working on the code. They highlighted how rebase keeps local history clean, avoids unnecessary merge commits, and makes it easier to test changes against the latest upstream code. As one user put it, "You use rebase to keep a branch that nobody is pulling from cleanly following its upstream branch." Others noted that rebase is particularly valuable for squashing messy work-in-progress commits before merging, with one commenter stating, "You rewrite your history as part of writing a merge request. That's just basic hygiene!" The consensus in this group was that rebase is a powerful tool for individual developers who want a tidy commit history.

## Merge Advocacy (27 Comments - 138 Upvotes)

A significant number of commenters pushed back against the pro-rebase stance, arguing that merge is safer and preserves valuable historical context. They warned that rebasing rewrites history, which can cause problems when multiple people work on the same branch or when you need to understand what actually happened during development. One critic wrote, "Rebase is kind of a noob trap. Rather than learn about git it seems to magically solve your problem. However the force-pushing should be a red flag that it's not ideal." Others pointed out that merge commits serve a purpose by showing when and how branches were integrated, with one user noting, "I care about the immediate history whilst developing a feature" and preferring to see the full development process preserved.

## Balanced Perspective (68 Comments - 406 Upvotes)

The largest group of commenters took a balanced, context-dependent approach, arguing that both rebase and merge are valid tools for different situations. The top-voted comment in the entire thread (233 upvotes) captured this sentiment well: "You use rebase to keep a branch that nobody is pulling from cleanly following its upstream branch. You use merge to get those changes into an upstream branch that many people are pulling from." Others echoed this, with one writing, "Rebase is 'better' for a branch that only you are working on. Merge is 'better' for a branch that multiple people are working on." This cluster viewed the debate as a false dichotomy, emphasizing that the right choice depends on team size, branch ownership, and workflow requirements.

## Practical Git Workflows (92 Comments - 204 Upvotes)

Many commenters shared specific git workflows and commands they use in their daily work. Popular patterns included rebasing feature branches onto the latest main before opening a PR, using "git merge --squash" to create a single clean commit on main, and employing "git pull --rebase" to keep local branches up to date. One user described their workflow: "We rebase main branches into feature branches. Subsequently, we merge feature branches onto the main branches." Another shared a streamlined approach: "merge main/master into your feature or rebase your f-b on main; merge squash your feature branch into main. One 'revert' if it's going wrong." These practical contributions showed that most teams use a hybrid approach rather than strictly rebasing or merging everything.

## Code Review & Collaboration (22 Comments - 58 Upvotes)

Several commenters discussed how the choice between rebase and merge affects code reviews and team collaboration. A major concern was that rebasing changes commit hashes, which can break tools like GitHub's "Changes since your last review" feature and make it harder for reviewers to track what changed. One reviewer wrote, "If I am reviewing your PR and you are using a rebase workflow I automatically hate you. It makes it much more difficult to re-review to see if you have actually addressed my comments." Others noted that merge conflict resolutions are more visible in merge commits, making it easier for teams to understand how conflicts were resolved. The debate highlighted that code review tools are often built around merge-based workflows, and rebasing can create friction in collaborative environments.

## Questions (64 Comments - 98 Upvotes)

A number of commenters asked clarifying questions about specific aspects of rebase and merge workflows. Questions ranged from basic inquiries like "What's wrong with 'git pull --rebase'?" to more nuanced ones about how rebase affects git bisect and whether squash commits preserve history. One new developer asked about handling rebase when a PR is already open on a staging branch, seeking advice on conflict resolution strategies. Others sought clarification on corporate workflows, asking how teams handle rebasing when multiple people work on the same feature branch. These questions revealed that many developers are still learning the trade-offs and seeking guidance on best practices.

## Brief Reactions & Humor (57 Comments - 73 Upvotes)

The thread included many short, humorous, and off-topic reactions. Comments like "BOTH!", "Sensei 🥋", "Unicorn 🦄", and "Yes. It's called a git tree, not a git skyscraper" added levity to the discussion. Some commenters made jokes about rebasing being a "noob trap" or about developers who never rebase being "unicorns." One user quipped, "After reading all the conversations here, you're all wrong. I'm going to just cherry-pick into main from now on." These brief reactions showed that while the topic is serious, many in the git community approach it with humor and a recognition that there's no one-size-fits-all answer.

(Total: 362 Comments - 1028 Upvotes)

# TOP COMMENTS

## 200+

u/Shadowratenator

"You use rebase to keep a branch that nobody is pulling from cleanly following its upstream branch. 

You use merge to get those changes into an upstream branch that many people are pulling from." (233 Upvotes) - https://www.reddit.com/r/git/comments/1nugs0l/rebase_is_better_then_merge_agree/nh0z9oq/

## 30+

u/FlipperBumperKickout

"No I don't. Rebase is nice for local branches but I strongly prefer my global history to be branched so I can see commits which are working on the same feature being grouped together in a branch.

Other than your second point I would agree.

edit: and your copy branch thing. Absolutely not." (38 Upvotes) - https://www.reddit.com/r/git/comments/1nugs0l/rebase_is_better_then_merge_agree/nh0yja4/

## 20+

u/homezlice

"the reason gitflow and other processes were created is because of what you're saying is BAD about rebase.  Informing others of the right branch all the time in a large project isn't efficient." (24 Upvotes) - https://www.reddit.com/r/git/comments/1nugs0l/rebase_is_better_then_merge_agree/nh0xx1i/

## 10+

u/ars0nisfun

"I have been professionally developing and using git for about 8 years now and have never had an issue merging lol. We have a big central branch for the product we develop, with each new feature/issue being it's own branch that gets merged in after it passes a suite of automated tests. Broadly, I just merge the central branch into my own before I push to ensure no merge conflicts, and so long as my branch doesn't take 2-3 weeks to get merged in I have never had an issue or needed to rebase." (19 Upvotes) - https://www.reddit.com/r/git/comments/1nugs0l/rebase_is_better_then_merge_agree/nh0zlvw/


# ORIGINAL POST

"Rebase is better then Merge. Agree?"


"I prefer Rebase over Merge. Why?

1. This avoids local merge commits (your branch and 'origin/branch' have diverged, happens so often!) `git pull --rebase`
2. Rebase facilitates linear history when rebasing and merging in fast forward mode.
3. Rebasing allows your feature branch to incorporate the recent changes from dev thus making CI really work! When rebased onto dev, you can test both newest changes from dev AND your not yet merged feature changes together. You always run tests and CI on your feature branch WITH the latests dev changes.
4. Rebase allows you rewriting history when you need it (like 5 test commits or misspelled message or jenkins fix or github action fix, you name it). It is easy to experiment with your work, since you can squash, re-phrase and even delete commits.

Once you learn how rebase really works, your life will never be the same 😎

Rebase on shared branches is BAD. Never rebase a shared branch (either main or dev or similar branch shared between developers). If you need to rebase a shared branch, make a copy branch, rebase it and inform others so they pull the right branch and keep working.

What am I missing? Why you use rebase? Why merge?

Cheers!"
