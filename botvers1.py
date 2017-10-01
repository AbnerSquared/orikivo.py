import discord
from discord.ext import commands

#client = discord.Client()
#if not discord.opus.is_loaded():
    #discord.opus.load_opus('opus')

#commands.when_mentioned_or

class Members():
    def __init__(self, bot):
        self.bot = bot

bot = commands.Bot(command_prefix=('-o-'), description='This is to make sure the bot knows what it is recieving.')
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

@bot.event
async def on_member_join(self, bot, member):
    server = member.server
    fmt = 'Fare greetings, {0.mention}. Stumbling into {1.name} may not have been your brightest idea, but we have yet to see.'
    await self.bot.send_typing(server)
    await self.bot.send_message(server, fmt.format(member, server))

@bot.event
async def on_ready():
    print('My code is now working, for I have been given life in a new coding program!')
    print(bot.user.name)
    print('ORIKIVO _ _ _ REPORTING FOR BOT DUTY.')
    print(bot.user.id)
    print('MY USER ID HAS BEEN REPORTED AS WELL.')
    print('---------------------')

@bot.event
async def on_message(message):    
    if message.author == bot.user:
        return

bot.run('MjkzMDc2NDQ4NDA5OTQ0MDY0.DEqTwA.H_pudki9h5g7PEYJUCV3chrqzxY')