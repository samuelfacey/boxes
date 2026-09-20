import discord
from discord import app_commands
from discord.ext import commands

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="box", description="Returns the contents of a box or displays a specific entry.")
    async def box(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here's the list!")

    @discord.app_commands.command(name="boxadd", description="Appends an entry to an existing named box, or creates a new box if one doesn't already exist.")
    async def boxadd(self, interaction: discord.Interaction):
        await interaction.response.send_message("Added!")

    @discord.app_commands.command(name="boxdel", description="Deletes a box, a specific entry, a list of entries, or all entries matching the provided options.")
    async def boxdel(self, interaction: discord.Interaction):
        await interaction.response.send_message("Deleted!")

async def setup(bot: commands.Bot):
    await bot.add_cog(BotCommands(bot))