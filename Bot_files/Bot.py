from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Constants, Token, logging, re, os, subprocess
logging.basicConfig(ormat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#####################################
# ------- Set Up ------- #
updater = Updater(token=Token.TOKEN)
dispatcher = updater.dispatcher
url_filter = re.compile("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)[\w\=]*)?")
#####################################

#####################################
# ------- Functions ------- #

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=Constants.Start_message)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=Constants.Help_message)

def about(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=Constants.About_message)

def download_song(bot, update):
    try:
        # Take URL from the message
        URL = url_filter.search(update.message.text).group()
        # Get current directory
        cwd = os.getcwd()
        # Execute download script
        command = "youtube-dl -o {}/%(title)s.%(ext)s --extract-audio --audio-format mp3 {}".format(cwd, URL)
        # Starting
        bot.send_message(chat_id=update.message.chat_id, text="Starting download!")
        subprocess.check_call(command.split())
        # Get song name
        song_name = None
        for root, dirs, files in os.walk(cwd):
            for f in files:
                filename = os.path.join(root, f)
                if filename.endswith('.mp3'):
                    song_name = str(f)
                    # Send music file
        bot.send_audio(audio = open(song_name,'rb'),chat_id=update.message.chat_id, title = song_name, caption="Downloaded, thank you!")
        # Delete song file
        os.system("rm {}/'{}'".format(cwd,song_name))
    except:
        bot.send_message(chat_id=update.message.chat_id, text=Constants.Not_URL_message)

# ------- Variable Handlers ------- #
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
about_handler = CommandHandler('about', about)
download_handler = MessageHandler(Filters.text, download_song)

# ------- Add Handlers ------- #
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(about_handler)
dispatcher.add_handler(download_handler)

# ------- Start ------- #
updater.start_polling()
