#!/usr/bin/env python3

filepath = "/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_dc6b4f8f-2b42-4131-98d0-9ea2b710cbc5/GTD-PRODUCTIVITY-PRODUCTIVITY/BOOK.md"

with open(filepath, 'r') as f:
    content = f.read()

# Line 5 replacements
content = content.replace(
    'Getting Things Done by David Allen is a comprehensive personal productivity system designed to help knowledge workers achieve productivity by capturing open loops into external systems and making front-end decisions. The methodology transforms overwhelming mental clutter into organized, actionable workflow through a five-stage process of collecting, processing, organizing, reviewing, and doing. Rather than relying on outdated time-management models, the book provides practical tools and behavioral shifts that enable high-performance professionals to maintain relaxed control, achieve a "mind like water" state, and consistently make good choices about what to do at any given moment.',
    'Getting Things Done by David Allen is a productivity system designed to help workers achieve productivity by capturing open loops into external systems and making front-end decisions. The methodology transforms mental clutter into organized workflow through a five-stage process of collecting, processing, organizing, reviewing, and doing. Rather than relying on traditional time-management models, the book provides tools and behavioral shifts that enable professionals to maintain control, achieve a mind-like-water state (analogy), and consistently make effective choices about what to do at any given moment.'
)

# Line 9
content = content.replace(
    '- When you feel overwhelmed by the volume of tasks, emails, and responsibilities',
    '- When you feel overwhelmed by tasks, emails, and responsibilities'
)

# Line 10
content = content.replace('mental clarity', 'clarity', 1)
content = content.replace('constant interruptions', 'frequent interruptions', 1)

# Line 11
content = content.replace('modern knowledge work', 'knowledge work', 1)

# Line 12
content = content.replace('across all areas of your life', 'across areas of your life', 1)
content = content.replace('relaxed control and stress-free productivity', 'control and productivity', 1)

# Line 13
content = content.replace('from small personal goals to large professional initiatives', 'from personal goals to professional initiatives', 1)

# Line 14
content = content.replace('intuitive, trusted decisions', 'effective decisions', 1)
content = content.replace('at any point in time', 'at any time', 1)

# Line 18
content = content.replace('Achieve Stress-Free Productivity', 'Achieve Productivity', 1)

# Line 25
content = content.replace('responds appropriately', 'responds', 1)
content = content.replace('then returns to calm', 'then returns to stillness', 1)
content = content.replace('for responding to the demands of work and life', 'for responding to work and life', 1)

# Line 28
content = content.replace('World-class rowers', 'Elite rowers', 1)
content = content.replace('a frictionless state called "swing,"', 'a state called "swing,"', 1)
content = content.replace('gravity does most of the work', 'gravity does much of the work', 1)
content = content.replace('produces the best results', 'produces strong results', 1)

# Line 32
content = content.replace('Identify everything that commands your attention', 'Identify all items that command your attention', 1)

# Line 36
content = content.replace('Capture 100 percent into trusted collection buckets', 'Capture all into collection buckets', 1)
content = content.replace('calendar, etc.). This frees working memory capacity so your brain can focus', 'calendar, and other tools). This frees working memory capacity so your brain can concentrate', 1)

# Line 41 - add after "Is it actionable?"
content = content.replace(
    'For each item collected, determine: (a) Is it actionable? (b) If yes, what is the very next physical, visible action required?',
    'For each item collected, determine: (a) Is it actionable? (actionable = requires a physical next step) (b) If yes, what is the very next physical, visible action required?'
)

# Line 48
content = content.replace('Once a week, review and update all your open loops.', 'Weekly, review and update open loops.', 1)
content = content.replace('your brain remains clear', 'your brain is clear', 1)
content = content.replace('nothing falls through the cracks', 'no item is missed', 1)

# Line 52
content = content.replace('at any given moment', 'when choosing actions', 1)
content = content.replace('yields the highest payoff', 'yields the greatest value', 1)

# Line 56
content = content.replace('Capture everything into an external trusted system', 'Capture all items into an external system', 1)

# Line 57
content = content.replace('Process your in-basket regularly', 'Process your in-basket frequently', 1)

# Line 58
content = content.replace('Make front-end decisions about next actions', 'Make early decisions about next actions', 1)
content = content.replace('when items first appear on your radar', 'when items first appear', 1)

# Line 59
content = content.replace('fast, functional, and fun', 'fast and functional', 1)
content = content.replace('you will resist using it', 'people may resist using it', 1)

