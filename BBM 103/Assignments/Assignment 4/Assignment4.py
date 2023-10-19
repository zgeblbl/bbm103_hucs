# Özge Bülbül 2220765008
# import sys
import sys
import os
current_dir_path = os.getcwd()
reading_player1_ship = "OptionalPlayer1.txt"
reading_file_path1 = os.path.join(current_dir_path, reading_player1_ship)
reading_player2_ship = "OptionalPlayer2.txt"
reading_file_path2 = os.path.join(current_dir_path, reading_player2_ship)
writing_file_name = "Battleship.out"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
moves_p1 = []
moves_p2 = []
p1_ships = []
p2_ships = []
bp_positions_p1 = []
bp_positions_p2 = []
game = "on"


def write(output):
    print(output, end='')
    with open(writing_file_path, 'a') as f:
        f.write(output)


for i in range(1, 5):
    try:
        if i == 1:
            with open(sys.argv[i], 'r') as file:
                for n in file:
                    line5 = n.strip("\n")
                    line5 = line5.split(";")
                    p1_ships.append(line5)
        if i == 2:
            with open(sys.argv[i], 'r') as file:
                for n in file:
                    line5 = n.strip("\n")
                    line5 = line5.split(";")
                    p2_ships.append(line5)
        if i == 3:
            with open(sys.argv[i], 'r') as file:
                for n in file:
                    lines = n[:-1]
                    moves_p1.extend(lines.split(";"))
        if i == 4:
            with open(sys.argv[i], 'r') as file:
                for n in file:
                    lines = n[:-1]
                    moves_p2.extend(lines.split(";"))

    except IOError:
        write("IOError: input file(s) {} is/are not reachable.".format(sys.argv[i]))


with open(reading_file_path1, 'r') as reading:
    for n in reading:
        line1 = n.strip(";\n")
        line1 = line1.replace(":", ";")
        bp_positions_p1.append(line1.split(";"))
with open(reading_file_path2, 'r') as reading2:
    for n in reading2:
        line2 = n.strip(";\n")
        line2 = line2.replace(":", ";")
        bp_positions_p2.append(line2.split(";"))

first_ships = []
second_ships = []
column_counter = 0
row_counter = 0
for line in p1_ships:
    row_counter += 1
    for cell in line:
        column_counter += 1
        if cell == "C" or cell == "S" or cell == "D":
            var = cell + "," + str(row_counter) + chr(column_counter + 64)
            first_ships.append(var)
    column_counter = 0
row_counter = 0
for line in p2_ships:
    row_counter += 1
    for cell in line:
        column_counter += 1
        if cell == "C" or cell == "S" or cell == "D":
            var = cell + "," + str(row_counter) + chr(column_counter + 64)
            second_ships.append(var)
    column_counter = 0
for ship in bp_positions_p1:
    ship_type = ship[0]
    start_point = ship[1].split(",")
    letter = start_point[1]
    num = start_point[0]
    if ship[2] == 'down':
        if ship_type[0] == 'B':
            first_ships.extend([ship_type + "," + str(x) + letter for x in range(int(num), int(num) + 4)])
        elif ship_type[0] == 'P':
            first_ships.extend([ship_type + "," + str(x) + letter for x in range(int(num), int(num) + 2)])
    elif ship[2] == 'right':
        if ship_type[0] == 'B':
            first_ships.extend([ship_type + "," + num + chr(x + 64) for x in range(ord(letter) - 64, ord(letter) - 60)])
        elif ship_type[0] == 'P':
            first_ships.extend([ship_type + "," + num + chr(x + 64) for x in range(ord(letter) - 64, ord(letter) - 62)])
for ship in bp_positions_p2:
    ship_type = ship[0]
    start_point = ship[1].split(",")
    letter = start_point[1]
    num = start_point[0]
    if ship[2] == 'down':
        if ship_type[0] == 'B':
            second_ships.extend([ship_type + "," + str(x) + letter for x in range(int(num), int(num) + 4)])
        elif ship_type[0] == 'P':
            second_ships.extend([ship_type + "," + str(x) + letter for x in range(int(num), int(num) + 2)])
    elif ship[2] == 'right':
        if ship_type[0] == 'B':
            second_ships.extend([ship_type + "," + num + chr(x + 64) for x in range(ord(letter) - 64, ord(letter) - 60)])
        elif ship_type[0] == 'P':
            second_ships.extend([ship_type + "," + num + chr(x + 64) for x in range(ord(letter) - 64, ord(letter) - 62)])


