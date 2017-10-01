from __future__ import print_function
import discord
import pickle
import time
import urllib.request
from PIL import ImageFilter
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands

class Conno():
    def __init__(self, bot):
        self.bot = bot
        #oriki_roles = ['Overwatch Addict', 'CS:Addict', 'TF2 Addict', 'Minecraft Addict', 'Unturned Addict', 'League Addict']

    #@commands.command(name='self')
    #async def adrl(self, ctx, role: discord.Role):
        #if role in oriki_roles:
            #role = discord.utils.get(ctx.message.server.roles, name=role)
            #if role is not None:
                #await bot.add_roles(ctx.message.author, role)
                #await bot.say("Role set.")

    #@commands.command(pass_context=True)
    #async def jndat(ctx, member: discord.Member = None):
        #if member is None:
            #member = ctx.message.author







    @commands.command(pass_context=True, no_pm=True)
    async def saveimg(self, ctx, url: str=None, filename: str=None):
        urllib.request.urlretrieve(url, filename + ".jpg")
        await self.bot.send_message(ctx.message.channel,"Saved your URL as: ```\n" + filename +"```\nFeel free to call it for editing anytime!")

        imagelist = []

        l_load = open('imglist.ori', 'rb')
        li_load = pickle.load(l_load)
        imagelist = li_load

        fn_save = filename
        imagelist.append(fn_save)
        
        l_overwrite = open('imglist.ori', 'wb')
        pickle.dump(imagelist, l_overwrite)
        l_overwrite.close()

    @commands.command(pass_context=True, no_pm=True)
    async def imglist(self, ctx, act: str=None):
        
        if act == "new":
            l_new = open('imglist.ori', 'wb')
            l_new.close()

        if act == "load":
            l_load = open('imglist.ori', 'rb')
            li_load = pickle.load(l_load)

            await self.bot.send_message(ctx.message.channel,"```\nImage Names:\n\n" + "\n".join(li_load) + "```")






















    @commands.command(pass_context=True, no_pm=True)
    async def editinfo(self, ctx):

        await self.bot.send_message(ctx.message.channel, "\nTo use this command, type: ```\n~edit [File Name ~ put oof for default.] [Method ~ blur, text, flip]\n\n- If the method is for the text, type:\n\n~edit [File Name] [Method ~ text to use this.] [Message] [Font Name] [Font Size] [Color 'R' Scale ~ 0-255] [Color 'G' Scale ~ 0-255] [Color 'B' Scale ~ 0-255] [X-POS of MSG ~ 0-644] [Y-POS of MSG ~ 0-499]```")

    @commands.command(pass_context=True, no_pm=True)
    async def edit(self, ctx, filn: str=None, ftr: str=None, msg: str=None, fnt: str=None, fntsize: int=None, clr_r: int=None, clr_g: int=None, clr_b: int=None, xpos: int=None, ypos: int=None):

        imgn = filn
        img = filn + ".jpg"
        im = Image.open(img)

        if ftr is None:
            await self.bot.send_file(ctx.message.channel, img)

        if ftr == "disp":
            im.show()

        if ftr == "blur":

            im = im.filter(ImageFilter.BLUR)
            im.save(imgn + "blur.jpg")
            await self.bot.send_file(ctx.message.channel, imgn + "blur.jpg")

        if ftr == "text":
            draw = ImageDraw.Draw(im)
            color = clr_r, clr_g, clr_b
            font = ImageFont.truetype(fnt + ".ttf", fntsize)

            draw.text((xpos, ypos), msg, color, font=font)

            im.save(imgn + "txt.jpg")
            await self.bot.send_file(ctx.message.channel, imgn + "txt.jpg")

        if ftr == "flip":
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
            im.save(imgn + "flip.jpg")
            await self.bot.send_file(ctx.message.channel, imgn + "flip.jpg")


    @commands.command(pass_context=True, no_pm=True)
    async def hlp(self, ctx, cmd: str=None):
        '''A command for retrieving information on every single command in existence.'''
        if cmd is None:
            await self.bot.send_message(ctx.message.author, "```This is a command in progress. Hang tight.```")
            await self.bot.send_message(ctx.message.channel, "Help consolations have been sent.")
        else:
            if cmd == "ping":
                await self.bot.send_message(ctx.message.author, "```Ping: A command made just for detecting what ping it has, if it it placed in a hosting server.```")
                await self.bot.send_message(ctx.message.channel, "Detailed information on the command: [~ping] has been sent.")
            else:
                pass



    @commands.command(pass_context=True, no_pm=True)
    async def saveit(self, ctx, save_vers: str=None, s1: str=None, s2: str=None, s3: str=None, s4: str=None, s5: str=None, i1: discord.Colour=None):
        def po():
            pickle_o = open(save_vers + ".ori", "wb")
            pickle.dump(t1s, pickle_o)
            pickle_o.close()


        if save_vers == "group":
            t1s = [s1, s2, s3, s4, s5]
            po()
            await self.bot.send_message(ctx.message.channel, "Your group has been saved.\n ```\n" + "\n".join(t1s) + "```")
        if save_vers == "string":
            t1s = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4 + ' ' + s5
            po()
            await self.bot.send_message(ctx.message.channel, "Your message has been saved.\n ```\n" + t1s + "```")
        if save_vers == "url":
            t1s = discord.Embed(title="URL HOLDER 50000", description=ctx.message.author.name + " has decided to keep this link safe!", color=i1)
            t1s.set_image(url=ctx.message.author.avatar_url)
            t1s.add_field(name="URL:", value=s1, inline=True)
            t1s.set_footer(text=".ori. - 2017")
            po()
            await self.bot.send_message(ctx.message.channel, "Your embed has been saved.\n ```\nembed=t1s```")
            await self.bot.send_message(ctx.message.channel, embed=t1s)

        if save_vers == "img":

            urllib.request.urlretrieve(s1, s2 + ".jpg")
            t2 = s2 + ".jpg"
            t1s = t2
            
            po()
            await self.bot.send_message(ctx.message.channel, "Your image has been saved.\n ```\n" + t1s + " ```")
            await self.bot.send_file(ctx.message.channel, t2)

    @commands.command(pass_context=True, no_pm=True)
    async def loadit(self, ctx, vers: str=None):
        if vers == "group":
            pickle_i = open(vers + ".ori", "rb")
            t1l = pickle.load(pickle_i)
            await self.bot.send_message(ctx.message.channel, "\n".join(t1l))
        if vers == "string":
            pickle_i = open(vers + ".ori", "rb")
            t1l = pickle.load(pickle_i)
            await self.bot.send_message(ctx.message.channel, t1l)
        if vers == "url":
            pickle_i = open(vers + ".ori", "rb")
            t1l = pickle.load(pickle_i)
            await self.bot.send_message(ctx.message.channel, embed=t1l)
        if vers == "img":
            pickle_i = open(vers + ".ori", "rb")
            t1l = pickle.load(pickle_i)
            await self.bot.send_file(ctx.message.channel, t1l)

    @commands.command(pass_context=True, no_pm=True)
    async def ping(self, ctx):
        '''A command for displaying the current ping.'''
        #pingtime = time.monotonic()
        #pingms = await ctx.send("Ping..")
        #ping = time.montotonic() - pingtime
        #await pingms.edit(content="Ping! `{%.ms" % ping)
        #pingms = await self.bot.send_message(ctx.message.channel, "Ping...")
        #pingms = await self.bot.send_message(ctx.message.channel, "Ping...")
        #await pingms.edit(content="{} // **{} ms**".format(pingms.content, pyping.ping("google.com").avg_rtt))
        #await self.bot.send_message(ctx.message.channel, "{} // **{} ms**".format(pingms.content, pyping.ping("google.com").avg_rtt))
        await self.bot.send_message(ctx.message.channel, "The ping system is currently unavailable, until my code gets placed into a hosting server. Sorry about that. :^(")
    
    @commands.command(pass_context=True, no_pm=True)
    async def pong(self, ctx):
        '''A command for mocking the use of typing pong instead of ping.'''
        await self.bot.send_message(ctx.message.author, 'Seriously? All these commands you could use, and you just simply want to spam me with pong? Good news, kiddo. Everytime you type that, this message returns once again to haunt you. Think twice before typing pong. >:(')

    @commands.command(pass_context=True, no_pm=True)
    async def phat(self, ctx):
        '''A command for randomly choosing out a meme made specifically for Phat Azz.'''
        await self.bot.send_file(ctx.message.channel, 'nowoter.png')

    @commands.command(pass_context=True)
    async def say(self, ctx, content):
        '''A command for replicating exactly what you type, provided with quotation marks.'''
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.say(content)
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True, no_pm=True)
    async def model(self, ctx):
        '''A command for referencing the current model edition the bot is referencing.'''
        embed = discord.Embed(title="Orikivo v0.2 - Model C1", description="**This model exclusive contains quite a respectful personality, with the drawbacks of being quite cocky at times. While used to defend, it often had some errors that sparked outrage in the world. Now up to date, it is ready to provide happiness.**", color=0x00ff00)
        embed.set_author(name="Orikivo - Bot Systematics: Document III, Section IV", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="Not much else is known, besides what was provided by Orikivo.", value="[ ori=(ORI.C1.VII); if ail = true: set discord.CrowdEvac=ori; ]")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/286613308432318464/349736801683898369/Orikivo-C1_Logo.png")
        embed.set_image(url=self.bot.user.avatar_url)
        embed.add_field(name="[Model Projection]", value="As shown above resides ORI.C1.VII.", inline=True)
        embed.set_footer(text="Orikivo - Bot Systematics [2016]")
        await self.bot.send_message(ctx.message.channel, embed=embed)
        #await self.bot.send_message(ctx.message.channel, 'My model type is known as MODEL C1. Now launching: Informational Sequence - [MODEL_C1]')
        #await self.bot.send_message(ctx.message.channel, '<INITIATING: Model-C1-Description:>')
        #await self.bot.send_message(ctx.message.channel, '**This model exclusive contains quite a respectful personality, with the drawbacks of being quite cocky at times. While used to defend, it often had some errors that sparked outrage in the world. Now up to date, it is ready to provide happiness.**')
        #await self.bot.send_message(ctx.message.channel, '<Model-Type:>')
        #await self.bot.send_file(ctx.message.channel, 'Orikivo-C1 Logo.png')

    @commands.command(pass_context=True, no_pm=True)
    async def nwpl(self, ctx):
        '''A command for altering the current "Now Playing" state the bot is in.'''
        await self.bot.change_presence(game=discord.Game(name='Oof', type=0))
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_message(ctx.message.channel, 'I only have Oof. :(')

    @commands.command(pass_context=True, no_pm=True)
    async def stpl(self, ctx):
        '''A command for removing the current "Now Playing" state the bot is in.'''
        await self.bot.change_presence(game=None, type=0)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_message(ctx.message.channel, 'I never liked playing Oof anyways. >:(')

    @commands.command(pass_context=True)
    async def clear(self, ctx, num: int, private: str=None):
        '''A command for deleting messages under the 14 day limit.'''
        #if member == None:
        #member: discord.Member=None):
        if private is None:
            await self.bot.delete_message(ctx.message)
            await self.bot.purge_from(ctx.message.channel, limit=num)
            await self.bot.send_message(ctx.message.channel, ctx.message.author.name + ' just **obliterated** ' + str(num) + ' message(s) in our wonderful channel of: ' + ctx.message.channel.mention + '.')
        else:
            if private is not None:
                await self.bot.delete_message(ctx.message)
                await self.bot.delete_messages(ctx.message.author)
                await self.bot.send_message(ctx.message.channel, ctx.message.author.name + ", your private chat has been cleared to the desired amount.")
            else:
                pass
        #else:
            #pass
            #def userdef():
                #return ctx.message.author == member
            #await self.bot.delete_message(ctx.message)
            #await self.bot.purge_from(ctx.message.channel, limit=num, check=userdef)
            #user = ctx.message.server.get_member(member.id.replace('<@', '').replace('>', ''))
            #await self.bot.send_message('~' + ctx.message.author.name + '#' + ctx.message.author.discriminator + 'just obliterated ' + str(num) + 'message(s) from ' + user.name + ' in our wonderful channel of:' + ctx.message.channel.mention + '.')
    
    @commands.command(pass_context=True)
    async def clearftd(self, ctx, num: int, repeat: int, private: str=None):
        '''A command for deleting the messages older than 14 days. [The first number has to be 1 for this to properly work for the old messages.]'''
        
        pongmsg1 = "Seriously? All these commands you could use, and you just simply want to spam me with pong? Good news, kiddo. Everytime you type that, this message returns once again to haunt you. Think twice before typing pong. >:("
        hlpgeneral = "```This is a command in progress. Hang tight.```"
        hlpping1 = "```Ping: A command made just for detecting what ping it has, if it it placed in a hosting server.```"

        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(self.bot.get_channel("362672790152937473"), "Purging with this method takes some time, and since you set it on repeat for about " + str(repeat) + " times, it should take about " + str(repeat) + " seconds, since if it went instantly, it would lag out, slowing down the process.")
        if private is None:
            for i in range(repeat):
                await self.bot.purge_from(ctx.message.channel, limit=num)
                time.sleep(1.2)
            await self.bot.send_message(ctx.message.channel, ctx.message.author.name + ' just **obliterated** our messages at the rate of: ' + str(num) + ' message(s) on loop for about ' + str(repeat) + ' repeats, in our wonderful channel of: ' + ctx.message.channel.mention + '.')
        else:
            if private is not None:
                for i in range(repeat):
                    await self.bot.delete_messages(pongmsg1, hlpgeneral, hlpping1)
                    time.sleep(1)
                await self.bot.send_message(ctx.message.channel, ctx.message.author.name + ', I have cleared any messages older than 14 days in the private chat to your desired amount.')
            else:
                pass
def setup(bot):
    '''Adds this whole set to be functional.'''
    bot.add_cog(Conno(bot))
