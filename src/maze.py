from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
    
    def _create_cells(self):
        self._cells = []
        for n in range(self._num_rows):
            row = []
            for m in range(self._num_columns):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)
        self._draw_cell()

    
    def _draw_cell(self):
        for n in range(self._num_rows):
            x1_pos = self._x1 + n * self._cell_size_x
            x2_pos = self._x1 + n * self._cell_size_x + self._cell_size_x
            for m in range(self._num_columns):
                x1_pos = self._x1 + m * self._cell_size_x
                x2_pos = self._x1 + m * self._cell_size_x + self._cell_size_x
                y1_pos = self._y1 + n * self._cell_size_y
                y2_pos = self._y1 + n * self._cell_size_y + self._cell_size_y
                self._cells[n][m].draw(x1_pos, y1_pos, x2_pos, y2_pos)
                self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)