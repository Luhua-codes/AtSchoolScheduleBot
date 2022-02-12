import discord 
from discord.ext import commands
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

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
    description="Select by clicking the emotes of the weekdays. Click the check mark when you are done."
    embed = discord.Embed(title=message, description=description)
    await ctx.channel.send("Message sent! Check your DMs.")
    dm = await ctx.author.send(embed=embed)

    # Add the reaction emotes for the weekdays on the embed
    emojis = ['👍', '✅']
    for emoji in emojis:
        await dm.add_reaction(emoji)

# Even listener for when a user clicks on a weekday emote to make their selection
selected_weekdays = []
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if str(reaction.emoji) == '👍':
        print("added thumbs up")
        selected_weekdays.append(Weekday.MONDAY.name)
        print(selected_weekdays)
    elif str(reaction.emoji) == '✅':
        await weekday_time(selected_weekdays, reaction.message.channel)
    # elif emoji == "emoji 3":
    #     pass
    # else:
    #     return

@client.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return
    if str(reaction.emoji) == '👍':
        print("removed thumbs up")
        selected_weekdays.remove(Weekday.MONDAY.name)
        print(selected_weekdays)
    elif emoji == '✅':
        await weekday_time(selected_weekdays, reaction.message.channel)


 # Helper function to ask a user what time they will be at school
async def weekday_time(weekdays, channel):
    for weekday in weekdays:
        on_campus_message = "What time are you at school on " + weekday.lower().capitalize() + "?"
        on_campus_description="Enter the time you arrive and leave (example format: 0900 1600)"
        on_campus_embed = discord.Embed(title=on_campus_message, description=on_campus_description)
        await channel.send(embed=on_campus_embed)

        def check_on_campus_time(msg):
            # TODO: validate format
            return True

        user_on_campus_times = await client.wait_for("message", check=check_on_campus_time)
        print(user_on_campus_times.content)

        available_message = "What times are you available on " + weekday.lower().capitalize() + "?"
        available_description="Enter up to 3 time slots (example format: 0900 1200, 1400 1600)"
        available_embed = discord.Embed(title=available_message, description=available_description)
        await channel.send(embed=available_embed)  

        def check_available_time(msg):
            # TODO: validate format
            return True
        user_available_times = await client.wait_for("message", check=check_available_time)
        print(user_available_times.content)

# Execute the bot with the specified token
client.run(TOKEN)