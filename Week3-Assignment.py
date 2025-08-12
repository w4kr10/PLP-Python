# Deliverable 1: Creating a function to calculate discount based on price and discount percentage
def calculate_discount(price, discount_percentage):
    if discount_percentage>= 20:
        discount = price * (discount_percentage / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
    # Deliverable 2: Calling the function and handling user input

try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percent)
    if final_price != price:
        print(f"Final price after discount: {final_price}")
    else:
        print(f"No discount applied. Final price: {price}")
except ValueError:
    print("Invalid input. Please enter a value.")