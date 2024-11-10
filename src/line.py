
class Line:
    def __init__(self, point_1, point_2):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = fill_colour, width=2)
