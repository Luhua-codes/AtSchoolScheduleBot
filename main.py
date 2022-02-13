import os
import discord
# from discord import emoji
from discord.ext import commands
from enum import Enum
import re
from google.cloud.sql.connector import connector
import sqlalchemy
from sqlalchemy.dialects.mysql import pymysql
from dotenv import load_dotenv
import pymysql

load_dotenv()


def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        os.environ["MYSQL_CONNECTION_NAME"],
        "pymysql",
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASS"],
        db=os.environ["MYSQL_DB"]
    )
    return conn


pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


TOKEN = open("token.txt", "r").readline()

intents = discord.Intents.default()
intents.members = True

# Get the client (bot) object from discord
client = commands.Bot(command_prefix="sb!", intents=intents)


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
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)


@client.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")


# DM the user
@client.command()
async def setup(ctx):
    # insert duid into database // TODO: check if user already in table
    insert_to_user = sqlalchemy.text("INSERT INTO user (discord_user_id) VALUES(:duid)", )
    with pool.connect() as db_conn:
        db_conn.execute(insert_to_user, duid=ctx.author.id)
    print(ctx.author.id, ctx.author)

    insert_to_user_servers = sqlalchemy.text("INSERT INTO user_servers (discord_user_id, discord_server_id) VALUES("
                                             ":duid, :dsid)", )
    with pool.connect() as db_conn:
        db_conn.execute(insert_to_user_servers, duid=ctx.author.id, dsid=ctx.guild.id)
    print(ctx.author, ctx.guild.id, ctx.guild.name)

    message = "What days are you usually at school?"
    description = "Select by clicking the emotes of the weekdays. Click the check mark when you are done."
    embed = discord.Embed(title=message, description=description)
    await ctx.channel.send("Message sent! Check your DMs.")
    dm = await ctx.author.send(embed=embed)

    # Add the reaction emotes for the weekdays on the embed
    emojis = ['🇲', '🇹', '🇼', '🇷', '🇫', '✅']
    for e in emojis:
        await dm.add_reaction(e)


# Even listener for when a user clicks on a weekday emote to make their selection
selected_weekdays = []


@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if str(reaction.emoji) == '🇲':
        print("added thumbs up")
        # selected_weekdays.append(Weekday.MONDAY.name)
        query = "SELECT * FROM user WHERE discord_user_id = %(duid)s"
        modify = "UPDATE user SET monday = true WHERE discord_user_id = %(duid)s"
        with pool.connect() as db_conn:
            print(user.id)
            db_conn.execute(modify, {'duid': user.id}) # update day boolean
            user_row = db_conn.execute(query, {'duid': user.id}) # to check row status
            print(user_row)
            print(user_row.first()[2])

        # print(selected_weekdays)
    elif str(reaction.emoji) == '🇹':
        pass
    elif str(reaction.emoji) == '🇼':
        pass
    elif str(reaction.emoji) == '🇷':
        pass
    elif str(reaction.emoji) == '🇫':
        pass
    if str(reaction.emoji) == '✅':
        await weekday_time(reaction.message.channel)


@client.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return
    if str(reaction.emoji) == '🇲':
        print("added thumbs up")
        selected_weekdays.remove(Weekday.MONDAY.name)
        # print(selected_weekdays)
    elif str(reaction.emoji) == '🇹':
        pass
    elif str(reaction.emoji) == '🇼':
        pass
    elif str(reaction.emoji) == '🇷':
        pass
    elif str(reaction.emoji) == '🇫':
        pass


# Helper function to ask a user what time they will be at school and not in class
async def weekday_time(channel):
    # QUERY WEEKDAYS HERE
    for weekday in weekdays:
        available_message = "What times are you available on " + weekday.lower().capitalize() + "?"
        available_description = "Enter up to 3 time slots (example format: 0900 1200, 1400 1600)"
        available_embed = discord.Embed(title=available_message, description=available_description)
        await channel.send(embed=available_embed)

        def check_available_time(msg):
            # TODO: validate format
            return True

        user_available_times = await client.wait_for("message", check=check_available_time)
        print(user_available_times.content)

        available_times = re.split(' |, ', user_available_times.content)
        print(available_times)

        # convert to timestamp format HH:MM:SS before storing in db 
        timestamps = []
        for time in available_times:
            hours = time[:2]
            mins = time[2:]
            timestamps.append(f"{hours}:{mins}:00")


# Execute the bot with the specified token
client.run(TOKEN)
