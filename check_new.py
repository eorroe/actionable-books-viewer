#!/usr/bin/env python3

filepath = "/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_59125815-2586-4203-86df-c64414e24637/FRUT-SPIRITUAL-WISDOM-DAILY/BOOK.md"

with open(filepath, 'r') as f:
    content = f.read()

new_strings = [
    "a daily spiritual guide covering all 18 chapters",
    "a genuine moral dilemma",
    "paralyzed by fear of consequences",
    "cultivate equanimity",
    "deepen devotion, practice single-minded worship",
    "identifying with the soul brings inner peace",
    "fosters humility",
    "According to the teaching, inaction itself carries karmic consequences",
    "According to the Bhagavad Gita, selfless action protects one from the fear of birth and death",
    "treat both success and failure as temporary states that do not define your identity",
    "Begin with simpler tasks",
    "The Tortoise Method (withdrawing attention at the first impulse)",
    "The mind is your greatest friend if controlled, and your worst enemy if not",
    "Channel surplus energy",
    "positive associations",
    "The modes are not enemies to be destroyed but forces to be understood and transcended",
    "Liberation comes from seeing through the illusion that these modes define who you are",
    "Treating Pleasure and Pain Equally",
    "innate biological drives",
    "equal respect and attention",
    "Treat all people equally",
    "cultivating trust through daily experience of divine presence expressed through love, wisdom, justice, and protection",
    "self-importance as distorted thinking",
    "reduce exposure to stimuli",
    "Established scriptures provide time-tested guidance for righteous living",
    "Single-Minded Devotion to a Personal Deity",
    "one period per week of reducing non-essential possessions and commitments and reflection",
    "All sincere worship elevates the devotee",
    "Give at the right place and time, with respect and dignity",
    "honors the recipient's dignity",
    "joy of giving",
    "the",
    "Complement external teaching with inward meditation",
    "notice that individuals who were self-taught or dropped out of formal education succeeded",
    "resulting in reduced reactivity",
    "Move beyond conditional faith",
    "specific practices you have selected through study or trusted recommendation",
    "Healthy skepticism and blind faith are distinct",
    "This understanding eliminates violence, selfishness, and conflict",
    "the same consciousness flows through both of you",
    "acknowledge the presence of the sacred in ordinary phenomena",
    "Let this understanding guide how you treat others",
    "Don't let differences in skill, status, or behavior create inner division",
    "The wise see God in all beings and therefore treat everyone with equal respect and compassion",
    "Metaphorically, at the level of the soul, there is no difference between any two beings",
    "Seeing others as different from you is the root of violence and conflict",
    "Practice feeling others' pain as your own without being overwhelmed",
    "Work aligned with your nature, even if difficult, sustains inner peace",
    "Humanity is classified by inherent qualities in traditional texts",
    "Work aligned with one's innate nature produces peace; work forced against one's nature creates suffering",
    "free from attachment to pleasure, free from aversion to pain, and free from ego",
    "Choose environments and media that promote clarity and peace",
    "Liberation requires seeing through the illusion that these modes define who you are",
    "Start with just 5 minutes of effort",
    "Self-knowledge is like fire that reduces old karmic bonds",
    "Spend time learning truths about impermanence and the unity of all beings",
    "Work toward freedom from the feeling of 'I' and 'my'",
    "Without self-knowledge, lasting inner peace is elusive",
    "single-minded devotion",
    "Past mistakes can be transformed through sincere repentance and surrender",
    "Cultivate unconditional faith in God",
    "Accept that it is never too late to begin a spiritual life",
    "Past mistakes can be transformed through sincere repentance and surrender",
    "Surrender does not mean abandoning critical thinking or discernment",
    "Enlightenment begins the moment you stop blaming and start looking inward with honesty",
    "Austerity of deed (respect to teachers, physical purity, non-violence)",
    "Austere of word (truthful, pleasant, beneficial speech)",
    "and austerity of thought (serenity, gentle thoughts, self-control)",
    "Austerity must be practiced without desire for personal reward",
    "Actions without sincere intention are ineffective and produce no meaningful results",
    "Use the practice of detachment to cut the roots of desire and attain liberation",
    "Treat work as desireless action offered to the divine",
    "examine whether it is true abandonment or necessary change",
    "serves the highest devotional purpose",
    "Practice it deliberately in your regular interactions",
    "Recognize that both material achievements (temporal) and spiritual identity (eternal) are not the unchanging reality beyond them",
    "freedom from the karmic cycle is attained not by abandoning duty",
    "The goal of human life",
    "there is lasting well-being, victory, welfare, and moral character",
    "rest in pure awareness",
    "rest in pure awareness",
    "True renunciation is not the absence of action but the absence of attachment to results",
    "Perform your duty without attachment to outcomes, and you will achieve liberation",
    "actions performed without faith produce no results",
    "the wise see all beings with equal vision",
    "presiding deities (fate/karma)",
    "presiding deities (fate/karma)",
    "king of all knowledge and most secret knowledge",
    "often leading to attachment",
    "king of all knowledge and most secret knowledge",
]

found = []
not_found = []
for s in new_strings:
    if s in content:
        found.append(s)
    else:
        not_found.append(s)

print(f"Total new strings: {len(new_strings)}")
print(f"Found: {len(found)}")
print(f"Not found: {len(not_found)}")
if not_found:
    print("\n=== NOT FOUND ===")
    for s in not_found:
        print(s)
