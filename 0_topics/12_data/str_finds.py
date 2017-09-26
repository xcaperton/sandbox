
import csv
import re


class CodeBlock():
    """Read text file and find specific cell breaks"""

    def __init__(self, file_str='', t_file=''):
        self.t_file = t_file
        self.file_str = file_str
        self.cell_break_str = "#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        self.cell_break_len = len(self.cell_break_str)
        self.cursor_position = 0
        if not file_str:
            with open(t_file, 'r') as file_object:
                self.file_str = file_object.read()

    def __repr__(self):
        return "Cell breaks: {}".format(str(self.cell_breaks()))

    def cell_breaks(self):
        """Return list of starting position of all cell breaks"""
        return [m.start() for m in re.finditer(self.cell_break_str, self.file_str)]

    def previous_cell_break(self):
        """Return start of previous cell break"""
        start = 0
        if self.cell_breaks():
            try:
                start = [x for x in self.cell_breaks() if x < self.cursor_position][-1]
            except IndexError:
                pass  # Cursor before first cell_break so return 0

        return start

    def next_cell_break(self):
        """Return start of next cell break"""
        end = 0
        if self.cell_breaks():
            try:
                end = [x for x in self.cell_breaks() if x > self.cursor_position][0]
            except IndexError:
                end = len(self.file_str)

        return end
