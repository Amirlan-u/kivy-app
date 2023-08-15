from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import os
from pytube import YouTube

li = list()

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        hl = BoxLayout()
        txt = Label(text='Выбери экран')
        vl.add_widget(ScrButton(self, direction='down', goal='first', text="Открыть последний путь"))
        vl.add_widget(ScrButton(self, direction='left', goal='second', text="Скачать видео"))
        vl.add_widget(ScrButton(self, direction='up', goal='third', text="Скачать видео с расширением .webm"))
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)
class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(.9, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        open_button = Button(text="Открыть папку", size_hint=(.9, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        open_button.bind(on_press=self.open_folder)
        btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.9, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        vl.add_widget(open_button)
        vl.add_widget(btn_back)
        self.add_widget(vl)
    def open_folder(self, instance):
        # Выбор папки через стандартный диалог выбора директории
        if len(li) == 0:
            os.system(r"explorer.exe " + os.path.abspath("C:"))
        elif li[0] != "":
            os.system(r"explorer.exe", li[0])
        else:
            os.system(r"explorer.exe " + os.path.abspath("C:"))

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        URL = Label(text="URL видео")
        self.URL = TextInput()
        path = Label(text="Путь сохранения")
        self.path = TextInput()
        regis = Button(text="Скачать")
        regis.bind(on_press=self.register)
        back = ScrButton(self, direction='down', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
        layout.add_widget(URL)
        layout.add_widget(self.URL)
        layout.add_widget(path)
        layout.add_widget(self.path)
        layout.add_widget(regis)
        layout.add_widget(back)
        self.add_widget(layout)

    def register(self, instance):
        URL = self.URL.text
        path = self.path.text

        if URL == "":
            msg = "Ты не написал URL"
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()
        elif path == "":
            yt = YouTube(URL)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            msg = "Видео скачено, путь к файлу: " + os.path.abspath("C:")
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()

        else:
            yt = YouTube(URL)
            stream = yt.streams.get_highest_resolution()
            stream.download(path)
            msg = "Видео скачено путь к файлу:".format(path)
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()



class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        URL = Label(text="URL видео")
        self.URL = TextInput()
        path = Label(text="Путь сохранения")
        self.path = TextInput()
        regis = Button(text="Скачать")
        regis.bind(on_press=self.register)
        back = ScrButton(self, direction='down', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
        layout.add_widget(URL)
        layout.add_widget(self.URL)
        layout.add_widget(path)
        layout.add_widget(self.path)
        layout.add_widget(regis)
        layout.add_widget(back)
        self.add_widget(layout)

    def register(self, instance):
        URL = self.URL.text
        path = self.path.text

        if URL == "":
            msg = "Ты не написал URL"
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()
        elif path == "":
            yt = YouTube(URL, use_oauth=True, allow_oauth_cache=True)
            striming = yt.streams.get_by_itag(251)
            striming.download()
            msg = "Файл был скачен, путь к файлу: " + os.path.abspath("C:")
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()
        else:
            yt = YouTube(URL, use_oauth=True, allow_oauth_cache=True)
            stream = yt.streams.get_highest_resolution()
            stream.download(path)
            msg = "Файл был скачен, путь к видео: " + path
            popup = Popup(title="Regisration", content=Label(text=msg), size_hint=(None, None), size=(600, 400))
            popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        return sm


MyApp().run()

