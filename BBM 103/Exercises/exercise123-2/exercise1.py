n = int(input("Write a number N:"))

odd = 0

for i in range(1, n + 1, 2):
    odd = odd + i
print("sum of odds:", odd)

even = (sum(i for i in range(n+1) if (i % 2 == 0))) / int(n/2)
print("average of evens:", even)
