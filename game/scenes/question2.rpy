init:
    default question2_wrong = False
    default question2_cordelia = False
    default question2_alex = False
    default question2_ember = False
    default question2_nia = False
    default question2_zara = False

label question2:
    menu:
        host "What is the name of our beautifully fair maiden guest?"
        "Alex":
            jump question2_alex
        "Cordelia" (correct=True) if question2_wrong:
            jump question2_cordelia
        "Ember":
            jump question2_ember
        "Nia":
            jump question2_nia
        "Zara":
            jump question2_zara

label question2_wrong:
    $ question2_wrong = True

    jump start

label question2_correct:

    jump question3

label question2_cordelia:
    $ question2_cordelia = True
    $ renpy.block_rollback()

    jump question2_correct

label question2_alex:
    $ question2_alex = True
    $ renpy.block_rollback()

    jump question2_wrong

label question2_ember:
    $ question2_ember = True
    $ renpy.block_rollback()

    jump question2_wrong

label question2_nia:
    $ question2_nia = True
    $ renpy.block_rollback()

    jump question1_wrong

label question2_zara:
    $ question2_zara = True
    $ renpy.block_rollback()

    jump question2_wrong