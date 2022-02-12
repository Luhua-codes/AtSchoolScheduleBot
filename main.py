import discord 
from discord.ext import commands
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

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

# Just testing stuff :)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

@client.command(name="ping")
async def ping(ctx):
	await ctx.channel.send("pong")

# DM the user 
@client.command()
async def setup(ctx):
    print(ctx.author)
    message="What days are you usually at school?"
    description="Select by clicking the emotes of the weekdays"
    embed = discord.Embed(title=message, description=description)
    await ctx.channel.send("Message sent! Check your DMs.")
    dm = await ctx.author.send(embed=embed)

    # Add the reaction emotes for the weekdays on the embed
    #yooo
    emojis = ['👍']
    for emoji in emojis:
        await dm.add_reaction(emoji)

# Even listener for when a user clicks on a weekday emote to make their selection
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if str(reaction.emoji) == '👍':
        print("got thumbs up")
        await weekday_time(Weekday.MONDAY, reaction.message.channel)
    # elif emoji == "emoji 2":
    #     pass
    # elif emoji == "emoji 3":
    #     pass
    # else:
    #     return

 # Helper function to ask a user what time they will be at school
async def weekday_time(weekday, channel):
    message = "What time are you at school on " + weekday.name.lower().capitalize() + "?"
    description="Select the start time and end time by clicking the emotes"
    # print(message)
    # print(description)
    # print(channel)
    embed = discord.Embed(title=message, description=description)
    await channel.send(embed=embed)
    
    # TODO: how are we going to do this start time/end time selection? Do we wait like 30 sec
    # for them to finalize their decision?? OR they select a time and we ask them to confirm?


# Execute the bot with the specified token
client.run(TOKEN)