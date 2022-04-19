from cube import Cube

# Very Easy | Sanity check
sudoku1 = [
    Cube(1,1,6), Cube(2,1,7), Cube(3,1,9), Cube(4,1,4), Cube(5,1,3), Cube(6,1,1), Cube(7,1,5), Cube(8,1,8), Cube(9,1,2),
    Cube(1,2,2), Cube(2,2,3), Cube(3,2,4), Cube(4,2,8), Cube(5,2,7), Cube(6,2,5), Cube(7,2,1), Cube(8,2,9), Cube(9,2,6),
    Cube(1,3,1), Cube(2,3,8), Cube(3,3,5), Cube(4,3,2), Cube(5,3,6), Cube(6,3,9), Cube(7,3,7), Cube(8,3,4), Cube(9,3,3),
    Cube(1,4,4), Cube(2,4,2), Cube(3,4,6), Cube(4,4,3), Cube(5,4,1), Cube(6,4,7), Cube(7,4,8), Cube(8,4,5), Cube(9,4,9),
    Cube(1,5,8), Cube(2,5,5), Cube(3,5,7), Cube(4,5,9), Cube(5,5,2), Cube(6,5,4), Cube(7,5,3), Cube(8,5,6), Cube(9,5,1),
    Cube(1,6,3), Cube(2,6,9), Cube(3,6,1), Cube(4,6,5), Cube(5,6,8), Cube(6,6,6), Cube(7,6,2), Cube(8,6,7), Cube(9,6,4),
    Cube(1,7,9), Cube(2,7,4), Cube(3,7,8), Cube(4,7,1), Cube(5,7,5), Cube(6,7,3), Cube(7,7,6), Cube(8,7,2), Cube(9,7,7),
    Cube(1,8,7), Cube(2,8,1), Cube(3,8,2), Cube(4,8,6), Cube(5,8,4), Cube(6,8,8),
    Cube(1,9,5), Cube(2,9,6), Cube(3,9,3), Cube(4,9,7), Cube(5,9,9), Cube(6,9,2)
]

sudoku1_false = [
    Cube(1,1,6), Cube(2,1,7), Cube(3,1,9), Cube(4,1,4), Cube(5,1,3), Cube(6,1,1), Cube(7,1,5), Cube(8,1,8), Cube(9,1,2),
    Cube(1,2,2), Cube(2,2,3), Cube(3,2,4), Cube(4,2,8), Cube(5,2,7), Cube(6,2,5), Cube(7,2,1), Cube(8,2,9), Cube(9,2,6),
    Cube(1,3,1), Cube(2,3,8), Cube(3,3,5), Cube(4,3,2), Cube(5,3,6), Cube(6,3,9), Cube(7,3,7), Cube(8,3,4), Cube(9,3,3),
    Cube(1,4,4), Cube(2,4,2), Cube(3,4,6), Cube(4,4,3), Cube(5,4,1), Cube(6,4,7), Cube(7,4,8), Cube(8,4,5), Cube(9,4,9),
    Cube(1,5,8), Cube(2,5,5), Cube(3,5,7), Cube(4,5,9), Cube(5,5,2), Cube(6,5,4), Cube(7,5,3), Cube(8,5,6), Cube(9,5,1),
    Cube(1,6,3), Cube(2,6,9), Cube(3,6,1), Cube(4,6,5), Cube(5,6,8), Cube(6,6,6), Cube(7,6,2), Cube(8,6,7), Cube(9,6,4),
    Cube(1,7,9), Cube(2,7,4), Cube(3,7,8), Cube(4,7,1), Cube(5,7,5), Cube(6,7,3), Cube(7,7,6), Cube(8,7,2), Cube(9,7,7),
    Cube(1,8,3), Cube(2,8,1), Cube(3,8,2), Cube(4,8,6), Cube(5,8,4), Cube(6,8,8),
    Cube(1,9,5), Cube(2,9,6), Cube(3,9,3), Cube(4,9,7), Cube(5,9,9), Cube(6,9,2)
]

