from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Controller(FloatLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    """
    pass


class Chronology(Widget):
    def __init__(self, **kwargs):
        super(Chronology, self).__init__(**kwargs)
        self.color = None
        self.left_line = None
        self.right_line = None
        self.draw()

    def draw(self):
        with self.canvas:
            line_kwargs = {
                'points': [],
                'width': 1,
            }
            self.color = Color(rgba=(1, 0, 0, 1.))

            self.left_line = Line(**line_kwargs)
            self.right_line = Line(**line_kwargs)

    def update_lines(self):
        self.left_line.points = [
            self.x, self.y,
            self.x, self.y + self.height,
        ]

        self.right_line.points = [
            self.x + self.width, self.y,
            self.x + self.width, self.y + self.height,
        ]

    def on_pos(self, instance, value):
        self.update_lines()

    def on_size(self, instance, value):
        self.update_lines()


class DaySeparator(Widget):
    def __init__(self, **kwargs):
        super(DaySeparator, self).__init__(**kwargs)
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
