init:
    define hostage_name = "hot girl"
    define hostage_outline_color = "#5588ff"
    define hostage = Character(name="hostage_name", dynamic=True, 
        who_color="#0000ff", who_prefix="{outlinecolor=[hostage_outline_color]}", who_suffix="{/outlinecolor}", 
        image="hostage")

    transform hostage_transform:
        ysize 1000
        fit "contain"

    image hostage = At("characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Defaultt.PNG", hostage_transform)
    image hostage neutral = At("characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Defaultt.PNG", hostage_transform)
    image hostage frustrated = At("characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Upset.PNG", hostage_transform)
    image hostage proud = At("characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Proud.PNG", hostage_transform)