def move_checker(x):
    for move in x:
        try:
            if len(move) < 3:
                raise IndexError
            if type(int(move[:-2])) != int or type(move[-1]) != str:
                raise ValueError
            if int(move[:-2]) > 10 or ord(move[-1]) > 74:
                raise AssertionError
        except IndexError:
            write("IndexError: Move value {} is insufficient.\n".format(move))
            moves_p1.remove(move)
        except ValueError:
            write("ValueError: Move value {} is invalid.\n".format(move))
            moves_p1.remove(move)
        except AssertionError:
            write("AssertionError: Move value {} is not possible.\n".format(move))
            moves_p1.remove(move)


move_checker(moves_p1)
move_checker(moves_p2)
sunk1 = []
sunk2 = []
c = "-"
sub = "-"
d = "-"
p = " - - - -"
b = "- -"
c2 = "-"
sub2 = "-"
d2 = "-"
p_2 = " - - - -"
b_2 = "- -"


def sunk_ship_checker():
    c_counter = 0
    s_counter = 0
    d_counter = 0
    general_p_counter = 0
    general_b_counter = 0
    b1_counter = 0
    b2_counter = 0
    p1_counter = 0
    p2_counter = 0
    p3_counter = 0
    p4_counter = 0
    for element in sunk1:
        element1 = element.split(",")
        type_ship = element1[0]
        if type_ship == "C":
            c_counter += 1
        if type_ship == "S":
            s_counter += 1
        if type_ship == "D":
            d_counter += 1
        if type_ship == "B1":
            b1_counter += 1
        if type_ship == "B2":
            b2_counter += 1
        if type_ship == "P1":
            p1_counter += 1
        if type_ship == "P2":
            p2_counter += 1
        if type_ship == "P3":
            p3_counter += 1
        if type_ship == "P4":
            p4_counter += 1
    if c_counter == 5:
        global c
        c = "X"
    if s_counter == 3:
        global sub
        sub = "X"
    if d_counter == 3:
        global d
        d = "X"
    if p1_counter == 2:
        general_p_counter += 1
    if p2_counter == 2:
        general_p_counter += 1
    if p3_counter == 2:
        general_p_counter += 1
    if p4_counter == 2:
        general_p_counter += 1
    if general_p_counter == 4:
        global p
        p = " X X X X"
    elif general_p_counter == 3:
        p = " X X X -"
    elif general_p_counter == 2:
        p = " X X - -"
    elif general_p_counter == 1:
        p = " X - - -"
    if b1_counter == 4:
        general_b_counter += 1
    if b2_counter == 4:
        general_b_counter += 1
    if general_b_counter == 2:
        global b
        b = "X X"
    elif general_b_counter == 1:
        b = "X -"
    c_counter2 = 0
    s_counter2 = 0
    d_counter2 = 0
    b1_counter2 = 0
    b2_counter2 = 0
    p1_counter2 = 0
    p2_counter2 = 0
    p3_counter2 = 0
    p4_counter2 = 0
    general_p_counter2 = 0
    general_b_counter2 = 0
    for element in sunk2:
        element1 = element.split(",")
        type_ship = element1[0]
        if type_ship == "C":
            c_counter2 += 1
        if type_ship == "S":
            s_counter2 += 1
        if type_ship == "D":
            d_counter2 += 1
        if type_ship == "B1":
            b1_counter2 += 1
        if type_ship == "B2":
            b2_counter2 += 1
        if type_ship == "P1":
            p1_counter2 += 1
        if type_ship == "P2":
            p2_counter2 += 1
        if type_ship == "P3":
            p3_counter2 += 1
        if type_ship == "P4":
            p4_counter2 += 1
    if c_counter2 == 5:
        global c2
        c2 = "X"
    if s_counter2 == 3:
        global sub2
        sub2 = "X"
    if d_counter2 == 3:
        global d2
        d2 = "X"
    if p1_counter2 == 2:
        general_p_counter2 += 1
    if p2_counter2 == 2:
        general_p_counter2 += 1
    if p3_counter2 == 2:
        general_p_counter2 += 1
    if p4_counter2 == 2:
        general_p_counter2 += 1
    if general_p_counter2 == 4:
        global p_2
        p_2 = " X X X X"
    elif general_p_counter2 == 3:
        p_2 = " X X X -"
    elif general_p_counter2 == 2:
        p_2 = " X X - -"
    elif general_p_counter2 == 1:
        p_2 = " X - - -"
    if b1_counter2 == 4:
        general_b_counter2 += 1
    if b2_counter2 == 4:
        general_b_counter2 += 1
    if general_b_counter2 == 2:
        global b_2
        b_2 = "X X"
    elif general_b_counter2 == 1:
        b_2 = "X -"


