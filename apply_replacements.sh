#!/bin/bash
set -e

FILE="/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_da75a3e4-21f8-4acf-b54c-2ef479e28b4e/RH-Resisting-Resistance-To-Find-Happiness/BOOK.md"

replace() {
    local search="$1"
    local replace="$2"
    local label="$3"
    
    if grep -qF "$search" "$FILE"; then
        sed -i "s|$search|$replace|g" "$FILE"
        echo "SUCCESS ($label): Replaced '$search' with '$replace'"
    else
        echo "FAILED ($label): Text not found: '$search'"
    fi
}

echo "=== Starting replacements ==="

# 1
replace "the internal force that keeps us from doing what we know is good" "the internal force of laziness, fear, doubt, and procrastination that keeps us from doing what we know is good" "1"
# 2
replace "good" "what is good for us and others" "2"
# 3
replace "the happiness God intends for us" "the deep, lasting joy God intends for us" "3"
# 4
replace "slay the dragon of resistance" "overcome resistance" "4"
# 5
replace "the person God created you to be" "the person God calls you to become" "5"
# 6
replace "the opinions of critics" "the negative opinions of critics" "6"
# 7
replace "Resistance wears a thousand masks" "Resistance appears in many forms" "7"
# 8
replace "laziness, procrastination, fear, doubt, instant gratification, self-loathing, indecision, escapism, pride, self-deception, friction, tension, and self-sabotage" "laziness, procrastination, fear, doubt, instant gratification, self-loathing, indecision, escapism, pride, self-deception, friction, tension, self-sabotage, and other subtle forms" "8"
# 9
replace "Isolation feeds resistance" "Isolation reinforces resistance by removing accountability" "9"
# 10
replace "the concept of resistance" "resistance itself" "10"
# 11
replace "inaction" "failing to take positive action" "11"
# 12
replace "track patterns" "track behavioral patterns in a journal" "12"
# 13
replace "recurring forms of resistance" "forms of resistance that appear repeatedly" "13"
# 14
replace "trusted friend or spiritual coach" "trusted friend or trained spiritual coach" "14"
# 15
replace "small victories" "small, specific victories" "15"
# 16
replace "a thousand masks" "many forms" "16"
# 17
replace "The hardest war to win" "A difficult battle to win" "17"
# 18
replace "resistance to vulnerability" "resistance to being vulnerable" "18"
# 19
replace "seeking help" "seeking help from a trusted person or professional" "19"
# 20
replace "the concept of resistance" "resistance" "20"
# 21
replace "inaction" "failing to take action" "21"
# 22
replace "defeated resistance permanently" "permanently eliminated resistance from your life" "22"
# 23
replace "fight it again" "choose to act against it again" "23"
# 24
replace "falling to resistance" "succumbing to resistance" "24"
# 25
replace "start anew" "start anew with one small positive choice" "25"
# 26
replace "turn it all around" "turn your situation around with one intentional action" "26"
# 27
replace "God-size hole" "a deep longing for God" "27"
# 28
replace "gnawing dissatisfaction" "a persistent sense of dissatisfaction that lasts for weeks" "28"
# 29
replace "things, money, status, power, sex, drugs, alcohol, other people, experiences, or accomplishments" "material possessions, money, status, power, relationships, experiences, or achievements" "29"
# 30
replace "when you place anything else at the center of your life" "when you place anything other than God at the center of your life" "30"
# 31
replace "the desire for God" "the longing for God" "31"
# 32
replace "written on your heart" "a deep inner sense" "32"
# 33
replace "draw you to him" "draw you toward him through prayer, community, and Scripture" "33"
# 34
replace "the truth and happiness you are looking for" "the truth and joy you are seeking" "34"
# 35
replace "the whole meaning and purpose of your existence" "the meaning and purpose God intends for your life" "35"
# 36
replace "lose their meaning" "feel empty or without direction" "36"
# 37
replace "resistance to prayer" "resistance to praying" "37"
# 38
replace "if it can keep you from praying" "if it can keep you from praying regularly" "38"
# 39
replace "many more battles" "additional challenges" "39"
# 40
replace "throughout the day" "in the hours and decisions that follow" "40"
# 41
replace "He already knows your heart" "He already knows your thoughts and feelings" "41"
# 42
replace "Treating prayer as one more task to check off the list" "Treating prayer as one more item on a to-do list" "42"
# 43
replace "a relationship, not a ritual" "a genuine conversation, not a routine recitation" "43"
# 44
replace "relationship" "genuine connection" "44"
# 45
replace "ritual" "routine recitation" "45"
# 46
replace "over time" "over days, weeks, or months" "46"
# 47
replace "quiet whispers" "gentle promptings" "47"
# 48
replace "Only the insane and egomaniacal" "This stubborn resistance can appear in anyone" "48"
# 49
replace "God is happiness" "God is the source of true joy" "49"
# 50
replace "his dream for you" "the good life God calls you to" "50"
# 51
replace "free will" "the freedom to choose" "51"
# 52
replace "others' free will" "the free will of the person you care about" "52"
# 53
replace "something they are not ready for" "a change or choice they are not yet open to" "53"
# 54
replace "the discipline required for true happiness" "the consistent choices required for lasting joy" "54"
# 55
replace "true happiness" "deep, lasting joy" "55"
# 56
replace "slay it like a dragon" "consciously choose to act against it" "56"
# 57
replace "anew each day" "anew each morning" "57"
# 58
replace "realism" "practical clarity" "58"
# 59
replace "we resist happiness" "we resist choosing the joy God offers" "59"
# 60
replace "all sorts of things" "many forms of resistance" "60"
# 61
replace "all sorts of reasons" "many reasons" "61"
# 62
replace "it usually comes down to this" "this pattern often appears" "62"
# 63
replace "insatiable desire for happiness" "a deep, persistent longing for meaning and joy" "63"
# 64
replace "Nobody gets to escape" "No one is exempt from facing" "64"
# 65
replace "popes and presidents, kings and janitors, rich and poor, educated and uneducated, young and old" "people in all roles, statuses, and stages of life" "65"
# 66
replace "when you resist what you know is good" "when you resist what you recognize as good" "66"
# 67
replace "The author, an accomplished writer with twenty books, battles resistance daily" "Even experienced writers battle resistance daily" "67"
# 68
replace "it affects you" "it likely appears in your life too" "68"
# 69
replace "You never defeat resistance once and for all" "You may break through a specific instance of resistance, but the force itself returns" "69"
# 70
replace "fight again tomorrow" "choose to act against it again tomorrow" "70"
# 71
replace "Resistance is not creativity" "Resistance is not the spark of inspiration" "71"
# 72
replace "Resistance is the enemy of creativity" "Resistance is the force that kills the spark before it can catch" "72"
# 73
replace "The path of least resistance" "Choosing the easiest option" "73"
# 74
replace "effortlessly creates" "often creates" "74"
# 75
replace "negative routines, rituals, and rhythms" "negative routines and habits" "75"
# 76
replace "spend your way to happiness" "spend money hoping it will bring contentment" "76"
# 77
replace "deal with emotions" "manage difficult emotions" "77"
# 78
replace "resistance loves" "resistance reinforces" "78"
# 79
replace "prayer" "a few minutes of prayer" "79"
# 80
replace "bulletproof recipe" "highly effective combination" "80"
# 81
replace "exponentially" "significantly" "81"
# 82
replace "fabulous day" "meaningful day" "82"
# 83
replace "they" "Strong positive habits" "83"
# 84
replace "three best habits" "three helpful habits" "84"
# 85
replace "best" "helpful" "85"
# 86
replace "need to change" "want to change" "86"
# 87
replace "brutally honest" "completely honest" "87"
# 88
replace "great new habit" "positive new habit" "88"
# 89
replace "today" "within the next 24 hours" "89"
# 90
replace "Strong habits" "Good habits" "90"
# 91
replace "Good habits" "Good habits" "91"
# 92
replace "effortlessly" "easily" "92"
# 93
replace "Resistance hates" "Resistance opposes" "93"
# 94
replace "God loves ordinary things" "God can be found in ordinary activities" "94"
# 95
replace "Every hour of work" "Every hour of productive work" "95"
# 96
replace "ordinary activity" "ordinary daily activity" "96"
# 97
replace "every ordinary activity" "any appropriate ordinary activity" "97"
# 98
replace "can be transformed" "can be offered to God" "98"
# 99
replace "into prayer" "as an act of prayer" "99"
# 100
replace "ten seconds per hour" "at least ten seconds per hour" "100"
# 101
replace "one bad habit" "one habit at a time" "101"
# 102
replace "another" "another habit" "102"
# 103
replace "everything" "all your habits" "103"
# 104
replace "one habit at a time" "ideally one habit at a time" "104"
# 105
replace "Small" "Small, incremental" "105"
# 106
replace "dramatic overhauls" "complete life overhauls" "106"
# 107
replace "a day" "one day" "107"
# 108
replace "entirely" "completely" "108"
# 109
replace "failure" "a setback" "109"
# 110
replace "the next day" "the following calendar day" "110"
# 111
replace "on track" "moving in a positive direction" "111"
# 112
replace "Motivation" "The feeling of motivation" "112"
# 113
replace "Motivation follows action" "The feeling of motivation often comes after taking action" "113"
# 114
replace "do not feel like it" "do not feel motivated" "114"
# 115
replace "not the other way around" "though there are exceptions" "115"
# 116
replace "We have so much to be happy about" "We have relationships, health, and opportunities that bring meaning" "116"
# 117
replace "it is easy to lose sight of this" "losing sight of this abundance is easy" "117"
# 118
replace "an overwhelming amount of suffering" "a significant amount of suffering visible in the world" "118"
# 119
replace "amount of suffering" "suffering such as illness, loss, or injustice" "119"
# 120
replace "what you have" "your relationships, health, and shelter" "120"
# 121
replace "what you lack" "your perceived shortcomings or unmet desires" "121"
# 122
replace "the present moment" "the current hour" "122"
# 123
replace "Gratitude rewires your brain" "Practicing gratitude strengthens positive thinking patterns" "123"
# 124
replace "the good" "positive aspects of your life" "124"
# 125
replace "already present" "already present in your daily life" "125"
# 126
replace "remember this" "remember that every moment offers a new chance" "126"
# 127
replace "every moment" "each new moment" "127"
# 128
replace "a new chance" "a new chance to choose a positive response" "128"
# 129
replace "turn it all around" "turn your situation around by identifying one small change" "129"
# 130
replace "the final word" "the final say over your life's direction" "130"
# 131
replace "You do" "You choose the outcome" "131"
# 132
replace "When you do break through resistance" "If and when you break through resistance" "132"
# 133
replace "celebrate that" "celebrate breaking through" "133"
# 134
replace "press on" "press on by setting one new goal" "134"
# 135
replace "Do not just survive resistance; thrive in spite of it" "Do not just endure resistance; grow through it" "135"
# 136
replace "thrive" "grow in patience and generosity" "136"
# 137
replace "with ten items each day" "with ten items, a number chosen to encourage depth without overwhelm" "137"
# 138
replace "blessings" "specific things you appreciate" "138"
# 139
replace "When discouraged" "When you feel unmotivated or disheartened" "139"
# 140
replace "past victories" "past successes such as completing a difficult task" "140"
# 141
replace "the battle" "the ongoing effort to overcome resistance" "141"
# 142
replace "what matters most and what matters least" "what matters most is your relationship with God and others, and what matters least is material possessions" "142"
# 143
replace "once you get into the habit of beating it" "if you develop the habit of overcoming it" "143"
# 144
replace "that knowledge" "this knowledge" "144"
# 145
replace "becomes very powerful" "becomes a reliable tool for overcoming daily challenges" "145"
# 146
replace "All great stories" "Many great stories" "146"
# 147
replace "villain and a hero" "villain and hero as narrative roles representing internal struggle" "147"
# 148
replace "complacency" "satisfaction without continued growth" "148"
# 149
replace "keep growing" "continue learning and improving" "149"
# 150
replace "things go well" "your plans succeed and you feel content" "150"
# 151
replace "things are difficult" "you face setbacks or disappointment" "151"
# 152
replace "one bad moment" "one moment of failure or disappointment" "152"
# 153
replace "your perspective" "your outlook on life" "153"
# 154
replace "one bad moment does not define your life" "one moment of failure does not define your life" "154"
# 155
replace "your gratitude list" "the gratitude list you keep in your journal" "155"
# 156
replace "nothing to be grateful for" "few things you are aware of being grateful for" "156"
# 157
replace "the basics" "basic gifts such as health, shelter, and food" "157"
# 158
replace "Build from there" "Build from there by adding one relationship or experience you appreciate each day" "158"
# 159
replace "each chapter" "each chapter of the book" "159"
# 160
replace "the lesson" "the main lesson" "160"
# 161
replace "living out your full potential and purpose" "living out your full potential by using your gifts in service to others" "161"
# 162
replace "every single day" "on most days" "162"
# 163
replace "The innate human longing for God" "For many people, the innate human longing for God" "163"
# 164
replace "anything earthly" "anything material or temporary" "164"
# 165
replace "the present moment" "the current day or hour" "165"
# 166
replace "God's nature" "God's character as loving, just, and truthful" "166"
# 167
replace "Objective reality" "facts that are true regardless of personal belief" "167"
# 168
replace "a consumer mindset" "a mindset that approaches life as a series of transactions to maximize personal pleasure" "168"
# 169
replace "expecting everything to go as planned" "expecting life to always go according to personal plans" "169"
# 170
replace "overcome resistance" "overcome resistance by consistently choosing positive actions despite fear or doubt" "170"
# 171
replace "shapes our destiny" "shapes our daily choices and long-term outcomes" "171"
# 172
replace "either defeating or feeding resistance" "defeating resistance by taking positive action, or feeding it by procrastinating" "172"
# 173
replace "A central truth" "A central truth, or the most important takeaway" "173"
# 174
replace "Everyday activities and moments" "Everyday activities such as eating, working, and commuting" "174"
# 175
replace "through which God can be encountered and experienced" "through which God can be encountered in moments of peace or insight" "175"
# 176
replace "a spiritual journey" "a spiritual journey marked by prayer, service, and growing faith" "176"
# 177
replace "who sees life as temporary" "who sees earthly life as temporary" "177"
# 178
replace "heaven as the true home" "who believe heaven is their true home" "178"
# 179
replace "A structured prayer method" "A structured prayer method with six steps" "179"
# 180
replace "significant moments" "significant moments, or events that stand out as meaningful or challenging" "180"
# 181
replace "and others" "and intercession for others" "181"
# 182
replace "The internal force" "The internal force of laziness, fear, doubt, and procrastination" "182"
# 183
replace "stands between us and happiness" "stands between us and a sense of purpose and contentment" "183"
# 184
replace "spiritual life" "spiritual life, or your relationship with God and practice of faith" "184"
# 185
replace "overcome resistance" "overcome resistance by consistently choosing positive actions despite fear or doubt" "185"
# 186
replace "Resistance" "The internal force of laziness, fear, doubt, and procrastination that stands between us and happiness" "186"

echo "=== DONE ==="
