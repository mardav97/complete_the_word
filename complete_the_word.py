import pandas as pd
import re
import os
import numpy as np
import sys

dictionary_path = 'F:\\My python study\\pycharm program\\My_Project\\jupyter\\words_alpha.txt'
# dictionary_path is the path for the word_alpha.csv
ser = pd.read_csv(dictionary_path, header=None)[0]


# input_string = input('Enter the word(with space separated form): ').lower()
input_string = sys.argv[1].lower()
checker = input_string.replace(' ', 'a')
while not checker.isalpha():
    print(f'Cannot process given word {input_string}')
    print("Please use space separated word i.e. : 'h llo'")
    input_string = input('Enter the word(with space separated form): ').lower()
    checker = input_string.replace(' ', 'a')

if input_string.isspace():
    pattern = '^.{' + str(len(input_string)) + '}' + input_string.strip().replace(' ', '.') + '$'
else:
    start_space = len(input_string) - len(input_string.lstrip())
    end_space = len(input_string) - len(input_string.rstrip())
    pattern = '^.{' + str(start_space) + '}' + input_string.strip().replace(' ', '.') + '.{' + str(end_space) + '}$'

result = ser.apply(lambda x: x if len(re.findall(pattern, str(x))) >= 1 else np.NaN).dropna().copy()
result_li = list(result.values)
if len(result_li) > 10:
    print('Result has more than 10 words do you wish to write the result in a text file? YES or NO?')
    answer = input().lower()
    while answer != 'yes' and answer != 'no':
        print("Please answer 'YES' or 'NO'")
        answer = input().lower()
    if answer == 'yes':
        text_file_path = "F:\\My python study\\pycharm program\\MY_Project\\jupyter\\resultfile.txt"
        # text_file_path this is the path for the text in which the result is being saved
        with open(text_file_path, 'w+') as file:
            list(map(lambda x: file.write(x + '\n'), result_li))
        os.system(f"notepad.exe {text_file_path}")
    else:
        print(result_li)
else:
    print(result_li)
