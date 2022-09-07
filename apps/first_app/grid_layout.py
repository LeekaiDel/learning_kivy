from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridApp(App):
    def build(self):
        gl = GridLayout(cols = 5, rows = 5, padding = [30], spacing = 3)

        for x in range(25):
            gl.add_widget(Button(text = str(x)))


        return gl

if __name__ == "__main__":
    GridApp().run()
