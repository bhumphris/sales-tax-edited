cost = 1
total_amount = 0
tax_percentage = .06

def tax(total):
    print("your subtotal is: " + str(total) + "$")
    final_cost = total * tax_percentage
    print("Your tax is: " + str(final_cost))
    print("a nd your grand total is: " + str(final_cost + total))

while cost > 0:
    amount = raw_input("enter the amount of your item, or press '0'\n")
    cost = float(amount)
    total_amount += cost
    #print("Your current total is: " + str(total_amount) + "$\n")
    print (total_amount)

tax(total_amount)


