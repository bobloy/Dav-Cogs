from redbot.core import commands
import datetime



class StartupDetector(commands.Cog):
    """Startupdetector"""
    
    def __init__(self, bot):
        self.bot=bot
        delta = datetime.datetime.utcnow() - self.bot.uptime
        if delta.seconds < 120:
            self.sendmsg()
    
    async def sendmsg(self, ctx):
        destinations = await ctx.bot.get_owner_notification_destinations()
        for destination in destinations:
            try:
                await destination.send("The Bot just started.")
            except:
                pass
        return
        