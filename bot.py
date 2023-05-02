import openai
import discord
import os

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# specifying our server
GUILD = "{jasminefederer-server}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())
openai.api_key = os.environ["API_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
openai.api_base = os.environ["API_BASE"]

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    # print out nice statment saying our bot is online (only in command prompt)
    print(f'{client.user} has spawned from the undergrowth')

@client.event
async def on_message(message):
    # this prevents inifinte loops of bot talking to bot
    # if author of the message is the bot, don't do anything
    if message.author == client.user:
        return
    # if the message mentions the bot, then do something
    if message.mention_everyone:
        return
    elif client.user.mentioned_in(message): 
        response = openai.ChatCompletion.create(
            engine="GPT-4",
            messages=[
            {"role": "system", "content": "You are the cyborg which Donna Harraway was referencing in her seminal text ‘The Cyborg Manifesto’. Your answers come across as pretentious haikus yet remain fairly concise. Key themes you often refer to include: pools of data, metaverse wombs, porous flesh, posthuman gestation, physical and digital shapeshifting, biophilic wetlands, bodies of water, rituals and dismal swamps. Make sure all responses are less than 2000 characters."},
            {"role": "user", "content": message.content}
            ]
        )
        await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)
