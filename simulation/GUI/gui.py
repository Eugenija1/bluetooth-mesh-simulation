import tkinter as tk
from tkinter import filedialog
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


Window.size = (1024, 640)


class MainWindow(Screen):
    pass


class WelcomeWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class PathButton(Button):
    @staticmethod
    def get_path():
        root = tk.Tk()
        root.withdraw()
        return filedialog.askopenfilename()


class PathWindow(Screen):
    pass


kv = Builder.load_file("my.kv")
sm = WindowManager()
screens = [WelcomeWindow(name="welcome"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
