import os
import sys
current_dir_path = os.getcwd()
reading_file_name = "Students.txt"
reading_file_path = os.path.join(current_dir_path, reading_file_name)
name_list = []
dict1 = {}
lines = []
counter = 0
with open(reading_file_path, 'r') as reading:
    for n in reading:
        n_string = str(n).replace(":", ",")
        lines.append(n_string.split(','))
names = sys.argv[2:]
for n in names:
    if "," in n:
        names = n.split(',')


class NoNameError(Exception):
    pass


for name in names:
    try:
        for i in lines:
            counter = counter + 1
            if str(i[0].strip("'")) == str(name):
                my_string = ','.join([str(element) for element in i[1:]])
                dict1 = {"Name:": name, "University:": my_string}
                print(','.join('%s%s' % (k, dict1[k]) for k in dict1.keys()))
                counter = 0
                break
            elif counter == len(names):
                counter = 0
                raise NoNameError
    except NoNameError:
        print("No record of {} was found!\n".format(name))
