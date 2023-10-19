def element_finder():
    my_list = [-45, 100, 200, 298, 900, 1000, 3579]
    n = int(input("Which element do you want to find? \n"))
    if n > 7:
        print("Please enter a number between 1 and 7")
    else:
        print(my_list[n-1])


element_finder()
