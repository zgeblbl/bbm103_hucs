b = int(input("b="))
c = int(input("c="))
delta = (b**2-4*c)
root1 = (-b+delta**0.5)/2
root2 = (-b-delta**0.5)/2
if delta < 0:
    print("There are no real roots.")
else:
    print("First Root:", root1, "\n Second Root:", root2)
