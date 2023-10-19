# Özge Bülbül 2220765008
import sys
counter1 = 0
counter2 = 0


def pyramid(number):
    if number >= 1:
        global counter2
        print(" " * number, "*" * (2 * counter2 - 1))
        counter2 += 1
        return pyramid(number - 1)


def reverse_pyramid(number):
    if number >= 1:
        global counter1
        print(" " * counter1, "*" * (2 * number - 1))
        counter1 += 1
        return reverse_pyramid(number - 1)


pyramid(int(sys.argv[1]))
reverse_pyramid(int(sys.argv[1]))
