import telebot
from decouple import config

import gold
import dollar
import tools

#معالج
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

gold_words = ["ذهب", "الذهب", "سعر الذهب", "gold"]
dollar_words = ["دولار", "الدولار", "سعر الدولار", "dollar"]
king = ["من صنعك", "من المطور"]

help_text = ("اهلا بك\n"
             "/gold  اسعار الذهب\n"
             "/dollar  سعر الدولار\n"
             "/calc  حاسبة مثل: /calc 5*(2+3)\n"
             "/db  تحويل نسبة الى ديسيبل مثل: /db 100")

bot.set_my_commands([
    telebot.types.BotCommand("gold", "اسعار الذهب"),
    telebot.types.BotCommand("dollar", "سعر الدولار"),
    telebot.types.BotCommand("calc", "حاسبة"),
    telebot.types.BotCommand("db", "تحويل نسبة الى ديسيبل"),
    telebot.types.BotCommand("help", "المساعدة"),
])


def get_args(message):
    # ما بعد الامر مثل: /calc 5+5 ترجع 5+5
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1:
        return parts[1]
    return ""


#__________________________________
#الاوامر

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=["gold"])
def gold_price(message):
    bot.send_message(message.chat.id, gold.get_gold())


@bot.message_handler(commands=["dollar"])
def dollar_price(message):
    bot.send_message(message.chat.id, dollar.get_dollar())


@bot.message_handler(commands=["calc"])
def calculator(message):
    bot.reply_to(message, tools.calc(get_args(message)))


@bot.message_handler(commands=["db"])
def decibel(message):
    bot.reply_to(message, tools.to_db(get_args(message)))


#__________________________________
#الرسائل العادية

def isMSG(message):
    return True


@bot.message_handler(func=isMSG)
def reply(message):
    # ازالة المسافات الزائدة بين الكلمات
    words_all = " ".join(str(message.text).split())

    if words_all in king:
        return bot.reply_to(message, "جعفر داؤد")

    elif words_all in gold_words:
        return bot.reply_to(message, gold.get_gold())

    elif words_all in dollar_words:
        return bot.reply_to(message, dollar.get_dollar())

    else:
        return bot.reply_to(message, " عذرا هذه الكلمة غير موجودة")


bot.infinity_polling()
