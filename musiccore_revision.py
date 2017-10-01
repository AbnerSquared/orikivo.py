import asyncio
import discord
from discord.ext import commands

if not discord.opus.is_loaded():
    discord.opus.load_opus("opus")

class VCEntry:
    """The entrance processes the VC performs when launching or queuing."""
    def __init__(self, message, player):
        self.req = message.author
        self.channel = message.channel
        self.radio = player

    def __str__(self):
        vfm = "Title: {0.title}" + "\n" + "Channel: {0.uploader}" + "\n" + "Requester: {1.display_name}"
        dur = self.radio.duration
        if dur:
            vfm = vfm + "{0[0]}:{[00]}".format(divmod(dur, 60))
        return vfm.format(self.radio, self.req)

class VCState:
    """An identifier of the current state the VC is in."""
    def __init__(self, bot):
        self.cur = None
        self.voice = None
        self.bot = bot
        self.playnextsong = asyncio.Event()
        self.songs = asyncio.Queue(maxsize=0)
        self.skipvotes = set()
        self.radioplayer = self.bot.loop.create_task(self.audioplayersys())

    def isplay(self):
        """A quick test to check if the bot has anything in queue."""
        if self.voice is None or self.cur is None:
            return False

        radio = self.cur.radio
        return not radio.is_done()

    @property
    def radio(self):
        """A subcommand to send the current state in a short rendition."""
        return self.cur.radio

    def skip(self):
        """A subcommand to control when a skip sequence has been confirmed."""
        # [Defined Code]
        # self.skipvotes.clear() - Once the skips have reached the desired number, it will clear the votes listed.
        # if self.isplay(): - Checks if the audio is playing to perform a desired skip.
        # self.radio.stop() - Cancels the current audio playing, intending to send the queue to continue the song listings.
    
        self.skipvotes.clear()
        if self.isplay():
            self.radio.stop()

    def toggnext(self):
        """A subcommand to send the sequence for the next following song queued."""
        self.bot.loop.call_soon_threadsafe(self.playnextsong.set)

    async def audioplayersys(self):
        """An identifier subcommand if anything has been queued."""
        while True:
            self.playnextsong.clear()
            self.cur = await self.songs.get()
            await self.bot.send_message(self.cur.channel, "Playing:" + "\n" + str(self.cur))
            self.cur.radio.start()
            await self.playnextsong.wait()

class VCSystem:
    """The core command systematics of the VC."""
    def __init(self, bot):
        self.bot = bot
        self.vstates = {}

    def getvcstate(self, server):
        """ """
        state = self.vstates.get(server.id)
        if state is None:
            state = VCState(self.bot)
            self.vstates[server.id] = state

        return state

    async def createvc(self, channel):
        """A subcommand to join a channel and grab its current state."""
        voice = await self.bot.join_voice_channel(channel)
        state = await self.getvcstate(channel.server)
        state.voice = voice

    def __unload(self):
        """A subcommand to disconnect and remove all connected voice systems."""
        for state in self.vstates.values():
            try:
                state.radioplayer.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def summon(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def play(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def volume(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def pause(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def stop(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def skip(self,):
    @commands.command(pass_context=True, no_pm=True)
    async def playing(self,):
def setup(bot):
    """What the cog calls the core commanding systematics."""
    bot.add_cog(VCSystem(bot))