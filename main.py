# main.py
import os
import asyncio
from dotenv import load_dotenv
from highrise import BaseBot
from theme_router import detect_theme
from builder import load_layout, build_room

# Load environment variables
load_dotenv()
EMAIL = os.getenv("HR_EMAIL")
PASSWORD = os.getenv("HR_PASSWORD")
ROOM_ID = os.getenv("ROOM_ID")

if not EMAIL or not PASSWORD or not ROOM_ID:
    print("ERROR: Missing environment variables. Please set HR_EMAIL, HR_PASSWORD, and ROOM_ID.")
    exit(1)

# Define the bot class
class BuilderBot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot connected to Highrise!")
        await self.highrise.chat("Builder bot online 🤖")

    async def on_chat(self, user, message):
        if message.startswith("/make"):
            theme = detect_theme(message)
            layout = load_layout(theme)
            await self.highrise.chat(f"Building a {theme} room!")

            for item in layout["items"]:
                tag = item["tag"]
                x = item["x"]
                y = item["y"]
                print(f"Placing {tag} at position ({x}, {y})")

# Start the bot
if __name__ == "__main__":
    bot = BuilderBot()
    # Use asyncio to start the bot
    asyncio.run(bot.start(
        email=EMAIL,
        password=PASSWORD,
        room_id=ROOM_ID
    ))
