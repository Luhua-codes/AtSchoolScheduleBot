import discord 
from discord.ext import commands

TOKEN = open("discord-token.txt","r").readline()

intents = discord.Intents.default()
intents.members = True

# Get the client (bot) object from discord
client = commands.Bot(command_prefix = "sb! ", intents = intents)

# Add event listeners
@client.event
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    print("my first bot is in " + str(guild_count) + " guilds")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

# DM the user 

@client.command(name="ping")
async def ping(ctx):
	await ctx.channel.send("pong")


@client.command()
async def dm(ctx):
    print(ctx.author)
    message="What days are you usually at school?"
    description="Select by clicking the emotes of the weekdays"
    embed = discord.Embed(title=message, description=description)
    await ctx.author.send(embed=embed)

# Execute the bot with the specified token
client.run(TOKEN)