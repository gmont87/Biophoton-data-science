# This is is how to do what I was trying to do in in yesterdays code (/Users/ginomontero/Documents/GitHub/Biophoton-data-lab/Biophoton-data-science/code_snippets/2025-10-18_Python_Dictionaries)
# I wanted to make a dictionary in which i could call on the genus, species, and common name seperatley. Here's how to do it:

# Dictionary of animal identifications
genus = {'canis':{'species':'lupis', 'common name':'wolf'},
         'lynx':{'species':'rufus', 'common name':'bobcat'},
         'pseudacris':{'species':'crucifer','common name':'spring peeper'} }

# Print out the common name of canis
print(genus['canis']['common name'])

# Create sub-dictionary anthro
anthro = {'species': 'sapien', 'common name': 'human'}

# Add anthro to genus under key 'homo' and print genus
genus['homo'] = anthro
print(genus)