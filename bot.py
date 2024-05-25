import discord
import os

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

client = discord.Client(intents=intents)

# Événement déclenché lorsque le bot est prêt
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Événement déclenché lorsqu'un message est reçu
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Récupérez le token Discord à partir des variables d'environnement
discord_token = os.getenv('DISCORD_TOKEN')

# Lancez le bot avec le token Discord récupéré
client.run(discord_token)
