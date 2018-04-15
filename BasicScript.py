"""With this script you will be able to download your music directly
to your ~/Music folder.

It uses youtube-dl to download the music and it has the same effect that if you
use the following command directly in your terminal :
- youtube-dl -o "~Music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 <URL>"""

import os

URL = raw_input("Paste here the song URL that you would like to download : ")
print("Downloading!\n")
command = "youtube-dl -o '~/Music/%(title)s.%(ext)s' --extract-audio --audio-format mp3 " + URL
os.system(command)
print("\nDone! Check yout ~/Music folder.")
