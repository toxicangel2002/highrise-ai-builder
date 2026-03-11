import json
import os
import random


def load_layout(theme):

    path = f"layouts/{theme}.json"

    if not os.path.exists(path):

        print("Layout not found, using cozy")

        path = "layouts/cozy.json"

    with open(path) as f:

        layout = json.load(f)

    return layout


def build_room(layout):

    print("Starting room build...")

    items = layout["items"]

    for item in items:

        tag = item["tag"]
        x = item["x"]
        y = item["y"]

        print(f"Placing {tag} at position ({x}, {y})")

    print("Room build complete!")
