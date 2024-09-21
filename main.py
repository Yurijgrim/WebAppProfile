from telebot import types
import telebot

token='your_token_bot'
bot = telebot.TeleBot(token)

u_taplink = "https://taplink.cc/test98729872"

def webAppKeyboardInline():
   keyboard = types.InlineKeyboardMarkup(row_width=1) 
   webApp = types.WebAppInfo(u_taplink) 
   one = types.InlineKeyboardButton(text="web profile", web_app=webApp) 
   keyboard.add(one) 
   return keyboard 

@bot.message_handler(commands=['start'])
def start_fun(message):
   bot.send_message( message.chat.id, 'Получение доступа к информации.', parse_mode="Markdown", reply_markup=webAppKeyboardInline()) #отправляем сообщение с нужной клавиатурой


if __name__ == '__main__':
   bot.infinity_polling()