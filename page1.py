from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import BooleanProperty, ObjectProperty


class LoginScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lowlayout=BoxLayout(orientation='horizontal')
        lowlayout1 = BoxLayout(orientation='vertical')
        self.lowtext1=Label(text='Какое имя?')
        self.lowinput1=TextInput(hint_text="Joe Dough")
        self.lowtext2=Label(text='Какой возраст?')
        self.lowinput2=TextInput(hint_text="99")
        lowlayout1.add_widget(self.lowtext1)
        lowlayout1.add_widget(self.lowinput1)
        lowlayout1.add_widget(self.lowtext2)
        lowlayout1.add_widget(self.lowinput2)
        lowlayout3 = BoxLayout(orientation='vertical')
        toplayout1 = BoxLayout(orientation='vertical')
        toplayout11 = BoxLayout(orientation="vertical")

        btn = Button(text='Go to Second Screen')
        btn.bind(on_press=self.switch_screen)
        toplayout1.add_widget(toplayout11)
        toplayout1.add_widget(btn)
        lowlayout3.add_widget(toplayout1)
        emptylowlayout1=BoxLayout(orientation='vertical')
        lowlayout2=BoxLayout(orientation='vertical')
        lowlayout2.add_widget(emptylowlayout1)
        lowlayout2.add_widget(lowlayout1)
        lowlayout.add_widget(lowlayout2)
        lowlayout.add_widget(lowlayout3)
        self.add_widget(lowlayout)

    def switch_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'second'
        # if self.lowinput1.text.strip()!='':
        #     try:
        #         age=int(self.lowinput2.text)
        #         if age >= 7:  
        #             self.manager.transition = SlideTransition(direction='left')
        #             self.manager.current = 'second'
        #     except:
        #         self.lowtext2.text = "Input valid age (more than 7)"
        # else:
        #     self.lowtext1.text = "Input valid name"