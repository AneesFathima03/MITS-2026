# WEEK 4 TUTORIAL
#STEP 1- Welcome message
print("Welcome to the Python Coffee Shop!")

#STEP 2- ask customer's name
customer_name = input('What is your name?')
print('Hello, ' + customer_name + '! Lets\'s order some coffee')

#STEP 3 print the prices
price_coffee = 2.50
price_latte = 4.50
price_mocha = 5.00
price_expresso = 3.50
print("\nCoffee : $" + str(price_coffee))
print("\nLatte : $" + str(price_latte))
print("\nMocha : $" +str(price_mocha))
print("\nExpresso : $" +str(price_expresso))

#STEP 4- short list menu
menu_items = ["Coffee","Latte", "espresso","mocha"]
print("\nOur menu : ", menu_items)

flag = 'yes'
total = 0

#while loop
while flag == "yes":
    #step-5 - getting customer order
    choice = input("\nWhat would you like to order? (coffee/latte/mocha/expresso): ").lower()

    # determining the cost of user's choice
    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    elif choice == "expresso":
        cost = price_expresso
    else:
        print("\nSorry, we do not have that.")
        cost = 0
    # asking user for quantity
    quantity = int(input("\nHow many cups would you like?"))

    # calculating total cost of the customer's choice
    total_cost = cost*quantity
    total += total_cost
    flag = input("Do you want to order more (yes/no): ").lower()

# ask customer if they are a student
status = input("\nAre you a student? (yes/no):").lower()
if status == 'yes':
    print('You get a 10% student discount!')
    total *= 0.9
else:
    print("Sorry, you don't get the student discount.")

# customer gets discount for ordering more than 1 item
if quantity > 1:
    print("\n You get a discount of $1.00!")
    total -= 1.00

# printing the thank you message
print("\nYour total is : $" + str(total_cost))
print("\nThank you, " + customer_name + "! please come again.")


