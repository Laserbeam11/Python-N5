#On The Computer: Basic Arithmetic
#task 2d
price_of_item = int(input("price of item: "))
discount_percentage = int(input("discount percentage: "))
discounted_price = price_of_item - (price_of_item * discount_percentage / 100)
print("the discounted price is:", discounted_price)