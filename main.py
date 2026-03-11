from theme_router import detect_theme
from builder import load_layout, build_room


def handle_command(command):

    if command.startswith("/make"):

        theme = detect_theme(command)

        print(f"Theme detected: {theme}")

        layout = load_layout(theme)

        build_room(layout)


def start_bot():

    print("Highrise AI Builder Bot Started")

    while True:

        command = input("Enter command: ")

        handle_command(command)


if __name__ == "__main__":
    start_bot()
