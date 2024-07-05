from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window
kv = """
FloatLayout:
    orientation: 'vertical'
    Camera:
        id: camera
        pos_hint: {'center_x': 0.5}
        resolution: (1600, 1200)
        play: True

    MDFloatingActionButton:
        icon: "camera"
        style: "large"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: app.capture()
"""

class CamApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def on_start(self):
        self.camera = self.root.ids.camera
        Window.bind(on_resize=self.on_window_resize)

    def on_window_resize(self, window, width, height):
        self.camera.resolution = (width, height)

    def capture(self):
        Window.bind(on_resize=self.on_window_resize)
        filename = 'capture.jpg'
        self.camera.export_to_png(filename)

if __name__ == "__main__":
    CamApp().run()
