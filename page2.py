from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class Test1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        text1=Label(text='Замерьте пульс за 3 минуты')
        self.input1=TextInput(hint_text="100")
        btn = Button(text='Go to 3rd screen')
        btn.bind(on_press=self.switch_screen)
        layout.add_widget(text1)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def switch_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'third'