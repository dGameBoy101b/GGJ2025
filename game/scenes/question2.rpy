init:
    default question2_wrong = False
    default question2_cordelia = False
    default question2_alex = False
    default question2_ember = False
    default question2_nia = False
    default question2_zara = False

label question2:
    menu:
        host "What is the name of our beautiful {i}maiden{/i} judge?"
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
    "My supposed \"judge\" whips around to face the host, indignant and accusatory."
    hostage "Did you really have to steal {i}everything{/i}?!"
    host "Rules are rules I'm afraid.{p} Now your verdict, if you would please?"
    hostage "Well of course she's fucking wrong because you {i}stole it{/i} from her!"
    host "Dear, oh dear~ Looks like our little contestant here has lost the game!"
    hostage "No wait!"
    "The host ignores the judge's pleas."
    #maybe the host chants some kind of catch phrase?
    "She turns to me instead. The fire of determination lighting in her eyes and searing my skin."
    hostage "Damn it! You better remember my fucking name next time!"
    scene black with dissolve
    "My mind becomes drowsy. Thoughts slipping away like air in drowning lungs."
    hostage "It's Cordelia and don't fucking forget!"
    jump start

label question2_correct:
    $ hostage_name = "Cordelia"
    hostage "Well lucky for you, you're right. Took you long enough Ciel."
    player "I'm not that fat, am I?..."
    hostage "'Course not, you're cute as hell."
    host "And I don't see a lick of fur nor whiskers on this one!"
    hostage "What the fuck is that suposed to mean!"
    host "She can't be much of a seal without whiskers now can she?"
    hostage "...Fuck's sake. Ciel, C-i-e-l not seal. It's your name doofus."
    $ player_name = Ciel
    player "Oh...{p} How do you know that?"
    "Cordelia's voice becomes muffled again before she can answer."
    host "-Well I think that's enough banter for this round. Time for question 3!"
    jump question3

label question2_cordelia:
    $ question2_cordelia = True
    $ hostage_name = "Cordelia?"
    $ renpy.block_rollback()
    player "Cordelia. Meaning daughter of the sea."
    host "Oh my, my, my~ however did you learn that little snippet of trivia, huh?"
    player "Ummm... I'm not sure actually. Just kind of came to me once I remembered her name."
    play sound success
    jump question2_correct

label question2_alex:
    $ question2_alex = True
    $ hostage_name = "Alex?"
    $ renpy.block_rollback()
    player "You look like...{p} an Alex to me."
    host "You don't seem so certain of yourself?"
    player "How am I supposed to know the name of whatever stranger you dragged down here with me?"
    host "Only one way to find out!"
    #"The definitely not wierd and monstrous host gestures towards the judge, as if presenting the crown jewel for the commoners below to gawk at."
    jump question2_wrong

label question2_ember:
    $ question2_ember = True
    $ hostage_name = "Ember?"
    $ renpy.block_rollback()
    player "Well she is kinda hot, so Ember?"
    host "Scandalous! Are we witnessing the budding of a passionate romance?!"
    "I feel blood rushing to my cheeks; eager to display my embarassment to whatever audience there might be here."
    host "Can she seduce our majestic judge?!"
    play sound failure
    jump question2_wrong

label question2_nia:
    $ question2_nia = True
    $ hostage_name = "Nia?"
    $ renpy.block_rollback()
    player "You look like you own the streets, so I'm going to go with Nia."
    host "Well that is quite an interest associate you've got there, perhaps you could explain more?"
    player "Err... what else do you want me to say? She looks tough and sharp witted."
    host "What a charmer we have here folks! But tell us this, why Nia of all names?"
    player "Umm... Because it sounds cool...?"
    host "Fabulous! But lets see if this impresses the judge."
    play sound failure
    jump question1_wrong

label question2_zara:
    $ question2_zara = True
    $ hostage_name = "Zara?"
    $ renpy.block_rollback()
    player "I don't know what it is about you, but your everything screams Zara to me."
    host "Quite a bold yet vague assessment there, care to expand upon it?"
    player "Ahh... I don't think I can. There's not any specific thing I put my finger on. Just that I hear Zara whenever I look at her."
    host "An aura or vibe one might say, huh? Or perhaps you've red her mind?!"
    play sound failure
    jump question2_wrong