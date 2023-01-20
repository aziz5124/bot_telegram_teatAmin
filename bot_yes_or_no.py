from asyncore import dispatcher
from cgitb import text
from telegram.ext import Updater 
from telegram.ext import CommandHandler, MessageHandler, Filters,Updater,ConversationHandler
from telegram import ReplyKeyboardMarkup
import requests




def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please say /yes or /no")

def dyw(update, context):
    reply_keyboard = [['yes', 'no']]
    update.message.reply_text(
        
        "do you want mem",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )   
    if reply_keyboard =="yes":
        return echo


    
def echo(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=getPhoto())

def getPhoto():
    content=requests.get('http://meme-api.herokuapp.com/gimme').json()
    url =content['url']
    return url 

def no_echo(update, context):
    update.message.reply_text('So, GooD by')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
     
echo_handler= MessageHandler(Filters.regex('^(yes)$') & (~Filters.command), echo)
        
no_echo_handler=MessageHandler(Filters.regex('^(no)$') & (~Filters.command), no_echo)




updater = Updater(token='5772604818:AAHfQrdNDADHqK5_YGfo7rKC_c5lg1C86aM', use_context=True)

dispatcher = updater.dispatcher
    
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(no_echo_handler)
updater.start_polling()

