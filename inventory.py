
"""
Inventory Manager

Author: Camila Medina

Algorithm
Inputs: price, quantity, product, entrys, sales
Outputs: final inventory
Process:
The program asks the user to enter at least 3 products and to enter the name, price and quantity for each product. The program stores each product as value1, value2, value3. Then he program calls the function total_value_ inventory to calculate the total inventory and it stores the result in a variable called stock
and prints it, then it asks the user for their entrys and stores it in stock, also their sales and it stores it again in stock. Prints to the user their final inventory after their entrys and sales and the program ends

"""


# This function is going to be used to calculate the amount of money a ceirtan quantity of a product represents
def value_price(price,quantity):
    """
    Inputs: price and quantity of the product
    Outputs: value of price multiplied by quantity
    Process: With the values of price and quantity of the product, calculates the amount of money it represents by price*quantity, it return the value
    """
    return price*quantity

#This function means to calculate the initial inventory summing up the values of the products introduced by the user 
def total_value_inventory(value1, value2, value3):
    """
    Inputs: value of each product introduced by the user
    Outputs: sum of values
    Process: sums the three values and stores it, returns the value of the sum
    """
    total= value1+value2+value3
    return total

#This function means to update the value of the inventory by adding up the entrys of the user
def register_stock_entry (initials, plusvalue):
    """
    Inputs: initial stock, amount of entering money 
    Outputs: Sum of new stock
    Process: With the initial stock, sums this value with the new amount of money that is entering, returns this new value
    """
    newinventory= (initials+plusvalue)
    return newinventory

#This function means to update the value of the inventory by resting the sales of the user 
def register_sale (initial, minusvalue):
    """
    Inputs: initial stock, amount of outing money
    Outputs: Value of new stock
    Process: With the initial stock, calculates the initial stock minus the amount of money that is going out, returns the new value of the stock.
    """
    newinventory2= (initial-minusvalue)
    return newinventory2

def main():
    print("Enter at least 3 products: ")
    product1= str(input("Enter the name of the product: "))
    price1= float(input("Enter the unit price of the product: "))
    quantity1= int(input("Enter the quantity of the product: "))
    value1= value_price(price1,quantity1)
    
    Product2= str(input("Enter the name of the product: "))
    price2= float(input("Enter the unit price of the product: "))
    quantity2= int(input("Enter the quantity of the product: "))
    value2= value_price(price2,quantity2)
    
    Product3= str(input("Enter the name of the product: "))
    price3= float(input("Enter the unit price of the product: "))
    quantity3= int(input("Enter the quantity of the product: "))
    value3= value_price(price3,quantity3)
    
    stock= total_value_inventory(value1,value2,value3)
    print ("Your initial stock is: ",stock)
    entrys=int(input("Enter your stock entrys: "))
    stock= register_stock_entry(stock,entrys)
    sales= int(input("Enter your sales: "))
    stock= register_sale(stock,sales)
    print ("Your final inventory is: ",stock)
main()
# This function means to test the possible outcomes of the program
def tests():
    print("Functions tests")
    print("Function value_price: ")
    print("Obtained: ",value_price(10.0,5),"Expected: 50.0")
    
    print("Function total_value_inventory")
    print("Obtained: ",total_value_inventory(10,20,30),"Expected: 60")
    
    print("Function register_stock_entry")
    print("Obtained: ",register_stock_entry(100,50),"Expected: 150")
    
    print("Function register_sale")
    print("Obtained: ",register_sale(150,20),"Expected: 130")
tests()
    
    
    