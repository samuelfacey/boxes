import os
import sys
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

try: 
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
except FileNotFoundError:
    print("Error: The .env file was not found.")
    sys.exit(1)
except ValueError:
    print("Error: Token in .env not found.")
    sys.exit(1)
except OSError as e:
    print(f"OS error occurred: {e}")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("boxes is open!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

if __name__ == "__main__":
    client.run(TOKEN)