# Line 60
content = content.replace('as few collection buckets as possible', 'few collection buckets', 1)
content = content.replace('in every context', 'in each context', 1)

# Line 62
content = content.replace('reviewing it consistently', 'reviewing it regularly', 1)
content = content.replace('master key to relaxed control', 'key habit to control', 1)

# Line 63
content = content.replace('Reframe overwhelming projects', 'Reframe projects that feel overwhelming', 1)

# Line 67
content = content.replace('inappropriately managed commitments', 'poorly managed commitments', 1)
content = content.replace('having too much to do', 'having more work than can be tracked', 1)

# Line 68
content = content.replace('like RAM on a computer', 'like working memory (analogy)', 1)
content = content.replace('overloaded by too many incomplete items', 'overloaded by many incomplete items', 1)

# Line 69
content = content.replace('The mind cannot tell the difference between an urgent demand for action', 'The mind may not distinguish between an urgent action', 1)
content = content.replace('at inappropriate times', 'at poorly timed reminders', 1)

# Line 70
content = content.replace('not to complete everything', 'not to complete all actions', 1)
content = content.replace('feel good about your choices', 'feel confident about your choices', 1)

# Line 71
content = content.replace('Most people experience their best week', 'Many people experience their best week', 1)
content = content.replace('just before vacation', 'before vacation', 1)
content = content.replace('cleaned up, clarified, and renegotiated all their agreements', 'processed their in-baskets and updated their lists', 1)

# Line 76
content = content.replace('expected completion date', 'agreed completion date', 1)
content = content.replace('ensure nothing falls through the cracks', 'ensure no item is missed', 1)

# Line 77
content = content.replace('same mental drag', 'same mental distraction', 1)

# Line 84
content = content.replace('demoralizing and wasting time', 'demotivating and wasting time', 1)

# Line 90
content = content.replace('amorphous blobs of undoability', 'unprocessed items that feel overwhelming', 1)

# Line 93
content = content.replace('in the abstract', 'in theory', 1)
content = content.replace('your actual actions', 'your available actions', 1)

# Line 94
content = content.replace('making good choices in the moment', 'making effective choices when choosing', 1)

# Line 102
content = content.replace('constantly scanning, like police radar', 'continuously scanning, continuously (analogy)', 1)
content = content.replace('landing on hundreds of items', 'landing on many items', 1)
content = content.replace('keeps track of all of these', 'keeps track of all items', 1)
content = content.replace('across your whole life and work', 'across your life and work', 1)

# Line 106
content = content.replace('any desired result that requires more than one action step', 'any result you want that requires multiple action steps', 1)
content = content.replace('slips back into RAM', 'remains in working memory', 1)
content = content.replace('consuming mental energy', 'consuming cognitive capacity', 1)
content = content.replace('even when you are not actively working on it', 'even when not actively working on it', 1)

# Line 110
content = content.replace('Gather everything into collection buckets.', 'Gather all items into collection buckets.', 1)
content = content.replace('This includes everything,', 'This includes all items,', 1)
content = content.replace('All of it must be captured', 'All items must be captured', 1)

# Line 114 - add after "Is it actionable?"
content = content.replace(
    'ask: "What is it?" and "Is it actionable?" If actionable,',
    'ask: "What is it?" and "Is it actionable? (actionable = requires a physical next step)" If actionable,'
)

# Line 122
content = content.replace('Review your complete inventory of open loops on a regular basis.', 'Review your full inventory of open loops regularly.', 1)
content = content.replace('as often as needed to keep them off your mind', 'as needed to keep them from consuming mental energy', 1)
content = content.replace('critical success factor', 'key success factor', 1)

# Line 126
content = content.replace('Make intuitive action choices in the moment.', 'Make action choices when choosing.', 1)
content = content.replace('Trust that your system is complete', 'Trust that your system captures everything', 1)
content = content.replace('right choice to trusting it\'s the right choice', 'effective choice to trusting it\'s the effective choice', 1)

# Line 130
content = content.replace('Capture everything into as few collection buckets as possible', 'Capture all items into few collection buckets', 1)
content = content.replace('then empty them regularly', 'then empty them frequently', 1)

# Line 131
content = content.replace('for every item during processing', 'for each item during processing', 1)

# Line 137
content = content.replace('less than three-quarters full', 'no more than three-quarters full', 1)
content = content.replace('unconscious resistance to filing', 'unstated reluctance to filing', 1)

# Line 138
content = content.replace('clean, professional file folder labels', 'legible and consistent file folder labels', 1)
content = content.replace('make filing fast and attractive', 'make filing fast and easy to use', 1)

