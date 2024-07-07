import discord
from discord.ext import commands
import asyncssh
import mcrcon
import os
import json

#informations
Bot_Token = ''

Rcon_Host = ''
Rcon_Pass = ''
Rcon_Port = ''

SSH_Host = ''
SSH_Name = ''
SSH_Pass = ''
SSH_Port = ''

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
        print(f"\033[32m{message.suther} run the command {contents}\033[0m")
        if contents in cmds['commands']:
            commands = cmds['commands'][contents]
            if "__player__" in commands:
                commands.replace("__player__", author)
        print(f"\033[32m{commands}\033[0m")


        



bot.run(Bot_Token)
