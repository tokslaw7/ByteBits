
## Candidate Classes

## Core Data Objects
- manage our customers
- tracking their names 
- past purchase history
- customer orders
- Menu 

### Manage Our Customers
- username
- order items
- total price
- receipt
- TransactionID

### Menu
- Food
- Drinks
- Deserts
- Breakfast order (order_type)
- Lunch Order (order_type)

### Track Customers
- username
- total price
- category by menu_order
- popularity by order_type
- TransactionID

### Customer Orders
- selected items
- total price

### Past Puchase history
- transactionID 

### Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the 
- name, 
- price, 
- category, and 
- popularity rating for every item we sell.

We also need a way to ***manage*** the full collection of items 
* a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a ***single transaction***. This transaction object should store the selected items and compute the total cost.

