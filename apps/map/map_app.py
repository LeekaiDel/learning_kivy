from tkinter import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Line)



class MapSolid(MapView):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0, 1)
            rad = 10
            Ellipse(pos = (touch.x - rad / 2, touch.y - rad / 2), size = (rad, rad))
            # touch.ud['line'] = Line(points = (touch.x, touch.y), width = 15)
            print(self.get_latlon_at(touch.x - rad / 2, touch.y - rad / 2))
            



class MapApp(App):
    def point_butt(self, instance):
        self.set_point = not self.set_point
        print("Point press " + str(self.set_point))
    

    def home_butt(self, instance):
        print("Home press")


    def send_butt(self, instance):
        print("Send press")


    def clear_points_butt(self, instance):
        pass

    def build(self):
        self.set_point = False

        self.map = MapSolid() #MapView(lat = 47.201738, lon = 38.934003, zoom = 18, size_hint = (0.8, 1))
                
        bl = BoxLayout()

        bl_buttons = BoxLayout(size_hint = (0.2, 1), orientation = 'vertical', spacing = 3)
        bl_buttons.add_widget(Label(text = 'lat:\nlon:\n'))
        bl_buttons.add_widget(Button(text = 'Point', on_press = self.point_butt))
        bl_buttons.add_widget(Button(text = 'Home', on_press = self.home_butt))
        bl_buttons.add_widget(Button(text = 'Send', on_press = self.send_butt))
        bl_buttons.add_widget(Button(text = 'Clear points', on_press = self.clear_points_butt))

        bl.add_widget(self.map)
        bl.add_widget(bl_buttons)

        return bl

if __name__ == "__main__":
    MapApp().run()