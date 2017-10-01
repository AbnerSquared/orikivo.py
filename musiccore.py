import asyncio
import discord
from discord.ext import commands

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

    
# I know it's basing off of the playlist example. This is the original version, and a revised one with better usage is in the works.
# And yes, I did type the entire example by scratch, despite it may look the exact same. :(

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        #fmt = "*{0.title}*, a wonderful video provided by: {0.uploader}, from which was added to existance by {1.display_name}"
        fmt = '*{0.title}*, {0.uploader}, {1.display_name}'
        duration = self.player.duration
        if duration:
            #fmt = fmt + " // Length - [{0[0]}m and {0[1]}s] =-".format(divmod(duration, 60))
            fmt = fmt + ' [{0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            #await self.bot.send_message(self.current.channel, "I am now playing: " + str(self.current))
            await self.bot.send_message(self.current.channel, 'play: ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = await self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        try:
            await self.create_voice_client(channel)
        except discord.InvalidArgument:
            #await self.bot.say("Excuse my programming, but I believe that this ID number you provided for me isn't even a voice channel. In reality, I'm not suprised.")
            await self.bot.say('not voic chan')
        except discord.ClientException:
            #await self.bot.say("Sorry to pardon, but I'm already in this exact channel you desire. Clean your eyes.")
            await self.bot.say('in chan')
        else:
            #await self.bot.say("Luckily, I was somehow able to find your ID number, and I'm now connected to " + channel.name + ".")
            await self.bot.say('connected to ' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            #await self.bot.say("Although I wish to be polite, I can't. You have to be in an audio channel for me to play anything, you Doug Dimmadimwit.")
            await self.bot.say('join chan')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            if not success:
                return

        try:
            #tmp = await self.bot.send_message(ctx.message.channel, "Exploring the many internets for: [ '" + song + "' ] ...for whatever reason may that be. Who knows? I sure don't.")
            player = await state.voice.create_ytdl_player(song, before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            #fmt = "A mishap occured, due to some error bug in either the writing, connections, or it could just be the plain fact that you don't even have the programs for this task. ```py\n{}: {}\n```"
            fmt = 'oh rip err ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            #await self.bot.say("Luckily, I was able to find this link! I dropped into the audio chamber: " + str(entry) + " to our queue of shattered wonders.")
            await self.bot.say('Added: ' + str(entry))
            await state.songs.put(entry)

    #@commands.command(pass_context=True, no_pm=True)
    #async def queue(self, ctx, *, song : str):


    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            #await self.bot.say("The new integer you just provided has now made the volume of future audio at: {:.0%}".format(player.volume))
            await self.bot.say('Now at: {:.0%}'.format(player.volume))

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()
            #await self.bot.say("The audio that has been currently playing is now paused. :^)")

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()
            #await self.bot.say("Your audio is once again alive, and is continuing your jam. :^)")

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()
        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            #await self.bot.say("Any audio from this point foward has officially been disabled, also unqueuing any future songs up the list. :^(")
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            #await self.bot.say("Sorry to barge, but I don't believe I'm playing anything at this moment.")
            await self.bot.say('no song')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            #await self.bot.say("Out of random shock, the requester of this audio has decided to skip it for unknown purposes. :o")
            await self.bot.say('req skip')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            #if total_votes >= 2:
            if total_votes >= 3:
                #await self.bot.say("The voting ritual has been accepted. The audio that was playing is now being sent to our sacrifice center up north. No need to worry. :^)")
                await self.bot.say('skipd')
                state.skip()
            else:
                #await self.bot.say('You have submitted a skipping ritual pass, now making the total amount to: [{}/2]'.format(total_votes))
                await self.bot.say('[{}/3]'.format(total_votes))
        else:
            #await self.bot.say("Excuse me, but you have already voted for this ritual amendment. Now, please stop asking, for it may lead to your very own. :^)")
            await self.bot.say('you vot alrdy')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            #await self.bot.say("From what I know, there isn't any existing audio to grab information about.")
            await self.bot.say('no song')
        else:
            skip_count = len(state.skip_votes)
            #await self.bot.say('Our spiffy new radio is now playing: {} [Skip Passes Sumbitted: {}/2]'.format(state.current, skip_count))
            await self.bot.say('Playing: {} Skips: [{}/3]'.format(state.current, skip_count))

def setup(bot):
    bot.add_cog(Music(bot))
