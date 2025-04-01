# Question 1:
# This function calculates the final price after applying a discount.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Question 2:
# Prompts the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Result
if final_price == price:
    print(f"No discount applied. The final price remains: Ksh {final_price:.2f}/-")
else:
    print(f"Discount applied! The final price is: Ksh {final_price:.2f}/-")
