
label start:
    $ player_name = "Me" #Ciel always forgets her own name
    
    play music shipwreck
    scene black
    player "Owww, my head..."

    show shipwreck with moveintop
    player "Where am I?"

    show shipwreck:
        linear .5 xalign 1.0
        pause 1
        linear 1 xalign 0.0
    show hostage at offscreenleft:
        pause 2.0
        linear .5 xalign 0.0
    extend "{nw=2.55}"

    hostage "I have no idea."

    show shipwreck with vpunch
    player "Ack! Who are you?"

    hostage "You don't remember me?..."
    
    player "Not one bit."
    
    show host snarky:
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear .1 align (0.5, 1.0)
    play music gameshow
    host "She's your prize! If you can make it to the end of our fantabulous foray into your forgotten memories!"
    
    show shipwreck with vpunch
    player "Ohmygod! What the fuck is that?!"
   
    $ host_name = "Host"
    host -snarky "A bit rude... but I'm your wonderful host!\nHere to guide you through this splendiferous voyage!"
    "I need to get the hell out of here, away from these creeps!"

    host snarky "Join me in a game of...{p}"
    host "POP QUIZ!!!"

    jump question1