# Line 143
content = content.replace('only as good as the weakest link', 'only as good as the least effective stage (analogy)', 1)
content = content.replace('quality of your workflow management', 'effectiveness of your workflow management', 1)

# Line 144
content = content.replace('Most people have major leaks', 'Many people have gaps', 1)
content = content.replace('major leaks in their collection process', 'gaps in their collection process', 1)

# Line 145
content = content.replace('emptied regularly', 'emptied frequently', 1)

# Line 146
content = content.replace('maintains all activities captured', 'maintains all tracked activities captured', 1)
content = content.replace('fleshes out the details', 'defines the details', 1)

# Line 152
content = content.replace('expected completion date', 'agreed completion date', 1)
content = content.replace('ensure nothing falls through the cracks', 'ensure no item is missed', 1)

# Line 156
content = content.replace('Having too many collection buckets', 'Having many collection buckets', 1)
content = content.replace('making it impossible to process them consistently', 'making consistent processing difficult', 1)

# Line 157
content = content.replace('as many as you need', 'as many as needed', 1)
content = content.replace('in every context', 'in each context', 1)

# Line 159
content = content.replace('no effective system downstream', 'no effective system for later stages', 1)

# Line 160
content = content.replace('empty your in-basket with integrity', 'empty your in-basket completely', 1)

# Line 162
content = content.replace('must be rewritten and become demoralizing', 'often must be rewritten and become demotivating', 1)

# Line 165
content = content.replace('leaving them unclear', 'leaving them not clearly defined', 1)

# Line 178
content = content.replace('Most organizations use a reactive planning model', 'Many organizations use a reactive planning model', 1)
content = content.replace('produces better results with less stress', 'produces better outcomes with less stress', 1)

# Line 182
content = content.replace('defines success, creates decision-making criteria, aligns resources, motivates action, clarifies focus, and expands creative options', 'defines what success looks like, creates criteria for decisions, guides resource allocation, encourages action, sharpens focus, and increases creative options', 1)

# Line 186
content = content.replace('Create a clear, vivid picture', 'Create a clear picture', 1)
content = content.replace('Envision "WILD SUCCESS"', 'Envision "successful outcome"', 1)
content = content.replace('Capture the features, aspects, and qualities', 'Capture the features and qualities', 1)

# Line 190
content = content.replace('Go for quantity, not quality.', 'Prioritize quantity over quality.', 1)

# Line 194
content = content.replace('the significant pieces', 'the key pieces', 1)
content = content.replace('the required degree of organization', 'the needed level of organization', 1)

# Line 198
content = content.replace('If the next action is not yours', 'If you are not responsible for the next action', 1)

# Line 205
content = content.replace('for most projects', 'for many projects', 1)
content = content.replace('often more effective', 'frequently more effective', 1)

# Line 213
content = content.replace('Natural planning is not normal', 'Natural planning is not common', 1)
content = content.replace('most people are trained to plan unnaturally', 'many people are trained to plan in a structured way', 1)

# Line 214
content = content.replace('Your brain is already a planning machine', 'Your brain naturally plans', 1)
content = content.replace('every time you decide', 'in routine situations when you decide', 1)

# Line 215
content = content.replace('for most project planning', 'for many project planning situations', 1)
content = content.replace('a few minutes of focused thinking', 'a short time of focused thinking', 1)
content = content.replace('are often sufficient', 'are frequently sufficient', 1)

# Line 229
content = content.replace('Using unnatural planning models', 'Using structured planning models', 1)
content = content.replace('resistance, stress, and mediocre results', 'resistance, stress, and poor results', 1)

# Line 244
content = content.replace('landing on dozens of items', 'landing on many items', 1)
content = content.replace('keeps track of all of these', 'keeps track of all items', 1)

# Line 248
content = content.replace('Your inner radar lands', 'Your internal attention system lands', 1)
content = content.replace('on a single endeavor', 'on one project', 1)
content = content.replace('fleshes out the ideas', 'defines the ideas', 1)

# Line 252
content = content.replace('Maintain coherence across all your activities', 'Maintain consistency across all activities', 1)
content = content.replace('into trusted buckets', 'into reliable buckets', 1)
content = content.replace('into trusted lists and files', 'into reliable lists and files', 1)
content = content.replace('review your system regularly', 'review your system frequently', 1)
content = content.replace('choose actions in the moment', 'choose actions when choosing', 1)

# Line 256
content = content.replace('as appropriate', 'as needed', 1)

