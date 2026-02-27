import discord
from discord import app_commands
import logging
from dotenv import load_dotenv
import os
from nasa_apod import send_apod

load_dotenv()
token: str = os.getenv("DISCORD_TOKEN")
guild_s: str = os.getenv("DISCORD_GUILD")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(
    name="apod",
    description="Astronomy Picture of the Day - NASA",
    guild=discord.Object(id=int(guild_s))
)
async def apod(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    try:
        await send_apod(interaction, os.getenv("NASA_API"))
    except Exception as e:
        interaction.followup.send(
            f"An error occurred while downloading APOD:\n`{str(e)[:180]}`",
            ephemeral=True
        )

@client.event
async def on_ready():
    print(f"Signed in: {client.user}")
    # tree.clear_commands(guild=discord.Object(id=int(guild_s)))
    # await tree.sync(guild=discord.Object(id=int(guild_s)))
    # print(f"The slash command has been cleared on the server: {int(guild_s)}")
    if guild_s:
        await tree.sync(guild=discord.Object(id=int(guild_s)))
        print(f"Synced for guild: {guild_s}")
    else:
        await tree.sync()
        print("Synchronization of commands in global mode may take up to an hour.")




if __name__ == "__main__":
    client.run(token, log_handler=handler, log_level=logging.DEBUG)