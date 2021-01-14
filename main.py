import discord
import os
import random
import moviepicker
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('token')
GUILD = os.getenv('guild')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    firstchar = message.content[0]
    rest = message.content[1:]
    if firstchar == "!":
        if rest == "RollDie":
            x =random.randint(1,7)
            await message.channel.send(x)

        elif rest == "FlipCoin":
            x =random.randint(0,1)
            choices = ["Heads","Tails"]
            await message.channel.send(choices[x])

        elif rest[0:7] == "Enhance":
            found = False
            if rest[8:] == "":
                found = True
                await message.channel.send(message.author.avatar_url_as(format=None, static_format='webp', size=1024))

            for member in client.guilds[0].members:
                if rest[8:] == member.name:
                    found = True
                    await message.channel.send(member.avatar_url_as(format=None, static_format='webp', size=1024))

            if not found:
                await message.channel.send("Could not find user. Please try again.")

        elif rest == "GetGenres":
            for genre in moviepicker.genres:
                await message.channel.send(genre)
            await message.channel.send("Leave blank for a movie of any genre!")

        elif rest[0:8] == "GetMovie":
            await message.channel.send(moviepicker.getmovie(rest[9:]))
        else: await message.channel.send(content="Invalid Input")


client.run(TOKEN)