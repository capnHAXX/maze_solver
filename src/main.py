from window import Window
from maze import Maze

win = Window(1000, 1000)
x1 = 25
y1 = 50
num_rows = 20
num_columns = 20
cell_size_x = 20
cell_size_y = 20
maze = Maze(x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win)
maze.solve()

win.wait_for_close()