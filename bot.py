import discord
import requests
from bs4 import BeautifulSoup

# Configuration
TOKEN = MTI0Mzk2NTU5MzA3NDI3MDI4OQ.GfmNKg.le3AFTO_w1wwuFGDbA454WLe4fcU65mZ8dUsF0
CHANNEL_ID = 1243967560647577710
URLS_TO_MONITOR = 'https://dafuqboom.shop'

# Create an instance of a Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Function to get the content of a webpage
def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()  # Or any specific part of the page you want to monitor

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    for index, url in enumerate(URLS_TO_MONITOR):
        # Get the previous content from a local file
        try:
            with open(f'previous_content_{index}.txt', 'r') as file:
                previous_content = file.read()
        except FileNotFoundError:
            previous_content = ''

        # Get the current content of the page
        current_content = get_page_content(url)

        # Compare the content and send a message if there is an update
        if current_content != previous_content:
            channel = client.get_channel(CHANNEL_ID)
            await channel.send(f'The page at {url} has been updated.')

            # Update the previous content file
            with open(f'previous_content_{index}.txt', 'w') as file:
                file.write(current_content)

    # Close the bot after the task is done
    await client.close()

client.run(TOKEN)
