import pytest
from .board import Board
from .cube import Cube
from .game import *

# def test_failed():
#     assert True, False

def test_sort_empty_cells_by_lower_optional_first():
    b = Board(9, sudoku1)
    b.empty_cells
    assert True, False
