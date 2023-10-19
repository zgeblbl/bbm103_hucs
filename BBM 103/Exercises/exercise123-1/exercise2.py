numberDeci = int(input("Enter the number you want to convert:"))
string= ""

while(numberDeci != 1):
    if(numberDeci%2 != 0):
        numberDeci = int(numberDeci / 2)
        string = "1" + string

    else:
        numberDeci=int(numberDeci/2)
        string="0"+string

string="1"+string
print(string)
