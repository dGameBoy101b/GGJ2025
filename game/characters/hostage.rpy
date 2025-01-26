init:
    define hostage_name = "hot girl"
    define hostage_outline_color = "#5588ff"
    define hostage = Character(name="hostage_name", dynamic=True, 
        who_color="#0000ff", who_prefix="{outlinecolor=[hostage_outline_color]}", who_suffix="{/outlinecolor}", 
        image="hostage")

    image hostage = "characters/Cordelia/CordeliaNeutral.PNG"
    image hostage frustrated = "characters/Cordelia/CordeliaFrustrated.PNG"
    image hostage proud = "characters/Cordelia/CordeliaProud.PNG"