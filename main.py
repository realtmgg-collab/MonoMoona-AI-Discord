from asyncio import events
from operator import truediv

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Logged in as, MONOMOONA :3")

@bot.event
async def on_member_join(member):
    await member.send("Welcome to the Judgement Hall {member.name} 🧑‍⚖️ https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWd2ZTJ5ZHp0aDBhZXBleHlyeHhzdGkxMHN2azBnaWNmMGxwNWE2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J4zT1A80r9q92/giphy.gif")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "ass" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "cunt" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "nigga" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "nigger" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)

    if "Asshole" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} HEY! LANGUAGE!!! 😒")

        await bot.process_commands(message)



# !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")



bot.run(token, log_handler=handler, log_level=logging.DEBUG)


