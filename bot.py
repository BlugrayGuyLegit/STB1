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
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            reply = response.choices[0].text.strip()
            print(f'Response: {reply}')  # Debugging

            # Send the response back to the Discord channel
            await message.channel.send(reply)
        except openai.error.OpenAIError as e:
            print(f'OpenAI API Error: {e}')  # Debugging API errors
            await message.channel.send("There was an error with the OpenAI API.")
        except Exception as e:
            print(f'General Error: {e}')  # Debugging other errors
            await message.channel.send("An error occurred while processing your request.")

# Run the bot with the retrieved Discord token
client.run(discord_token)
