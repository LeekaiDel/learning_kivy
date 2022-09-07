from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation = "vertical", padding = [50, 25, 40, 0], spacing = 100)
        bl.add_widget(Button(text = "Button 1"))
        bl.add_widget(Button(text = "Button 2"))
        return bl

if __name__ == "__main__":
    BoxApp().run()