from board import Board
from presets_games import *

from copy import deepcopy

from custom_exceptions import WinException, LoseException
from logger import logger
log = logger.getLogger(__name__)


class Game:
    
    def __init__(self, input_cubes: list[Cube]) -> None:
        self.board = Board(size=9, level=input_cubes)

    def run(self):
        try:
            log.info(self.board.draw_board())
            solve(self.board)
        except WinException as we:
            log.info(f"Sudoku solved! we Won!!! ||| {we}\n{self.board.draw_board()}")
        except LoseException:
            log.info(f"Not valid sudoku board! | {self.board.draw_board()}")


    
def solve(board: Board):
    log.info({f"({k.row},{k.col}): {v.optional_nums}" for k,v in board.grid.items() if k in board.empty_cells})
    board.assign_all_single_option()
    if board.empty_cells:
        empty_cell = board.empty_cells.pop()
        log.info(f'Update {empty_cell} optionals, '
                    f'op:{board.grid[empty_cell].optional_nums}, '
                    f'non-op: {board.grid[empty_cell].not_optional_nums}'
        )
        curent_optional_cube_nums = board.grid[empty_cell].optional_nums
        if not curent_optional_cube_nums:
            raise LoseException(f'{board.grid[empty_cell]} has no optional_nums')

        for num in curent_optional_cube_nums:
            b = deepcopy(board)
            b.grid[empty_cell].number = num
            log.info(f'reg flow: Set {num} in {empty_cell}\n{b.draw_board()}')
            try:
                b.refresh_empty()
                result = solve(b)
            except LoseException as le:
                log.info(f'{le}\n'
                            f'Not valid sudoku board! ({empty_cell}) '
                            f'iterate to next number {num} -> {curent_optional_cube_nums}'
                            f'\n{b.draw_board()}'
                )
    else:
        log.info(f'Final Board\n{board.draw_board()}')
        raise WinException("No more empty cubes", winning_board=board)
