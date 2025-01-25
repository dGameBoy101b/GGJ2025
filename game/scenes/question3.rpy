init:
    default question3_here = False
    default question3_coffee = False
    default question3_art = False
    default question3_class = False
    default question3_beach = False

label question3:
    menu:
        host "Final question: Where did you first meet Cordelia?"
        "Wherever here is":
            jump question3_here
        "Coffee Shop" if False: #needs to be dependent on 1 wrong answer in previous questions
            jump question3_coffee
        "Art Show" (correct=True) if False: #needs to be dependent multiple wrong answers in previous questions
            jump question3_art
        "Literature Class" if False: #needs to be dependent on 1 wrong answer in previous questions
            jump question3_class
        "Beach" if False: #needs to be dependent on 1 wrong answer in previous questions
            jump question3_beach

label question3_wrong:

    jump start

label question3_correct:

    jump escape

label question3_coffee:
    $ question3_coffee = True
    $ renpy.block_rollback()

    jump question3_wrong

label question3_here:
    $ question3_here = True
    $ renpy.block_rollback()

    jump question3_wrong

label question3_art:
    $ question3_art = True
    $ renpy.block_rollback()

    jump question3_correct

label question3_class:
    $ question3_class = True
    $ renpy.block_rollback()

    jump question3_wrong

label question3_beach:
    $ question3_beach = True
    $ renpy.block_rollback()

    jump question3_wrong