import os
import asyncio
from dotenv import load_dotenv
from highrise import BaseBot
from builder import load_layout
from theme_router import detect_theme

# Load environment variables
load_dotenv()
EMAIL = os.getenv("HR_EMAIL")
PASSWORD = os.getenv("HR_PASSWORD")
ROOM_ID = os.getenv("ROOM_ID")

# Safety check
if not EMAIL or not PASSWORD or not ROOM_ID:
    print("ERROR: Missing environment variables: HR_EMAIL, HR_PASSWORD, ROOM_ID")
    exit(1)

# Define the bot
class BuilderBot(BaseBot):
    async def on_start(self, session_metadata):
        print("✅ Bot connected to Highrise!")
        # Optional: send a message in the room
        await self.highrise.chat("Builder bot online 🤖")

    async def on_chat(self, user, message):
        # Only respond to /make commands
        if message.startswith("/make"):
            theme = detect_theme(message)
            layout = load_layout(theme)

            await self.highrise.chat(f"Building a {theme} room!")

            for item in layout.get("items", []):
                tag = item.get("tag", "unknown")
                x = item.get("x", 0)
                y = item.get("y", 0)
                # For now just print
                print(f"Placing {tag} at ({x},{y})")

# Run the bot
if __name__ == "__main__":
    bot = BuilderBot()
    # Correct Highrise SDK method
    asyncio.run(bot.start(
        email=EMAIL,
        password=PASSWORD,
        room_id=ROOM_ID
    ))
