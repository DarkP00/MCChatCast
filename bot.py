import discord
from discord.ext import commands
import mcrcon
from mcrcon import MCRcon
import os
import json

#informations
Bot_Token = ''

Rcon_Host = ''
Rcon_Pass = ''
Rcon_Port = ''

#reding valid cmds
with open('Asstes/cmd.json', 'r') as cmd:
    cmds = json.load(cmd)

# Initiating BOT
intents = discord.Intents.default()
intents.message_content = True
bot = commands.bot(command_prefix = '>', intents = intents)
@bot.event
async def on_ready():
    await print(f"\033[32mBot logged in as {bot.user.name} - {bot.user.id}\033[0m")
    await print(f"\033[32m'------'\033[0m")

# Runing cmds that are valid
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('>'):
        contents = message.content[1:].split(' ')
        author = message.author
        print(f"\033[32m{author} run the command {contents}\033[0m")
        if contents in cmds['commands']:
            commands = cmds['commands'][contents]
            if "__player__" in commands:
                commands.replace("__player__", author)
        print(f"\033[32m{commands}\033[0m")

        # Opening SSH and Writing commands
        with MCRcon(Rcon_Host, Rcon_Pass, port=Rcon_Port) as comm:
            result = comm.command(commands)
            print(result)

# Message discord to server
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.content.startswith('>'):
        contents = message.content[1:].split(' ')
        author = message.author
        await print(f"\033[32m{author} sent the message {contents}\033[0m")

        # Opening SSH and Writing commands
        with mcrcon(Rcon_Host, Rcon_Pass, port=Rcon_Port) as comm:
            result = comm.command(f"say @a {author} said, {contents}")
            await print(result)

# Copy and Prossess the chat
def chat_prossess(response):
    messages = []
    lines = response.split('\n')
    for line in lines:
        if 'INFO' in line and '<' in line and '>' in line:
            timestamp, content = line.split('INFO]: ')
            messages.append(content)
    return messages

# Send Chat to Discord with mcrcon
def send_chet_to_discord():
    try:
        with MCRcon(Rcon_Host, Rcon_Pass, port=Rcon_Port) as comm:
            response = comm.command(LOG_COMMAND)
            messages = chat_prossess(response)
            for message in messages:
                message.channel.send(message)
    except Exception as e:
        print(f"erorr: {e}")

# Run send_chet_to_discord ficntion
if __name__ == "__send_chet_to_discord__":
    send_chet_to_discord()

bot.run(Bot_Token)
