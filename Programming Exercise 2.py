# Jonathan Stanley, CIS156

# Gets the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculates the tip amount.
tip = original_price * (0.18)

#Calculates the sales tax.
tax = original_price * (0.07)

# Calculates the sale price.
sale_price = original_price + tax + tip

#Displays the sale price.
print('the sale price is', sale_price)