from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Constants, Token, logging, os
logging.basicConfig(ormat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token=Token.TOKEN)

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=Constants.Start_message)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=Constants.Help_message)

def download_song(bot, update):
    URL = update.message.text
    cwd = os.getcwd()
    command = "youtube-dl -o '{}/%(title)s.%(ext)s' --extract-audio --audio-format mp3 {}".format(cwd, URL)
    os.system(command)
    song_name = None
    for root, dirs, files in os.walk(cwd):
        for f in files:
            filename = os.path.join(root, f)
            if filename.endswith('.mp3'):
                song_name = str(f)
    bot.send_audio(audio = open(song_name,'rb'),chat_id=update.message.chat_id, title = song_name, caption="Downloaded, thank you!")
    #bot.send_message(chat_id=update.message.chat_id, text= ("Song Downloaded! > " + str(song_name)))
    os.system("rm %s/'%s'" %(cwd,str(song_name)))

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
download_handler = MessageHandler(Filters.text, download_song)

# ------- Handlers ------- #
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(download_handler)

# ------- Start ------- #
updater.start_polling()
