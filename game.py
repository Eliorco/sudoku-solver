from board import Board
from cube import Cube
import logging
import os
import time
import argparse
# from frontend_input import WebUiInput

class Game:
    #default levels
    # Very Easy | Sanity check
    sudoku1 = [Cube(0, 0, 6), Cube(1, 0, 7), Cube(2, 0, 9), Cube(3, 0, 4), Cube(4, 0, 3), Cube(5, 0, 1), Cube(6, 0, 5),
               Cube(7, 0, 8), Cube(8, 0, 2),
               Cube(0, 1, 2), Cube(1, 1, 3), Cube(2, 1, 4), Cube(3, 1, 8), Cube(4, 1, 7), Cube(5, 1, 5), Cube(6, 1, 1),
               Cube(7, 1, 9), Cube(8, 1, 6),
               Cube(0, 2, 1), Cube(1, 2, 8), Cube(2, 2, 5), Cube(3, 2, 2), Cube(4, 2, 6), Cube(5, 2, 9), Cube(6, 2, 7),
               Cube(7, 2, 4), Cube(8, 2, 3),
               Cube(0, 3, 4), Cube(1, 3, 2), Cube(2, 3, 6), Cube(3, 3, 3), Cube(4, 3, 1), Cube(5, 3, 7), Cube(6, 3, 8),
               Cube(7, 3, 5), Cube(8, 3, 9),
               Cube(0, 4, 8), Cube(1, 4, 5), Cube(2, 4, 7), Cube(3, 4, 9), Cube(4, 4, 2), Cube(5, 4, 4), Cube(6, 4, 3),
               Cube(7, 4, 6), Cube(8, 4, 1),
               Cube(0, 5, 3), Cube(1, 5, 9), Cube(2, 5, 1), Cube(3, 5, 5), Cube(4, 5, 8), Cube(5, 5, 6), Cube(6, 5, 2),
               Cube(7, 5, 7), Cube(8, 5, 4),
               Cube(0, 6, 9), Cube(1, 6, 4), Cube(2, 6, 8), Cube(3, 6, 1), Cube(4, 6, 5), Cube(5, 6, 3), Cube(6, 6, 6),
               Cube(7, 6, 2), Cube(8, 6, 7),
               Cube(0, 7, 7), Cube(1, 7, 1), Cube(2, 7, 2), Cube(3, 7, 6), Cube(4, 7, 4), Cube(5, 7, 8),
               Cube(0, 8, 5), Cube(1, 8, 6), Cube(2, 8, 3), Cube(3, 8, 7), Cube(4, 8, 9), Cube(5, 8, 2)]
    # Easy
    sudoku2 = [Cube(0, 0, 6), Cube(1, 0, 7), Cube(2, 0, 9), Cube(3, 0, 4), Cube(4, 0, 3), Cube(5, 0, 1), Cube(6, 0, 5),
               Cube(7, 0, 8), Cube(8, 0, 2),
               Cube(0, 1, 2), Cube(1, 1, 3), Cube(3, 1, 8), Cube(4, 1, 7), Cube(5, 1, 5), Cube(6, 1, 1), Cube(7, 1, 9),
               Cube(8, 1, 6),
               Cube(0, 2, 1), Cube(1, 2, 8), Cube(2, 2, 5), Cube(3, 2, 2), Cube(4, 2, 6), Cube(8, 2, 3),
               Cube(0, 3, 4), Cube(1, 3, 2), Cube(2, 3, 6), Cube(3, 3, 3), Cube(4, 3, 1), Cube(5, 3, 7), Cube(6, 3, 8),
               Cube(7, 3, 5), Cube(8, 3, 9),
               Cube(0, 4, 8), Cube(1, 4, 5), Cube(3, 4, 9), Cube(4, 4, 2), Cube(5, 4, 4), Cube(6, 4, 3), Cube(7, 4, 6),
               Cube(8, 4, 1),
               Cube(0, 5, 3), Cube(1, 5, 9), Cube(5, 5, 6), Cube(6, 5, 2), Cube(7, 5, 7), Cube(8, 5, 4),
               Cube(0, 6, 9), Cube(1, 6, 4), Cube(3, 6, 1), Cube(5, 6, 3), Cube(8, 6, 7),
               Cube(0, 7, 7), Cube(1, 7, 1), Cube(2, 7, 2), Cube(3, 7, 6), Cube(4, 7, 4), Cube(5, 7, 8),
               Cube(0, 8, 5)]
    # Medium
    sudoku3 = [Cube(0, 0, 6), Cube(7, 0, 8), Cube(8, 0, 2),
               Cube(0, 1, 2), Cube(1, 1, 3), Cube(3, 1, 8), Cube(4, 1, 7), Cube(5, 1, 5), Cube(6, 1, 1), Cube(7, 1, 9),
               Cube(8, 1, 6),
               Cube(4, 2, 6), Cube(8, 2, 3),
               Cube(1, 3, 2), Cube(2, 3, 6), Cube(7, 3, 5), Cube(8, 3, 9),
               Cube(1, 4, 5), Cube(3, 4, 9), Cube(5, 4, 4), Cube(6, 4, 3), Cube(7, 4, 6), Cube(8, 4, 1),
               Cube(0, 6, 9), Cube(1, 6, 4), Cube(5, 6, 3), Cube(8, 6, 7),
               Cube(1, 7, 1), Cube(4, 7, 4), Cube(5, 7, 8),
               Cube(0, 8, 5)]
    # really hard sudoku from yediot weekend news paper
    sudoku4expert = [Cube(1, 0, 6), Cube(4, 0, 5), Cube(7, 0, 4),
                     Cube(0, 1, 1), Cube(4, 1, 9), Cube(8, 1, 6),
                     Cube(3, 2, 8), Cube(5, 2, 7),
                     Cube(2, 3, 7), Cube(6, 3, 3),
                     Cube(0, 4, 3), Cube(1, 4, 9), Cube(7, 4, 5), Cube(8, 4, 7),
                     Cube(2, 5, 5), Cube(6, 5, 1),
                     Cube(3, 6, 4), Cube(5, 6, 1),
                     Cube(0, 7, 5), Cube(4, 7, 3), Cube(8, 7, 1),
                     Cube(1, 8, 8), Cube(4, 8, 2), Cube(7, 8, 7)]
    # # Expert
    sudoku4expert_2 = [Cube(4, 0, 1), Cube(5, 0, 9), Cube(7, 0, 8),
                     Cube(0, 1, 9), Cube(2, 1, 5),
                     Cube(3, 2, 4), Cube(6, 2, 9), Cube(8, 2, 1),
                     Cube(1, 3, 3), Cube(7, 3, 5), Cube(8, 3, 6),
                     Cube(6, 4, 3), Cube(7, 4, 4),
                     Cube(0, 5, 7), Cube(1, 5, 6), Cube(3, 5, 8),
                     Cube(0, 6, 8), Cube(2, 6, 1),
                     Cube(0, 7, 2), Cube(8, 7, 4),
                     Cube(1, 8, 4), Cube(3, 8, 6), Cube(5, 8, 7)]

    def __init__(self, board):
        self.board = board
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(
            filename=rf"{os.path.dirname(os.path.realpath(__file__))}/logs/sudoko-solver/log_{int(time.time())}.log",
            level=logging.DEBUG,  # if args.verbose else logging.CRITICAL,
            format=LOG_FORMAT)
        self.logger = logging.getLogger()

    def start(self, level: list) -> bool:
        # setup game board / level / preferences
        is_win = False
        self.board = Board(9)
        self.board.set_numbers_in_cubes(level)
        ts = time.time()

        # start the game
        start_str = f"Game started initiated on {ts:2.2f}"
        print(start_str + "\n")
        self.logger.info(start_str)

        if self.play():
            te = time.time()
            is_win = True
            print(f"Game Over!!!, we won! it took: {(te - ts):2.2f} seconds")
        else:
            print(f"we lost...it took: {(time.time() - ts):2.2f} seconds")
        # returns bool, win or lose
        return is_win


    def play(self):
        cube = self.board.find_next_empty_cube()
        self.logger.info(f"Get next free cube at: {cube}")
        if cube:
            self.board.update_cube_numbers(cube)
            self.logger.info(f"Update opt and none for {cube}")

            if len(cube.optional_nums) == 0:  # free cube found but no more optionals, go back to iterate last number
                self.logger.info(f"No more opt for {cube}")
                self.logger.info(f"we ran into a wall!...that's a shame, we'll go back and start over")
                return False
            else:
                for i,inum in enumerate(cube.optional_nums):
                    cube.number = inum
                    self.logger.info(f"Cube: {cube}, number as been set to {cube.number}")
                    if not self.board.set_cube_in_board(cube):
                        continue
                    print(self.board.draw_board())
                    if self.play():
                        self.logger.info(f"Lucky guess! {cube}")
                        return True
                    else:
                        cube.number = None
                return False

        else:  # no empty cube found in grid means that we won cause we grid is full without duplicate numbers in row/column/cube
            self.logger.info("We Won!!!")
            return True

