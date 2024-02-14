################################
# Author: Keidy Lopez
# Filename: problem #8.py
# Description: program that determines whether one qualifies for loans
################################

def main():

    # variables and inputs
    val1 = input("Are you employed (Y/N)? ")
    val2 = input("Have you graduated from college in the past two years (Y/N)? ")

    # if statements that determines whether one qualifies
    if val2.upper() and val1.upper() == "Y":
        print("Yes. You qualify for the special interest rate!")
    else:
        print("No. You do not qualify for the special interest rate.")




if __name__=="__main__":
    main()
