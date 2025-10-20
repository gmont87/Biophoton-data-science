# Python Learning Log
## 📘 Table of Contents

- [10-17-2025 — DataCamp: Python Basics Notes](#10-17-2025--datacamp-python-basics-notes)
- [10-18-2025 — DataCamp: Dictionaries Part 1 + Git Ignore & Cleanup](#10-18-2025--datacamp-dictionaries-part-1--git-ignore--cleanup)
- [10-19-2025 — DataCamp: Dictionaries Part 2](#10-19-2025--datacamp-dictionaries-part-2)
- [10-20-2025 — Python Dictionary practice](https://github.com/gmont87/Biophoton-data-science/blob/main/docs/python_learning_log.md#10-20-2025--python-dictionary-practice)




### 10-17-2025 — DataCamp: Python Basics Notes
** Importing packages:**
Python uses packages that contain an assortment of tools developed by the open source community thereby increasing the options available through the python language. Packages may be installed by entering pip install (package name) in the command prompt. After package installation is completed, the package can be imported using the following commands:

import PackageName #imports the package without an alias
import PackageName as pn # Imports the package with chosen alias
from PackageName import ObjectName # Imports an object from the package

** Operators: **
Arithmetic operators:
(+) Add
(-) Subtract
(*)  Multiply
(/)  Divide
(**)  Exponent
(%)  Returns 1, Get the remainder after division with %

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
#### Lists are created using [], elements seperated by commas
x = [1, 3, 2]

List Functions and Methods:

x.sorted(x) # Return a sorted copy of the list e.g., [1,2,3]
x.sort() # Sorts the list in-place (replaces x)
reversed(x) # Reverst the order in x e.g., [2,3,1]
x.reversed() # Reverse the list in-place
x.count(2) # Count the number of element 2 in the list

Selecting list elements:
- Python lists us zero-indexing
#### Define the list
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
#### convert a python list to a NumPy array
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

### 10-18-2025 — DataCamp: Dictionaries Part 1 + Git Ignore & Cleanup

- How to check Python and pip versions ('python3 --version', 'pip3 --version').
    - python3 --version, tells me which version of pyhtin is installed on my system. Currently i have Python 3.9.6.
    - pip3 --version, tells me which version of Python package installed is available and which Python it is associated with.
    * So i was attempting to run some code for the photon count simulation but it wouldn't work because I did not have NumPy nor Matplotlib installed. so i when i attempted to run 'pip install numpy matplotlib' in the terminal in VS Code I encountered this: zsh: command not found: pip. So I determined my version of python using python3 --version, and found that I had Python 3.9.6 installed. Then I was lead to ensure that the pip (pachake installer) was properly set up for this version. I did this by running 'python3 -m ensurepip --upgrade' in the VS Code terminal, which told Python to install or repair pip if it was missing. Next I ran 'pip3 --version' in order to determine my pip version which was 'pip 21.2.4' and demonstrated that pip3 is installed and working and correctly tied to Python 3.9. So, now i ran the command 'pip3 install numpy matplotlib', which worked.


- Installed 'numpy' and 'matplotlib' with pip.
    - NumPy -> library for efficient math operation, arrays, and numerical computations.
    - Matplotlib -> library for plotting vissually
    * These will be importan for simulating photon counts and manipulating arrays, aswell as, enabling me to visualize emission patterns.
- Created a virtual environment using:
python3 -m venv venv
source venv/bin/activate
    * This created an isolated Python environment inside of my project folder. This enables me to install packages within the folder rather than globally on my system.
    - 'source venv/bin/activate' initiates the vitual environment so that the terminal uses it.
    * This enables me to maintain my projects seperate so that, for example, installation of library doesnt break another project.
    * It also facilitates reproducibility.
    * Lastly, it apparently prevents "dependency hell" when multiple projects require different versions of the same library.

pip install numpy matplotlib
- Learned to freeze environment dependencies ('pip freeze > requirements.txt').
- Added 'venv/' to '.gitignore' to avoid commiting large folders to GitHub.

- Tested setup with a simple sine wave plot using NumPy + Matplotlib.
_ Understood the difference between:
- **Commit** -> saves changes locally.
- **Push** -> uploads changes to GitHub.com.


### Course: DataCamp_Dictionaries, Part 1

-Dictionaries use {}
* Reminder: 'x.index(y)' finds the place of y in list x. Then if I assign a value to this index, say, 'a = x.index(y)' I can use 'a' to call the same place in a corresponding list, say, 'b[a]'. Remeber to use the [ ] for lists.

- A dictionary seems to have a key with a corresponding value as such:
    my_dict = {
   "key1":"value1",
   "key2":"value2",}

- The keys in a dictionary can be printed by adding .keys() to the dictionary name.
- Similarly, the value corresponding to a key may be returned by calling the dictionare with the key in [}: my_dict["key1"]

Example: [Python Basic Dictionary Script](/Users/ginomontero/Documents/GitHub/Biophoton-data-lab/Biophoton-data-science/code_snippets/2025-10-18_Python_Dictionaries)

#### Understanding .gitignore, tracked files, and the cleanup command
- This was neccessary to understand because after creating the virtual environment, 1000s of files appeard in my GitHub desktop in the files changed area instead of just the ones that I wanted to commit to GitHub. Instruction provide by ChatGPT.
1. How Git Tracks Files
    - Git tracks every file that is added and commited once a Git repository is created and will then monitor those tracked files for any changes (even if it is later added to .gitignore).
2. '.gitignore'
    - This file tells GIt to ignore whatever files you tell it to by using git add ..
    
    Examples:
    - .DS_Store -> macOS system file that clutters repos
    - __pycache__/ and *.pyc -> Python's compiled bytecode (not needed in Git)
    - venv/ -> Virtual environment, can be reuilt later using requiremnts.txt

    These files don't belong in GIt because: They're automatically generated by my system or python, they make the repo unnecessarily large, and the differ from computer to computer
3. Reason why so many files appeared:
    - venv/ folder and system cache files were already commited before adding the .gitignore, therfore, Git was still tracking them.
4. Cleanup Process
    - In order for Git to forget everything it is tracking and then only re-track what's allowed by .gitignore:
    
git rm -r --cached .
git add .
git commit -m "Clean up ignored files"

    - git rm -r --cached .
        removes all tracked files from Git's index but keeps them safe on my disk.
    - git add .
        adds everything back except the files listed in .gitignore
    - git commit -m "Clean up ignored files"
        Saves this cleaned up state to my repo history.
* Some Take-aways:
    1. Always create a .gitignore first.
    2. Typical .gitignore setup:
(# macOS system files
.DS_Store

(# Python cache
__pycache__/
*.pyc

(# Virtual environment
venv/

(# Logs or temporary files
*.log
*.tmp

    3. Check 'changes' in GitHub Desktop before commiting and use the cleanup trick if I forget
    4. Keep the repo lean
        - Only Track files that define the project - code, data, and documentation. Anything that can be regenerated (logs, cache, venvs) should never be committed.



### 10-19-2025 — DataCamp: Dictionaries Part 2 + Markdown formating

-Keys are "immutable" (can't be changed). Strings, floats, booleans, int. Lists are mutable.
- Using a list as akey will give you an error.

List: 
    - Select, update, and remove with []
    - Indexed by range of numbers
    - Collection of values, order matters, for selecting entire subsets
Dictionary:
    - Select, update, and remove with []
    - Indexed by unique keys
    - Lookup tables with unique keys

- Add new values to a dictionary with dict['x'] = y  
- Delete and item in a dict. with del(dict['x']) 
- Created code snippet : /Users/ginomontero/Documents/GitHub/Biophoton-data-lab/Biophoton-data-science/code_snippets/2025-10-19_Python_Dictonaries_cont.py

#### Understanding how the Markdown (.md) format works
(#) Defines the heading level
(#) - Main title (Biggest)
(##) - Section title
(###) - Subsection
(####) - smaller subheading
(- or *) at the beginning of a line create a bullet point 
**bold** bold - emphasize key terms (**bold** )
_italic_ italic - highlight minor points (_italic_)
'code' code - show inline code ('code')
> Quote or note - Quote/emphasixe text (>)
--- Horizontal line - Seperate sections (---)



### 10-20-2025 — Python Dictionary practice

- Learned from chatGPT about .get()
    - Hase two arguments -> .get(key, default_value)
    - key -> The key I want to look up in the dictionary.
    - default_value -> The value that .get() returns if the key does not exist.
    - If I dont add a value for the 2nd argument then it returns none.
- .items() loops throught each item in the dictionary and its readings dictionary.
-readings.get() looks for the object specified in the .get()
-"f-strings" in python are formatted string literals. They allow you to embed a variable directly into a string
Example: 
name = "Marigold"
count = 120

print(f"{name} Day1 photon count: {count}")

-without the f, {name} and {count} will be returned instead of Marigold and 120, respectively.
- Created practice code: [2025-10-20_dictionaries_practice.py](/Users/ginomontero/Documents/GitHub/Biophoton-data-lab/Biophoton-data-science/code_snippets/2025-10-20_Python_dictionaries_practice.py)

#### Linked Reading
[High-Resolution Imaging of Plant Delayed Luminescence](../reading_notes/2025-10-20_High-Resolution_Imaging_of_Plant_Delayed_Luminescence.md
)

