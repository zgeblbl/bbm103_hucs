# Student Name: Özge Bülbül
# Student ID: 2220765008

# os module is imported to get the current directories for reading and writing the files.
import os
# sys module is imported to get the input file as an argument.
import sys


current_dir_path = os.getcwd()
reading_file_name = sys.argv[1]
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = "output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
categories = []  # Holds record of the categories so that the same category is not created again.
ticket_list = []  # The main list that holds the football fan's name, ticket type, category and seat numbers.
check_list = []  # Created for bugfix in the sell() function.
ticket_type = []  # Holds the ticket types of sold seats for the balance() function.
cat_seats = {}  # Holds the category name and its column and row numbers such as 'category-1A': '15x15'.


# This is the function that (when called) writes the outputs to the output file.
def write(output):
    with open(writing_file_path, 'a') as f:
        f.write(output)


# This is the function that creates the categories with the requested layouts.
def create_cat(x):
    row = x.split()
    seats = row[2].split('x')
    seats_num = int(seats[0])*int(seats[1])  # Number of seats is calculated by multiplying row and column numbers.
    for cat in categories:
        if row[1] in cat:
            write("Warning: Cannot create the category for the second time. The stadium has already {}\n"
                  .format(row[1]))
            return
    categories.append(row[1])
    cat_seats[row[1]] = row[2]
    write("The category '{}' having {} seats has been created\n".format(row[1], seats_num))


# This is the function that sells the free and existing seats to the football fans.
def sell(y):
    row = y.split()
    seat_list = row[4:]
    mult = cat_seats[row[3]].split('x')
    # Row and column numbers are separated to use while examining if the requested seat exists.
    row_number = int(mult[0])
    column_number = int(mult[1])
    for s in seat_list:
        if '-' in s:  # This is for separately handling the ranged seats because they have '-' in them.
            # Getting the row letter to add to the seat number and compare it to the category's row number later on.
            let = s[0]
            s_split = s[1:].split('-')
            s_range = [x for x in range((int(s_split[0])), (int(s_split[1]) + 1))]
            s_range = [let + str(x) for x in s_range]
            if int(s_split[1]) > column_number and (ord(let) - 64) > row_number:
                write("Error: The category '{}' has less row and column than the specified index {}!\n"
                      .format(row[3], s))
            elif int(s_split[1]) > column_number:
                write("Error: The category '{}' has less column than the specified index {}!\n".format(row[3], s))
            elif (ord(let) - 64) > row_number:
                write("Error: The category '{}' has less row than the specified index {}!\n".format(row[3], s))
            else:
                if len(ticket_list) == 0:
                    list3 = list(row[1:4])
                    list3.append(s_range)
                    ticket_list.append(list3)
                    write("Success: {} has bought {} at {}\n".format(row[1], s, row[3]))
                else:
                    for data in ticket_list:
                        if any(item in s_range for item in data) and row[3] == data[2]:
                            check_list.append('true')
                    if 'true' in check_list:
                        write("Warning: The seats {} cannot be sold to {} due some of them have already been sold\n"
                              .format(s, row[1]))
                    for data in ticket_list:
                        if len(check_list) != 0:
                            check_list.clear()
                            break
                        else:
                            write("Success: {} has bought {} at {}\n".format(row[1], s, row[3]))
                            if row[1] == data[0]:
                                data.extend(s_range)
                            else:
                                list4 = list(row[1:4])
                                list4.extend(s_range)
                                ticket_list.append(list4)
                                break
        else:
            s_number = int(s[1:])
            let = s[0]
            if s_number > column_number and (ord(let) - 64) > row_number:
                write("Error: The category '{}' has less row and column than the specified index {}!\n"
                      .format(row[3], s))
            elif s_number > column_number:
                write("Error: The category '{}' has less column than the specified index {}!\n".format(row[3], s))
            elif (ord(let) - 64) > row_number:
                write("Error: The category '{}' has less row than the specified index {}!\n".format(row[3], s))
            else:
                if len(ticket_list) == 0:
                    list1 = list(row[1:4])
                    list1.append(s)
                    ticket_list.append(list1)
                    write("Success: {} has bought {} at {}\n".format(row[1], s, row[3]))
                else:
                    for data in ticket_list:
                        if row[3] == data[2] and s in data:
                            write("Warning: The seats {} cannot be sold to {} due some of them have already been sold\n"
                                  .format(s, row[1]))
                        elif row[1] == data[0]:
                            data.append(s)
                            write("Success: {} has bought {} at {}\n".format(row[1], s, row[3]))
                        else:
                            list2 = list(row[1:4])
                            list2.append(s)
                            ticket_list.append(list2)
                            write("Success: {} has bought {} at {}\n".format(row[1], s, row[3]))
                            break


