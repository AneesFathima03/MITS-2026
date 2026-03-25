# Step 1: Create movie dictionary (title → price)
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

# Step 2: Create empty list to store purchases
purchases = []  # (title, qty, price_each)

# Start loop (runs until user types 'done')
while True:

    #  Ask for movie title
    title = input("Enter movie title (or 'done' to finish): ").title()

    # Exit condition
    if title == "done":
        break

    # Validate movie title
    if title not in movies:
        #print("Available movies:", list(movies.keys()))
        print("Invalid movies. Try again!")
        continue

    # Step 8: Ask for quantity
    qty = int(input("Enter quantity: "))

    # Step 9: Get price from dictionary
    price = movies[title]

    # Step 10: Store purchase in list
    purchases.append((title, qty, price))

    # Step 11: Update subtotal
    subtotal += qty * price

    # Step 12: Show running total
    print("Added to cart. Current subtotal:", subtotal)

# Step 13: Display all purchases
print("\nPurchases:", purchases)

# Step 14: Display final total
print("Final total:", subtotal)

