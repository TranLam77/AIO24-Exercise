# -*- coding: utf-8 -*-
"""ExerciseM1W2_II.3.count_word.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n8CU7hex7L6aGIKO9DjA85FGjDsa9qV5
"""

#Cau hoi trac nghiem - Cau hoi 3
! gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

def count_word(file_path):
    counter = {}

    # Your Code Here
    # read file
    with open(file_path,'r') as file:
        data = file.read()
        file.close()
    # remove new line character
    data = data.split('\n')
    # count words, line by line
    for line in data:
        for word in line.split(' '):
            if counter.get(word.lower()) is None:
                counter[word.lower()] = 1
            else:
                counter[word.lower()] += 1
    counter = dict(sorted(counter.items()))
    # End Code Here

    return counter

file_path = '/content/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print (result['man'])

# Đáp án là a) ’s’: 2, ’m’: 1, ’i’: 1, ’l’: 1, ’e’: 1