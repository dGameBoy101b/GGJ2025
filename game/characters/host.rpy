init:
    define host_name = "weird tentacle thing"
    define host_outline_color = "#0000ff"
    define host = Character(name="host_name", dynamic=True, image="host", 
        who_color="#ff00ff", who_prefix="{outlinecolor=[host_outline_color]}", who_suffix="{/outlinecolor}")
    
    transform host_transform:
        ysize 1.0
        fit "contain"

    image host = At("characters/Host/Pops_Sprites/Pops_Sprite_Default.PNG", host_transform)
    image host questioning = At("characters/Host/Pops_Sprites/Pops_Sprite_Default.PNG", host_transform)
    image host disbelief = At("characters/Host/Pops_Sprites/Pop_Sprite_Upset.PNG", host_transform)
    image host snarky = At("characters/Host/Pops_Sprites/Pop_Sprite_Wave.PNG", host_transform)
    