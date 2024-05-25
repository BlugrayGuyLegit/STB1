import discord
import openai
import os

# Configurer les intents
intents = discord.Intents.default()
intents.message_content = True

# Créer une instance du client Discord avec les intents
client = discord.Client(intents=intents)

# Récupérer les clés API à partir des variables d'environnement
discord_token = os.getenv('DISCORD_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Configurer l'API OpenAI
openai.api_key = openai_api_key

# Événement déclenché lorsque le bot est prêt
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Événement déclenché lorsqu'un message est reçu
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!ask'):
        prompt = message.content[len('!ask '):]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        await message.channel.send(response.choices[0].text.strip())

# Lancer le bot avec le token Discord récupéré
client.run(discord_token)
