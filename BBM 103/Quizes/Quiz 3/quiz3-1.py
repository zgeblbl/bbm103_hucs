# Özge Bülbül 2220765008
import sys


x = int(sys.argv[1])
n = int(sys.argv[2])
total = 0
tot = 0
condition = True
a = str(x**n)
digits = [int(i) for i in str(a)]
sum_string = [str(f) for f in digits]
if len(digits) > 1:
    for j in digits:
        total = j + total
    if len(str(total)) > 1:
        while condition:
            total1 = [int(k) for k in str(total)]
            for y in total1:
                tot = tot + y
            if len(str(tot)) > 1:
                condition = True
            else:
                condition = False
        sum_string1 = [str(g) for g in total1]
        print(x, "^", n, "=", x ** n, "=", ' + '.join(sum_string), "=", total, "=", ' + '.join(sum_string1), "=", tot)
    else:
        print(x, "^", n, "=", x**n, "=", ' + '.join(sum_string), "=", total)
else:
    print(x, "^", n, "=", x**n)
