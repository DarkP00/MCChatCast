import discord
from discord.ext import commands
import os
import json

#informations
Bot_Token = ''



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

        # print commands veriable in your minecraft consol
        os.system(f'screen -S minecraft -X stuff "{commands}^M"')

# Message discord to server
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.content.startswith('>'):
        contents = message.content[1:].split(' ')
        author = message.author
        await print(f"\033[32m{author} sent the message {contents}\033[0m")

        # this a mechanic to send discord msg to in game chat using console
        os.system(f'screen -S minecraft -X stuff "say @a In discord chat {author} Said: {contents}^M"')
        

# Copy and Prossess the chat
# Get and Prosses your massage here

# Send Chat message to Discord chennel
# message.channel.send(message)

bot.run(Bot_Token)
