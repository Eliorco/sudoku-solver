from cube import Cube

class Board:
    def __init__(self, size):
        self.size = size
        # initialize first
        self.grid = [[Cube(y,x) for x in range(size)] for y in range(size)]

    def get_row(self, row_num):
        row = []
        for i in range(self.size):
            row.append(self.grid[i][row_num])
        return row

    def get_col(self, col_num):
        col = []
        for i in range(self.size):
            col.append(self.grid[col_num][i])
        return col
    
    def get_all_cubic(self, cubic_cat):
        cubic = []
        for i in range(self.size):
            for j in range(self.size):
                cube = self.grid[i][j]
                if cubic_cat == cube.cubic:
                    cubic.append(cube)
        return cubic

    def to_board_val(self, row):
        # TODO: This represanttion is for debug mode only
        # Change it later to complay with real sudoku board
        temp_list = []
        for item in row:
            temp_list.append(str(item))
        return temp_list

    def find_next_empty_cube(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[j][i].number == None:
                    return self.grid[j][i]
        print("No empty cubes") # TODO: delete it after testing
        return False

    def set_numbers_in_cubes(self, list_of_cubes):
        for cube in list_of_cubes:
            if not self.set_cube_in_board(cube):
                print(f"cube has not been set because of duplicate number: {cube.number}, at: ({cube.col},{cube.row})")
        return True

    def set_cube_in_board(self, cube):
        row = self.t__get_row_numbers(cube)
        col = self.t__get_col_numbers(cube)
        cubic = self.t__get_cubic_numbers(cube)
        big_list = list(set(list(row + col + cubic)))
        if not cube.number in big_list:
            self.grid[cube.col][cube.row] = cube
            return True
        return False

    def update_cube_numbers(self, cube):
        row_numbers = [row_n.number for row_n in self.get_row(cube.row) if row_n.number != None]
        col_numbers = [col_n.number for col_n in self.get_col(cube.col) if col_n.number != None]
        cubic_numbers = [cubic_n.number for cubic_n in self.get_all_cubic(cube.cubic) if cubic_n.number != None]
        cube.not_optional_nums = list(set(list(row_numbers + col_numbers + cubic_numbers)))
        cube.optional_nums = list(set(cube.num_list) - set(cube.not_optional_nums))
        
    def draw_board(self):
        first_line = """      0  |  1  |  2  ||  3  |  4  |  5  ||  6  |  7  |  8  |\n   |-------------------------------------------------------|\n"""
        some_dict = {}
        template = ''
        for i in range(self.size):
            for item in self.get_row(i):
                num = item.number if item.number != None else " "
                some_dict[str(item.col)] = num

            kiko_str = f"""{i}  |  {some_dict["0"]}  |  {some_dict["1"]}  |  {some_dict["2"]}  ||  {some_dict["3"]}  |  {some_dict["4"]}  |  {some_dict["5"]}  ||  {some_dict["6"]}  |  {some_dict["7"]}  |  {some_dict["8"]}  |\n"""
            line_sep = "   |-----------------||-----------------||-----------------|\n" if (i+1) % 3 != 0 else "   |=================||=================||=================|\n"    
            template = template + kiko_str + line_sep
        return first_line + template
     
    def t__get_col_numbers(self, cube):
        not_optional = []
        for i in range(self.size):
            if i == cube.row:
                continue
            cur_cube = self.grid[cube.col][i]
            if cur_cube.number != None and cur_cube != cube:
                not_optional.append(cur_cube.number)
        return not_optional

    def t__get_row_numbers(self, cube):
        not_optional = []
        for i in range(self.size):
            if i == cube.col:
                continue
            cur_cube = self.grid[i][cube.row]
            if cur_cube.number != None and cur_cube != cube:
                not_optional.append(cur_cube.number)
        return not_optional

    def t__get_cubic_numbers(self, cube):
        cubic_not_optional = []
        cubic = self.get_all_cubic(cube.cubic)

        for item in cubic:
            if item.col == cube.col and item.row == cube.row:
                continue
            if item.number != None and item != cube:
                cubic_not_optional.append(item.number)
        return cubic_not_optional

