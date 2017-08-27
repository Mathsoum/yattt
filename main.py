import kivy
from kivy.app import App

from views import Controller

kivy.require('1.10.0')


class YatttApp(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
    YatttApp().run()
