import discord
from discord import app_commands
from discord.ext import commands

from main.views.roles_view.roles_view import RolesView

class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roles", description="Select a role from the categories available!")
    async def roles(self, interaction: discord.Interaction):
        view = RolesView()
        await interaction.response.send_message("Choose a catergory to select a role from", view=view, ephemeral=True)
        
    @app_commands.command(name="prune", description="Prune users who do not have a role")
    @commands.has_role("Server Bot Team")
    async def prune(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        members = interaction.guild.members
        roles = [interaction.guild.get_role(580751998752784385), interaction.guild.get_role(580751767541907496), 
                 interaction.guild.get_role(580751510246260757), interaction.guild.get_role(580751306495623168),
                 interaction.guild.get_role(580829130581475339)]
        count = 0 
        for member in members:
            check = any(item in roles for item in member.roles)
            if not check:
                await interaction.guild.kick(member)    
                count = count + 1   
                if count >= 50:
                    break    
        await interaction.followup.send('Kicked ' + str(count) + ' member(s)')


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
