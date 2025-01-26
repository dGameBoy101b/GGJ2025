init:
    default question1_red = False
    default question1_yellow = False
    default question1_green = False
    default question1_blue = False

label question1:
    menu:
        host questioning "What is the favourite colour of our fabulous judge over there?"
        "red":
            jump question1_red
        "yellow":
            jump question1_yellow
        "green":
            jump question1_green
        "blue" (correct=True):
            jump question1_blue

label question1_wrong:
    hostage frustrated "Obviously blue is my favourite colour."
    hostage "I'm even wearing a blue dress!"
    host snarky "How unfortunate! Looks like it's time for your punishment!"
    player "Punishment?! You never said anything about a punishment!"
    host questioning "Oh don't worry, you won't feel a thing."
    scene black with dissolve
    play music shipwreck fadeout 3 fadein 1
    "The adrenaline that's been racing through me seems to slow to a crawl."
    host "{cps=*.5}Just let it all wash away...{/cps}"
    jump start

label question1_red:
    $ question1_red = True
    $ renpy.block_rollback()
    player "Red."
    hostage "Eww, no."
    play sound failure
    host "Wowzers! Quite the sharp tongue there. No holding back!"
    jump question1_wrong

label question1_yellow:
    $ question1_yellow = True
    $ renpy.block_rollback()
    player "Yellow?"
    hostage "What gave you that idea?"
    hostage "Do you see any {i}yellow{/i} around here?"
    host snarky "Why my dearest judge I don't believe one might find even a speck of radiant yellow~"
    host questioning "We are quite far down you see..."
    hostage frustrated "Of course not!"
    play sound failure
    host snarky "Looks like our contestant might be a little colourblind!"
    jump question1_wrong

label question1_green:
    $ question1_green = True
    $ renpy.block_rollback()
    player "Green..."
    extend " I think."
    hostage "While I do like it, I don't think I could say it's my favourite..."
    play sound failure
    host snarky "So close! Yet so far..."
    jump question1_wrong

label question1_blue:
    $ question1_blue = True
    $ renpy.block_rollback()
    player "Definitely blue."
    player "She can't go anywhere without her favourite blue dress."
    host snarky "Well, well, well! That's quite a lot of confidence you have there. But does it pay off?"
    hostage proud "She's right!"
    play sound success
    host "Well done! Round of applause!"
    host questioning "Time for question 2."
    jump question2