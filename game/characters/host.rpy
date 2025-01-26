init:
    define host_name = "weird tentacle thing"
    define host_outline_color = "#0000ff"
    define host = Character(name="host_name", dynamic=True, image="host", 
        who_color="#ff00ff", who_prefix="{outlinecolor=[host_outline_color]}", who_suffix="{/outlinecolor}")
    
    image host = "characters/Host/HostQuestioning.PNG"
    image host disbelief = "characters/Host/HostDisbelief.PNG"
    image host snarky = "characters/Host/HostSnarky.PNG"
    