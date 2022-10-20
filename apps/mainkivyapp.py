from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text="My new App open to World",
            pos=(50,50),
            size = (250,50),
            size_hint=(None,None)) #percent of width and height
            

if __name__=="__main__":
    LanguageLearnerApp().run()

