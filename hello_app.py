from kivy.app import App
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        # Create and return a button with the label "Say Hello"
        return Button(text="Say Hello", on_release=lambda btn: print("Hello"))

if __name__ == "__main__":
    HelloApp().run()
