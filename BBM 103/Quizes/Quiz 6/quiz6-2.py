# Özge Bülbül 2220765008
import sys


def diamond_maker(number):
    lines = [" " * abs(number - i - 1) + "*" * (2 * (number - abs(number - i - 1)) - 1) for i in range(2 * number - 1)]
    for line in lines:
        print(line)


diamond_maker(int(sys.argv[1]))
