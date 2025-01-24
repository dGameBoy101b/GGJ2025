init:
    define narrator = Character(what_prefix="{i}(", what_suffix="){/i}")
    define player_name = "me"
    define player = Character(name="player_name", dynamic=True, image="player", who_color="#00ffff")

    image player = Placeholder("girl")
    