sudoku1_5 = [
    Cube(1,1,6), Cube(1,2,7), Cube(1,3,9), Cube(1,4,4), Cube(1,5,3), Cube(1,6,1), Cube(1,7,5), Cube(1,8,8), Cube(1,9,2),
    Cube(2,1,2), Cube(2,2,3), Cube(2,3,4), Cube(2,4,8), Cube(2,5,7), Cube(2,6,5), Cube(2,7,1), Cube(2,8,9), Cube(2,9,6),
    Cube(3,1,1), Cube(3,2,8), Cube(3,3,5), Cube(3,4,2), Cube(3,5,6), Cube(3,6,9), Cube(3,7,7), Cube(3,8,4), Cube(3,9,3),
    Cube(4,1,4), Cube(4,2,2), Cube(4,3,6), Cube(4,4,3), Cube(4,5,1), Cube(4,6,7), Cube(4,7,8), Cube(4,8,5), Cube(4,9,9),
    Cube(5,1,8), Cube(5,2,5), Cube(5,3,7), Cube(5,4,9), Cube(5,5,2), Cube(5,6,4), Cube(5,7,3), Cube(5,8,6), Cube(5,9,1),
    Cube(6,1,3), Cube(6,2,9), Cube(6,3,1), Cube(6,4,5), Cube(6,5,8), Cube(6,6,6), 
    Cube(7,1,9), Cube(7,2,4), Cube(7,3,8), Cube(7,4,1), Cube(7,5,5), Cube(7,6,3), 
    Cube(8,1,7), Cube(8,2,1), Cube(8,3,2), Cube(8,4,6), Cube(8,5,4), Cube(8,6,8),
    Cube(9,1,5), Cube(9,2,6), Cube(9,3,3), Cube(9,4,7), Cube(9,5,9), Cube(9,6,2)
]

sudoku1_6 = [
    Cube(1,1,6), Cube(1,2,7), Cube(1,5,3), Cube(1,6,1), Cube(1,7,5), Cube(1,8,8), Cube(1,9,2),
    Cube(2,1,2), Cube(2,5,7), Cube(2,6,5),
    Cube(3,3,5), Cube(3,7,7), Cube(3,8,4), Cube(3,9,3),
    Cube(4,2,2), Cube(4,5,1), Cube(4,6,7), Cube(4,7,8), Cube(4,8,5), Cube(4,9,9),
    Cube(5,6,4), Cube(5,7,3), Cube(5,8,6), Cube(5,9,1),
    Cube(6,2,9), Cube(6,3,1), Cube(6,4,5), Cube(6,5,8), Cube(6,6,6), 
    Cube(7,2,4), Cube(7,3,8), Cube(7,4,1), Cube(7,5,5), Cube(7,6,3), 
    Cube(8,1,7), Cube(8,2,1), Cube(8,4,6), Cube(8,5,4), Cube(8,6,8),
    Cube(9,1,5), Cube(9,3,3), Cube(9,4,7), Cube(9,5,9), Cube(9,6,2)
]

# Easy
sudoku2 = [
    Cube(0,0,6), Cube(1,0,7), Cube(2,0,9), Cube(3,0,4), Cube(4,0,3), Cube(5,0,1), Cube(6,0,5), Cube(7,0,8), Cube(8,0,2),
    Cube(0,1,2), Cube(1,1,3), Cube(3,1,8), Cube(4,1,7), Cube(5,1,5), Cube(6,1,1), Cube(7,1,9), Cube(8,1,6),
    Cube(0,2,1), Cube(1,2,8), Cube(2,2,5), Cube(3,2,2), Cube(4,2,6), Cube(8,2,3),
    Cube(0,3,4), Cube(1,3,2), Cube(2,3,6), Cube(3,3,3), Cube(4,3,1), Cube(5,3,7), Cube(6,3,8), Cube(7,3,5), Cube(8,3,9),
    Cube(0,4,8), Cube(1,4,5), Cube(3,4,9), Cube(4,4,2), Cube(5,4,4), Cube(6,4,3), Cube(7,4,6), Cube(8,4,1),
    Cube(0,5,3), Cube(1,5,9), Cube(5,5,6), Cube(6,5,2), Cube(7,5,7), Cube(8,5,4),
    Cube(0,6,9), Cube(1,6,4), Cube(3,6,1), Cube(5,6,3), Cube(8,6,7),
    Cube(0,7,7), Cube(1,7,1), Cube(2,7,2), Cube(3,7,6), Cube(4,7,4), Cube(5,7,8),
    Cube(0,8,5)
]

