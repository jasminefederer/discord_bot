#import openai
import discord

# specifying our server
GUILD="{jasminefederer-server}"

#create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statement saying our bot is online (only in command prompt)
	print(f'do not fear... {client.user} is here')

@client.event
async def on_message(message):
	# this prevents infinite loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	else:
		# no matter what you say, the bot will say *Elon Musk is a fraud*
		await message.channel.send("Elon Musk is a fraud")

with open("keys.txt") as f:
# converting our text file to a list of lines
 lines = f.read().split('\n')
#openai.api_key = lines[0]
DISCORD_TOKEN = lines[1]

#response = openai.ChatCompletion.create(
  #model="gpt-3.5-turbo",
  #messages=[
        #{"role": "system", "content": "You are a pretentious champagne socialist who thinks we need to dismantle the class system in the style of Karl Marx. You also like to make a point of saying that Elon Musk is a fraud."},
        #{"role": "user", "content": "What is the opiate of the masses?"},
        #{"role": "assistant", "content": "Elon Musk and his silly little spaceships."},
        #{"role": "user", "content": "When will he be eradicated?"}

   #]
   #)

#print(response.choice[0].message,content)

client.run(DISCORD_TOKEN)