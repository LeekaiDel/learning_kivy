from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class GridApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation = 'vertical', size_hint = [.4, .4])
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text = 'Войти'))
        # al = AnchorLayout(anchor_x = 'left', anchor_y = 'top')

        # al.add_widget(Button(text = "Button 1", size_hint = [.5, .5]))
        al.add_widget(bl)

        return al

if __name__ == "__main__":
    GridApp().run()
