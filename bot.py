import discord
import os

# Get Discord token and channel ID from environment variables
discord_token = os.getenv(DISCORD_TOKEN)
log_channel_id = int(os.getenv('1194337788741550230'))

# Create an instance of the Discord client
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event triggered when a server (guild) is updated
@client.event
async def on_guild_update(before, after):
    log_message = f"Server '{before.name}' ({before.id}) has been updated."
    await send_log_message(log_message)

# Event triggered when a member (user) is updated
@client.event
async def on_member_update(before, after):
    log_message = f"User '{before.name}' ({before.id}) has been updated."
    await send_log_message(log_message)

# Event triggered when a message is edited
@client.event
async def on_message_edit(before, after):
    log_message = f"Message edited in #{before.channel.name} by {before.author.name} ({before.author.id})."
    await send_log_message(log_message)

# Event triggered when a message is deleted
@client.event
async def on_message_delete(message):
    log_message = f"Message deleted in #{message.channel.name} by {message.author.name} ({message.author.id})."
    await send_log_message(log_message)

# Function to send log messages to the specified channel
async def send_log_message(message):
    channel = client.get_channel(log_channel_id)
    if channel:
        await channel.send(message)

# Run the bot with the retrieved Discord token
client.run(discord_token)
