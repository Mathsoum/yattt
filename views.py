from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Controller(FloatLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    """
    pass


class Separator(Widget):
    def __init__(self, **kwargs):
        super(Separator, self).__init__(**kwargs)
        self.color = None
        self.line = None
        self.draw_line()

    def draw_line(self):
        line_kwargs = {
            'points': [],
            'width': 1,
        }

        with self.canvas:
            # Add a red color
            self.color = Color(rgba=(1, 1, 1, 1.))

            # Add a rectangle
            self.line = Line(**line_kwargs)

    def update_line(self):
        self.line.points = [
            self.x, self.y, self.x + self.width, self.y
        ]

    def on_pos(self, instance, value):
        self.update_line()

    def on_size(self, instance, value):
        self.update_line()

