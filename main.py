# Import
from kivymd.app import MDApp
from kivy.lang import Builder

# Build app

class Test(MDApp):
    def build(self):
        self.title = 'Programming'
        return Builder.load_file('Main.kv')

# Run app
Test().run()
