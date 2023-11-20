from telebot import TeleBot
from config import *
from time import sleep
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


bot = TeleBot(api_token, parse_mode='html')


# Sending chat action
def send_chat_action(chat_id, action: str, time: int = 2) -> None:
    sleep(time)
    bot.send_chat_action(chat_id, action)


def get_menu_keyboard(menu_buttons: list, one_time: bool = True) -> ReplyKeyboardMarkup | None:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time)
    if menu_buttons:
        for btn in menu_buttons:
            keyboard.add(KeyboardButton(btn))

        return keyboard
    return


# Write start message
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    if message.from_user.last_name is not None:
        user += f' {message.from_user.last_name}'

    keyboard = get_menu_keyboard(['Menu', 'Help', 'Exit'])
    send_chat_action(message.chat.id, chat_actions['text'])
    bot.send_message(message.chat.id,
                     f'Hello, {user}!\nPress button to open menu.',
                     reply_markup=keyboard)


# Check text messages
@bot.message_handler(content_types=['text'])
def check_message(message):
    if message.text.lower() == 'exit':
        keyboard = get_menu_keyboard(['START'])
        send_chat_action(message.chat.id, chat_actions['text'])
        bot.send_message(message.chat.id, 'Goodbye!', reply_markup=keyboard)
    elif message.text.lower() == 'menu':
        send_chat_action(message.chat.id, chat_actions['text'])
        keyboard = get_menu_keyboard([])
        bot.send_message(message.chat.id, 'Menu is opening', reply_markup=keyboard)
    elif message.text.lower() == 'help':
        keyboard = get_menu_keyboard(['Menu'])
        send_chat_action(message.chat.id, chat_actions['text'])
        bot.send_message(message.chat.id, f'Help list: {help_list}', reply_markup=keyboard)
    elif message.text.upper() == 'START':
        keyboard = get_menu_keyboard(['Menu'])
        send_chat_action(message.chat.id, chat_actions['text'])
        bot.send_message(message.chat.id, 'Hello!\nPress button to open menu!', reply_markup=keyboard)
    else:
        keyboard = get_menu_keyboard(['Menu'])
        send_chat_action(message.chat.id, chat_actions['text'])
        bot.send_message(message.chat.id, "Sorry, I don't understand!\nUse help to open help list\n"
                                          "Or press button to open menu",
                         reply_markup=keyboard)
