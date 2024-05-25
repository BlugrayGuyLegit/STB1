import discord
import os

# Get Discord token from environment variables
discord_token = os.getenv('DISCORD_TOKEN')

# Channel ID for logging
log_channel_id = 1194337788741550230

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
    if before.name != after.name:
        log_message = f"Server '{before.name}' ({before.id}) renamed to '{after.name}'."
        await send_log_message(log_message)

# Event triggered when a member (user) is updated
@client.event
async def on_member_update(before, after):
    if before.name != after.name:
        log_message = f"User '{before.name}' ({before.id}) renamed from '{before.name}' to '{after.name}'."
        await send_log_message(log_message)

# Event triggered when a role is updated
@client.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        log_message = f"Role '{before.name}' ({before.id}) renamed to '{after.name}'."
        await send_log_message(log_message)

# Event triggered when a channel is updated
@client.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        log_message = f"Channel '{before.name}' ({before.id}) renamed to '{after.name}'."
        await send_log_message(log_message)

# Event triggered when an emoji is updated
@client.event
async def on_guild_emojis_update(guild, before, after):
    # Compare the old and new list of emojis
    added = set(after) - set(before)
    removed = set(before) - set(after)
    
    for emoji in added:
        log_message = f"Emoji '{emoji.name}' ({emoji.id}) added to the guild."
        await send_log_message(log_message)
    
    for emoji in removed:
        log_message = f"Emoji '{emoji.name}' ({emoji.id}) removed from the guild."
        await send_log_message(log_message)

# Function to send log messages to the specified channel
async def send_log_message(message):
    channel = client.get_channel(log_channel_id)
    if channel:
        await channel.send(message)

# Run the bot with the retrieved Discord token
client.run(discord_token)
