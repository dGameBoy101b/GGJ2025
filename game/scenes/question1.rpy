init:
    default question1_red = False
    default question1_yellow = False
    default question1_green = False
    default question1_blue = False

label question1:
    menu:
        host "What is the favourite colour of our fabulous guest over there?"
        "red":
            jump question1_red
        "yellow":
            jump question1_yellow
        "green":
            jump question1_green
        "blue" (correct=True):
            jump question1_blue

label question1_wrong:
    hostage "Obviously blue is my favourite colour."
    hostage "I'm even wearing a blue dress!"
    host "How unfortunate! Looks like it's time for your punishment!"
    jump start

label question1_correct:
    play sound success
    hostage "She's right!"
    host "Well done! Round of applause!"
    host "Time for question 2."
    jump question2

label question1_red:
    $ question1_red = True
    $ renpy.block_rollback()
    player "Red."
    play sound failure
    hostage "Eww, no."
    host "Wowzers! Quite the sharp tongue there. No holding back!"
    jump question1_wrong

label question1_yellow:
    $ question1_yellow = True
    $ renpy.block_rollback()
    player "Yellow?"
    play sound failure
    hostage "What gave you that idea?"
    hostage "Do you see any {i}yellow{/i} around here?"
    host "Why my dearest guest I don't believe one might find even a speck of radiant yellow~"
    host "We are quite far down you see..."
    hostage "Of course not!"
    jump question1_wrong

label question1_green:
    $ question1_green = True
    $ renpy.block_rollback()
    player "Green..."
    play sound failure
    extend " I think."
    hostage "While I do like it, I don't think I could say it's my favourite..."
    host "So close yet so far..."
    jump question1_wrong

label question1_blue:
    $ question1_blue = True
    $ renpy.block_rollback()
    player "Definitely blue."
    player "She can't go anywhere without her favourite blue dress."
    host "Well, well, well! That's quite a lot of confidence you have there. But does it pay off?"
    jump question1_correct