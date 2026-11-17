
"""
Inventory Manager

Author: Camila Medina

Algorithm
Inputs: the menu option chosen, product name, unit price and quantity when a product is added, product name and quantity for every stock entry or sale
Outputs: inventory reports, total value, low stock alerts, and the files catalog.txt and sales_history.txt
Process:
When the program starts it makes sure catalog.txt and sales_history.txt exist, and creates them empty if they do not. The catalog is loaded into the list "inventory", where each line becomes a dictionary
(name, price, quantity). The user then picks options from the menu. Every time the inventory changes, catalog.txt is rewritten so nothing is lost. Every entry or sale is added at the end of
sales_history.txt as soon as it happens. Choosing "Save and exit" closes the program.
"""


CATALOG_FILE = "catalog.txt"
SALES_HISTORY_FILE = "sales_history.txt"
LOW_STOCK_LIMIT = 5


#This function verifies if a file already exists, if not, creates it and leaves it empty.
def ensure_file_exists(filename):
    """
    Inputs: the name of the file the program needs
    Outputs: none, the file exists afterwards and its current content is not changed
    Process: opens the file with append, which creates it if it is missing and keeps any content it already has, then closes it
    """
    with open(filename, "a", encoding= "utf-8") as file:
        file.write("")
        
def load_catalog(filename):
    """
    Inputs: filename, the file with the  matrix inventory with each product as a line 
    Outputs: the inventory
    Process: reads every line of the matrix, splits it by commas, converts price and quantity to numbers and adds each product dictionary to the list
    """
    inventory= []
    with open(filename, "r", encoding= "utf_8") as file:
        for line in file:
            line= line.strip()
            if line != "":
                product_name, product_price, product_quantity = line.split(",")
                product = {
                    "name": product_name,
                    "price": float(product_price),
                    "quantity": int(product_quantity),
                }
                inventory.append(product)
    return inventory

#This function writes the inventory into the file
def save_catalog(filename, inventory):
    """
    Inputs: Receives the name of the file and the inventory with the dictionaries.
    Outputs: None, the file gets filled with the inventory dictionaries
    Process: opens the file with write and writes each product as a line
    
    """
    with open(filename, "w", encoding="utf-8") as file:
        for product in inventory:
            product_line = f"{product['name']},{product['price']},{product['quantity']}\n"
            file.write(product_line)
            
