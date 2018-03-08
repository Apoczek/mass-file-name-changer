#Program which rename every file in directory according to pattern:
#<new_name>[i].ext
#new_name - core of the new name
#[i] - another number
#.ext - given type of file


import os

i = 1
new_name = 'notka'
file_type = '.txt'
for file in os.listdir('.'):
    if file.endswith('.txt'):
        os.rename(file, new_name + str(i) + file_type)
        print(file + ' --> ' + new_name + str(i) + file_type)
        i += 1
