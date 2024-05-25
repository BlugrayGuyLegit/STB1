import discord
import openai
import os

# Configure intents
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the Discord client with intents
client = discord.Client(intents=intents)

# Get API keys from environment variables
discord_token = os.getenv('DISCORD_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Configure the OpenAI API
openai.api_key = openai_api_key

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event triggered when a message is received
@client.event
async def on_message(message):
    print(f'Received message: {message.content}')  # Debugging
    if message.author == client.user:
        return
    
    if message.content.startswith('!ask'):
        prompt = message.content[len('!ask '):]
        print(f'Prompt: {prompt}')  # Debugging
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            reply = response.choices[0].text.strip()
            print(f'Response: {reply}')  # Debugging
            await message.channel.send(reply)
        except Exception as e:
            print(f'Error: {e}')  # Debugging errors

# Run the bot with the retrieved Discord token
client.run(discord_token)
