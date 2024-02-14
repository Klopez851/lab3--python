################################
# Author: Keidy lopez
# file name: problem #1.py
# Purpose: to determine whether int input is even or odd
################################

def main():
    # takes number given by user
    num1 = int(input("Enter a whole number: "))

    # divides number given by user
    div = num1 % 2

    # determines and displays whether input is even or odd
    if div == 1:
        print("that's an odd number!")
    else:
        print("that's an even number!")

if __name__ == "__main__":
    main()