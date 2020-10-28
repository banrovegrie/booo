import os

try:
    from discord.ext import commands
    from dotenv import load_dotenv
except:
    os.system("pip3 install discord.py")
    os.system("pip3 install python-dotenv")
    from discord.ext import commands
    from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen('on_ready')
async def ready_function():
    print("Connected")

@bot.command(name='test')
async def test_function(ctx):
    await ctx.send("Testing")

@bot.listen('on_message')
async def message_function(ctx):
    message = ctx.message
    print(f"{message.author.name} sent a message")

bot.run(TOKEN)