import os
from img_classify import *

try:
    from PIL import Image
    import discord
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

pic_ext = ['.jpg', '.png', '.jpeg']


async def classify_and_detect(message, addr, top_image_addr):
    # val = classify(addr)
    det_boxes, non_nude = detect(addr, top_image_addr)
    channel = message.channel
    non_nude.save("./images/non_nude.png")

    if len(det_boxes) > 0:
            await message.delete()
            result = "According to that image, you are horny. I have deleted that image for Zeeshan's protection."
            await channel.send(result)
            await channel.send(file=discord.File('./images/non_nude.png'))

    # await channel.send(f"Val: `{val}`")
    # await channel.send(f"```\n{detection_result}\n```")  

@bot.listen('on_message')
async def message_function(message):
    if message.author.bot:
        return
    print(f"{message.author.name} sent a message")

    if message.attachments != []:
        for attachment in message.attachments:
            for ext in pic_ext:
                if attachment.url.endswith(ext):
                    save_img(attachment.url, ext)
                    await classify_and_detect(message, f"./images/test_image{ext}", "./images/pumpkin.png")

    else:
        for ext in pic_ext:
            if message.content.endswith(ext) and message.content.startswith('https://'):
                print(message.content)
                save_img(message.content, ext)
                await classify_and_detect(message, f"./images/test_image{ext}", "./images/pumpkin.png")

bot.run(TOKEN)
