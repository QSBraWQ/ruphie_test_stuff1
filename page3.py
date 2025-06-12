from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import BooleanProperty
from kivy.clock import Clock
from Timer import Timer

class Test2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Go to 4th screen')
        btn.bind(on_press=self.switch_screen)
        text1=Label(text="Таймеры")
        timer_layout = BoxLayout(orientation='horizontal')
        
        timer1 = Timer(text="Я таймер")
        timer2 = Timer(text="Я таймер")
        timer3 = Timer(text="Я таймер")
        timer_layout.add_widget(timer1)
        timer_layout.add_widget(timer2)
        timer_layout.add_widget(timer3)
        layout.add_widget(text1)
        layout.add_widget(timer_layout)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def switch_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'fourth'


