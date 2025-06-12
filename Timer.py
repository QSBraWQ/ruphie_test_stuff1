from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import BooleanProperty
from kivy.clock import Clock

class Timer(Label):
    done = BooleanProperty(False)
    def _init__(self, total=600, **kwargs):
        super().__init__(**kwargs)
        self.current = 0
        self.total = total
        self.text = f"{self.current} s"
        self.event = None
    def restart(self, total=15):
        if self.event:
            self.event.cancel()
            self.done = False
            self.total = total
            self.current = 0
            self.text = f"{self.current} s"
            self.start()
    def start(self):
        self.event = Clock.schedule_interval(self.change, 1)
    def change (self, dt):
        self.current += 1
        self.text = f"{self.current} s" 
        if self.current >= self.total:
              self.done = True
        return False