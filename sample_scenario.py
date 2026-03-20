from models import MenuItem, MenuCatalog, Order, Transaction, User

# --- 1. Create a user ---
user = User(userId="u001", username="alex")

# --- 2. Build the menu catalog ---
catalog = MenuCatalog()

catalog.addItem(MenuItem("m001", "Spicy Burger",   8.99, "Burgers", 4.8))
catalog.addItem(MenuItem("m002", "Veggie Wrap",    7.49, "Wraps",   4.2))
catalog.addItem(MenuItem("m003", "Large Soda",     2.49, "Drinks",  4.5))
catalog.addItem(MenuItem("m004", "Mango Smoothie", 4.99, "Drinks",  4.7))
catalog.addItem(MenuItem("m005", "Brownie",        3.49, "Desserts",4.9))
catalog.addItem(MenuItem("m006", "Ice Cream Cup",  3.99, "Desserts",4.6))

# --- 3. Sort all menu items by popularity (highest first) ---
sorted_items = sorted(catalog.items, key=lambda item: item.popularityRating, reverse=True)
print("Menu sorted by popularity:")
for item in sorted_items:
    print(f"  {item.name} ({item.category}) - ${item.price:.2f} | rating: {item.popularityRating}")

# --- 4. Filter by category ---
drinks = catalog.filterByCategory("Drinks")
print("\nDrinks available:")
for drink in drinks:
    print(f"  {drink.name} - ${drink.price:.2f}")

# --- 5. Place an order ---
order = Order(orderId="o001")
order.addItem(catalog.items[0])  # Spicy Burger
order.addItem(catalog.items[2])  # Large Soda
order.addItem(catalog.items[4])  # Brownie

print(f"\nOrder items:")
for item in order.selectedItems:
    print(f"  {item.name} - ${item.price:.2f}")
print(f"Order total: ${order.totalCost:.2f}")

# --- 6. Process payment ---
transaction = Transaction(
    transactionId="t001",
    amountPaid=20.00,
    paymentMethod="credit card",
    order=order
)
success = transaction.processPayment()
print(f"\nPayment status: {transaction.paymentStatus} (processed: {success})")

# --- 7. Save order to user history ---
order.status = "complete"
user.addOrder(order)
print(f"\n{user.username}'s purchase history: {len(user.purchaseHistory)} order(s)")
