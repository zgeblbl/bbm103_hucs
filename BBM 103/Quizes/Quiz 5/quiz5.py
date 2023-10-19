import sys
try:
    try:
        with open(sys.argv[1], "r") as operands:
            rows = operands.readlines()
    except IOError:
        print("IOError: cannot open {}\n˜ Game Over ˜".format(sys.argv[1]))
        quit()
    try:
        with open(sys.argv[2], "r") as comparison:
            lines1 = comparison.readlines()
    except IOError:
        print("IOError: cannot open {}\n˜ Game Over ˜".format(sys.argv[2]))
        quit()
except IndexError:
    print("IndexError: number of input files less than expected.\n˜ Game Over ˜")
    quit()
mylist = []
counter = -1
lines = []
for element in rows:
    line = element.split()
    lines.append(line)


def rounder(num):  # We weren't allowed to use round function, so I defined this.
    if float(num) - int(float(num)) < 5:
        return int(float(num))
    else:
        return int(float(num)) + 1


class MissingLineError(Exception):  # If there are missing lines in comparison_data.txt, custom exception defined.
    pass


class MissingOperandError(Exception):  # If there are missing lines in operands.txt, custom exception defined.
    pass


try:
    for line in lines:
        print("------------")
        counter = counter + 1
        try:
            if len(lines1) < counter + 1:
                raise MissingLineError
            for i in range(rounder(line[2]), rounder(line[3]) + 1):
                if i % rounder(line[0]) == 0 and i % rounder(line[1]) != 0:
                    mylist.append(str(i))
            print("My results:\t\t", *mylist, "\nResults to compare:\t {}".format(lines1[counter].strip('\n')))
            compare_list = lines1[counter].split()
            assert mylist == compare_list
            print("Goool!!!")
            mylist.clear()
        except MissingLineError:
            print("MissingLineError: There is nothing to compare!\nGiven input:", *line)
            mylist.clear()
        except ZeroDivisionError:
            print("ZeroDivisionError: You can’t divide by 0.\nGiven input:", *line)
        except IndexError:
            print("IndexError: number of operands less than expected.\nGiven input:", *line)
        except AssertionError:
            print("AssertionError: results don’t match.")
            mylist.clear()
        except ValueError:
            print("ValueError: only numeric input is accepted.\nGiven input:", *line)
        except Exception:
            print("kaBOOM: run for your life!")
finally:
    try:
        if counter + 1 == len(lines) and counter + 1 < len(lines1):
            raise MissingOperandError
    except MissingOperandError:
        print("------------\nMissingOperandError: There is more to compare but nothing to operate!")
        mylist.clear()
    print("\n˜ Game Over ˜")
