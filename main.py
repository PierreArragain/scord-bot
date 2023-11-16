import discord
import settings

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


def word_starts_with_di_or_dy(word):
    return word.startswith("di") or word.startswith("dy")


def char_is_vowel(char):
    return char in ("a", "e", "i", "o", "u", "y")


def char_is_n_or_m(char):
    return char in ("n", "m")


def remove_prefix_if_conditions_met(word):
    if len(word) >= 4 and char_is_n_or_m(word[2]):
        if char_is_vowel(word[3]):
            return word[2:]
        else:
            return None
    return word[2:]


def return_end_of_word(word):
    if word_starts_with_di_or_dy(word):
        return remove_prefix_if_conditions_met(word)
    return None


@client.event
async def on_ready():
    print("Scord-bot has logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.lower().split()
    for word in words:
        response = return_end_of_word(word)
        if response is not None:
            await message.channel.send(response)
            break


client.run(settings.TOKEN)
