#12- Create a function that receives a shopping list and returns the number of times each product was purchased.

def quantity_times_purchased(shopping_list):
    product_quantity_times={}
    for product in shopping_list:
        if product not in product_quantity_times:
            product_quantity_times[product]=1
        else:
            product_quantity_times[product]+=1
    return product_quantity_times


def main():
    shopping_list=["water","milk","tomato","milk","water","water"]
    product_quantity_times=quantity_times_purchased(shopping_list)
    for product,quantity in product_quantity_times.items():
        print(f"the product {product} has been sold {quantity} times")

main()
    
