"""
Script:
    YoutuBot.py
Description:
    This is a bot created to download your favourite songs from youtube!
Author:
    Javier Presmanes Cardama
Creation date:
    15/04/2018
Last modified date:
    20/04/2018
Version:
    1.2.0 - Multi-language support
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Token, logging, re, os, subprocess
import Constants
logging.basicConfig(ormat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#####################################
# ------- Set Up ------- #
updater = Updater(token=Token.TOKEN)
dispatcher = updater.dispatcher
url_filter = re.compile("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)[\w\=]*)?")
TEXT = Constants.TEXT
LANG = Constants.Language
# ------- Functions ------- #

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=TEXT[LANG]['START'])

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=TEXT[LANG]['HELP'])

def about(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=TEXT[LANG]['ABOUT'])

def set_language(bot, update, args):
    chat_id_ = update.message.chat_id
    MODE = ''
    # print(LANG)
    if len(args) == 1:
        lang_provided = args[0].upper()
        if lang_provided in TEXT:
            if lang_provided != LANG:
                global LANG
                LANG = lang_provided
                MODE = 'CHANGE'
            else:
                MODE = 'SAME'
        else:
            MODE = 'UNIDENTIFIED'
    else:
        MODE = 'NOTARG'
    bot.send_message(chat_id = update.message.chat_id, text = TEXT[LANG]['LANGUAGE'][MODE])

def download_song(bot, update):
    try:
        chat_id_ = update.message.chat_id
        chat_text = update.message.text
        # Take URL from the message
        URL = url_filter.search(chat_text).group()
        # Get current directory
        cwd = os.getcwd()
        # Execute download script
        command = "youtube-dl -o {}/%(title)s.%(ext)s --extract-audio --audio-format mp3 {}".format(cwd, URL)
        # Starting
        bot.send_message(chat_id= chat_id_, text=TEXT[LANG]['DOWNLOAD']['START'])
        subprocess.check_call(command.split())
        # Get song name
        song_name = None
        for root, dirs, files in os.walk(cwd):
            for f in files:
                filename = os.path.join(root, f)
                if filename.endswith('.mp3'):
                    song_name = str(f)
        # Send music file
        bot.send_audio(audio = open(song_name,'rb'),chat_id=chat_id_, title = song_name, caption=TEXT[LANG]['DOWNLOAD']['FINISH'])
        # Delete song file
        os.system("rm {}/'{}'".format(cwd,song_name))
    except:
        bot.send_message(chat_id=chat_id_, text=TEXT[LANG]['NOTURL'])



# ------- Main ------- #
def main():

    # ------- Variable Handlers ------- #
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    about_handler = CommandHandler('about', about)
    language_handler = CommandHandler('language', set_language, pass_args=True)
    download_handler = MessageHandler(Filters.text, download_song)

    # ------- Add Handlers ------- #
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(language_handler)
    dispatcher.add_handler(download_handler)

    # ------- Start ------- #
    updater.start_polling()

if __name__ == '__main__':
    main()
