# builder.py
import json
import os

# Load a room layout from layouts folder
def load_layout(theme_name: str):
    layouts_dir = os.path.join(os.path.dirname(__file__), "layouts")
    filename = f"{theme_name.lower().replace(' ', '_')}.json"
    path = os.path.join(layouts_dir, filename)

    if not os.path.exists(path):
        print(f"⚠️ Layout not found for theme '{theme_name}', using default layout.")
        # Return a default empty layout
        return {"items": []}

    with open(path, "r") as f:
        return json.load(f)

# Optional: placeholder function if we want to expand
def build_room(layout):
    # For now, just return items to main.py
    return layout.get("items", [])
