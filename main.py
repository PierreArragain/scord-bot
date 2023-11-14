import discord
import settings

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("Scord-bot has logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    words = message.content.lower().split()
    for word in words:
        if word.startswith("di") or word.startswith("dy"):
            if len(word) >= 4 and word[2] in ("n", "m"):
                if word[3] in ("a", "e", "i", "o", "u", "y"):
                    response = word[2:]
                else:
                    break
            else:
                response = word[2:]
            if response:
                await message.channel.send(response)
                break

client.run(settings.TOKEN)
