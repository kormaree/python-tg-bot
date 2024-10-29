import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    stick = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный, чтобы рассылать своим ученикам задания для подготовки к экзаменам. Пока нахожусь в разработке(".format(message.from_user, bot.get_me()), parse_mode='html')


bot.polling(non_stop=True)