# 5 - A farmer who grows organic oranges and lemons wants to calculate the annual profits from their sales.
# For this reason, we will design an application that requests the sales (in kilos) for each semester for each fruit.
# The application will display the total amount, knowing that the price per kilo of oranges is set at 1.25€ and lemons at 1.90€.

def input_message(message):
    print(message)

def input_data():
    sale = float(input())
    return sale

def output_data(total_profit):
    print(f"The total profits from both sales were: {total_profit} €")

def company_formula_per_kilo(lemons_sale_1, lemons_sale_2, oranges_sale_1, oranges_sale_2):
    total_profit = 1.9 * (lemons_sale_1 + lemons_sale_2) + 1.25 * (oranges_sale_1 + oranges_sale_2)
    return total_profit

def main():
    input_message("Enter the lemon sales for the first semester")
    lemons_sale_1 = input_data()
    input_message("Enter the lemon sales for the second semester")
    lemons_sale_2 = input_data()
    input_message("Enter the orange sales for the first semester")
    oranges_sale_1 = input_data()
    input_message("Enter the orange sales for the second semester")
    oranges_sale_2 = input_data()
    total_profit = company_formula_per_kilo(lemons_sale_1, lemons_sale_2, oranges_sale_1, oranges_sale_2)
    output_data(total_profit)

main()

    