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

Language = 'SP'

TEXT = {
    'EN': {
        'START' : \
            'Welcome to the Music Downloader Bot!\n\n' \
            'I am here to give you the music you want.',

        'HELP' : \
            'How may I help you?',

        'NOTURL' : \
            'Please, send me a real URL, otherwise I cant do nothing.\n\n' \
            'Thank you.',

        'ABOUT' : \
            'This is an open-source bot with GPL-GNU license, created by ' \
            'the telegram user:' \
            '\n- @Presmanes3.\n' \
            'You can find my source code at:\n' \
            '- https://github.com/Presmanes3/YoutuBot\n\n' \
            'Please, if you find an error or you have an issue, feed me back.',

        'DOWNLOAD': {
            'START' : \
                'Starting download!',
            'FINISH' : \
                'Downloaded, thank you!'
                },
        'LANGUAGE' : {
            'CHANGE' : \
                'Language changed sucessfull!',
            'SAME' : \
                'Language unchanged, same language detected as argument.',
            'UNIDENTIFIED' : \
                'Language not identified, choose an available one.'\
                'If you dont know which are available use the command /help',
            'NOTARG' : \
                'Language not detected, you forgot to put a language as argument.'
                }
        },
    'SP': {
        'START' : \
            'Bienvenidos al Bot Descargador de Musica!\n\n' \
            'Estoy aqui para darte la musica que quieres.',

        'HELP' : \
            'Como podria ayudarle?',

        'NOTURL' : \
            'Por favor, mandame una URL real, de otra manera no puedo hacer nada.\n\n' \
            'Gracias.',

        'ABOUT' : \
            'Este es un bot open-source con licencia GPL-GNU, creado por ' \
            'el usuario de telegram:' \
            '\n- @Presmanes3.\n' \
            'puedes encontrar mi codigo en:\n' \
            '- https://github.com/Presmanes3/YoutuBot\n\n' \
            'Por favor, si encuentras algun error o inconveniente, avisame.',

        'DOWNLOAD': {
            'START' : \
                'Descarga iniciada!',
            'FINISH' : \
                'Descargada, gracias!'
                },
        'LANGUAGE' : {
            'CHANGE' : \
                'Idioma cambiado satisfactoriamente!',
            'SAME' : \
                'Idioma no cambiado, se detecto la misma lengua como argumento.',
            'UNIDENTIFIED' : \
                'Idioma sin identificar, elige uno disponible.\n'\
                'Si no sabes cuales estan disponibles usa el comando /help',
            'NOTARG' : \
                'Idioma no detectado, olvidaste poner uno como argumento.'
                }
        }
}
