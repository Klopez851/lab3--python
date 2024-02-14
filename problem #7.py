################################
# Author: Keidy Lopez
# Filename: problem #7.py
# Description: program that gives back amount of money fined for speeding
################################

def main():
    # speed and clocked speed inputs and variables
    speed = int(input("What is the speed limit? "))
    clocked = int(input("What is the clocked speed limit? "))

    # determines which function to use to calculate fine and prints out the specifics of the calculations
    if clocked <= speed:
        print("\tSpeed limit: " + str(speed) + "MPH")
        print("\tClocked speed limit: " + str(clocked)+ "MPH")
        print("\t\tLegal speed, no fining needed.")
    elif speed < clocked < 90:
        print("\tSpeed limit: " + str(speed) + "MPH")
        print("\tClocked speed limit: " + str(clocked) + "MPH")
        print("\t\tSpeed is over the legal limit!")
        print("\t\tYou have been fined: $" + str(fineLessThanNinety(clocked, speed)))
    else:
        print("\tSpeed limit: " + str(speed) + "MPH")
        print("\tClocked speed limit: " + str(clocked) + "MPH")
        print("\t\tSpeed is over the legal limit!")
        print("\t\tYou have been fined: $" + str(fineMoreThanNinety(clocked, speed)))

# calculated fine if clocked speed is less than 90
def fineLessThanNinety (A, B):
        fine_total = (((A - B)* 5) + 50)
        round(fine_total, 2)
        return float(fine_total)

# calculated fine if clocked speed is more than 90
def fineMoreThanNinety (A, B):
        fine_total = ((((A - B)* 5) + 50) + 200)
        round(fine_total, 2)
        return float(fine_total)


if __name__=="__main__":
    main()