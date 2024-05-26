# coin_toss_debug.py - Task Description

#### _From Automate the Boring Stuff with Python. Chapter 10. Practice Project - Debugging Coin Toss:_

Say you have a list value like this:

`spam = ['apples', 'bananas', 'tofu', 'cats']`

The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it's an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

`import random`<br>
`guess = ''`<br>
`while guess not in ('heads', 'tails'):`<br>
&emsp;&emsp;`print('Guess the coin toss! Enter heads or tails:')`<br>
&emsp;&emsp;`guess = input()`<br>
`toss = random.randint(0, 1) # 0 is tails, 1 is heads`<br>
`if toss == guess:`<br>
&emsp;&emsp;`print('You got it!')`<br>
`else:`<br>
&emsp;&emsp;`print('Nope! Guess again!')`<br>
&emsp;&emsp;`guesss = input()`<br>
&emsp;&emsp;`if toss == guess:`<br>
&emsp;&emsp;&emsp;&emsp;`print('You got it!')`<br>
&emsp;&emsp;`else:`<br>
&emsp;&emsp;&emsp;&emsp;`print('Nope. You are really bad at this game.')`<br>