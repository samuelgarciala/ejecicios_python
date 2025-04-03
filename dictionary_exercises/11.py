#11- Create a dictionary that stores the stock of a store. Then, implement a function to update the
#stock when a sale is made.


def update_sale(current_stock,sold_product,sold_product_quantity):
#    current_stock[sold_product]=current_stock.get(sold_product) - sold_product_quantity
    current_stock[sold_product]-=sold_product_quantity

def main():
    current_stock={
    "water":40,
    "cola":35,
    "fanta":20,
    "beer":30
    }
    update_sale(current_stock,"water",10)
    print(current_stock)
    
main()