# This function adds one movement at the end of the sales history file
def append_movement(filename, movement_type, name, quantity):
    """
    Inputs: filename, the history file, the movement type ("Entry" or "Sale"), the product name and the quantity
    Outputs: none, one line type,name,quantity is added at the end of the history file
    Process: opens the file with append and writes the new movement 
    """
    with open(filename, "a", encoding="utf-8") as file:
        movement_line = f"{movement_type},{name},{quantity}\n"
        file.write(movement_line)
    

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
    Outputs: a product name that is not empty and does not already exist in inventory
    Process: asks for a name and, while it is empty or already exists, keeps asking again
    """
    name = input(message).strip()
    while name == "" or "," in name or search_product(inventory, name) != "the product does not exist":
        if name == "":
            print("The name cannot be empty, try again.")
        elif "," in name:
            print("The name cannot contain commas, try again.")
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

#This function adds a new product to the inventory and saves the catalog
def add_new_product(inventory):
    """
    Inputs: the inventory, a list of dictionaries
    Outputs: none, the new product is appended to the inventory and the catalog file is updated
    Process: asks for a valid name, price and quantity, appends the product dictionary to the list
             and rewrites the catalog file
    """
    product_name = ask_valid_name("Enter the name of the new product: ", inventory)
    product_price = ask_valid_value("Enter the unit price of the product: ")
    product_quantity = int(ask_valid_value("Enter the quantity of the product: "))
    new_product = {"name": product_name, "price": product_price, "quantity": product_quantity}
    inventory.append(new_product)
    save_catalog(CATALOG_FILE, inventory)
    print("Product", product_name, "was added to the inventory.")
    
    
def register_stock_entry_for_product(inventory):
    """
    Inputs: the inventory that is a list of dictionaries
    Outputs: none, the product quantity increases, the catalog is rewritten and the movement is added to the history file
    Process: finds the product by name, asks for the incoming quantity, updates the quantity,saves the catalog and appends the movement to the sales history
    """
    product_name = input("What product do you want to register an entry for? ").strip()
    product_index = search_product(inventory, product_name)
    if product_index == "the product does not exist":
        print("That product does not exist in your inventory.")
    else:
        incoming_quantity = int(ask_valid_value("How many items are entering? "))
        current_quantity = inventory[product_index]["quantity"]
        inventory[product_index]["quantity"] = register_stock_entry(current_quantity, incoming_quantity)
        save_catalog(CATALOG_FILE, inventory)
        append_movement(SALES_HISTORY_FILE, "Entry", product_name, incoming_quantity)
        print("Entry registered. New quantity of", product_name, "is", inventory[product_index]["quantity"])
        
        
# This function registers a sale for an existing product and saves the changes
def register_sale_for_product(inventory):
    """
    Inputs: the inventory that is a list of dictionaries
    Outputs: none, the product quantity decreases, the catalog is rewritten and the movement is added to the history file
    Process: finds the product by name, asks for the outgoing quantity, checks there is enough stock,
             updates the quantity, saves the catalog and appends the movement to the sales history
    """
    product_name = input("What product do you want to register a sale for? ").strip()
    product_index = search_product(inventory, product_name)
    if product_index == "the product does not exist":
        print("That product does not exist in your inventory.")
    else:
        outgoing_quantity = int(ask_valid_value("How many items are getting out? "))
        current_quantity = inventory[product_index]["quantity"]
        if outgoing_quantity > current_quantity:
            print("You don't have enough stock for that sale.")
        else:
            inventory[product_index]["quantity"] = register_sale(current_quantity, outgoing_quantity)
            save_catalog(CATALOG_FILE, inventory)
            append_movement(SALES_HISTORY_FILE, "Sale", product_name, outgoing_quantity)
            print("Sale registered. New quantity of", product_name, "is", inventory[product_index]["quantity"])


#This function searches for a product by name and shows its information
def search_for_product(inventory):
    """
    Inputs: the inventory, a list of dictionaries
    Outputs: none, the product information is printed or an error message is shown
    Process: asks for a name, searches it in the inventory and prints its quantity, price and value
    """
    product_name = input("Which product do you want to search for? ").strip()
    product_index = search_product(inventory, product_name)
    if product_index == "the product does not exist":
        print("That product does not exist in your inventory.")
    else:
        product = inventory[product_index]
        product_value = value_price(product["price"], product["quantity"])
        print(product["name"], "has", product["quantity"], "items,", product["price"], "$ each, value:", f"{product_value:.2f}", "$")


    
# This function prints the current state of the inventory with the percentage of each product in the inventory
def show_inventory(inventory):
    """
    Inputs: the inventory, the list of dictionaries
    Outputs: none, prints every product and the percentage of the total value it represents
    Process: calculates the total value once, then goes through every product printing
    its data and its percentage of participation in the inventory
    """
    total = total_value_inventory(inventory)
    print("Your actual inventory is: ")
    for product in inventory:
        product_value = value_price(product["price"], product["quantity"])
        if total == 0:
            percentage = 0
        else:
            percentage = (product_value * 100) / total
        print(product["name"], "=", product["quantity"], "items,", product["price"], "$ each -", f"{percentage:.2f}", "% of the inventory")

# This function prints the total value of the inventory
def show_total_value(inventory):
    """
    Inputs: the inventory, a list of dictionaries
    Outputs: none, the total value is printed on the screen
    Process: calculates the total value with total_value_inventory and prints it with two decimals
    """
    total = total_value_inventory(inventory)
    print("Your total inventory value is:", f"{total:.2f}", "$")
    

# This function prints an alert for every product whose quantity is at or below the low stock limit
def show_low_stock_alerts(inventory):
    """
    Inputs: the inventory, a list of dictionaries
    Outputs: none, one alert line per low stock product is printed
    Process: goes through every product and prints an alert when its quantity is at or below LOW_STOCK_LIMIT
    """
    alerts_found = 0
    for product in inventory:
        if product["quantity"] <= LOW_STOCK_LIMIT:
            print("LOW STOCK:", product["name"], "has only", product["quantity"], "items left")
            alerts_found += 1
    if alerts_found == 0:
        print("No products are low on stock.")


def show_menu():
    """
    Inputs: none
    Outputs: none, the menu options are printed on the screen
    Process: prints each of the eight options.
    """
    print("1. Add new product")
    print("2. Register stock entry")
    print("3. Register sale")
    print("4. Search product")
    print("5. Show inventory")
    print("6. Show total inventory value")
    print("7. Show low stock alerts")
    print("8. Save and exit")


def main():
    print("Welcome! Let's register your inventory.")

    ensure_file_exists(CATALOG_FILE)
    inventory = load_catalog(CATALOG_FILE)

    ensure_file_exists(SALES_HISTORY_FILE)

    continuee = True
    while continuee:
        show_menu()
        option = int(input("What do you want to do? "))

        match option:
            case 1:
                add_new_product(inventory)
            case 2:
                register_stock_entry_for_product(inventory)
            case 3:
                register_sale_for_product(inventory)
            case 4:
                search_for_product(inventory)
            case 5:
                show_inventory(inventory)
            case 6:
                show_total_value(inventory)
            case 7:
                show_low_stock_alerts(inventory)
            case 8:
                continuee = False
                print("Your data was saved. Goodbye!")
            case _:
                print("Invalid option, try again.")

main()
