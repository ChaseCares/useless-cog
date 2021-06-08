from redbot.core import commands


class UselessCog(commands.Cog):
    """My useless cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("@Addy can't do stuff!")
