import random

class Cube:
    cubic_cat = {
        "1": [ (1,1) ,  (2,1) ,  (3,1) ,  (1,2) ,  (2,2) ,  (3,2),   (1,3) ,  (2,3) ,  (3,3) ],
        "2": [ (4,1) ,  (5,1) ,  (6,1) ,  (4,2) ,  (5,2) ,  (6,2) ,  (4,3) ,  (5,3) ,  (6,3) ],
        "3": [ (7,1) ,  (8,1) ,  (9,1) ,  (7,2) ,  (8,2) ,  (9,2) ,  (7,3) ,  (8,3) ,  (9,3) ],
        "4": [ (1,4) ,  (2,4) ,  (3,4) ,  (1,5) ,  (2,5) ,  (3,5) ,  (1,6) ,  (2,6) ,  (3,6) ],
        "5": [ (4,4) ,  (5,4) ,  (6,4) ,  (4,5) ,  (5,5) ,  (6,5) ,  (4,6) ,  (5,6) ,  (6,6) ],
        "6": [ (7,4) ,  (8,4) ,  (9,4) ,  (7,5) ,  (8,5) ,  (9,5) ,  (7,6) ,  (8,6) ,  (9,6) ],
        "7": [ (1,7) ,  (2,7) ,  (3,7) ,  (1,8) ,  (2,8) ,  (3,8) ,  (1,9) ,  (2,9) ,  (3,9) ],
        "8": [ (4,7) ,  (5,7) ,  (6,7) ,  (4,8) ,  (5,8) ,  (6,8) ,  (4,9) ,  (5,9) ,  (6,9) ],
        "9": [ (7,7) ,  (8,7) ,  (9,7) ,  (7,8) ,  (8,8) ,  (9,8) ,  (7,9) ,  (8,9) ,  (9,9) ]
}
    num_list = [num for num in range(1,10)]

    def __init__(self,col ,row, number=None):
        self.number = number
        self.row = row
        self.col = col
        self.cubic = self._set_cubic()
        self.optional_nums = self._set_optional_init()
        self.not_optional_nums = []

    def __str__(self):
        return f"({self.col},{self.row}) |{self.number}| {self.cubic}"

    def __eq__(self, other):
        return (self.col,self.row) == (other.col,other.row) and self.number == other.number

    def __ne__(self, other):
        return (self.col,self.row) != (other.col,other.row) or self.number != other.number

    def _set_optional_init(self):
        nums = self.num_list[:]
        return nums

    def _set_cubic(self):
        for key in self.cubic_cat:
            if (self.col+1,self.row+1) in self.cubic_cat[key]:
                return int(key)
    # TODO: TBD
    def move_to_no(self):
        self.not_optional_nums.append(self.number)
        self.optional_nums.remove(self.number)
