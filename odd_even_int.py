# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program checks if the integer is either odd or even number


def main():

    user_number = input("Enter any number: ")
    try:
        user_number = int(user_number)
        if user_number % 2 == 0:
            print("This number is an even number.")

        else:
            print("This number is an odd number.")

    except:
        print("This is not a number")

    finally:
        print("Thank you and have a nice day")


if __name__ == "__main__":
    main()
