themes = {
    "dating": [
        "dating",
        "romantic",
        "love",
        "valentine"
    ],

    "gaming": [
        "gaming",
        "game",
        "arcade",
        "streamer"
    ],

    "cozy": [
        "cozy",
        "warm",
        "cottage",
        "fireplace"
    ]
}


def detect_theme(text):

    text = text.lower()

    for theme, words in themes.items():

        for word in words:

            if word in text:

                return theme

    return "cozy"
