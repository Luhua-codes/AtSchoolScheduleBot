from enum import Enum
import discord
from discord.ext import commands


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


class User:
    servers = []
    monday = False
    tuesday = False
    wednesday = False
    thursday = False
    friday = False
    ms1 = None
    ms2 = None
    ms3 = None
    me1 = None
    me2 = None
    me3 = None
    ts1 = None
    ts2 = None
    ts3 = None
    te1 = None
    te2 = None
    te3 = None
    ws1 = None
    ws2 = None
    ws3 = None
    we1 = None
    we2 = None
    we3 = None
    rs1 = None
    rs2 = None
    rs3 = None
    re1 = None
    re2 = None
    re3 = None
    fs1 = None
    fs2 = None
    fs3 = None
    fe1 = None
    fe2 = None
    fe3 = None


TOKEN = open("token.txt", "r").readline()
users = {}

intents = discord.Intents.default()
intents.members = True

# get client (bot) obj from dc
client = commands.Bot(command_prefix="sb!", intents=intents)


@client.event  # turn on bot
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")  # display all servers joined
        guild_count += 1
    print("ASSbot is in", str(guild_count), "guilds")  # display number of servers joined


# DM user for setup dialogue
@client.command()
async def setup(ctx):  # use context
    users.update({ctx.author.id: User()})  # add user to dictionary
    users[ctx.author.id].servers.append(ctx.guild.id)  # add to user server set

    # prompt user for days on campus
    message = "What days are you on campus?"
    description = "Select by clicking the emotes corresponding to each weekday. Click the checkmark when you're done."
    embed = discord.Embed(title=message, description=description)
    await ctx.channel.send("Message sent! Check your DMs.")
    dm = await ctx.author.send(embed=embed)

    # add reaction emotes for weekdays on embed
    emojis = ["<:mon:942345965338243072>", "<:tue:942345965388566538>", "<:wed:942345965342457856>", "<:thu:942345965342429244>", "<:fri:942345965266944020>", '✅']  # TODO: update with custom emotes
    for e in emojis:
        await dm.add_reaction(e)

    print(users.keys())


# event listener for user weekday reactions
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if str(reaction.emoji) == "<:mon:942345965338243072>":
        users[user.id].monday = True
        print(user.id, "selected Monday")
    elif str(reaction.emoji) == "<:tue:942345965388566538>":
        users[user.id].tuesday = True
        print(user.id, "selected Tuesday")
    elif str(reaction.emoji) == "<:wed:942345965342457856>":
        users[user.id].wednesday = True
        print(user.id, "selected Wednesday")
    elif str(reaction.emoji) == "<:thu:942345965342429244>":
        users[user.id].thursday = True
        print(user.id, "selected Thursday")
    elif str(reaction.emoji) == "<:fri:942345965266944020>":
        users[user.id].friday = True
        print(user.id, "selected Friday")

    if str(reaction.emoji) == '✅':
        print("checkmark clicked")
        await weekday_time(reaction.message.channel, user)


@client.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    if str(reaction.emoji) == "<:mon:942345965338243072>":
        users[user.id].monday = False
        print(user.id, "unselected Monday")
    elif str(reaction.emoji) == "<:tue:942345965388566538>":
        users[user.id].tuesday = False
        print(user.id, "unselected Tuesday")
    elif str(reaction.emoji) == "<:wed:942345965342457856>":
        users[user.id].wednesday = False
        print(user.id, "unselected Wednesday")
    elif str(reaction.emoji) == "<:thu:942345965342429244>":
        users[user.id].thursday = False
        print(user.id, "unselected Thursday")
    elif str(reaction.emoji) == "<:fri:942345965266944020>":
        users[user.id].friday = False
        print(user.id, "unselected Friday")


@client.event
async def weekday_time(channel, user):
    pass


# Execute the bot with the specified token
client.run(TOKEN)
