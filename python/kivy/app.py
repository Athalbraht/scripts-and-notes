import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Connect(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="xD:"))
        self.xd = TextInput(multiline=False)
        self.add_widget(self.xd)
        self.add_widget(Label(text="xD2:"))
        self.xd2 = TextInput(multiline=False)
        self.add_widget(self.xd2)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)
    def join_button(self, instance):
        xd = self.xd.text
        xd2 = self.xd2.text
        print("xD")
        myapp.info_page.update_info(xd)
        myapp.screen_manager.current = "Info"
        Clock.schedule_once(self.connect, 1)
    def connect(self,_):
        a = "123"
        myapp.create_page()
        myapp.screen_manager.current = "New"


class NewPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="left", valign="top", font_size=20,text = "New")
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="left", valign="top", font_size=20)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)



class Main(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = Connect()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    def create_page(self):
        self.page = NewPage()
        screen = Screen(name="New")
        screen.add_widget(self.page)
        self.screen_manager.add_widget(screen)

if __name__ == "__main__":
    myapp = Main()
    myapp.run()
