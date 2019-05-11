
class GamePlay:
    def __init__(self, board):
        self.board = board
    
    # TODO: TBD | part of other solution 
    def _is_in_row_or_col(self, cube):
        # check column
        for i in range(self.board.size):
            if self.board.grid[cube.col][i].number != None and self.board.grid[cube.col][i].number == cube.number:
                return False
        # check row
            elif self.board.grid[i][cube.row].number != None and self.board.grid[i][cube.row].number == cube.number:
                return False
    # TODO: TBD
    def _is_in_cubic(self, cube):
        # check cubic
        cubic = self.board.get_all_cubic(cube.cubic).remove(cube)
        for item in range(len(cubic)):
            if item.number != None and cube != item:
                return False
        return True

    # TODO: TBD
    def is_valid(self, cube):
        not_opt_lst = self.get_all_not_optional_numbers(cube)
        if not_opt_lst !=[]:
            if cube.number in not_opt_lst :
                return False
        
        return True 

    # TODO: TBD
    def fix_duplictes(self, a):
        return list(dict.fromkeys(a))
        



    # TODO: TBD
    def _get_col_numbers(self, cube):
        not_optional = []
        for i in range(self.board.size):
            cur_cube = self.board.grid[cube.col][i]
            if cur_cube.number != None and cur_cube != cube:
                not_optional.append(cur_cube.number)
        return not_optional

    # TODO: TBD
    def _get_row_numbers(self, cube):
        not_optional = []
        for i in range(self.board.size):
            cur_cube = self.board.grid[i][cube.row]
            if cur_cube.number != None and cur_cube != cube:
                not_optional.append(cur_cube.number)
        return not_optional

    # TODO: TBD
    def _get_cubic_numbers(self, cube):
        cubic_not_optional = []
        cubic = self.board.get_all_cubic(cube.cubic)

        for item in cubic:
            if item.number != None and item != cube:
                cubic_not_optional.append(item.number)
        return cubic_not_optional
        
    def check_if_game_is_over(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                cube1 = self.board.grid[i][j]
                if i == 0 and j == 0:
                    if not cube1.number in self.get_all_not_optional_numbers(cube1):
                        pass
                    else:
                        False

                cube2 = self.board.grid[j][i]
                if cube1.number == None or cube2.number == None:
                    return False
                else:
                    if not cube1.number in self.get_all_not_optional_numbers(cube1) and not cube2.number in self.get_all_not_optional_numbers(cube2):
                        pass
                    else:
                        return False

        return True

    def get_all_not_optional_numbers(self, cube):
        row_numbers = self.board.t__get_row_numbers(cube)
        col_numbers = self.board.t__get_col_numbers(cube)
        cubic_numbers = self.board.t__get_cubic_numbers(cube)
        return list(set(list(row_numbers + col_numbers + cubic_numbers)))

