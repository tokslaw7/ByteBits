
User → Order

One user can place many orders.

Each order is associated with one user.

Menu → MenuItem

A menu contains multiple menu items.

This is composition because menu items are part of the menu structure.

Order → MenuItem

One order contains one or more selected menu items.

This shows the items grouped into a single order.

Order → Transaction

An order may have zero or one transaction.

0..1 is useful because an order can exist before payment is completed.

Once payment happens, the transaction records the payment details.

Difference between Order and Transaction

Order = the food selection itself

Transaction = the payment record for that order

So the flow is:

User places Order → Order contains MenuItems → Order is paid through Transaction