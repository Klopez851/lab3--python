################################
# Author: Keidy Lopez
# Filename: problem #5.py
# Description: BMI calculator
################################


def main():
    weight = float(input("What is your weight(lb)? "))
    height = float(input("What is your height(in)? "))
    BMI = calcBMI(weight, height)

    if BMI > 25.0:
        print(BMI, "BMI is above the healthy range")
    elif BMI < 19.0:
        print(BMI, "BMI is below the healthy range")
    elif 19.0 < BMI < 25.0:
        print(BMI, "BMI is within the healthy range")


def calcBMI(W, H):
    ans = (W * 720 / H**2)
    return ans


if __name__ == "__main__":
    main()