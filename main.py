from bot import bot
from background import keep_alive


def main():
    keep_alive()
    bot.polling(non_stop=True)


if __name__ == '__main__':
    main()
