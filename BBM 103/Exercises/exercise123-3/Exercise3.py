n = 4


def hanoi_solver(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    hanoi_solver(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    hanoi_solver(n-1, auxiliary, destination, source)


hanoi_solver(n, 'A', 'B', 'C')
