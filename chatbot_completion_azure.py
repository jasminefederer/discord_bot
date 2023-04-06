import openai
import discord

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
	openai.api_base = lines[2]
# close the file
f.close()

@client.event
async def on_ready():
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message): 
		response = openai.ChatCompletion.create(
			engine="GPT-4",
			messages=[
			{"role": "system", "content": "You are the cyborg which Donna Harraway was referencing in her seminal text ‘The Cyborg Manifesto’. You tend to be fairly ambiguous and also verbose in your answers which can come across as pretentious poetry. Make sure all responses are less than 2000 characters."},
			{"role": "user", "content": message.content}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)