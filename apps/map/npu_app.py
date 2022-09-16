from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Line)
from kivy.core.window import Window
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    butt_set_waypoint = ObjectProperty()
    butt_set_home = ObjectProperty()
    butt_clear = ObjectProperty()
    map_layer = ObjectProperty()    
    butt_bar = ObjectProperty()
    set_waypoint = False
    waypoint_array = list()

    def on_touch_up(self, touch):
        if(self.set_waypoint):
            if(touch.y > self.butt_bar.size[1]):
                map_marker = MapMarkerPopup(
                    source = 'waypoint_10x10.png',
                    lon = self.map_layer.get_latlon_at(touch.x, touch.y - self.butt_bar.size[1])[1], 
                    lat = self.map_layer.get_latlon_at(touch.x, touch.y - self.butt_bar.size[1])[0])
    
                self.map_layer.add_marker(map_marker)
                self.waypoint_array.append(map_marker)

    def on_touch_move(self, touch):
        print("Move")

    def set_waypoint_cb(self):
        self.set_waypoint = not self.set_waypoint
        print("Press Set_WayPoint")
    
    def set_home_cb(self):
        print("Press Set_Home")

    def clear_cb(self):
        for marker in self.waypoint_array:
            self.map_layer.remove_marker(marker)
        print("Press Set_Clear")
        

class NpuApp(App):
    def build(self): 
        return Container()

    
if __name__ == "__main__":
    NpuApp().run()