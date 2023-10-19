def mailcheck(mail):
    character1 = "@"
    character2 = "."

    for element in character1 and character2:
        if element in mail:
            print("This is a valid e-mail address.")
        else:
            print("This e-mail address is not valid.")
mailcheck(input("Enter your e-mail address:"))
