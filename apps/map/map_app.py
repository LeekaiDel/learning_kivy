from tkinter import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker, MapSource
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Line)
# from kivy_garden.mapview import 

class MapLayer(MapView):
    def __init__(self, **kwargs):
        self.set_point = False
        super(MapLayer, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if(self.set_point) and touch.button == 'left':
            self.add_marker(marker = MapMarker(lon = self.get_latlon_at(touch.x, touch.y)[1], lat = self.get_latlon_at(touch.x, touch.y)[0]))
        
        if(touch.button == 'scrollup'):
            if(self.zoom < self.map_source.get_max_zoom()):
                self.zoom += 1
        elif(touch.button == 'scrolldown'):
            if(self.zoom > self.map_source.get_min_zoom()):
                self.zoom -= 1

    def on_touch_move(self, touch):     
        self.center_on(self.get_latlon_at(float(self.center_x) - float(touch.dx), float(self.center_y) - float(touch.dy)))
        

class MapApp(App):
    def point_butt(self, instance):
        self.set_point = not self.set_point
        self.map.set_point = self.set_point
        print("Point press " + str(self.set_point))


    def home_butt(self, instance):
        print("Home press")


    def send_butt(self, instance):
        print("Send press")


    def clear_points_butt(self, instance):
        # self.map.remove_marker()
        pass


    def build(self):
        self.set_point = False

        self.map = MapLayer(lat = 47.201738, lon = 38.934003, zoom = 18, double_tap_zoom = False) #MapView(lat = 47.201738, lon = 38.934003, zoom = 18, size_hint = (0.8, 1))
        
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