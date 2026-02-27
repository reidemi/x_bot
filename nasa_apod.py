import requests
import discord


async def send_apod(interaction: discord.Interaction, api_key: str):
    try:
        r = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={"api_key": api_key},
            timeout=12
        ).json()

        embed = discord.Embed(
            title=r["title"],
            url=r.get("hdurl", r["url"]),
            description=r["explanation"],
            color=discord.Color.from_rgb(30, 60, 120)
        )
        embed.set_image(url=r.get("hdurl", r["url"]))
        embed.set_footer(text=f"{r['date']} • APOD NASA")

        await interaction.followup.send(embed=embed)

    except Exception as e:
        await interaction.followup.send(f"Error: {str(e)[:200]}", ephemeral=True)