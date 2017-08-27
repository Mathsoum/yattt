from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Controller(FloatLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    """
    pass


class Chronology(Widget):
    TIME_INTERVAL_COUNT = 24 * 2

    def __init__(self, **kwargs):
        super(Chronology, self).__init__(**kwargs)
        self.color = None
        self.time_lines = []
        self.draw()

    def draw(self):
        with self.canvas:
            line_kwargs = {
                'points': [],
                'width': 1,
            }
            self.color = Color(rgba=(1, 0, 0, 1.))

            self.time_lines = [Line(**line_kwargs) for i in range(self.TIME_INTERVAL_COUNT + 1)]

    def update_lines(self):
        margin_hours_height = self.height * 0.1
        margin_halves_height = self.height * 0.4
        for i in range(self.TIME_INTERVAL_COUNT + 1):
            if (i % 2) == 0:
                self.time_lines[i].points = [
                    self.x + (((self.width * 0.05) / 2) + (self.width * 0.95 * i) / self.TIME_INTERVAL_COUNT), self.y + margin_hours_height,
                    self.x + (((self.width * 0.05) / 2) + (self.width * 0.95 * i) / self.TIME_INTERVAL_COUNT), self.y + self.height - margin_hours_height,
                ]
            else:
                self.time_lines[i].points = [
                    self.x + (((self.width * 0.05) / 2) + (self.width * 0.95 * i) / self.TIME_INTERVAL_COUNT), self.y + margin_halves_height,
                    self.x + (((self.width * 0.05) / 2) + (self.width * 0.95 * i) / self.TIME_INTERVAL_COUNT), self.y + self.height - margin_halves_height,
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
