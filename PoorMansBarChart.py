"""

Python script that takes a sentence (string) as input and returns a simple bar chart–type display

"""


from pprint import *
from collections import defaultdict

#Getting sentence from user
text = input("Enter a sentence: ").lower()


all_letters = []
a_dict =defaultdict(list)

#banned characters
forbidden_characters = ['" "', "' '", "'", '.', "!", "?", ' ']

#analyse every letter in the users input
for letter in text:
    #skipping forbidden characters so thei're not appended in the list
    if letter in forbidden_characters:
        pass
    #appending every other character
    else:
        all_letters.append(letter)

        a_dict[letter].append(letter)


pprint(a_dict)