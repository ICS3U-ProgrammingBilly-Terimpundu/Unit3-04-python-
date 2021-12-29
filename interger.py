# Created by Billy Terimpundu
# Created on December 2021
# This program gets the user to enter an integer
# between -10 and 10 and tells them if it's positive, negative or 0.

def main():
    user_number = int(input("Enter your number: "))

    if user_number > 10:
        print("Number is big")
        quit()

    elif user_number < -10:
        print("number is small")
        quit()

    elif user_number > 0:
        print("Number is positive.")

    elif user_number < 0:
        print("Number is negative")

    else:
        print("Number is zero")


if __name__ == "__main__":
    main()