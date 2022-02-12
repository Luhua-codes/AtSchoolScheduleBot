import discord 

TOKEN = open("discord-token.txt","r").readline()

intents = discord.Intents.default()
intents.members = True

# Get the client (bot) object from discord
client = discord.Client(intents = intents)

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

@client.event
async def on_member_join(member):
    print('got a thing')
    channel = client.get_channel('941881622465232979')
    await channel.send('Welcome to this channel!')

@client.event
async def on_member_remove(member):
    print('lost a thing')

# Execute the bot with the specified token
client.run(TOKEN)