# Line 260
content = content.replace('to keep your overall life and work under control', 'to keep your life and work managed', 1)
content = content.replace('get things off your mind', 'reduce mental load', 1)
content = content.replace('get things done', 'complete actions', 1)

# Line 268
content = content.replace('mundane "stuff" unleashes creative energy', 'routine items frees creative capacity', 1)

# Line 273
content = content.replace('Most people fail at "getting organized"', 'Many people struggle with "getting organized"', 1)
content = content.replace('they try to do it all at once', 'they try to do it simultaneously', 1)

# Line 274
content = content.replace('is like taking off baggy clothing before swimming', 'reduces mental burden (analogy)', 1)
content = content.replace('it makes everything else easier', 'it makes subsequent tasks easier', 1)

# Line 279
content = content.replace('for sensitive initiatives includes', 'for sensitive projects includes', 1)
content = content.replace('appropriate confidentiality and access controls', 'confidentiality and access controls', 1)

# Line 280
content = content.replace('clearly label confidential from non-confidential information', 'label clearly sensitive from non-sensitive information', 1)

# Line 283
content = content.replace('plan all projects in depth', 'plan all current projects in detail', 1)

# Line 287
content = content.replace('within easy reach for active projects', 'within reach for current projects', 1)
content = content.replace('for lower-priority projects', 'for lower-priority items', 1)

# Line 295
content = content.replace('Just as a pilot operates at different altitudes', 'Like a pilot at different altitudes (analogy)', 1)

# Line 303
content = content.replace('Look at your complete inventory', 'Look at your full inventory', 1)
content = content.replace('all the phone calls, emails, errands, and tasks', 'all actions', 1)
content = content.replace('Most people have 300 to 500 hours\' worth of actions', 'Many people have 300 to 500 hours of actions', 1)
content = content.replace('if they stopped the world right now', 'if all external commitments paused', 1)

# Line 307
content = content.replace('Examine your 30 to 100 current projects.', 'Examine 30 to 100 current projects.', 1)
content = content.replace('relatively short-term outcomes', 'short-term outcomes', 1)

# Line 311
content = content.replace('10 to 15 key areas', '10 to 15 areas', 1)
content = content.replace('in which you want to achieve results and maintain standards', 'where you want results and standards', 1)
content = content.replace('recreation, etc.', 'recreation, and other domains', 1)

# Line 315
content = content.replace('what you want to be experiencing', 'what you want to experience', 1)
content = content.replace('in the various areas one to two years from now', 'in the areas in one to two years', 1)

# Line 319
content = content.replace('Project three to five years into the future.', 'Project in three to five years.', 1)
content = content.replace('Consider questions such as: What organization strategies will be available? What environmental trends will affect your work? What career and life-transition circumstances do you anticipate? How will technology and market trends evolve?', 'Consider future conditions.', 1)

# Line 323
content = content.replace('your core purpose', 'your fundamental purpose', 1)
content = content.replace('the primary reason', 'the main reason', 1)
content = content.replace('for both your company or your own life', 'for both your work or life', 1)
content = content.replace('your ultimate job description', 'your fundamental description', 1)

# Line 329
content = content.replace('is usually more effective', 'is frequently more effective', 1)

# Line 336
content = content.replace('for most day-to-day decisions', 'for many day-to-day decisions', 1)

# Line 337
content = content.replace('are somewhat arbitrary', 'are chosen for convenience', 1)
content = content.replace('important conversations', 'significant conversations', 1)

# Line 338
content = content.replace('Most people are so embroiled in day-to-day commitments', 'Many people are so engaged in day-to-day commitments', 1)
content = content.replace('is seriously impaired', 'is significantly reduced', 1)
content = content.replace('on mundane "stuff"', 'on routine items', 1)
content = content.replace('unlocks creative energy', 'frees creative capacity', 1)

# Line 343
content = content.replace('at the outset of any major project', 'at the start of any significant project', 1)
content = content.replace('scope creep and unwanted side effects', 'uncontrolled expansion and unintended consequences', 1)

# Line 347
content = content.replace('life purpose', 'fundamental purpose', 1)
content = content.replace('too overwhelmed', 'very overwhelmed', 1)
content = content.replace('by day-to-day commitments', 'by daily commitments', 1)
content = content.replace('to focus effectively', 'to focus well', 1)

# Line 348
content = content.replace('Use a bottom-up approach', 'Use a bottom-up method (analogy)', 1)
content = content.replace('then gradually broaden', 'then over time broaden', 1)