check = False


def hidden_board():
    sunk_ship_checker()
    global game
    global check
    if c == "X" and sub == "X" and d == "X" and p == " X X X X" and b == "X X" and c2 == "X" and sub2 == "X" and d2 == "X" and p_2 == " X X X X" and b_2 == "X X" and not check:
        write("It is a Draw!\n\nFinal Information\n\n")
        check = True
        game = "over"
        return
    if c == "X" and sub == "X" and d == "X" and p == " X X X X" and b == "X X" and not check:
        write("Player2 Wins!\n\nFinal Information\n\n")
        check = True
        game = "over"
        return
    if c2 == "X" and sub2 == "X" and d2 == "X" and p_2 == " X X X X" and b_2 == "X X" and not check:
        write("Player1 Wins!\n\nFinal Information\n\n")
        check = True
        game = "over"
        return
    write("Player1's Hidden Board\t\tPlayer2's Hidden Board\n  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
    check = False
    if tarantino:
        a = round_num
        if round_num == len(moves_p1) + 1:
            move = moves_p2[round_num - 2]
        else:
            move = moves_p2[round_num - 1]
    else:
        a = round_num - 1
        if round_num == len(moves_p1) + 1:
            move = moves_p2[round_num - 2]
        else:
            move = moves_p2[round_num - 1]
    for row in range(10):
        write(str(row + 1))
        for column in range(10):
            x = False
            for number in range(round_num - 1):
                let = moves_p2[number][-1]
                num1 = moves_p2[number][:-2]
                if row == 9 and column + 1 == ord(let) - 64 and row + 1 == int(num1):
                    for s in first_ships:
                        s1 = s.split(",")
                        position = s1[1]
                        if position[-1] == let and position[:-1] == num1:
                            check = True
                            if s not in sunk1:
                                sunk1.append(s)
                    if check:
                        write("X ")
                        x = True
                        check = False
                    else:
                        write("O ")
                        x = True
                elif column + 1 == ord(let) - 64 and row + 1 == int(num1):
                    for s in first_ships:
                        if s[-1] == let and s[-2] == num1:
                            check = True
                            if s not in sunk1:
                                sunk1.append(s)
                    if check:
                        write(" X")
                        x = True
                        check = False
                    else:
                        write(" O")
                        x = True
            if row == 9 and not x:
                write("- ")
            elif not x:
                write(" -")
        write("\t\t")
        write(str(row + 1))
        for column in range(10):
            y = False
            for number in range(a):
                let2 = moves_p1[number][-1]
                num2 = moves_p1[number][:-2]
                if row == 9 and column + 1 == ord(let2) - 64 and row + 1 == int(num2):
                    for s in second_ships:
                        s1 = s.split(",")
                        position = s1[1]
                        if position[-1] == let2 and position[:-1] == num2:
                            check = True
                            if s not in sunk2:
                                sunk2.append(s)
                    if check:
                        write("X ")
                        y = True
                        check = False
                    else:
                        write("O ")
                        y = True
                elif column + 1 == ord(let2) - 64 and row + 1 == int(num2):
                    for s in second_ships:
                        if s[-1] == let2 and s[-2] == num2:
                            check = True
                            if s not in sunk2:
                                sunk2.append(s)
                    if check:
                        write(" X")
                        y = True
                        check = False
                    else:
                        write(" O")
                        y = True
            if row == 9 and not y:
                write("- ")
            elif not y:
                write(" -")
        write("\n")
    write("\nCarrier\t\t{}\t\t\t\tCarrier\t\t{}\nBattleship\t{}\t\t\t\tBattleship\t{}\nDestroyer\t{}\t\t\t\t"
          "Destroyer\t{}\nSubmarine\t{}\t\t\t\tSubmarine\t{}\nPatrol Boat{}\t\t\tPatrol Boat{}\n\n"
          .format(c, c2, b, b_2, d, d2, sub, sub2, p, p_2))
    if game != "over":
        write("Enter your move: {}\n\n".format(move))


write("Battle of Ships Game\n\n")
for round_num in range(1, len(moves_p1) + 2):
    if game != "over":
        write("Player1's Move\n\nRound : {}\t\t\t\t\tGrid Size: 10x10\n\n".format(round_num))
        tarantino = False
        hidden_board()
        tarantino = True
        write("Player2's Move\n\nRound : {}\t\t\t\t\tGrid Size: 10x10\n\n".format(round_num))
        hidden_board()
if game == "over":
    check = True
    round_num = len(moves_p1)
    hidden_board()

