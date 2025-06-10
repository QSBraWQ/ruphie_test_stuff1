# напиши здесь свое приложение
# p1=int(input())
# p2=int(input())
# p3=int(input())
# formula=(p1+p2+p3-200)/10
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from page1 import LoginScreen
from page2 import Test1Screen
from page3 import Test2Screen
from page4 import Test3Screen
from page5 import SitsScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='first'))
        sm.add_widget(Test1Screen(name='second'))
        sm.add_widget(Test2Screen(name='third'))
        sm.add_widget(Test3Screen(name='fourth'))
        sm.add_widget(SitsScreen(name='fifth'))
        return sm

if __name__ == '__main__':
    MyApp().run()