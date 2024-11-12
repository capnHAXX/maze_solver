from point import Point
from line import Line

class Cell:
    def __init__(self, win = None, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True):
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.left_wall:    
            self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x1, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x1, self._y2)), "white")
        if self.right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1),Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1),Point(self._x2, self._y2)), "white")
        if self.top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x2, self._y1)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x2, self._y1)), "white")
        if self.bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2),Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2),Point(self._x2, self._y2)), "white")
    
    def draw_move(self, to_cell, undo = False):
        if not undo:
            fill_colour = "red"
        else:
            fill_colour = "gray"
        
        x_a = (self._x1 + self._x2)//2
        y_a = (self._y1 + self._y2)//2
        x_b = (to_cell._x1 + to_cell._x2)//2
        y_b = (to_cell._y1 + to_cell._y2)//2
        self._win.draw_line(Line(Point(x_a, y_a),Point(x_b, y_b)), fill_colour)