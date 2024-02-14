################################
# Author: Keidy Lopez
# Filename: problem #2.py
# Description: generates a random number and determines whether it is between 75 and 100 or not
################################
import random

def main():

    # generates a random number and assigns that number a variable
    number = random.randint(1, 200)
    random1 = number

    # determines whether or not number is between 75 and 100 and diplays the answer
    if number > 75 and number < 100:
        print(random1, "is between 75 and 100 :D")
    else:
        print(random1, "is not between 75 and 100 :(")








if __name__ == "__main__":
    main()