# Discord APOD Bot

A simple Discord bot that displays NASA's **Astronomy Picture of the Day (APOD)** using slash commands. Further development in progress.

![Example APOD embed](https://apod.nasa.gov/apod/image/2602/JellyfishBeecroft_final1_2048.jpg)
*(Example of what the bot can show – real content changes daily)*

## Features

- `/apod` slash command – shows today's NASA Astronomy Picture of the Day
- Displays title, date, explanation, and high-resolution image
- Uses the official NASA APOD API
- Handles basic errors gracefully
- Currently supports images only (skips videos and other media types)

## Requirements

Python 3.9 or higher

Install dependencies with:

```bash
pip install -r requirements.txt
git