if __name__ == "__main__":
    try:
        # WebUiInput()
        # parser = argparse.ArgumentParser()
        # group = parser.add_mutually_exclusive_group()
        # group.add_argument("-se", "--SuperEasy", help="Set up super easy board Sudoku", action="store_true")
        # group.add_argument("-e", "--Easy", help="Set up easy board Sudoku", action="store_true")
        # group.add_argument("-m", "--Medium", help="Set up medium board Sudoku", action="store_true")
        # group.add_argument("-ex", "--Expert", help="Set up expert board Sudoku", action="store_true")
        # parser.add_argument('-v', '--verbose', action='store_true', default=False)
        # args = parser.parse_args()
        # game_level = sudoku4expert
        #
        # if args.SuperEasy:
        #     print("super easy turned on")
        #     game_level = sudoku1
        # elif args.Easy:
        #     game_level = sudoku2
        #     print("easy turned on")
        # elif args.Medium:
        #     game_level = sudoku3
        #     print("medium turned on")
        # else:
        #     game_level = sudoku4expert
        #     print("hard turned on")

        # LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        # logging.basicConfig(
        #     filename=rf"{os.path.dirname(os.path.realpath(__file__))}/logs/sudoko-solver/log_{int(time.time())}.log",
        #     level=logging.DEBUG,# if args.verbose else logging.CRITICAL,
        #     format=LOG_FORMAT)
        # logger = logging.getLogger()
        pass
    except Exception as e:
        print(e)
