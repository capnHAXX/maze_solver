from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        self._cells = []
        for n in range(self._num_rows):
            row = []
            for m in range(self._num_columns):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)

        for row in range(self._num_rows):
            for col in range(self._num_columns):
                self._draw_cell(row, col)

    
    def _draw_cell(self, row, col):
        if self._win is None:
            return
        x1_pos = self._x1 + col * self._cell_size_x
        x2_pos = x1_pos + self._cell_size_x
        y1_pos = self._y1 + row * self._cell_size_y
        y2_pos = y1_pos + self._cell_size_y
        self._cells[row][col].draw(x1_pos, y1_pos, x2_pos, y2_pos)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_columns - 1].right_wall = False
        self._draw_cell(self._num_rows - 1, self._num_columns - 1)
    
    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        while True:
            to_visit = []
            if row - 1 >= 0 and self._cells[row - 1][col].visited is False:
                to_visit.append("Up")
            if row + 1 < self._num_rows and self._cells[row + 1][col].visited is False:
                to_visit.append("Down")
            if col - 1 >= 0 and self._cells[row][col - 1].visited is False:
                to_visit.append("Left")
            if col + 1 <self._num_columns and self._cells[row][col + 1].visited is False:
                to_visit.append("Right")
            if len(to_visit) == 0:
                self._draw_cell(row, col)
                return
            direction = random.choice(to_visit)
            if direction == "Up":
                self._cells[row][col].top_wall = False
                self._cells[row - 1][col].bottom_wall = False
                self._draw_cell(row, col)
                self._break_walls_r(row - 1, col)
            elif direction == "Down":
                self._cells[row][col].bottom_wall = False
                self._cells[row + 1][col].top_wall = False
                self._draw_cell(row, col)
                self._break_walls_r(row + 1, col)
            elif direction == "Left":
                self._cells[row][col].left_wall = False
                self._cells[row][col - 1].right_wall = False
                self._draw_cell(row, col)
                self._break_walls_r(row, col - 1)
            elif direction == "Right":
                self._cells[row][col].right_wall = False
                self._cells[row][col + 1].left_wall = False
                self._draw_cell(row, col)
                self._break_walls_r(row, col + 1)
    
    def _reset_cells_visited(self):
        for row in range(self._num_rows):
            for col in range(self._num_columns):
                self._cells[row][col].visited = False