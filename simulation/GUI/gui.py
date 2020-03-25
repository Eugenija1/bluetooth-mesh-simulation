from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.app import App
from kivy.lang import Builder

Window.size = (1024, 640)


class MainWindow(Screen):
    pass


class ScreenFileChooser(Screen):
    def __init__(self, **kwargs):
        super(ScreenFileChooser, self).__init__(**kwargs)
        # filter added. Since windows will throw error on sys files
        self.fclv = FileChooserIconView(filters=[lambda folder, filename: not filename.endswith('.sys')])
        self.add_widget(self.fclv)


class WelcomePanel(RelativeLayout):
    pass


class ConfigPanel(RelativeLayout):
    pass


kv = Builder.load_file("C:\\Users\\Berezka\\programming\\symulacja\\bluetooth-mesh-simulation\\simulation\\GUI\\my.kv")
sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(ScreenFileChooser(name='chooser'))


class MyMainApp(App):
    def build(self):
        return sm

    def open_chooser(self):
        print("switch screens")
        sm.transition.duration = 1
        sm.transition = FadeTransition()
        sm.current = 'chooser'


if __name__ == "__main__":
    MyMainApp().run()