def cancel(z):
    row = z.split()
    let = row[2][0]  # The letter of the seat that will be cancelled.
    number = int(row[2][1:])  # The number of the seat that will be cancelled.
    mult = cat_seats[row[1]].split('x')
    row_number = int(mult[0])
    column_number = int(mult[1])
    if (ord(let) - 64) > row_number and number > column_number:
        write("Error: The category '{}' has less row and column than the specified index {}!\n".format(row[1], row[2]))
    elif (ord(let) - 64) > row_number:
        write("Error: The category '{}' has less row than the specified index {}!\n".format(row[1], row[2]))
    elif number > column_number:
        write("Error: The category '{}' has less column than the specified index {}!\n".format(row[1], row[2]))
    else:
        for element in ticket_list:
            if row[1] == element[2] and row[2] in element:
                element.remove(row[2])
                write("Success: The seat {} at '{}' has been canceled and now ready to sell again\n"
                      .format(row[2], row[1]))
                return
        write("Error: The seat {} at '{}' has already been free! Nothing to cancel\n".format(row[2], row[1]))


def balance(t):
    row = t.split()
    for element in ticket_list:
        if row[1] == element[2]:
            num_of_tickets = len(element[3:])
            ticket_type.extend([element[1]] * num_of_tickets)
    student = ticket_type.count('student')
    full = ticket_type.count('full')
    season = ticket_type.count('season')
    revenue = student * 10 + full * 20 + season * 250
    hyphen = '-'
    while len(hyphen) != len("category report of '" + str(row[1]) + "'"):
        hyphen += '-'
    write("category report of '{}'\n{}\n"
          "Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars\n"
          .format(row[1], hyphen, student, full, season, revenue))
    ticket_type.clear()


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
letter = {}
check = False


def show(k):
    global check
    row = k.split()
    write("Printing category layout of {}\n\n".format(row[1]))
    mult = cat_seats[row[1]].split('x')
    layout_list = []  # The list that holds ticket type and the seat like "FB3".
    for data in ticket_list:
        if data[2] == row[1]:
            if data[1] == 'student':
                layout_list.extend('S' + str(x) for x in data[3:])
            if data[1] == 'full':
                layout_list.extend('F' + str(x) for x in data[3:])
            if data[1] == 'season':
                layout_list.extend('T' + str(x) for x in data[3:])
    for i in range(int(mult[0])):
        x = alphabet[i]
        letter[i] = x
    for k in reversed(range(int(mult[0]))):
        write(letter[k])
        for j in range(int(mult[1])):
            if layout_list is not None:
                for element in layout_list:
                    ticket_kind = element[0]
                    let = element[1]
                    num = int(element[2:])
                    # If the column & row numbers are the same, write the ticket type.
                    if j == num and k == ord(let) - 65:
                        write(" " + str(ticket_kind) + " ")
                        check = True
                        break
                if not check:
                    write(" X ")
                else:
                    check = False
            else:
                write(" X ")
        write("\n")
    # Puts two spaces if the number has one character and one space if it has more than one character.
    for i in range(int(mult[1])):
        if i < 10:
            write("  " + str(i))
        else:
            write(" " + str(i))
    write("\n")


# This part reads the input file and calls the necessary functions.
with open(reading_file_path, 'r') as reading:
    for n in reading:
        if n.startswith("CREATECATEGORY "):
            create_cat(n)
        if n.startswith("SELLTICKET "):
            sell(n)
        if n.startswith("CANCELTICKET "):
            cancel(n)
        if n.startswith("BALANCE "):
            balance(n)
        if n.startswith("SHOWCATEGORY "):
            show(n)
