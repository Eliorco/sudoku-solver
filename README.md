# Sudoku-Solver
If you tried really hard to solve expert level sudoku and eventually give up? this is the right repo for you!

All you need to do is to create Cube array with their col,row,number('<COLUMN>', '<ROW>', '<NUMBER>')

Most Top-Left cube is: 0,0

Most Bottom-Right cube is: 9,9

```my_grid = [Cube(1,1,4), Cube(4,1,1), Cube(5,1,9),..., Cube(1,3,3),...]```
<br><H2>Coming Soon</H2>
<p>Web User Interface to easly insert sudoku board.</p>


## Update
Version 2.0 is here, this is HUGE performance change that solve the hardest level under 2 seconds(!!!).
for reference the previous version did it within 153 seconds, and V1.0 even did it slower than that.


<hr>
screenshots:

this:
```
      1  |  2  |  3  ||  4  |  5  |  6  ||  7  |  8  |  9  |
   |-------------------------------------------------------|
1  |     |  9  |     ||     |     |  7  ||  8  |  2  |     |
   |-----------------||-----------------||-----------------|
2  |     |     |     ||  3  |     |  6  ||     |     |  4  |
   |-----------------||-----------------||-----------------|
3  |     |  5  |     ||     |     |     ||  1  |     |     |
   |=================||=================||=================|
4  |     |     |  4  ||     |     |  8  ||     |     |  6  |
   |-----------------||-----------------||-----------------|
5  |  1  |     |     ||     |     |     ||     |     |     |
   |-----------------||-----------------||-----------------|
6  |  9  |     |     ||     |     |     ||     |     |  7  |
   |=================||=================||=================|
7  |     |     |  9  ||     |  3  |     ||     |     |     |
   |-----------------||-----------------||-----------------|
8  |  8  |     |     ||  5  |  4  |     ||     |     |     |
   |-----------------||-----------------||-----------------|
9  |     |     |  1  ||  6  |     |     ||     |  4  |     |
   |=================||=================||=================|

```

turn into this:
```
      1  |  2  |  3  ||  4  |  5  |  6  ||  7  |  8  |  9  |
   |-------------------------------------------------------|
1  |  4  |  9  |  6  ||  1  |  5  |  7  ||  8  |  2  |  3  |
   |-----------------||-----------------||-----------------|
2  |  2  |  1  |  8  ||  3  |  9  |  6  ||  5  |  7  |  4  |
   |-----------------||-----------------||-----------------|
3  |  3  |  5  |  7  ||  2  |  8  |  4  ||  1  |  6  |  9  |
   |=================||=================||=================|
4  |  5  |  3  |  4  ||  7  |  2  |  8  ||  9  |  1  |  6  |
   |-----------------||-----------------||-----------------|
5  |  1  |  8  |  2  ||  9  |  6  |  3  ||  4  |  8  |  5  |
   |-----------------||-----------------||-----------------|
6  |  9  |  6  |  2  ||  4  |  1  |  3  ||  5  |  8  |  7  |
   |=================||=================||=================|
7  |  6  |  4  |  9  ||  8  |  3  |  1  ||  7  |  5  |  2  |
   |-----------------||-----------------||-----------------|
8  |  8  |  7  |  3  ||  5  |  4  |  2  ||  6  |  9  |  1  |
   |-----------------||-----------------||-----------------|
9  |  5  |  2  |  1  ||  6  |  7  |  9  ||  3  |  4  |  8  |
   |=================||=================||=================|

Sudoku solved! we Won!!! | No more empty cubes

```