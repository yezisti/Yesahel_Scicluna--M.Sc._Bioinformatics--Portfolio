'''
assemble.py - assembles overlapping fragments of strings

Author: Yesahel Scicluna (assisted by ChatGPT)

Source: Arthur M. Lesk, Introduction to Bioinformatics. Chapter 1. Problem 1.5
- Task Description: see assemble.md

Required Files: fragments.txt
'''

# locates text file containing the overlapping fragments
text = open('C:\\Users\\yesah\\Documents\\fragments.txt')    # amend filepath as necessary

# reads and stores fragments line by line
fragments = [line.strip() for line in text]

'''
This program exploits two fragment relationships in performing fragment reassembly. It detects:

(1) Which fragment shares the longest suffix with the prefix of another fragment
    - Reveals which fragment should follow the other

(2) Which fragment shares no prefix with the suffix of any another fragment
    - Reveals which fragment is the first in sequence
'''

# sets default dict. value of each fragment to 'noprefixfound'
prefix = {fragment: 'noprefixfound' for fragment in fragments}

# initiliases dict. obj. in which to store predecessor:successor pairs
successor = {}

# loop over fragments
for i in fragments:

    # initialises longest suffix to null
    longestsuffix = ""

    # loops over fragment pairs
    for j in fragments:

        # prevents checking against self
        if i != j:
            
            # concatenates fragments with fence XXX
            combine = i + 'XXX' + j

            import re

            # checks for repeated sequences of characters (ie an overlap)
            match = re.search(r'([\S ]{2,})XXX\1', combine)

            # evaluates True if an overlap is found and
            #                if it is the longest overlap yet recorded
            if match and len(match.group(1)) > len(longestsuffix):

                # records overlapping suffix
                longestsuffix = match.group(1)

                # records that j follows i
                successor[i] = j

    # evaluates True if a successor has been recorded for fragment i
    if i in successor:

        # records 'prefixfound' for i's successor
        # overwrites default value of 'noprefixfound'
        prefix[successor[i]] = 'prefixfound'

# finds fragment that retains default value 'noprefixfound'
# starts fragment assembly with this fragment in first position
outstring = next(fragment for fragment in fragments if prefix[fragment] == 'noprefixfound')

# feeds 'noprefixfound' fragment into the following loop
nextstring = outstring

# loops over each fragment in sequence
while nextstring in successor:

    # selects current fragment's successor 
    nextstring = successor[nextstring]  

    # appends successor after the current fragment
    outstring += 'XXX' + nextstring

    # removes overlapping segment from assembly
    outstring = re.sub(r'([\S ]+)XXX\1', r'\1', outstring)

# changes '\\n' in assembly to actual newline char.
outstring = outstring.replace('\\n', '\n')  

# prints final assembly
print(outstring)  