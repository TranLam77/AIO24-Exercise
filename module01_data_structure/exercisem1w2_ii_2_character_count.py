# -*- coding: utf-8 -*-
"""ExerciseM1W2_II.2.character_count.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IuxhL2m7ZI9OsakSuNMASzObQz41R5-G
"""

#Cau hoi trac nghiem - Cau hoi 2
def character_count(word) :
    character_statistic = {}

    # Your Code Here
    for char in word:
        if character_statistic.get(char) is None:
            character_statistic[char] = 1
        else:
            character_statistic[char] += 1
    # End Code Here

    return character_statistic

assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print (character_count('smiles'))

# Đáp án là a) ’s’: 2, ’m’: 1, ’i’: 1, ’l’: 1, ’e’: 1