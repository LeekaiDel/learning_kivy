from turtle import pos
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource, MapMarkerPopup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Line)
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout


class MapLayer(MapView):
    def __init__(self, **kwargs):
        self.set_point = False
        super(MapLayer, self).__init__(**kwargs)

    def on_touch_up(self, touch):
        print(touch) 

        # if(self.set_point) and touch.button == 'left':
        #     self.add_marker(marker = MapMarkerPopup(source = 'waypoint_10x10.png', lon = self.get_latlon_at(touch.x, touch.y)[1], lat = self.get_latlon_at(touch.x, touch.y)[0]))
        # if(touch.button == 'scrolldown'):
        #     if(self.zoom < self.map_source.get_max_zoom()):
        #         self.zoom += 1
        # elif(touch.button == 'scrollup'):
        #     if(self.zoom > self.map_source.get_min_zoom()):
        #         self.zoom -= 1

    def on_touch_move(self, touch):    
        # if(touch.button == 'left'):
        #     self.center_on(self.get_latlon_at(float(self.center_x) + float(touch.dx), float(self.center_y) + float(touch.dy)))
        pass

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
        box_layout = BoxLayout()
        layout_butts = BoxLayout(orientation = 'vertical', size_hint = (0.1, 1), spacing = (3))
        # self.size_butt_bar = butt_layout.size 
        # self.map = MapLayer(lat = 47.201738, lon = 38.934003, zoom = 18) #MapView(lat = 47.201738, lon = 38.934003, zoom = 18, size_hint = (0.8, 1))
        # self.map.pos
        # bl_buttons = BoxLayout(orientation = 'horizontal', spacing = 3)
        # self.map.add_widget(Label(text = 'lat:\nlon:\n'))
        layout_butts.add_widget(Button(text = 'Point', on_press = self.point_butt, size = (100, 50)))
        layout_butts.add_widget(Button(text = 'Home', on_press = self.home_butt, size = (100, 50)))
        layout_butts.add_widget(Button(text = 'Send', on_press = self.send_butt, size = (100, 50)))
        layout_butts.add_widget(Button(text = 'Clear points', on_press = self.clear_points_butt, size = (100, 50)))
        box_layout.add_widget(layout_butts)

        self.map = MapLayer()
        box_layout.add_widget(self.map)

        return box_layout

if __name__ == "__main__":
    MapApp().run()