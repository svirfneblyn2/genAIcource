import unittest
from shipping import Order, shipping_cost

class ShippingTests(unittest.TestCase):
    def test_domestic_standard(self):
        self.assertEqual(shipping_cost(Order(50, "US")), 7.50)

    def test_international_standard(self):
        self.assertEqual(shipping_cost(Order(50, "DE")), 18.00)

    def test_free_shipping_over_100(self):
        self.assertEqual(shipping_cost(Order(100, "US")), 0.0)

    def test_negative_subtotal_rejected(self):
        with self.assertRaises(ValueError):
            shipping_cost(Order(-1, "US"))

if __name__ == "__main__":
    unittest.main()
