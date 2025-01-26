init:
    default question3_here = False
    default question3_coffee = False
    default question3_art = False
    default question3_class = False
    default question3_beach = False

label question3:
    show hostage neutral
    menu:
        host questioning "Final question: Where did you first meet Cordelia?"
        "Art Show" (correct=True) if question3_beach: #needs to be dependent multiple wrong answers in previous questions
            jump question3_art
        "Beach" if question3_here:
            jump question3_beach
        "Coffee Shop" if False: #needs to be dependent on 1 wrong answer in previous questions
            jump question3_coffee
        "Literature Class" if False: #needs to be dependent on 1 wrong answer in previous questions
            jump question3_class
        "Wherever here is":
            jump question3_here

label question3_coffee:
    $ question3_coffee = True
    $ renpy.block_rollback()

    play sound failure
    jump start

label question3_here:
    $ question3_here = True
    $ renpy.block_rollback()
    player "I met her here didn't I?"
    host questioning "A chance happening one might say hmm?"
    player "Yeah...{w=.5} I still don't know why or how I'm here in the first place."
    host snarky "Quite the confounding mystery to be sure!"
    host questioning "But will our gorgeous judge be intrigued?"
    hostage frustrated "What?! No!"
    play sound failure
    host snarky "Sounds like a wrong answer to me!"
    hostage "God! I can't believe you interrupted our beach date for this farce!"
    player "Date? You mean I had a shot at someone as beautiful as you?!{w} And it worked?!"
    host disbelief "Ah, ah, ah! No spoilers my dear."
    host questioning "And it's bedtime for you young missy."
    show black with dissolve
    play music shipwreck fadeout 3 fadein 1
    "Oh no... I'm pasing out again..."
    "{cps=*.5}I hope Cordelia won't be too mad at me...{/cps}"
    jump start

label question3_art:
    $ question3_art = True
    $ renpy.block_rollback()
    player "I remember it clearly."
    player "I was just minding my own business, walking to class, until someone suddenly grabbed me!"
    player "I turn to look at my potential kidknapper, ready to run or scream or something."
    show hostage proud
    player "But imagine my surprise when I lock eyes with {i}this{/i} drop-dead woman who insists on showing me something."
    player "That something being her exhibit at the local art gallery."
    player "Afterwards she invited me back to hang out more, which I of course agreed to."
    player "And the rest is history."
    host snarky "What a truely heart felt story!"
    host questioning "I ahh..."
    play music shipwreck fadeout 1 fadein 1
    host disbelief "Gosh, what am I even doing?"
    extend " You should go."
    "The bubbles surrounding myself and Cordelia pop. Leaving me struggling for air."
    scene black with disolve
    "The last thing I see is Cordelia swimming over to me in a panic and scooping me up."
    host "{cps=*.5}Look after my dearest daughter...{/cps}"
    return #jump escape

label question3_class:
    $ question3_class = True
    $ renpy.block_rollback()

    play sound failure
    jump start

label question3_beach:
    $ question3_beach = True
    $ renpy.block_rollback()
    player "We were on a beach date right? So I must have met her there."
    host questioning "A date you say? On the beach huh?"
    extend snarky " What a steamy revelation folks! Our contestant here, thinks she was on a date of all things with our beautiful judge!"
    host disbelief "Quite the delusion I must say!"
    host questioning "But let's confirm it with our judge shall we?"
    extend "Dearest judge, did this lowly human first meet you at the beach?"
    hostage "Well we were having a lovely date by the beach."
    extend frustrated "Until you fucking {i}abducted{/i} us!"
    host snarky "Details, details, my sweet!"
    host questioning "And you still haven't answered the question: was that your first meeting?"
    hostage neutral "No..."
    play sound failure
    host "Ooo... too bad!"
    host snarky "From the top!"
    scene black with dissolve
    play music shipwreck fadeout 3 fadein 1.0
    "Dammit. We were so close..."
    hostage "{cps=.5}Remember the art gallery!...{/cps}"
    jump start