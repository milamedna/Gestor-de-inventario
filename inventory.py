
"""
Inventory Manager - Fase 3

Author: Camila Medina

Algorithm
Inputs: how many products to register, name/price/quantity for each one, and later the product name and quantity for every entry or sale the user wants to register
Outputs: the current inventory (with percentage of participation of each product) and confirmation messages for every entry/sale
Process:
The program first asks how many products the user wants to manage, then for each one asks for its name, price and quantity, storing every product as a dictionary (name, price,
quantity) inside a list called "inventario". A second structure, "history", is a matrix that keeps a record of every entry/sale registered, where each row is [type of movement, product name, quantity].
The user then interacts with a menu to show the inventory, register an entry or a sale by typing the product's name, or exit. Because every product dictionary is stored by reference inside
"inventory", every entry/sale updates the real data, so the inventory shown is always
up to date.
"""


# This function calculates the amount of money a certain quantity of a product represents
def value_price(price, quantity):
    """
    Inputs: price and quantity of the product
    Outputs: value of price multiplied by quantity
    Process: multiplies price by quantity and returns the result
    """
    return price * quantity


# This function calculates the total value of the whole inventory
def total_value_inventory(inventory):
    """
    Inputs: the inventory that is a list of dictionaries, each one of them with name,price and quantity
    Outputs: the sum of the value of every product
    Process: goes through every product in the list, calculates its value with the function value_price and adds it to a counter with the total
    """
    total = 0
    for product in inventory:
        total += value_price(product["price"], product["quantity"])
    return total


# This function updates the quantity of a product after a stock entry
def register_stock_entry(currentQuantity, incomingQuantity):
    """
    Inputs: current quantity of a product, quantity that is entering
    Outputs: new quantity after the entry
    Process: sums both quantities and returns the result
    """
    return currentQuantity + incomingQuantity


# This function updates the quantity of a product after a sale
def register_sale(currentQuantity, outgoingQuantity):
    """
    Inputs: current quantity of a product, quantity that is leaving
    Outputs: new quantity after the sale
    Process: restss the outgoing quantity from the current quantity and returns it
    """
    return currentQuantity - outgoingQuantity


# This function asks for a number and validates it until it is 0 or positive
def ask_valid_value(message):
    """
    Inputs: the value the user enters
    Outputs: a float number that is not negative
    Process: asks for a number and while its negative keeps asking again
    """
    value = float(input(message))
    while value < 0:
        print("The value cant be negative, try again.")
        value = float(input(message))
    return value


# This function asks for a product name to verify that is not empty and that is not already registered
def ask_valid_name(message, inventory):
    """
    Inputs: the product the user enters, the current inventory
    Outputs: a product name that is not empty and does not already exist in inventario
    Process: asks for a name and, while it is empty or already exists, keeps asking again
    """
    name = input(message).strip()
    while name == "" or search_product(inventory, name) != "the product does not exist":
        if name == "":
            print("The name cannot be empty, try again.")
        else:
            print("That product already exists, try again.")
        name = input(message).strip()
    return name


# This function looks for a product by name inside the inventory (the matrix)
def search_product(inventory, name):
    """
    Inputs: the inventory that is a list of dictionaries, the name to search
    Outputs: the index where the product is found, or "the product does not exist" if it does not exist
    Process: goes through the list comparing names until it finds a match
    """
    i = 0
    while i < len(inventory):
        if inventory[i]["name"] == name:
            return i
        i += 1
    return "the product does not exist"


# This function adds one row to the movements history matrix
def register_movement(history, typeE, name, quantity):
    """
    Inputs: the history matrix, the type of movement ("Entry"/"Sale"), the product name and the quantity moved
    Outputs: none, appends a new row [type, name, quantity] to the history matrix
    Process: builds a row with the three values and appends it to historial
    """
    row= [typeE, name, quantity]
    history.append(row)


def show_menu():
    print("1. Show inventory")
    print("2. Register stock entry")
    print("3. Register sale")
    print("4. Exit")


# This function prints the current state of the inventory with the percentage of each product in the inventory
def show_inventory(inventory):
    """
    Inputs: the inventory (list of dictionaries)
    Outputs: none, prints every product and the percentage of the total value it represents
    Process: calculates the total value once, then goes through every product printing
    its data and its percentage of participation
    """
    total = total_value_inventory(inventory)
    print("Your actual inventory is: ")
    for product in inventory:
        name= product["name"]
        price = product["price"]
        quantity = product["quantity"]
        value = value_price(price, quantity)
        percentage = (value * 100) / total
        print(name, "=", quantity, "items,", price, "$ each -", f"{percentage:.2f}", "% of the inventory")
    print("Your total inventory value is:", f"{total:.2f}", "$")


def main():
    print("Welcome! Let's register your inventory.")
    inventory = []
    history = []

    number_products = int(ask_valid_value("How many products do you want to register? "))
    while number_products <= 0:
        print("You need to register at least 1 product.")
        number_products = int(ask_valid_value("How many products do you want to register? "))

    counter = 1
    while counter <= number_products:
        print("Product ", counter)
        name = ask_valid_name("Enter the name of the product: ", inventory)
        price = ask_valid_value("Enter the unit price of the product: ")
        quantity = int(ask_valid_value("Enter the quantity of the product: "))
        product = {"name": name, "price": price, "quantity": quantity}
        inventory.append(product)
        counter += 1

    show_inventory(inventory)

    continuar = True
    while continuar:
        show_menu()
        opcion = int(input("What do you want to do? "))

        match opcion:
            case 1:
                show_inventory(inventory)

            case 2:
                search_name = input("What product do you want to register an entry for? ")
                indice = search_product(inventory, search_name)
                if indice == "the product does not exist":
                    print("That product does not exist in your inventory.")
                else:
                    enter_quantity = int(ask_valid_value("How many items are entering? "))
                    inventory[indice]["quantity"] = register_stock_entry(inventory[indice]["quantity"], enter_quantity)
                    register_movement(history, "Entry", search_name, enter_quantity)
                    print("Entry registered. New quantity of", search_name, "is", inventory[indice]["quantity"])

            case 3:
                search_name = input("What product do you want to register a sale for? ")
                indice = search_product(inventory, search_name)
                if indice == "the product does not exist":
                    print("That product does not exist in your inventory.")
                else:
                    out_quantity = int(ask_valid_value("How many items are getting out? "))
                    if out_quantity > inventory[indice]["quantity"]:
                        print("You don't have enough stock for that sale.")
                    else:
                        inventory[indice]["quantity"] = register_sale(inventory[indice]["quantity"], out_quantity)
                        register_movement(history, "Sale", search_name, out_quantity)
                        print("Sale registered. New quantity of", search_name, "is", inventory[indice]["quantity"])

            case 4:
                continuar = False
                print("Goodbye!")

            case _:
                print("Invalid option, try again.")


main()
