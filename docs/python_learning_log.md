# Python Learning Log
## Day 5 - [10.17.25]
### Course: DataCamp - Python Basics Notes
** Importing packages:**
Python uses packages that contain an assortment of tools developed by the open source community thereby increasing the options available through the python language. Packages may be installed by entering pip install (package name) in the command prompt. After package installation is completed, the package can be imported using the following commands:

import PackageName #imports the package without an alias
import PackageName as pn # Imports the package with chosen alias
from PackageName import ObjectName # Imports an object from the package

** Operators: **
Arithmetic operators:
+ #Add
- # Subtract
* # Multiply
/ # Divide
** # Exponent
% # Returns 1 # Get the remainder after division with %

Assignment operators:
a = 5 # assigns a value to a
x[0] # Change the value of an item in a list

Numeric comparison operators:
3 == 3 # Test for equality
3 != 3 # Test for inequality
3 > 1 # Test greater than
>= # greater than or egual
<
<=

** Lists: **
# Lists are created using [], elements seperated by commas
x = [1, 3, 2]

List Functions and Methods:

x.sorted(x) # Return a sorted copy of the list e.g., [1,2,3]
x.sort() # Sorts the list in-place (replaces x)
reversed(x) # Reverst the order in x e.g., [2,3,1]
x.reversed() # Reverse the list in-place
x.count(2) # Count the number of element 2 in the list

Selecting list elements:
- Python lists us zero-indexing
# Defin the list
x = ['a', 'b', 'c', 'd', 'e']
x[0] # Select the 0th element in the list
x[-1] # Select the last element of the list
x[1:3] # Select 1st (inclusive) to 3rd (exclusive) e.g. (b,c)
x[2:] # Select the 2nd to the end e.g. ( c, d, e)
x[:3] # Select 0th to 3rd (exlusive) e.g. (a, b, c)
- lists can be added and multipled

** NumPy arrays: **
- The NumPy package enables scientific computing capabilites in python. It provides multidimensional array objects and their effecient operations. To import Numpy run the code import numpy as np

To create array:
# convert a python list to a NumPy array
np.array([1, 2, 3]) # Returns array ([1, 2, 3])
np.arrange(1, 5) # Returns a sequence from start (inclusive) to end (exclusive) e.g. ([1, 2, 3, 4])
np.arrange(1,5,2) # Returns a stepped sequence from start(inclusive) to end(exclusive) and seems like the 2 indicates every other number stepping e.g. ([1, 3])
np.repeat([1, 3, 6], 3) # Repeats values n times e.g. ([1, 1, 1, 3, 3, 3, 6, 6, 6,])
np.title([1, 3, 6], 3) # Repeats the list n times e.g. ([1, 3, 6, 1, 3, 6, 1, 3, 6])

NumPy Math functions and methods:
np.log(x)
np.exp(x) # Calculate exponential
np.max(x) # Calc max value
np.min(x) # calc min
np.sum(x) # Calc sum
np.mean(x)
np.quantile(x, q) # Calc q-th quantile (-point that divides a dataset into groups of equal probability or size e.g quartiles(4 groups))
np.round(x, n) # Round to n decimal places
np.var(x) # Calculate variance (- a statistical measure of how spread out a data set is from its mean, calculated as the average of the squared differences from the mean) 
np.std(x) # Calc standard deviation

# test commit