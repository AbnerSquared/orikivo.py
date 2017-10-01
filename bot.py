import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["corecomms", "musiccore"]

bot = discord.ext.commands.Bot(command_prefix='~', description='description')

@bot.event
async def on_ready():
    print('I have been given life once again! Now processing...')
    print('Username found!')
    print(bot.user.name)
    print('User ID identified!')
    print(bot.user.id)


@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Fare greetings, {0.mention}. Stumbling into {1.name} may not have been your brightest idea, but we have yet to see.'
    await bot.send_message(server, fmt.format(member, server))

@bot.command()
async def shdw():
    await bot.say("It's been nice seeing you again. Now shutting down all services...")
    await bot.close()
    #except discord.errors.Forbidden:
        #await bot.say("Well I enjoy your attempt to terminate me, you don't have the permissions to do so.")
        #return

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("Extension: '{}' has been booted.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("Extension: '{}' has been shut down.".format(extension_name))

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to approve the extension: '{}\n{}'".format(extension, exc))

    bot.run('MjkzMDc2NDQ4NDA5OTQ0MDY0.DEqTwA.H_pudki9h5g7PEYJUCV3chrqzxY')