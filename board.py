from typing import List, Set
from cube import Cube, Cell
import logging
from custom_exceptions import LoseException
from collections import OrderedDict

logger = logging.getLogger(__name__)
class Board:
    def __init__(self, size: int, level: List[Cube]):
        self.size = size
        self.level_to_dict = { Cell(cube.row, cube.col): cube for cube in level}
        self.grid = {
            Cell(x,y): self._get_exiting_cube_or_new_from_init_state(x,y) 
            for x in range(1,size+1) for y in range(1,size+1)
        }
        self.empty_cells = (
            set(self.grid.keys()) - set(self.level_to_dict.keys()))
        self.cell_row_n_col_n_cubic_map = dict()
        self.refresh_empty()

    def _get_all_non_optionals_for_cube(self, cell: Cell) -> set[int]:
        cube = self.grid.get(cell)
        all_relevant_keys = self.get_all_cell_keys(cube)
        all_relevant_keys.discard(cell)

        non_optional = set()
        for k in all_relevant_keys:
            cu = self.grid.get(k)
            if cu.number:
                non_optional.add(cu.number)

        return non_optional

    def _refresh_cube_optionals(
        self, 
        cube: Cube, 
        non_optionals: set[Cell]
    ) -> None:
        cube.not_optional_nums = non_optionals
        cube.optional_nums.difference_update(non_optionals)
        logger.info(f'{Cell(cube.row, cube.col)} update his optionals '
                    f'to: {cube.optional_nums - non_optionals}')

    def refresh_empty(self):
        logger.debug(f"Refreshing empty cells({len(self.empty_cells)})")
        if not self.empty_cells:
            # check validity
            return

        empty_cells = OrderedDict()
        for key in self.empty_cells:
            cube = self.grid.get(key)
            if cube:
                non_optional = self._get_all_non_optionals_for_cube(key)                

                if cube.not_optional_nums != non_optional:
                    self._refresh_cube_optionals(cube, non_optional)

                if not cube.optional_nums:
                    raise LoseException(f'No optional numbers for cell')
                # updating empty cell dict length of optionals per cell key
                empty_cells[key] = len(cube.optional_nums)
        # print(f'Before: {empty_cells}')
        # em = sorted(empty_cells, key=empty_cells.__getitem__, reverse=True)
        # em = OrderedDictsorted(empty_cells.items(), key=lambda item: item[1], reverse=True)
        # print(f'After: {empty_cells}')
        self.empty_cells = {it for it in empty_cells.keys()}


    def assign_all_single_option(self):
        keys_to_delete = set()
        for key in list(self.empty_cells)[::-1]:
            cube = self.grid[key]
            if len(cube.optional_nums) == 1:
                num = cube.optional_nums.pop()
                if num not in self._get_all_non_optionals_for_cube(key):

                    logger.info(f'assign single: Set {num} in {key}')
                    cube.number = num
                    keys_to_delete.add(key)
                else:
                    raise LoseException(f'Tried to assign {num} which is non optional')
                    # cube.optional_nums.add(num)
            else:
                logger.info(f'{key} has 2 or more optionals')

        self.empty_cells = self.empty_cells - keys_to_delete
        if keys_to_delete:
            self.refresh_empty()

    def _get_non_optional_from_keys(self, keys: Set[Cell]) -> Set[int]:
        return set(self.grid[k].number for k in keys if self.grid[k].number)

    def _get_exiting_cube_or_new_from_init_state(self, row, col):
        return (
            self.level_to_dict.get(Cell(row, col))
            or Cube(row, col)
        )


    def get_all_cell_keys(self, cube) -> set[Cell]:
        key = Cell(cube.row, cube.col)
        if key not in self.cell_row_n_col_n_cubic_map:
            logger.debug(f'Creating cache const keys for {key}')
            self.cell_row_n_col_n_cubic_map[key] = set().union(
                self.get_cell_col_and_row_optionals(cube),
                self.get_cell_cubic_optionals(cube)
            )
        return self.cell_row_n_col_n_cubic_map[key]


    def get_cell_col_and_row_optionals(self, cube):
        return {cell for  cell in self.grid.keys() if cell.row == cube.row or cell.col == cube.col}

    
    def get_cell_cubic_optionals(self, cube):
        return cube.cubic_cat[cube.cubic]

        
    def draw_board(self):
        first_line = """      1  |  2  |  3  ||  4  |  5  |  6  ||  7  |  8  |  9  |\n   |-------------------------------------------------------|\n"""
        some_dict = {}
        template = ''
        for i in range(1,self.size+1):
            for j in range(1,self.size+1):
                item = self.grid[Cell(i,j)]
                num = item.number if item.number != None else " "
                some_dict[item.col] = num

            line_str = f"""{i}  |  {some_dict[1]}  |  {some_dict[2]}  |  {some_dict[3]}  ||  {some_dict[4]}  |  {some_dict[5]}  |  {some_dict[6]}  ||  {some_dict[7]}  |  {some_dict[8]}  |  {some_dict[9]}  |\n"""
            line_sep = "   |-----------------||-----------------||-----------------|\n" if i % 3 != 0 else "   |=================||=================||=================|\n"    
            template = template + line_str + line_sep
        return first_line + template
