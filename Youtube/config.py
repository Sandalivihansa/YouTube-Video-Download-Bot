import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7683501869:AAEpWF8IZIL2KRYlD2a7fFlpWmSUkXrXMRM", "")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("047d9ed308172e637d4265e1d9ef0c27", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("-1001259556688", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
