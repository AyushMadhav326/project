from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import os

kivy.require('1.9.0')

Window.size =(800,600)

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot,self).__init__()

    def generate_number(self):
        os.startfile(r'D:\ay\New folder\Emotion_Detection_CNN-main\Facial-Emotion-Recognition-with-OpenCV-and-Deepface-main\gui\MusicWindow1.py')

    def motion_open(self):
        os.startfile(r'D:\ay\New folder\Emotion_Detection_CNN-main\Facial-Emotion-Recognition-with-OpenCV-and-Deepface-main\gui\MotionWindow.py')

class app(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    app().run()