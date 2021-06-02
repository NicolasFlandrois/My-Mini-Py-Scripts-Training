#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Wed 02 June 2021 10:03:57 CEST
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date: Wed 02 June 2021 10:51:45 CEST
# Python 3.9
# Kivy 2.0.0
# Description: Basics of Kivy Framework. "Hello Wolrd!"
# Simple rendering window, custom layouts, render an image and Text,
# Taking input, User interaction Button, callbacks

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    """
    Class managing the app.
    NB: Kivy works in OOP only.
    """
    def build(self):
        """Display rendering. Window size keep dynamic/responsive design"""
        # Manage Grid & Window layout
        self.window = GridLayout()
        self.window.cols = 1

        # Redesign the window/Custom/Beautify
        # Add Padding (40% & 30%) 1-PaddingTarget%
        self.window.size_hint = (0.6, 0.7)
        # Global Center enverything
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # Image Widget (Build/Render Image)
        self.window.add_widget(Image(source="PythonPoweredHelloWorld.png"))

        # Laber Widget (Static Text Rendering)
        self.greeting = Label(
                              text="What's your name ?",
                              font_size=18,  # Change Font (Beautify process)
                              color='#F18700'  # Change Color
                              # (Beautify process)
                              )
        self.window.add_widget(self.greeting)

        # Text input widget
        self.user = TextInput(
                              multiline=False,
                              padding_y=(20, 20),  # Add Padding to input
                              # text box, on Y axis, makes it easier to read
                              # (Beautify process)
                              size_hint=(1, 0.5)  # Change Box Size keep
                              # width within 1 col, hight decreased in Half
                              # (Beautify process)
                              )
        self.window.add_widget(self.user)

        # Button Widget (Validate Button)
        self.button = Button(
                             text="GREET",
                             size_hint=(1, 0.5),  # Change Box Size keep width
                             # within 1 col, hight decreased in Half
                             # (Beautify process)
                             bold=True,  # Just makes the text inside Button
                             # BOLD (Beautify process)
                             background_color='#F18700',  # Self explainatory,
                             # same color as text. However the color isn't
                             # quite the same, darker if no extra attributes.
                             # (Beautify process)
                             background_normal=''  # Extra argument to get
                             # the true background color. (not darker, but
                             # just as asked for) But for your eyes, might
                             # wanna keep it a shade darker. (Beautify process)
                             )
        self.button.bind(on_press=self.callback)  # Binding input to what to
        # do from user interactions, so we can display it in window
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        """Manages user interactions, on clic from button, catch input text"""
        self.greeting.text = f'Hello {self.user.text} !'
        # Note... No return!...


if __name__ == "__main__":
    SayHello().run()
