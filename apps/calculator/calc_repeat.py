from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)

class CalculatorApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def add_operation(self, instance):
        if(self.formula == "0"):
            return
        
        if(str(instance.text).lower() == "x"):
            self.formula += "*"    
        else:
            self.formula += str(instance.text)
        self.update_label()

    def add_number(self, instance):
        if(self.formula == "0"):
            self.formula = ""
            self.formula += str(instance.text)
        else:
            self.formula += str(instance.text)
        self.update_label()
        # print(self.formula)

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = "vertical")
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, 0.6))
        
        self.lbl = Label(text = self.formula, font_size = 40, size_hint = (1, 0.4), text_size = (400 - 50, 500 * 0.4 - 50), halign = "right")

        bl.add_widget(self.lbl)

        gl.add_widget( Button(text = "7", on_press = self.add_number) )
        gl.add_widget( Button(text = "8", on_press = self.add_number) )
        gl.add_widget( Button(text = "9", on_press = self.add_number) )
        gl.add_widget( Button(text = "X", on_press = self.add_operation) )

        gl.add_widget( Button(text = "4", on_press = self.add_number) )
        gl.add_widget( Button(text = "5", on_press = self.add_number) )
        gl.add_widget( Button(text = "6", on_press = self.add_number) )
        gl.add_widget( Button(text = "-", on_press = self.add_operation) )

        gl.add_widget( Button(text = "1", on_press = self.add_number) )
        gl.add_widget( Button(text = "2", on_press = self.add_number) )
        gl.add_widget( Button(text = "3", on_press = self.add_number) )
        gl.add_widget( Button(text = "+", on_press = self.add_operation) )

        gl.add_widget( Widget() )
        gl.add_widget( Button(text = "0", on_press = self.add_number) )
        gl.add_widget( Button(text = ".", on_press = self.add_operation) )
        gl.add_widget( Button(text = "=", on_press = self.calc_result) )

        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    CalculatorApp().run()