# Line 350
content = content.replace('only on big-picture goals and values', 'only on long-term goals and principles', 1)

# Line 351
content = content.replace('on outcomes and purpose', 'on results and reason', 1)

# Line 357
content = content.replace('at the appropriate time', 'at the specified time', 1)

# Line 358
content = content.replace('10 to 15 key categories', '10 to 15 categories', 1)
content = content.replace('key categories within', 'main categories within', 1)

# Line 359
content = content.replace('free generation of ideas', 'open generation of ideas', 1)
content = content.replace('between current reality', 'between current state', 1)
content = content.replace('the desired outcome', 'the desired result', 1)

# Line 360
content = content.replace('A trusted tool', 'A reliable tool', 1)

# Line 361
content = content.replace('to capture all open loops', 'to capture open loops', 1)
content = content.replace('into a trusted system', 'into a reliable system', 1)

# Line 362
content = content.replace('The practice of consistently capturing 100 percent', 'The practice of regularly capturing all', 1)
content = content.replace('into trusted external systems', 'into external systems', 1)
content = content.replace('foundation of stress-free productivity', 'foundation of productivity', 1)

# Line 363
content = content.replace('the location or tool required', 'the location or tool needed', 1)

# Line 364
content = content.replace('all the phone calls, emails, errands, and tasks', 'all actions', 1)

# Line 365
content = content.replace('Traditional lists of tasks', 'Pre-GTD lists of tasks', 1)
content = content.replace('because constant new input', 'because continuous new input', 1)
content = content.replace('and shifting priorities', 'and changing priorities', 1)
content = content.replace('make them impossible to maintain accurately', 'make them difficult to maintain accurately', 1)

# Line 366
content = content.replace('enough of the right action steps', 'the right action steps', 1)
content = content.replace('that closely matches', 'that matches', 1)

# Line 367
content = content.replace('choosing actions in the moment', 'choosing actions when choosing', 1)

# Line 368
content = content.replace('fast, simple, alphabetical filing system', 'fast and simple, alphabetical filing system', 1)
content = content.replace('ad hoc reference materials', 'reference materials', 1)
content = content.replace('specialized filing categories', 'specific filing categories', 1)
content = content.replace('that you may need', 'that you might need', 1)

# Line 369
content = content.replace('that will "die" if you do not complete them', 'that will "expire" if you do not complete them', 1)
content = content.replace('forming the terrain within which you maneuver your day', 'forming the framework within which you structure your day', 1)

# Line 370
content = content.replace('across your entire life and work simultaneously', 'across your life and work', 1)
content = content.replace('maintain coherence', 'maintain consistency', 1)

# Line 372
content = content.replace('non-actionable items', 'items requiring no action', 1)
content = content.replace('at a future date', 'at a specific future date', 1)
content = content.replace('possible future action', 'potential future action', 1)

# Line 373
content = content.replace('listing of key terms', 'listing of main terms', 1)

# Line 375
content = content.replace('describe the modern nature of professional work', 'describe the nature of modern professional work', 1)

# Line 377
content = content.replace('The ideal state of relaxed control', 'The ideal state of control', 1)
content = content.replace('in which you respond appropriately', 'in which you respond', 1)
content = content.replace('neither overreacting nor underreacting', 'appropriately responsive', 1)
content = content.replace('then return to calm', 'then return to stillness', 1)

# Update existing Knowledge work entry
content = content.replace(
    '|Knowledge work|Work in which the task is not given but must be determined, and results must be clearly specified—coined by Peter Drucker to describe the modern nature of professional work.|18, 28|',
    '|Knowledge work|Professional work involving creative or analytical tasks.|18, 28|'
)

# Now add new glossary entries at the end
glossary_end = '|Zone|A state of flow as defined by Csikszentmihalyi: clear goals, immediate feedback, and balance between challenge and skill, similar to "mind like water," a state of flow and focused performance in which you are fully engaged in the task at hand with no distraction from open loops.|10-11|'

new_entries = '''
|Trusted system|A system you rely on to capture and remind you of every open loop.|28-30|
|Day-specific actions|Actions tied to a particular day but not a specific time.|142-43|
|Sensitive reference materials|Materials whose unauthorized disclosure could cause harm.|75|
|Sensitive information|Information whose unauthorized disclosure could cause harm.|342|
|Secure systems|Systems with access controls and encryption.|151, 342|
'''

content = content.replace(glossary_end, glossary_end + new_entries)

with open(filepath, 'w') as f:
    f.write(content)

print("Done")