# Medium
sudoku3 = [
    Cube(0,0,6), Cube(7,0,8), Cube(8,0,2),
    Cube(0,1,2), Cube(1,1,3), Cube(3,1,8), Cube(4,1,7), Cube(5,1,5), Cube(6,1,1), Cube(7,1,9), Cube(8,1,6),
    Cube(4,2,6), Cube(8,2,3),
    Cube(1,3,2), Cube(2,3,6), Cube(7,3,5), Cube(8,3,9),
    Cube(1,4,5), Cube(3,4,9), Cube(5,4,4), Cube(6,4,3), Cube(7,4,6), Cube(8,4,1),
    Cube(0,6,9), Cube(1,6,4), Cube(5,6,3), Cube(8,6,7),
    Cube(1,7,1), Cube(4,7,4), Cube(5,7,8),
    Cube(0,8,5)
]

# Expert
sudoku4expert = [
    Cube(5,1,1), Cube(6,1,9), Cube(8,1,8),
    Cube(1,2,9), Cube(3,2,5),
    Cube(4,3,4), Cube(7,3,9), Cube(9,3,1),
    Cube(2,4,3), Cube(8,4,5), Cube(9,4,6),
    Cube(7,5,3), Cube(8,5,4),
    Cube(1,6,7), Cube(2,6,6), Cube(4,6,8),
    Cube(1,7,8), Cube(3,7,1),
    Cube(1,8,2), Cube(9,8,4),
    Cube(2,9,4), Cube(4,9,6), Cube(6,9,7)
]

# Expert
sudoku4expert_new = [
    Cube(1,4,1), Cube(1,6,4), Cube(1,7,8),
    Cube(2,1,2), Cube(2,9,9),
    Cube(3,3,9), Cube(3,7,1),
    Cube(4,2,2), Cube(4,5,8), Cube(4,6,9), Cube(4,7,6), Cube(4,9,7),
    Cube(5,2,7), Cube(5,5,1), Cube(5,8,3),
    Cube(6,1,9), Cube(6,3,6), Cube(6,4,4), Cube(6,5,7), Cube(6,8,8),
    Cube(7,3,7), Cube(7,7,2),
    Cube(8,1,4), Cube(8,9,6),
    Cube(9,3,2), Cube(9,4,5), Cube(9,6,1)
]

sudoku4expert_new2 = [
    Cube(1,1,6), Cube(1,6,5),
    Cube(2,4,3), Cube(2,6,9), Cube(2,8,5),
    Cube(3,5,4), Cube(3,8,6),
    Cube(4,1,4), Cube(4,3,3),
    Cube(5,2,8), Cube(5,4,7), Cube(5,7,2),
    Cube(6,6,1), Cube(6,7,7),
    Cube(7,5,9), Cube(7,9,6),
    Cube(8,3,5), Cube(8,5,2),Cube(8,7,8), Cube(8,8,4), Cube(8,9,9),
    Cube(9,2,4), Cube(9,6,3)
]

# Master
sudokuMaster = [
    Cube(1,1,6), Cube(2,1,4), Cube(3,1,3), Cube(5,1,5), Cube(9,1,2),
    Cube(1,2,2), Cube(4,2,6), Cube(5,2,7), Cube(8,2,5), Cube(9,2,3),
    Cube(1,3,5), Cube(9,3,6), Cube(2,3,3),
    Cube(8,4,9), Cube(4,4,7),
    Cube(1,5,9), Cube(3,5,6), Cube(3,5,4), Cube(5,5,8),Cube(6,5,5), Cube(7,5,2), Cube(8,5,3),
    Cube(2,6,3), Cube(4,6,9), Cube(5,6,1),
    Cube(1,7,8), Cube(4,7,5), Cube(6,7,7), Cube(8,7,6),Cube(9,7,9),
    Cube(1,8,3), Cube(2,8,5), Cube(2,8,9), Cube(4,8,2),Cube(5,8,7),Cube(6,8,6),Cube(9,8,4),
    Cube(2,9,6), Cube(5,9,9), Cube(6,9,3), Cube(8,9,2),Cube(9,9,5)
]