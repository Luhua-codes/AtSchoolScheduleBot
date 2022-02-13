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
    emojis = ['🇲', '🇹', '🇼', '🇷', '🇫', '✅']  # TODO: update with custom emotes
    for e in emojis:
        await dm.add_reaction(e)

    print(users)


# event listener for user weekday reactions
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if str(reaction.emoji) == '🇲':
        users[user.id].monday = True
        print(user.id, "selected Monday")

# Execute the bot with the specified token
client.run(TOKEN)