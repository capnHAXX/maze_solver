from window import Window
from cell import Cell

win = Window(800, 600)
c1 = Cell(win)
c1.draw(50, 50, 100, 100)

c2 = Cell(win)
c2.draw(125, 125, 200, 200)

c1.draw_move(c2)


win.wait_for_close()