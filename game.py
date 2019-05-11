from gameplay import GamePlay
from board import Board
from cube import Cube
import random
import time
import datetime
from copy import deepcopy

# Very Easy | Sanity check
sudoku1 = [Cube(0,0,6), Cube(1,0,7), Cube(2,0,9), Cube(3,0,4), Cube(4,0,3), Cube(5,0,1), Cube(6,0,5), Cube(7,0,8), Cube(8,0,2),
    Cube(0,1,2), Cube(1,1,3), Cube(2,1,4), Cube(3,1,8), Cube(4,1,7), Cube(5,1,5), Cube(6,1,1), Cube(7,1,9), Cube(8,1,6),
    Cube(0,2,1), Cube(1,2,8), Cube(2,2,5), Cube(3,2,2), Cube(4,2,6), Cube(5,2,9), Cube(6,2,7), Cube(7,2,4), Cube(8,2,3),
    Cube(0,3,4), Cube(1,3,2), Cube(2,3,6), Cube(3,3,3), Cube(4,3,1), Cube(5,3,7), Cube(6,3,8), Cube(7,3,5), Cube(8,3,9),
    Cube(0,4,8), Cube(1,4,5), Cube(2,4,7), Cube(3,4,9), Cube(4,4,2), Cube(5,4,4), Cube(6,4,3), Cube(7,4,6), Cube(8,4,1),
    Cube(0,5,3), Cube(1,5,9), Cube(2,5,1), Cube(3,5,5), Cube(4,5,8), Cube(5,5,6), Cube(6,5,2), Cube(7,5,7), Cube(8,5,4),
    Cube(0,6,9), Cube(1,6,4), Cube(2,6,8), Cube(3,6,1), Cube(4,6,5), Cube(5,6,3), Cube(6,6,6), Cube(7,6,2), Cube(8,6,7),
    Cube(0,7,7), Cube(1,7,1), Cube(2,7,2), Cube(3,7,6), Cube(4,7,4), Cube(5,7,8),
    Cube(0,8,5), Cube(1,8,6), Cube(2,8,3), Cube(3,8,7), Cube(4,8,9), Cube(5,8,2)]
# Easy
sudoku2 = [Cube(0,0,6), Cube(1,0,7), Cube(2,0,9), Cube(3,0,4), Cube(4,0,3), Cube(5,0,1), Cube(6,0,5), Cube(7,0,8), Cube(8,0,2),
    Cube(0,1,2), Cube(1,1,3), Cube(3,1,8), Cube(4,1,7), Cube(5,1,5), Cube(6,1,1), Cube(7,1,9), Cube(8,1,6),
    Cube(0,2,1), Cube(1,2,8), Cube(2,2,5), Cube(3,2,2), Cube(4,2,6), Cube(8,2,3),
    Cube(0,3,4), Cube(1,3,2), Cube(2,3,6), Cube(3,3,3), Cube(4,3,1), Cube(5,3,7), Cube(6,3,8), Cube(7,3,5), Cube(8,3,9),
    Cube(0,4,8), Cube(1,4,5), Cube(3,4,9), Cube(4,4,2), Cube(5,4,4), Cube(6,4,3), Cube(7,4,6), Cube(8,4,1),
    Cube(0,5,3), Cube(1,5,9), Cube(5,5,6), Cube(6,5,2), Cube(7,5,7), Cube(8,5,4),
    Cube(0,6,9), Cube(1,6,4), Cube(3,6,1), Cube(5,6,3), Cube(8,6,7),
    Cube(0,7,7), Cube(1,7,1), Cube(2,7,2), Cube(3,7,6), Cube(4,7,4), Cube(5,7,8),
    Cube(0,8,5)]
