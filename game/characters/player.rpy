init:
    define narrator = Character(what_prefix="{i}", what_suffix="{/i}")
    define player_name = "me"
    define player_outline_color = "#003ec5"
    define player = Character(name="player_name", dynamic=True, image="player", 
        who_color="#00ffff", who_prefix=f"{{outlinecolor={player_outline_color}}}", who_suffix="{/outlinecolor}")

    image player = Placeholder("girl")
    