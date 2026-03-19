'''
This models.py file defines the data structures for a food ordering app. It includes the following classes:
***User
Represents the customer using the app. Stores the user's basic details and keeps track of their past orders.

***MenuCatalog
Represents the full list of available food and drink items. It helps organize and filter items by category.

***MenuItem
Represents a single food or drink product. Stores details such as name, price, category, and popularity rating.

***Order
Represents the items a user selects in one purchase request. It groups chosen menu items and calculates the total cost.

***Transaction
Represents the payment record linked to an order. It stores payment details such as amount paid, payment status, method, and date.
'''

from datetime import date


class MenuItem:
    def __init__(self, itemId: str, name: str, price: float, category: str, popularityRating: float):
        self.itemId = itemId
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating


class MenuCatalog:
    def __init__(self):
        self.items: list[MenuItem] = []

    def addItem(self, item: MenuItem) -> None:
        self.items.append(item)

    def filterByCategory(self, category: str) -> list[MenuItem]:
        return [item for item in self.items if item.category.lower() == category.lower()]


class Order:
    def __init__(self, orderId: str):
        self.orderId = orderId
        self.selectedItems: list[MenuItem] = []
        self.totalCost: float = 0.0
        self.status: str = "pending"

    def addItem(self, item: MenuItem) -> None:
        self.selectedItems.append(item)
        self.calculateTotal()

    def calculateTotal(self) -> float:
        self.totalCost = sum(item.price for item in self.selectedItems)
        return self.totalCost


class Transaction:
    def __init__(self, transactionId: str, amountPaid: float, paymentMethod: str, order: Order):
        self.transactionId = transactionId
        self.amountPaid = amountPaid
        self.paymentStatus: str = "unpaid"
        self.paymentMethod = paymentMethod
        self.transactionDate: date = date.today()
        self.order = order

    def processPayment(self) -> bool:
        if self.amountPaid >= self.order.totalCost:
            self.paymentStatus = "paid"
            return True
        self.paymentStatus = "failed"
        return False


class User:
    def __init__(self, userId: str, username: str):
        self.userId = userId
        self.username = username
        self.purchaseHistory: list[Order] = []
