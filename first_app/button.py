from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text = "Press me", 
        font_size = 28, 
        on_press = self.btn_press,
        background_color = [0, 1, 0, 1],
        background_normal = '')

    def btn_press(self, instance):
        print("Кнопка нажата!")


if __name__ == "__main__":
    MyApp().run()