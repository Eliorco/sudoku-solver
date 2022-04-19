from board import Board
from presets_games import *

from copy import deepcopy
from utils import timing
from custom_exceptions import WinException, LoseException
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)  # noqa
logger = logging.getLogger(__name__)

def play(board: Board):
    logger.info({f"({k.row},{k.col}): {v.optional_nums}" for k,v in board.grid.items() if k in board.empty_cells})
    board.assign_all_single_option()
    if board.empty_cells:
        empty_cell = board.empty_cells.pop()
        logger.info(f'Update {empty_cell} optionals, '
                    f'op:{board.grid[empty_cell].optional_nums}, '
                    f'non-op: {board.grid[empty_cell].not_optional_nums}'
        )
        curent_optional_cube_nums = board.grid[empty_cell].optional_nums
        if not curent_optional_cube_nums:
            raise LoseException(f'{board.grid[empty_cell]} has no optional_nums')

        for num in curent_optional_cube_nums:
            b = deepcopy(board)
            b.grid[empty_cell].number = num
            logger.info(f'reg flow: Set {num} in {empty_cell}\n{b.draw_board()}')
            try:
                b.refresh_empty()
                play(b)
            except LoseException as le:
                logger.info(str(le))
                logger.info(f'Not valid sudoku board! '
                            f'iterate to next number {num} -> {curent_optional_cube_nums}'
                            f'\n{b.draw_board()}'
                )
    else:
        logger.info(f'Final Board\n{board.draw_board()}')
        raise WinException("No more empty cubes")

@timing
def main():
    # b = Board(size=9, level=sudoku1_false) #### # not a valid board
    b = Board(size=9, level=sudoku1_6)
    # b = Board(size=9, level=sudokuMaster) #### # not a valid board
    # b = Board(size=9, level=sudoku4expert)
    # b = Board(size=9, level=sudoku4expert_new2)

    try:
        logger.info(b.draw_board())
        play(b)
    except WinException as we:
        logger.info(f"Sudoku solved! we Won!!! ||| {we}\n{b.draw_board()}")
    except LoseException:
        logger.info(f"Not valid sudoku board! | {b.draw_board()}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
