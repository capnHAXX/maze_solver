from window import Window
from maze import Maze

win = Window(800, 600)
x1 = 150
y1 = 50
num_rows = 10
num_columns = 15
cell_size_x = 50
cell_size_y = 50
maze = Maze(x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win)
maze._create_cells()
for row in maze._cells:
    print(row)

win.wait_for_close()