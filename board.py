from cube import Cube

RED_TEXT = "\033[2;30;41m"
BLACK_TEXT = "\033[0;30;48m"

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[Cube(y, x) for x in range(size)] for y in range(size)]

    def get_row(self, row_num):
        row = []
        for i in range(self.size):
            row.append(self.grid[i][row_num])
        return row

    def find_next_empty_cube(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[j][i].number is None:
                    return self.grid[j][i]
        return False

    def set_numbers_in_cubes(self, list_of_cubes):
        for cube in list_of_cubes:
            big_list = self.get_all_not_opt_numbers_for_cube(cube)
            if cube.number not in big_list:
                self.grid[cube.col][cube.row] = cube
        return True

    def set_cube_in_board(self, cube):
        if cube.number not in cube.not_optional_nums:
            self.grid[cube.col][cube.row] = cube
            return True
        return False

    def update_cube_numbers(self, cube):
        cube.not_optional_nums = self.get_all_not_opt_numbers_for_cube(cube)
        cube.optional_nums = list(set(cube.num_list) - set(cube.not_optional_nums))

    def get_all_not_opt_numbers_for_cube(self, cube):
        row_numbers = self.t__get_row_numbers(cube)
        col_numbers = self.t__get_col_numbers(cube)
        cubic_numbers = self.t__get_cubic_numbers(cube)
        return list(set(list(row_numbers + col_numbers + cubic_numbers)))

    def draw_board(self):
        first_line = """      0  |  1  |  2  ||  3  |  4  |  5  ||  6  |  7  |  8  |\n   |-------------------------------------------------------|\n"""
        some_dict = {}
        template = ''
        for i in range(self.size):
            for item in self.get_row(i):
                num = item.number if item.number is not None else " "
                some_dict[str(item.col)] = num

            kiko_str = f"""{i}  |  {some_dict["0"]}  |  {some_dict["1"]}  |  {some_dict["2"]}  ||  {some_dict[
                "3"]}  |  {some_dict["4"]}  |  {some_dict["5"]}  ||  {some_dict["6"]}  |  {some_dict["7"]}  |  {
            some_dict["8"]}  |\n"""
            line_sep = "   |-----------------||-----------------||-----------------|\n" if (i + 1) % 3 != 0 else\
                "   |=================||=================||=================|\n"
            template = template + kiko_str + line_sep
        return first_line + template

    def t__get_col_numbers(self, cube):
        return [self.grid[cube.col][j].number for j in range(self.size) if self.grid[cube.col][j].number is not None]

    def t__get_row_numbers(self, cube):
        return [self.grid[i][cube.row].number for i in range(self.size) if self.grid[i][cube.row].number is not None]

    def t__get_cubic_numbers(self, cube):
        return [self.grid[x - 1][y - 1].number for x, y in iter(cube.cubic_cat[str(cube.cubic)]) if
                self.grid[x - 1][y - 1].number is not None]
