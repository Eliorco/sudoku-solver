from typing import NamedTuple

class Cell(NamedTuple):
    row: int
    col: int


class Cube:
    cubic_cat = {
        1: { Cell(1,1), Cell(1,2), Cell(1,3), Cell(2,1), Cell(2,2), Cell(2,3), Cell(3,1), Cell(3,2), Cell(3,3) },
        2: { Cell(1,4), Cell(1,5), Cell(1,6), Cell(2,4), Cell(2,5), Cell(2,6), Cell(3,4), Cell(3,5), Cell(3,6) },
        3: { Cell(1,7), Cell(1,8), Cell(1,9), Cell(2,7), Cell(2,8), Cell(2,9), Cell(3,7), Cell(3,8), Cell(3,9) },
        4: { Cell(4,1), Cell(4,2), Cell(4,3), Cell(5,1), Cell(5,2), Cell(5,3), Cell(6,1), Cell(6,2), Cell(6,3) },
        5: { Cell(4,4), Cell(4,5), Cell(4,6), Cell(5,4), Cell(5,5), Cell(5,6), Cell(6,4), Cell(6,5), Cell(6,6) },
        6: { Cell(4,7), Cell(4,8), Cell(4,9), Cell(5,7), Cell(5,8), Cell(5,9), Cell(6,7), Cell(6,8), Cell(6,9) },
        7: { Cell(7,1), Cell(7,2), Cell(7,3), Cell(8,1), Cell(8,2), Cell(8,3), Cell(9,1), Cell(9,2), Cell(9,3) },
        8: { Cell(7,4), Cell(7,5), Cell(7,6), Cell(8,4), Cell(8,5), Cell(8,6), Cell(9,4), Cell(9,5), Cell(9,6) },
        9: { Cell(7,7), Cell(7,8), Cell(7,9), Cell(8,7), Cell(8,8), Cell(8,9), Cell(9,7), Cell(9,8), Cell(9,9) }
}
    num_list = {num for num in range(1,10)}

    def __init__(self, row, col, number=None):
        self.number = number
        self.row = row
        self.col = col
        self.cubic = self._set_cubic()
        self.optional_nums = self._set_optional_init()
        self.not_optional_nums = {self.number} if number else {}

    def __str__(self):
        return f"({self.row},{self.col}) |={self.number}| {self.cubic} | op: {self.optional_nums}| op_len: {len(self.optional_nums)}"

    def __eq__(self, other):
        return (self.col, self.row) == (other.col, other.row) and self.number == other.number

    def __ne__(self, other):
        return (self.col, self.row) != (other.col, other.row) or self.number != other.number

    def _set_optional_init(self):
        nums = set(self.num_list)
        if self.number in nums:
            nums.discard(self.number)
        return nums

    def _set_cubic(self):
        for key in self.cubic_cat:
            if (self.row, self.col) in self.cubic_cat[key]:
                return key
