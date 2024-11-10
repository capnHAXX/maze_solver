from window import Window
from point import Point
from line import Line

win = Window(800, 600)
point_1 = Point(10, 100)
point_2 = Point(400, 400)
point_3 = Point(720, 50)
line1 = Line(point_1, point_2)
line2 = Line(point_2, point_3)
line3 = Line(point_3, point_1)
win.draw_line(line1,"red")
win.draw_line(line2,"green")
win.draw_line(line3,"blue")
win.wait_for_close()