#14- Create a dictionary that stores products with their price and stock. Then, create a function to calculate the
#total value of the inventory.

inventory = {"water": {"price": 10, "stock": 2}, "cola": {"price": 12, "stock": 6}, "orange": {"price": 12, "stock": 4}}

def calculate_total_inventory_value(inventory):
    individual_value_quantity_list=[]
    for product_dict in inventory.values():
        total_price=1
        for price_stock_dict in product_dict.values():
            total_price*=price_stock_dict
        individual_value_quantity_list.append(total_price)
            
    inventory_value=sum(individual_value_quantity_list)
    return inventory_value
        
def main():
    inventory_value=calculate_total_inventory_value(inventory)
    print(inventory_value)

main()