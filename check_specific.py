#!/usr/bin/env python3

filepath = "/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_59125815-2586-4203-86df-c64414e24637/FRUT-SPIRITUAL-WISDOM-DAILY/BOOK.md"

with open(filepath, 'r') as f:
    lines = f.readlines()

# Build a mapping of line numbers (1-indexed) to content
line_map = {i+1: line.rstrip('\n') for i, line in enumerate(lines)}

replacements = [
    (5, "offering a daily commentary that extracts one actionable lesson per day from each chapter", "a daily spiritual guide covering all 18 chapters"),
    (9, "a moral dilemma where duties conflict and no option satisfies all obligations", "a genuine moral dilemma"),
    (10, "when you have been unable to act for more than 48 hours due to fear of negative outcomes and need guidance on performing your duty", "paralyzed by fear of consequences"),
    (13, "cultivate steady observation of pleasure and pain without elation or despondency", "cultivate equanimity"),
    (17, "increase daily meditation time by 5 minutes weekly and focus on one deity form for 30 minutes without distraction", "deepen devotion, practice single-minded worship"),
    (113, "identifying with the soul reduces reactivity to external events, measured by fewer instances of speaking before thinking, making unplanned purchases, or reacting with anger per day", "identifying with the soul brings inner peace"),
    (153, "fosters the habit of giving credit to others and acknowledging contributing factors", "fosters humility"),
    (167, "inaction itself carries karmic consequences", "According to the teaching, inaction itself carries karmic consequences"),
    (168, "selfless action protects one from the fear of birth and death", "According to the Bhagavad Gita, selfless action protects one from the fear of birth and death"),
    (178, "treat both success and failure as temporary states that do not define your worth", "treat both success and failure as temporary states that do not define your identity"),
    (181, "Begin with tasks that require less than 30 minutes of focused effort", "Begin with simpler tasks"),
    (190, "The Tortoise Method (withdrawing attention at the first impulse, like a tortoise retracting its limbs)", "The Tortoise Method (withdrawing attention at the first impulse)"),
    (225, "An uncontrolled mind leads to impulsive actions you later regret; a controlled mind leads to deliberate choices aligned with your values", "The mind is your greatest friend if controlled, and your worst enemy if not"),
    (260, "Channel energy that remains after completing your required daily tasks", "Channel surplus energy"),
    (266, "relationships that do not criticize your practice and environments that allow at least 30 minutes of uninterrupted meditation daily", "positive associations"),
    (280, "This means observing when rajas, sattva, or tamas dominate your mood and consciously choosing your response", "The modes are not enemies to be destroyed but forces to be understood and transcended"),
    (282, "Liberation comes from recognizing that your true self is the witness of these modes, not the modes themselves", "Liberation comes from seeing through the illusion that these modes define who you are"),
    (303, "responding to pleasure and pain with the same neutral facial expression and tone of voice for 60 seconds before reacting", "Treating Pleasure and Pain Equally"),
    (307, "the five innate drives for survival, reproduction, rest, social bonding, and exploration described in the chapter", "innate biological drives"),
    (315, "maintaining eye contact for 3–5 seconds and using the same greeting tone regardless of role", "equal respect and attention"),
    (316, "Treat all individuals with equal respect by maintaining eye contact for 3–5 seconds and using the same greeting tone regardless of role", "Treat all people equally"),
    (365, "cultivating trust by reflecting on daily experiences of kindness from others, moral order in nature, and protection from harm", "cultivating trust through daily experience of divine presence expressed through love, wisdom, justice, and protection"),
    (372, "self-importance as thinking that overestimates your personal contribution by more than 50% of the actual outcome", "self-importance as distorted thinking"),
    (374, "reduce your exposure to people, places, and media that fuel craving and lead to attachment by half", "reduce exposure to stimuli"),
    (393, "The Bhagavad Gita and related Vedic texts provide time-tested guidance for righteous living", "Established scriptures provide time-tested guidance for righteous living"),
    (415, "devotion that maintains focus on one deity form for at least 20 minutes without the mind wandering to other objects", "Single-Minded Devotion to a Personal Deity"),
    (430, "one dedicated session per week of 30–60 minutes for sorting possessions, donating items not required for your basic needs, and reflecting on attachment", "one period per week of reducing non-essential possessions and commitments and reflection"),
    (448, "According to the Bhagavad Gita, sincere worship supports spiritual progress; all forms of worship are expressions of the one Supreme Being", "All sincere worship elevates the devotee"),
    (470, "Give privately, in a manner that preserves the recipient's dignity and avoids public embarrassment", "Give at the right place and time, with respect and dignity"),
    (472, "gives in a way that the recipient can accept without feeling shamed, such as privately rather than publicly", "honors the recipient's dignity"),
    (484, "Substitute the pursuit of personal pleasure with the measurable increase in positive mood (self-rated 1–10) reported by you within 24 hours of giving", "joy of giving"),
    (483, "the the", "the"),
    (525, "After each study session, spend 10 minutes in silent meditation to internalize the teaching", "Complement external teaching with inward meditation"),
    (531, "notice that many individuals who were self-taught or dropped out of formal education succeeded", "notice that individuals who were self-taught or dropped out of formal education succeeded"),
    (548, "resulting in at least one fewer impulsive reaction per day, measured by journaling", "resulting in reduced reactivity"),
    (572, "Move beyond faith that depends only on what your senses can perceive", "Move beyond conditional faith"),
    (590, "practices such as daily meditation, scriptural study, or selfless service that you selected through study or trusted recommendation", "specific practices you have selected through study or trusted recommendation"),
    (610, "Healthy skepticism examines claims against evidence and experience while remaining open to new information; blind faith accepts claims without examination or evidence", "Healthy skepticism and blind faith are distinct"),
    (631, "The chapter teaches that this understanding can reduce violence, selfishness, and conflict for practitioners who apply it consistently", "This understanding eliminates violence, selfishness, and conflict"),
    (634, "This means recognizing that both you and the other person possess the same capacity for awareness, moral reasoning, and suffering", "the same consciousness flows through both of you"),
    (640, "acknowledge the interconnectedness of all life in daily experiences", "acknowledge the presence of the sacred in ordinary phenomena"),
    (643, "Let this understanding guide you to treat others with the same respect you would want for yourself", "Let this understanding guide how you treat others"),
    (654, "Don't let differences in skill, status, or behavior change how you respect another person's inherent worth", "Don't let differences in skill, status, or behavior create inner division"),
    (660, "According to the Bhagavad Gita, the wise see God in all beings", "The wise see God in all beings and therefore treat everyone with equal respect and compassion"),
    (661, "This means that at the level of fundamental consciousness, all beings share the same capacity for awareness and suffering", "Metaphorically, at the level of the soul, there is no difference between any two beings"),
    (662, "The chapter identifies seeing others as fundamentally different as a common cause of violence and conflict in the epic's narrative", "Seeing others as different from you is the root of violence and conflict"),
    (671, "Practice empathy by imagining yourself in the other person's situation for 30 seconds, then returning to your own perspective to avoid overwhelm", "Practice feeling others' pain as your own without being overwhelmed"),
    (674, "add_after", "Seeing others as different from you is the root of violence and conflict", "Treat this as a conceptual illustration, not a literal causal claim"),
    (684, "Work aligned with your nature, even if difficult, reduces chronic stress and increases daily satisfaction", "Work aligned with your nature, even if difficult, sustains inner peace"),
    (687, "The Bhagavad Gita classifies humanity by inherent qualities into four categories", "Humanity is classified by inherent qualities in traditional texts"),
    (718, "Work aligned with one's innate nature reduces chronic stress and increases daily energy; work forced against one's nature increases fatigue and dissatisfaction", "Work aligned with one's innate nature produces peace; work forced against one's nature creates suffering"),
    (744, "not cling to pleasure, not avoid pain, and not identify with the sense of being the sole doer", "free from attachment to pleasure, free from aversion to pain, and free from ego"),
    (765, "Choose environments and media that promote focused thinking and reduce anxiety, such as nature walks, study materials, and calm music", "Choose environments and media that promote clarity and peace"),
    (775, "Liberation requires recognizing that your true identity is the witness of these modes, not the modes themselves", "Liberation requires seeing through the illusion that these modes define who you are"),
    (789, "Start with one physical action such as standing up, stretching, or walking for 5 minutes", "Start with just 5 minutes of effort"),
    (801, "This means that self-knowledge directly dispels the ignorance that causes suffering, reducing the mental patterns that lead to harmful actions", "Self-knowledge is like fire that reduces old karmic bonds"),
    (811, "Spend time reflecting on specific observations: all physical objects change over time, and all beings share the same basic needs for safety and belonging", "Spend time learning truths about impermanence and the unity of all beings"),
    (812, "Practice mentally offering your actions and their fruits to something greater than yourself, reducing the mental habit of claiming sole ownership", "Work toward freedom from the feeling of 'I' and 'my'"),
    (832, "According to Chapter 15, without self-knowledge, lasting inner peace is elusive", "Without self-knowledge, lasting inner peace is elusive"),
    (854, "devotion that redirects attention back to the divine within 3 seconds of distraction, sustained for 30 minutes daily", "single-minded devotion"),
    (860, "According to the Bhagavad Gita, past mistakes can be transformed through sincere repentance and surrender", "Past mistakes can be transformed through sincere repentance and surrender"),
    (872, "Cultivate faith in God", "Cultivate unconditional faith in God"),
    (876, "sincere effort is valuable in at least 80% of cases where practical constraints do not limit capacity", "Accept that it is never too late to begin a spiritual life"),
    (886, "According to the Bhagavad Gita, past mistakes can be transformed through sincere repentance and surrender", "Past mistakes can be transformed through sincere repentance and surrender"),
    (893, "According to the Gita, surrender does not mean abandoning critical thinking", "Surrender does not mean abandoning critical thinking or discernment"),
    (898, "The process of enlightenment begins when you stop blaming and start looking inward", "Enlightenment begins the moment you stop blaming and start looking inward with honesty"),
    (910, "Austerity of deed: show respect to teachers and wise persons, maintain cleanliness through regular hygiene, and practice non-violence", "Austerity of deed (respect to teachers, physical purity, non-violence)"),
    (911, "Austere of word: speak only words that are truthful, kind, and constructive", "Austere of word (truthful, pleasant, beneficial speech)"),
    (912, "and austerity of thought: cultivate calmness by redirecting angry or anxious thoughts, and practice self-control by pausing before reacting", "and austerity of thought (serenity, gentle thoughts, self-control)"),
    (942, "According to the Bhagavad Gita, austerity must be practiced without desire for personal reward", "Austerity must be practiced without desire for personal reward"),
    (943, "According to the Gita, actions without sincere intention are ineffective and produce no meaningful spiritual results", "Actions without sincere intention are ineffective and produce no meaningful results"),
    (966, "Use the practice of detachment to gradually reduce craving by observing desires without acting on them, redirecting attention to spiritual practices", "Use the practice of detachment to cut the roots of desire and attain liberation"),
    (972, "Treat work as action performed without attachment to specific outcomes, mentally offering the effort to the welfare of all", "Treat work as desireless action offered to the divine"),
    (974, "examine whether it is avoidance of responsibility disguised as renunciation, or a necessary change to align with your nature", "examine whether it is true abandonment or necessary change"),
    (981, "serves the purpose of inspiring others toward self-realization and ethical living", "serves the highest devotional purpose"),
    (984, "Practice it by pausing for 3 seconds before speaking or acting to consider whether your response aligns with this quality", "Practice it deliberately in your regular interactions"),
    (987, "Recognize that neither material achievements nor spiritual identity constitute the unchanging reality itself", "Recognize that both material achievements (temporal) and spiritual identity (eternal) are not the unchanging reality beyond them"),
    (1009, "According to the Gita, freedom from the karmic cycle is attained not by abandoning duty", "freedom from the karmic cycle is attained not by abandoning duty"),
    (1010, "A primary goal of human life, according to the Gita, is to realize the divine within and live without attachment to the fruits of action", "The goal of human life"),
    (1011, "According to the Gita, where devotion is present, victory and moral character follow", "there is lasting well-being, victory, welfare, and moral character"),
    (1022, "rest in the state of observing thoughts and sensations without identifying with them", "rest in pure awareness"),
    (1023, "rest in your true nature as awareness", "rest in pure awareness"),
    (1037, "According to the Gita, true renunciation is not the absence of action but the absence of attachment to results", "True renunciation is not the absence of action but the absence of attachment to results"),
    (1038, "Perform your prescribed duty without attachment to outcomes, and you will achieve liberation", "Perform your duty without attachment to outcomes, and you will achieve liberation"),
    (1039, "According to the Bhagavad Gita, actions performed without faith produce no spiritual results", "actions performed without faith produce no results"),
    (1040, "The Gita states that the wise see all beings with equal vision, recognizing the same divine consciousness in everyone", "the wise see all beings with equal vision"),
    (1049, "presiding deities of fate and karma", "presiding deities (fate/karma)"),
    (1059, "presiding deities of fate and karma", "presiding deities (fate/karma)"),
    (1067, "supreme and most secret knowledge", "king of all knowledge and most secret knowledge"),
    (1074, "frequently leading to attachment", "often leading to attachment"),
    (1077, "supreme and most secret knowledge", "king of all knowledge and most secret knowledge"),
]

# Check line 483 for "the the" typo
for i, line in enumerate(lines):
    if "the the" in line:
        print(f"Found 'the the' typo at line {i+1}: {line.strip()}")

# Check specific lines
for lineno in [167, 168, 190, 365, 374, 448, 483, 548, 590, 674, 832, 872, 898, 911, 912, 1010, 1011]:
    if lineno <= len(lines):
        print(f"Line {lineno}: {lines[lineno-1].strip()}")
