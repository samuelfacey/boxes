import os
import sys
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

class Boxes(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="/", intents=intents)
    
    def load_token(self) -> str:
        load_dotenv()
        TOKEN = os.getenv("DISCORD_TOKEN")
        if not TOKEN:
            raise RuntimeError("API key missing. Is the .env in the path?")
        return TOKEN

    async def on_ready(self):
        print("boxes is open!")

    async def setup_hook(self):
        try:
            await self.load_extension("cogs.commands")
            print("Commands loaded!")
            await self.tree.sync()
            print("Commands synced!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    bot = Boxes()
    TOKEN = bot.load_token()
    bot.run(TOKEN)