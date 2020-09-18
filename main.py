from bot.insta_bot import InstaBot
from decouple import config


def inicia_bot():
    bot = InstaBot()
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    bot.go_to_home_of('duartepaula23')
    import ipdb; ipdb.set_trace()


def main():
    inicia_bot()


if '__main__' == __name__:
    main()
