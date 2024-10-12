"""
---"subplot" syntax (Check around line 1411 in pyplot.py)---

@_docstring.interpd
def subplot(*args, **kwargs) -> Axes:

1. The "->" syntax stands for a function annotation: it has been introduced with Python3 and it only documents the various
   types in our code, but it has no effects at runtime (not slower, not faster). I can write whatever I want without
   influence my code.
   
   Example #1:
   def sum(x: int, y: int) -> int:
        return x + y
   
   Here I'm saying to the user that "x" should be an integer as well as "y" and that the return value will be an integer too.
   So if I run sum(1, 2) I'll get 3.
   
   If now I change my function definition into:
   def sum(x: str, y: int) -> str:
        return x + y
   
   Here I'm saying to the user that "x" as well as the return value should be a string while "y" should be an integer.
   If I run sum(1, 2) I'll get another time 3, and this because I have only made a function annotation that doesn't
   influence at all during the runtime. Thus, Python doesn't interpret a string as "x" only because I've written "x: str".
   
   To access function annotaions I can type:
   sum.__annotation__
   
   While to access function documentation (that is explicited into """ """ after the "def" keyword) I can type:
   sum.__doc__
   
   Check the links below for more info:
   https://www.youtube.com/watch?v=k56rEoRjK4k&t=192s
   https://peps.python.org/pep-3107/

2. Explain the "@" syntax before function definition...

3. Explain what "*" and "**" mean...

4.  subplot(nrows, ncols, index). The subplot will take the "index" position on a grid with "nrows" rows and *ncols* columns.
    "index" starts at 1 in the upper left corner and increases to the right.
    
    Example #1:
    nrows = 2
    ncols = 1
    index = 1
    I'm creating a matrix with 2 rows and 1 col and my plot is going to occupy the upper half of the figure.
    
    Example #2:
    nrows = 3
    ncols = 1
    index = (1,2) -> "index" is a two-touple (a Python's touple is a sort of Matlab's cell) this time...
    Here I'm creating a plot that is going to occupty the uppermost 2/3 of the figure. If "index" is a two-touple
    element, the first touple's element indicates the starting index in the grid, while the second one the lasting.
    
5. subplot(211) = subplot(2, 1, 1)
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
#1
figure = plt.figure()
ax = figure.add_subplot(111)
ax2 = ax.twinx()
ax2.cla()#or clear() ; doesn't work both ways
ax.set_ylabel('ax_label')
ax2.set_ylabel('ax2_label')#expected to be on the right
plt.show()
"""

"""
#2
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
for i in range(2):
    # do some plotting here
    ax2.set(ylabel=f'ylabel of plot # {i}', ylim=(1, i + 2))
    ax2.yaxis.set_label_position('right')
    fig.savefig(f'{i}.png')
    ax1.cla()
    ax2.cla()
"""

"""
#3
ax0 = plt.subplot(211) # subplot(211) = subplot(2,1,1)
ax1 = plt.subplot(212, sharex=ax0)
ax0.plot(range(100))
ax1.plot(range(100))
ax0.cla()
plt.show()
"""

"""
ax0 = plt.subplot(211) # subplot(211) = subplot(2,1,1)
ax1 = plt.subplot(212,sharex=ax0)
a=range(50)
b=range(70)
ax0.plot(a)
ax1.plot(b)
list(a)
a=range(100)
ax0.plot(a)
list(a)
ax0.cla()
plt.show()
list(a)
"""

ax0 = plt.subplot(111)
ax1 = ax0.twinx()
ax1.set_ylabel("ay1")
ax1.yaxis.label.set_color("red")
ax0.plot(range(30))
ax1.plot(range(60))
#ax1.cla() # This is not an hard clear
a=3
ax0.set_xlabel("ax0", loc='left')
ax0.set_ylabel("ay0")
ax0.yaxis.label.set_color("red")

ax1.cla(reset=False) # Soft clear
ax1.set_xlabel("ax1", loc='right')
ax1.set_ylabel("ay1", loc='bottom')
ax1.yaxis.label.set_color("blue")
#plt.show()

ax0.yaxis.set_ticks([1,2,3,4,5,6,7,25,30])
ax1.yaxis.set_ticks([1,2,3,4,5,6,7,25,30,35,55,80])

#ax0.set_ylabel("ax0")
#ax0.yaxis.label.set_color("red")
ax0.cla(reset=5674,trgt=898) # Here the labels should stay
ax1.cla(reset=True)
#ax1.cla(reset='casa', trt=99)
#ax1.axhline(70)
plt.show()
b=1