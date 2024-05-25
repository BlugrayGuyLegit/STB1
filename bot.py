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

        # Try to get a response from OpenAI
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content'].strip()
            print(f'Response: {reply}')  # Debugging

            # Send the response back to the Discord channel
            await message.channel.send(reply)
        except Exception as e:
            print(f'Error: {e}')  # Debugging errors
            await message.channel.send("An error occurred while processing your request.")

# Run the bot with the retrieved Discord token
client.run(discord_token)
