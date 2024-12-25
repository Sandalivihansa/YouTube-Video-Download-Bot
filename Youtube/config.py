import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7683501869:AAEpWF8IZIL2KRYlD2a7fFlpWmSUkXrXMRM")
    API_ID = int(os.environ.get("5047271", ))
    API_HASH = os.environ.get("API_HASH", "7683501869:AAEpWF8IZIL2KRYlD2a7fFlpWmSUkXrXMRM")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1001259556688")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
