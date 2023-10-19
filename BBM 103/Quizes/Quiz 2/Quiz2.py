import sys


def healthStatus(height, weight):
    bmi = weight/height**2

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# This part was written to solve possible errors that may emerge
try:
    basketball_score = int(sys.argv[1])*2 + int(sys.argv[2])*3 + int(sys.argv[3])
    print(basketball_score)
except IndexError:
    print("Please enter three integers")
except ValueError:
    print("Please enter three integers")
# Özge Bülbül 2220765008

