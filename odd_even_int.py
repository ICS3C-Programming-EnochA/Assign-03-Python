# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program checks if the integer is either odd or even number


def main():
    print("Hello and welcome to Enoch's math program")
    # Enter any number
    user_number = input("Enter any number: ")
    try:
        user_number = int(user_number)
    # if the user_number is divisible by two and gives a zero it's an even number
        if user_number % 2 == 0:
            print("This number is an even number.")

        else:
            # if the user_number is divisible by three and gives you a zero it's an odd number
            print("This number is an odd number.")

    except:
        # if user_number is not a number the below code will display it is not a number
        print("This is not a number")

    finally:
        # Thank you for playing
        print("Thank you and have a nice day")


if __name__ == "__main__":
    main()
