#14- Create a dictionary that stores products with their price and stock. Then, create a function to calculate the
#total value of the inventory.

#modify add the stock

#def enter_data():
#    inventory={}
#    key=None
#    while True:
#        product=input("enter the product: ")
#        inventory[product]=int(input("enter price: "))
#        key=input("enter the letter x if you want to finish the record")
#        if key == "x":
#            break
#
#    return inventory

inventory = {"water": {"price": 10, "stock": 2}, "cola": {"price": 12, "stock": 6}, "orange": {"price": 12, "stock": 4}}

def calculate_total_inventory_value(inventory):
    individual_value_quantity_list=[]
    for product_dict in inventory.values():
        price=product_dict["price"]
        stock=product_dict["stock"]
        total_price=price*stock
        individual_value_quantity_list.append(total_price)
            
    inventory_value=sum(individual_value_quantity_list)
    return inventory_value
        
def main():
    inventory_value=calculate_total_inventory_value(inventory)
    print(inventory_value)

main()