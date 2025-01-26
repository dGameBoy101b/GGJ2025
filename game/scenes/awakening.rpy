init:
    default loop_count = 0

label start:
    $ player_name = "Me" #Ciel always forgets her own name
    $ loop_count += 1
    $ renpy.block_rollback()
    
    play music shipwreck if_changed
    scene black
    player "{cps=*.5}Owww, my head...{/cps}"

    show shipwreck with moveintop
    player "Where am I?"

    show shipwreck:
        linear .5 xoffset -500
        pause 1
        linear .5 xoffset 0
    show hostage neutral at offscreenleft:
        pause 1.5
        linear .5 xalign 0.0
    extend "{nw=2.05}"

    hostage "I have no idea."

    show shipwreck with vpunch
    player "Ack! Who are you?"

    hostage "You don't remember me?..."
    
    player "Not one bit."
    
    show host snarky:
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear .1 align (0.5, 1.0)
    play music gameshow volume 0.5
    host "She's your prize! If you can make it to the end of our fantabulous foray into your forgotten memories!"
    
    show shipwreck with vpunch
    player "Ohmygod! What the fuck is that?!"
   
    $ host_name = "Host"
    host questioning "A bit rude... but I'm your wonderful host!\nHere to guide you through this splendiferous voyage!"
    "I need to get the hell out of here, away from these creeps!"

    host "Join me in a game of..."

    show shipwreck with hpunch
    play sound fanfare
    host snarky "POP QUIZ!!!"

    host questioning "The game is simple. Each round I'll ask you a question about our delightful judge over there. You answer. And she'll tell us whether you got it right or wrong!"
    host "Get it right and you move onto the next round! Get it wrong and I have a {i}fun{/i} surprise in store for you!"
    player "What if I don't want to answer...?"
    host disbelief "Well, I guess we'll be down here long time and that little bubble of yours ain't infinite..."
    "It's only now I realise the spherical iridecent film surrounding me."
    "What's worse yet is the oceans-worth of water pressure squeezing down on my prison come lifeline."
    host questioning "Besides we wouldn't want to bore our audience now would we?"
    player "I suppose not..."
    host snarky "Without further ado, it's time for the first question!"
    jump question1
