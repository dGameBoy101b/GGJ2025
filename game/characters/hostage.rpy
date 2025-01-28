init:
    define hostage_name = "hot girl"
    define hostage_outline_color = "#5588ff"
    define hostage = Character(name="hostage_name", dynamic=True, 
        who_color="#0000ff", who_prefix="{outlinecolor=[hostage_outline_color]}", who_suffix="{/outlinecolor}", 
        image="hostage")

    layeredimage hostage:
        group emotion:
            ysize 1.0
            fit "contain"
            attribute neutral default:
                "characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Defaultt.PNG"
            attribute frustrated:
                "characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Upset.PNG"
            attribute proud:
                "characters/Cordelia/Cordelia_Sprites/Cordelia_Sprite_Proud.PNG"