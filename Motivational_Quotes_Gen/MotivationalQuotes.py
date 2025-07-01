import requests
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size = (600,500)     # Specifies a window size to be default when opened on desktop

class XspireQuotes(MDApp):
    quote=StringProperty('')        # Quote is defined as an empty string property

    def build(self):
        self.theme_cls.primary_palette='Indigo'     # Primary Palette (For Buttons, Text Fields, etc.)
        self.theme_cls.theme_style='Dark'       # Theme (Can be Dark or Light)
        screen = Builder.load_file('quotes.kv')     # Loading the .kv file
        return screen
    
    def quotes(self):

        ''' Requests quotes from zenquotes api and changes the value of quote variable '''

        response=requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data=response.json()[0]
            self.quote = data['q'] + '\n\n-' + data['a'] + '\n'
        elif response.status_code == 404:
            self.quote = 'Error connecting to the server. Try again later.'
        elif response.status_code == 429:
            self.quote = 'Too many requests. Please try again after a while.' + '\n\n-' + 'Xspire' + '\n'
        else:
            self.quote = f"Unexpected status code: {response.status_code}. Please try again later."

if __name__=='__main__':
    XspireQuotes().run()
