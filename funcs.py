cart = []
manager_access_data = ["manager", "password"]
customer_money = 15000
promo_code = "123"

Laptops = [
    {"title": "HP",
     "price": "20000"},
    {"title": "Acer",
     "price": "10000"},
    {"title": "Lenovo",
     "price": "15000"}
]

Desktops = [
    {"title": "HP",
     "price": "20000"},
    {"title": "Acer",
     "price": "10000"},
    {"title": "Lenovo",
     "price": "15000"}
]

Telephones = [
    {"title": "iPhone",
     "price": "20000"},
    {"title": "Samsung",
     "price": "10000"},
    {"title": "Nokia",
     "price": "15000"}
]

Tablets = [
    {"title": "Lenovo",
     "price": "20000"},
    {"title": "Samsung",
     "price": "10000"},
    {"title": "iPad",
     "price": "15000"}
]


def quit_or_continue():
    choice = input("Type 1 to continue or 2 to quit: ")
    if choice == "1":
        customer_choice()
    elif choice == "2":
        print("Have a nice day!")
    else:
        print("You've typed something strange, buddy. Please try again")
        quit_or_continue()


def manager_quit_or_continue():
    choice = input("Type 1 to continue or 2 to quit: ")
    if choice == "1":
        manager_panel()
    elif choice == "2":
        print("Have a nice day!")
    else:
        print("You've typed something strange, buddy. Please try again")
        manager_quit_or_continue()


def buy_product():
    category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
    if category_choice == "1":
        category = Laptops
    elif category_choice == "2":
        category = Desktops
    elif category_choice == "3":
        category = Telephones
    elif category_choice == "4":
        category = Tablets
    else:
        print("Sorry, wrong number. Please try again")
        buy_product()
    product = input("Please type the product you want to buy: ")
    n = 0
    while n < len(category):
        if category[n]["title"] == product:
            cart.append(product)
            cart.append(category[n]["price"])
            if int(category[n]["price"]) > customer_money:
                print("Sorry, you don't have enough money to buy this product")
                quit_or_continue()
            elif int(category[n]["price"]) <= customer_money:
                promo = input("Enter the promo code if you have it or enter N: ")
                promo = promo.lower()
                if promo == "n":
                    print("Please pay", category[n]["price"])
                    quit_or_continue()
                elif promo == promo_code:
                    new_price = int(category[n]["price"]) * 0.9
                    print("Please pay", new_price)
                    quit_or_continue()
                else:
                    print("Please pay", category[n]["price"])
                    quit_or_continue()
        n = n + 1


def display_category(category):
    n = 0
    while n < len(category):
        print(category[n]["title"] + ": " + category[n]["price"])
        n = n + 1
    choice = input("Do you want to buy something? Y or N: ")
    choice = choice.lower()
    if choice == "y":
        buy_product()
    elif choice == "n":
        choice_2 = input("Type 1 to continue or 2 to quit: ")
        if choice_2 == "1":
            customer_choice()
        elif choice_2 == "2":
            print("Have a nice day!")
        else:
            print("You've typed something strange, buddy. Please try again")
            customer_choice()
    else:
        print("You've typed something strange, buddy. Please try again")
        customer_choice()


def customer_choice():
    choice = input("Please type 1 if you want to see the products and 2 if you want to buy a product: ")
    if choice == "1":
        category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
        if category_choice == "1":
            display_category(Laptops)
        elif category_choice == "2":
            display_category(Desktops)
        elif category_choice == "3":
            display_category(Telephones)
        elif category_choice == "4":
            display_category(Tablets)
        else:
            print("You've typed something strange, buddy. Please try again")
            customer_choice()
    elif choice == "2":
        buy_product()
    else:
        print("You've typed something strange, buddy. Please try again")
        customer_choice()


def add(category):
    title = input("Please enter the product title: ")
    price = input("Please enter the product price: ")
    category.append({"title": title, "price": price})
    manager_quit_or_continue()


def add_product():
    category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
    if category_choice == "1":
        add(Laptops)
    elif category_choice == "2":
        add(Desktops)
    elif category_choice == "3":
        add(Telephones)
    elif category_choice == "4":
        add(Tablets)
    else:
        print("You've typed something strange, buddy. Please try again")
        add_product()


def delete(category):
    title = input("Please enter the product title: ")
    price = input("Please enter the product price: ")
    category.remove({"title": title, "price": price})
    manager_quit_or_continue()


def delete_product():
    category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
    if category_choice == "1":
        delete(Laptops)
    elif category_choice == "2":
        delete(Desktops)
    elif category_choice == "3":
        delete(Telephones)
    elif category_choice == "4":
        delete(Tablets)
    else:
        print("You've typed something strange, buddy. Please try again")
        delete_product()


def edit(category):
    title = input("Please enter the product title: ")
    price = input("Please enter the product price: ")
    new_price = input("Please enter the new product price: ")
    category.remove({"title": title, "price": price})
    category.append({"title": title, "price": new_price})
    manager_quit_or_continue()


def edit_product():
    category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
    if category_choice == "1":
        edit(Laptops)
    elif category_choice == "2":
        edit(Desktops)
    elif category_choice == "3":
        edit(Telephones)
    elif category_choice == "4":
        edit(Tablets)
    else:
        print("You've typed something strange, buddy. Please try again")
        edit_product()


def manager_panel():
    choice = input("Type 1 to add a product, 2 to delete a product, 3 to edit a product, and 4 to see products: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        delete_product()
    elif choice == "3":
        edit_product()
    elif choice == "4":
        category_choice = input("Please type 1 for Laptops, 2 for Desktops, 3 for Telephones, and 4 for Tablets: ")
        if category_choice == "1":
            display_category(Laptops)
        elif category_choice == "2":
            display_category(Desktops)
        elif category_choice == "3":
            display_category(Telephones)
        elif category_choice == "4":
            display_category(Tablets)
    else:
        print("You've typed something strange, buddy. Please try again")
        manager_panel()


def manager_access():
    login = input("PLease enter your login: ")
    if login == manager_access_data[0]:
        password = input("Please enter your password: ")
        if password == manager_access_data[1]:
            manager_panel()
        else:
            print("Incorrect password. Please try again")
            manager_access()
    else:
        print("Incorrect login. Please try again")
        manager_access()

