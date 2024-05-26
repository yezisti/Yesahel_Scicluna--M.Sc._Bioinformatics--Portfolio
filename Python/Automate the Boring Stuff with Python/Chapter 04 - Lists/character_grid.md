# character_grid.py - Task Description

#### _From Automate the Boring Stuff with Python. Chapter 4. Practice Project - Character Picture Grid:_

Say you have a list of lists where each value in the inner lists is a one-character string, like this:

`grid =[`<br>
&emsp;&emsp;`['.', '.', '.', '.', '.', '.'],`<br>
&emsp;&emsp;`['.', 'O', 'O', '.', '.', '.'],`<br>
&emsp;&emsp;`['O', 'O', 'O', 'O', '.', '.'],`<br>
&emsp;&emsp;`['O', 'O', 'O', 'O', 'O', '.'],`<br>
&emsp;&emsp;`['.', 'O', 'O', 'O', 'O', 'O'],`<br>
&emsp;&emsp;`['O', 'O', 'O', 'O', 'O', '.'],`<br>
&emsp;&emsp;`['O', 'O', 'O', 'O', '.', '.'],`<br>
&emsp;&emsp;`['.', 'O', 'O', '.', '.', '.'],`<br>
&emsp;&emsp;`['.', '.', '.', '.', '.', '.']]`

You can think of `grid[x][y]` as being the character at the x- and
y-coordinates of a "picture" drawn with text characters. The `(0, 0)` origin will be in the upper-left corner, the x-coordinates increase going right, and w the y-coordinates increase going down.

Copy the previous grid value, and write code that uses it to print the image:

`..OO.OO..`<br>
`.OOOOOOO.`<br>
`.OOOOOOO.`<br>
`..OOOOO..`<br>
`...OOO...`<br>
`....O....`

Hint: You will need to use a loop in a loop in order to print `grid[0][0]`, then `grid[1][0]`, then `grid[2][0]`, and so on, up to `grid[8][0]`. This will finish the first row, so then print a newline. Then your program should print `grid[0][1]`, then `grid[1][1]`, then `grid[2][1]`, and so on. The last thing your program will print is `grid[8][5]`. 

Also, remember to pass the end keyword argument to `print()` if you don't want a newline printed automatically after each `print()` call.