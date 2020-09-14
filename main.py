from bot.insta_bot import InstaBot
from decouple import config


def inicia_bot():
    bot = InstaBot()
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
