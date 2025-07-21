import telebot

TOKEN = "7996956567:AAGY5uI4ApMHXQTsQ6k88qAqW_RwD7S1Zw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! به ربات هوش مصنوعی خوش اومدی.")

bot.polling()
