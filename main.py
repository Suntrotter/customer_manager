from funcs import *

def main():
    choice = input("Please type 1 if you are a customer or 2 if you are a manager: ")
    if choice == "1":
        customer_choice()
    elif choice == "2":
        manager_access()
    else:
        print("You've typed something strange, buddy. Please try again")
        main()


if __name__ == '__main__':
    main()

