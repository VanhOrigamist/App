# # Import
# from kivymd.app import MDApp
# from kivy.lang import Builder

# # Build app

# class Test(MDApp):
#     def build(self):
#         self.title = 'Programming'
#         return Builder.load_file('Main.kv')

# # Run app
# Test().run()
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Hello world')
MyApp().run()
