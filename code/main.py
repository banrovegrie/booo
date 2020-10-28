import os
import sys

import init
from init import *

from googleapiclient import discovery
from dotenv import load_dotenv
import discord
from discord.ext import commands

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='*')
    print("I am feeling hot")

if __name__ == "__main__":
    main()
