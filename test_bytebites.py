import unittest
from models import MenuItem, MenuCatalog, Order, Transaction, User


class TestOrderTotal(unittest.TestCase):

    def test_calculate_total_with_multiple_items(self):
        # A $10 Spicy Burger + $5 Large Soda should total $15
        order = Order("o001")
        order.addItem(MenuItem("m001", "Spicy Burger", 10.00, "Burgers", 4.8))
        order.addItem(MenuItem("m002", "Large Soda",    5.00, "Drinks",  4.5))
        self.assertEqual(order.totalCost, 15.00)


class TestEmptyOrderTotal(unittest.TestCase):

    def test_calculate_total_on_empty_order(self):
        # An order with no items should have a total of $0
        order = Order("o002")
        self.assertEqual(order.calculateTotal(), 0.0)


class TestFilterByCategory(unittest.TestCase):

    def test_filter_returns_only_matching_category(self):
        # Only "Drinks" items should be returned when filtering by "Drinks"
        catalog = MenuCatalog()
        catalog.addItem(MenuItem("m001", "Spicy Burger",   10.00, "Burgers", 4.8))
        catalog.addItem(MenuItem("m002", "Large Soda",      5.00, "Drinks",  4.5))
        catalog.addItem(MenuItem("m003", "Mango Smoothie",  4.99, "Drinks",  4.7))

        drinks = catalog.filterByCategory("Drinks")
        self.assertEqual(len(drinks), 2)
        self.assertTrue(all(item.category == "Drinks" for item in drinks))


class TestProcessPayment(unittest.TestCase):

    def _make_order(self):
        order = Order("o003")
        order.addItem(MenuItem("m001", "Spicy Burger", 10.00, "Burgers", 4.8))
        order.addItem(MenuItem("m002", "Large Soda",    5.00, "Drinks",  4.5))
        return order  # totalCost == 15.00

    def test_payment_succeeds_when_amount_covers_total(self):
        # Paying exactly $15 for a $15 order should set paymentStatus to "paid"
        order = self._make_order()
        txn = Transaction("t001", 15.00, "credit_card", order)
        result = txn.processPayment()
        self.assertTrue(result)
        self.assertEqual(txn.paymentStatus, "paid")

    def test_payment_fails_when_amount_is_insufficient(self):
        # Paying $10 for a $15 order should set paymentStatus to "failed"
        order = self._make_order()
        txn = Transaction("t002", 10.00, "credit_card", order)
        result = txn.processPayment()
        self.assertFalse(result)
        self.assertEqual(txn.paymentStatus, "failed")


class TestPurchaseHistory(unittest.TestCase):

    def test_add_order_appends_to_purchase_history(self):
        # After adding an order, it should appear in the user's purchaseHistory
        user = User("u001", "alice")
        order = Order("o004")
        user.addOrder(order)
        self.assertIn(order, user.purchaseHistory)


class TestFilterByCategoryCaseInsensitive(unittest.TestCase):

    def test_filter_matches_regardless_of_case(self):
        # "drinks" (lowercase) should match items with category "Drinks"
        catalog = MenuCatalog()
        catalog.addItem(MenuItem("m001", "Large Soda", 5.00, "Drinks", 4.5))
        result = catalog.filterByCategory("drinks")
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
