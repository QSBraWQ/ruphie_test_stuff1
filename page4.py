from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class Test3Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Go to 5th screen')
        btn.bind(on_press=self.switch_screen)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def switch_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'fifth'