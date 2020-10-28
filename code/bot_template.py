''' Basic Discord bot template(main.py) for use for Hackathons'''

import os
''' Importing os to run pip install'''
try:
    from discord.ext import commands
    from dotenv import load_dotenv
except:
    os.system("pip3 install discord.py")
    os.system("pip3 install python-dotenv")
    from discord.ext import commands
    from dotenv import load_dotenv

load_dotenv()
''' Loading environment variable and its components '''
TOKEN = os.getenv('DISCORD_TOKEN')
''' Saves the value of token, available from dev portal '''

bot = commands.Bot(command_prefix='!')
''' Fixing the prefix of the bot which it will use to respond specific commands '''

@bot.listen('on_ready')
''' One time functions which runs when the bot initializes '''
async def bot_init():
    print("Connected")

@bot.listen('on_ready')
async def bot_init_copy():
    print("Connected copy")

@bot.command(name='command')
''' Invokes this command for "!command" message '''
async def test_function(ctx):
''' ctx stands for context , which holds the details for the message recieved'''
    await ctx.send("message to be sent to the channel")
    ''' 
    Waits for the command to be executed before proceeding to other
    requests. 
    '''

@bot.listen('on_message')
''' To observe all the messages and triggers based on keywords '''
async def message_function(ctx):
    
    message = ctx.message
    ''' ctx.message gives the message string '''

    print(f"{message.author.name} sent a message")

bot.run(TOKEN)
''' TOKEN is the connection to the actual bot. This command runs the script as the bot '''