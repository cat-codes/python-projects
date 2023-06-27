inventory_list = []

store = {
    "dress": 39.99,
    "t-shirt": 15.89,
    "jeans": 29.79,
    "shoes": 50.69,
    "hat": 9.59,
    "hoodie": 19.49,
    "skirt": 25.39,
    "shorts": 18.29,
    "sandals": 17.19
}

print("Welcome to online clothing store.")


def menu():
    print("\nWhat would you like to do?")
    print("\n\t(B)rowse store.")
    print("\t(A)dd a new product.")
    print("\t(E)dit product's quantity.")
    print("\t(R)emove a product.")
    print("\t(V)iew cart.")
    print("\t(Q)uit.")

    action = input("\nI would like to... ").lower()

    if action == "b":
        browse_store()

    if action == "a":
        add_product(inventory_list)

    if action == "e":
        edit_product(inventory_list)

    elif action == "r":
        remove_product(inventory_list)

    elif action == "v":
        view_cart(inventory_list)

    elif action == "q":
        print("Thank you for shopping!")
        quit()

    # else:
    #     print("Error")


# open menu
def open_menu():
    yes = "y"
    answer = input("\nBack to menu? (Y/N). ").lower()
    if answer == yes:
        menu()
    else:
        quit()


# browse store
def browse_store():
    print("\nThe store offers these items: ")
    import pprint
    pprint.pprint(store)


# add product
def add_product(inventory_list):
    name = input("Add the name of the item: ")
    quantity = int(input("Add the quantity of the item: "))
    price = (store[name]) * quantity
    item = {"name": name, "quantity": quantity, "price": price}
    inventory_list.append(item)
    print("\nThe item was successfully added to the cart.")
    print("---------------------")
    print("Name: ", name)
    print("Quantity: ", quantity)
    print("Price: ", price)
    print("---------------------")


# edit product
def edit_product(inventory_list):
    e_product = input("Choose which product to edit: ")
    new_quantity = int(input("Enter new quantity of the product: "))

    for product in inventory_list:
        if product["name"] == e_product:
            product["price"] = product["price"] / product["quantity"] * new_quantity
            product["quantity"] = new_quantity
    print("\nQuantity of the product", e_product, "was successfully updated.")
    print("\nUpdated product in cart: ")
    print("---------------------")
    print("Name: ", e_product)
    print("Quantity: ", new_quantity)
    print("Price: ", product["price"])
    print("---------------------")


# remove product
def remove_product(inventory_list):
    r_product = input("Choose which product to remove: ")
    for product in inventory_list:
        if product["name"] == r_product:
            inventory_list.remove(product)
            print("\nProduct", r_product, "was removed from the cart.")


# view cart
def view_cart(inventory_list):
    print("\nInventory list: ")
    print("---------------------")
    if not inventory_list:
        print("No products in inventory.")
        print("---------------------")
    else:
        total = 0
        for product in inventory_list:
            print("Name: ", product["name"])
            print("Quantity: ", product["quantity"])
            print("Price: ", product["price"])
            print("---------------------")
            total += float(product["price"])
        print()
        print("Total price: ", total)


# calling functions
menu()

while True:
    open_menu()
