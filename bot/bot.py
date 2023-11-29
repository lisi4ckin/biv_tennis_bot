from django.conf import settings
import telebot
from users.main import UserService
from bot.data.users_list import users_list
from bot.data.bot_command import commands

bot = telebot.TeleBot(settings.TOKEN_BOT)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
for command in commands:
    add_button = telebot.types.InlineKeyboardButton(text=command)
    keyboard.add(add_button)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать в мир тенниса BIV. Я твой помощник. С моей помощью ты сможешь "
                     "проверить свой рейтинг, проследить за текущим турниром. Для более подробной "
                     "информации воспользуйся командой Помощь. Желаю удачи в твоем непростом пути к "
                     "вершинам тенниса BIV:)", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == 'Зарегистрироваться':
        registration_user_in_system(message)
    if message.text == 'Помощь':
        send_help(message)
    if message.text == 'Общий рейтинг':
        get_users_rates(message, None)
    if message.text == 'Мой рейтинг':
        get_users_rates(message, message.chat.id)


# Create user with message
def registration_user_in_system(message):
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
    for user in users_list:
        add_button = telebot.types.InlineKeyboardButton(text=user, callback_data=user)
        inline_keyboard.add(add_button)
    bot_message = "Выберите один из предложенных вариантов"
    bot.send_message(message.from_user.id, bot_message, reply_markup=inline_keyboard)


def send_help(message):
    bot.send_message(message.chat.id, "{}".format("\n".join(commands[0:])))


def get_users_rates(message, user_chat_id: str):
    all_users = UserService.get_all_tennis_users(user_chat_id)
    bot.send_message(message.chat.id, "{}".format("\n".join(str(user) for user in all_users)))


@bot.callback_query_handler(func=lambda call: call.data in users_list)
def create_user(call):
    chat_id = None
    new_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for command in commands[1:]:
        add_button = telebot.types.InlineKeyboardButton(text=command)
        new_keyboard.add(add_button)
    try:
        message = call.message
        chat_id = message.chat.id
        UserService.create_user(create_username=call.data,
                                user_chat_id=chat_id)
        bot.send_message(chat_id, "Вы успешно зарегистрировались в системе".format(call.data),
                         reply_markup=new_keyboard)
    except ValueError:
        bot.send_message(chat_id, "Пользователь {} уже зарегистрирован в системе".format(call.data),
                         reply_markup=new_keyboard)
