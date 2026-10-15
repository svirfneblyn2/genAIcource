import unittest
from delivery_fee import Order, delivery_fee


class DeliveryFeeTests(unittest.TestCase):
    def test_city_standard(self):
        self.assertEqual(delivery_fee(Order(50, "CITY")), 7.50)

    def test_outside_standard(self):
        self.assertEqual(delivery_fee(Order(50, "OUTSIDE")), 18.00)

    def test_free_delivery_from_100(self):
        self.assertEqual(delivery_fee(Order(100, "CITY")), 0.0)

    def test_prime_free_at_75(self):
        self.assertEqual(delivery_fee(Order(75, "CITY", True)), 0.0)

    def test_prime_below_75_pays(self):
        self.assertEqual(delivery_fee(Order(74.99, "CITY", True)), 7.50)

    def test_non_prime_at_75_pays(self):
        self.assertEqual(delivery_fee(Order(75, "CITY", False)), 7.50)

    def test_negative_subtotal_rejected(self):
        with self.assertRaises(ValueError):
            delivery_fee(Order(-1, "CITY"))


if __name__ == "__main__":
    unittest.main()
