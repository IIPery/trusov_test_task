import telebot
from telebot.types import Message

from config import BOT_TOKEN
from service import get_currency_converter_data

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_message(message.chat.id, 'Добрый день👋 Как вас зовут?')


@bot.message_handler()
def show_currency_data(message: Message) -> None:
    username = message.text
    bot.send_message(message.chat.id, f'Рад знакомству, {username}!')
    bot.send_message(message.chat.id, f'Курс доллара сегодня {get_currency_converter_data()} руб')


def main() -> None:
    bot.infinity_polling()


if __name__ == '__main__':
    main()
