
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
    Process: With the values of price and quantity of the product, calculates the amount of money it represents by price*quantity, it returns the value
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

def menu():
    print ("1. Show inventory")
    print ("2. Register stock entry")
    print ("3. Register sale")
    print ("4. Exit")


def main():
    """
The operations are with the initial inventory, the inventory doesn´t change with each sale or entering
"""
    print("Welcome! Enter 3 products: ")
    counter= 1
    while counter<=3:
        product= str(input("Enter the name of the product: "))
        price= float(input("Enter the unit price of the product: "))
        quantity= int(input("Enter the quantity of the product: "))
        value= value_price(price,quantity)
        
        if counter==1:
            product1=product
            price1=price
            quantity1=quantity
            value1= value
            
        elif counter==2:
            product2=product
            price2=price
            quantity2=quantity
            value2= value
            
        elif counter==3:
            product3=product
            price3=price
            quantity3=quantity
            value3= value
        counter += 1
    continuar = True   
    while continuar==True:
        menu()
        option= int(input("What do you want to do? (Enter the number) "))
        if option==1:
            print ("Your actual inventory is: ")
            print (product1,"=",quantity1,"items",price1,"$")
            print (product2,"=",quantity2,"items",price2,"$")
            print (product3,"=",quantity3,"items",price3,"$")
            print ("Your total inventory is:",(total_value_inventory(value1,value2,value3)),"$")
            per1= value1*100/(total_value_inventory(value1,value2,value3))
            per2= value2*100/(total_value_inventory(value1,value2,value3))
            per3= value3*100/(total_value_inventory(value1,value2,value3))
            print (product1,"represents the",(f"{per1:.2f}"),"% of your total inventory")
            print (product2,"represents the",(f"{per2:.2f}"),"% of your total inventory")
            print (product3,"represents the",(f"{per3:.2f}"),"% of your total inventory")
        elif option==2:
            res=str(input("What item do you want register? "))
            if res==product1:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are entering?"))
                enter= items*(value1/quantity1)
                print("Now your inventory is:",register_stock_entry(initialstock, enter))
            elif res==product2:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are entering?"))
                enter= items*(value2/quantity2)
                print("Now your inventory is:",register_stock_entry(initialstock, enter))
            elif res==product3:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are entering?"))
                enter= items*(value3/quantity3)
                print ("Now your inventory is:",register_stock_entry(initialstock, enter))
        elif option==3:
            res=str(input("What item do you want register? "))
            if res==product1:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are getting out?"))
                enter= items*(value1/quantity1)
                print("Now your inventory is:",register_sale(initialstock, enter))
            elif res==product2:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are getting out?"))
                enter= items*(value2/quantity2)
                print("Now your inventory is:",register_sale(initialstock, enter))
            elif res==product3:
                initialstock= total_value_inventory(value1,value2,value3)
                items= int(input("How many items are getting out?"))
                enter= items*(value3/quantity3)
                print ("Now your inventory is:",register_sale(initialstock, enter))
        elif option==4:
            print ("Goodbye!")
        
        res= str(input("Do you want to go back to the initial menu?(y/n)"))
        if res=="y":
            continuar =True
        elif res=="n":
            continuar= False
    
main()

    
    