# Medium
sudoku3 = [Cube(0,0,6), Cube(7,0,8), Cube(8,0,2),
    Cube(0,1,2), Cube(1,1,3), Cube(3,1,8), Cube(4,1,7), Cube(5,1,5), Cube(6,1,1), Cube(7,1,9), Cube(8,1,6),
    Cube(4,2,6), Cube(8,2,3),
    Cube(1,3,2), Cube(2,3,6), Cube(7,3,5), Cube(8,3,9),
    Cube(1,4,5), Cube(3,4,9), Cube(5,4,4), Cube(6,4,3), Cube(7,4,6), Cube(8,4,1),
    Cube(0,6,9), Cube(1,6,4), Cube(5,6,3), Cube(8,6,7),
    Cube(1,7,1), Cube(4,7,4), Cube(5,7,8),
    Cube(0,8,5)]
# Expert
sudoku4expert = [Cube(4,0,1), Cube(5,0,9), Cube(7,0,8),
Cube(0,1,9), Cube(2,1,5),
Cube(3,2,4), Cube(6,2,9), Cube(8,2,1),
Cube(1,3,3), Cube(7,3,5), Cube(8,3,6),
Cube(6,4,3), Cube(7,4,4),
Cube(0,5,7), Cube(1,5,6), Cube(3,5,8),
Cube(0,6,8), Cube(2,6,1),
Cube(0,7,2), Cube(8,7,4),
Cube(1,8,4), Cube(3,8,6), Cube(5,8,7)]

def write_to_file(text_list):
    with open(f"game_{tm}.log", "a+") as f:
        for tex in text_list:
            f.write(tex)

def get_time_stamp():
    t = time.time()
    return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

def set_easy_board(game):
    lst = []
    for i in range(0,9):
        for j in range(0,9):
            if i == 0 or j == 0:
                cube = Cube(i,j)
                cube.number = random.randint(1,9)
                if game.is_valid(cube):
                    lst.append(cube)
            if i == 6 and j == 6:
                break

    return lst

def _create_dummy_game():
    cube_list = {}
    cube_unique_list = []
    last_cube = None
    for i in range(0,10):
        cube = Cube(random.randint(0,8),random.randint(0,8))
        if last_cube == cube:
            pass
        else:
            cube.number = random.randint(1,9)
            if not cube.number in cube_list:
                cube_unique_list.append(cube)
                cube_list[str(cube.number)] = cube
        last_cube = cube.number

    return cube_unique_list

tm = get_time_stamp()
def play(game):
    cube = game.board.find_next_empty_cube()
    if cube:
        game.board.update_cube_numbers(cube)
        write_to_file([f"\tempty cube found: {str(cube)}\n",f"\toptional numbers: {cube.optional_nums}\n",f"\tnot optional numbers: {cube.not_optional_nums}\n","\t==========================================\n",game.board.draw_board()])
        
        if len(cube.optional_nums) == 0: # no more optional but in a bad way...loop back to safe shore
            write_to_file([f"\tEmpty optional numbers for cube: {str(cube)}\n",f"\tOptional numbers: {cube.optional_nums}"])
            # if we won :)
            if game.check_if_game_is_over():
                return True
            else: # we lost :(
                write_to_file(["We lost this iteration, going over another :(\n"])
                return False

        else: 
            if len(cube.optional_nums) == 0:
                return True
            tmp_board = deepcopy(game.board)
            for inum in iter(cube.optional_nums):
                cube.number = inum
                if not game.board.set_cube_in_board(cube):
                    continue
                # game.board.grid[cube.col][cube.row] = cube
                print(game.board.draw_board())
                if play(game):
                    return True
                else:
                    cube.number = None
                    game.board = tmp_board
                    # cube.move_to_no()
            return False
                    
    else: # ==> no empty cube was found in grid
        return game.check_if_game_is_over()


def main():
    # Board and game creation
    b = Board(9)
    g = GamePlay(b)
    # set game values
    # b.set_numbers_in_cubes(sudoku1)
    # b.set_numbers_in_cubes(sudoku2)
    b.set_numbers_in_cubes(sudoku3) # V
    # b.set_numbers_in_cubes(sudoku4expert) #V

    write_to_file(["Game starts!\n",b.draw_board()])
    print("Game starts!\n")
    print(b.draw_board())

    if play(g):
        print("Game Over!!!, we won!")
        print(b.draw_board())
    else: 
        print("we lost...")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)