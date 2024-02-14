################################
# Author:  Keidy Lopez
# File name: problem #3.py
# Description: takes a Celcius temp and converts it to Fahrenheit
################################

def main():

    # takes number from user and assigns it a value
    c = float(input("What temperature would you like to convert? "))
    convertion = CtoF(c)
    round(convertion, 1)

    # determines whether number is between 32 and 80, more than 80 or less than 32 and displays answer
    if convertion <= 80 and convertion >= 32:
        print(c ,"°C is", convertion, "°F")
    elif convertion > 32:
        print(c, "°C is", convertion, "°F, that's really hot!")
    elif convertion < 80:
        print(c, "°C is", convertion, "°F, that's really cold!")

# takes input from user and converts it into °F
def CtoF(X):
    f = ((1.8 * X) + 32)
    return f

if __name__ == "__main__":
    main()