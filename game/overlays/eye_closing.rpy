init:
    transform eye_transform:
        xysize (1., 1.)
        xycenter (.5, .5)

    image eye open = At("overlays/Blink Open.PNG", eye_transform)
    image eye mid = At("overlays/Blink Mid.PNG", eye_transform)
    image eye closed = At("overlays/Blink Close.PNG", eye_transform)
    image eye none = Null()

    define eye_delay = .5

    image eye closing:
        "eye open" with Dissolve(eye_delay)
        pause eye_delay
        "eye mid" with Dissolve(eye_delay)
        pause eye_delay
        "eye closed" with Dissolve(eye_delay)
        pause eye_delay
        "black" with Dissolve(eye_delay)

    image eye opening:
        "eye closed" with Dissolve(eye_delay)
        pause eye_delay
        "eye mid" with Dissolve(eye_delay)
        pause eye_delay
        "eye open" with Dissolve(eye_delay)
        pause eye_delay
        "eye none" with Dissolve(eye_delay)
