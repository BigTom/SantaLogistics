from unittest import TestCase
from till_oop import SackRequest, Till


class Test(TestCase):
    def test_read_the_sack_items(self):
        expected = {"workshop": "ELVES",
                    "gifts": {"TOP": 10,
                              "HOOP": 40,
                              "HULA HOOP": 20}}

        my_sack_request = SackRequest("../data/example_sack.csv", self.generate_dummy_till())
        self.assertEqual(expected["workshop"], my_sack_request.workshop)
        self.assertEqual(expected["gifts"], my_sack_request.gifts)

    def test_construct_till(self):
        gift_prices = {"TOP": 2.00,
                       "HOOP": 3.50,
                       "DOLL": 4.65,
                       "BLOCKS": 12.00,
                       "HULA HOOP": 5.25}
        discount_rates = {"TOTALS": [10, 50, 100, 500, 1000],
                          "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]}
        my_till = Till(gift_prices, discount_rates)
        self.assertEqual(gift_prices, my_till.gift_prices)
        self.assertEqual(discount_rates, my_till.discount_rates)

    def generate_dummy_till(self):
        gift_prices = {"TOP": 2.00,
                       "HOOP": 3.50,
                       "DOLL": 4.65,
                       "BLOCKS": 12.00,
                       "HULA HOOP": 5.25}
        discount_rates = {"TOTALS": [10, 50, 100, 500, 1000],
                          "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]}
        return Till(gift_prices, discount_rates)

    def test_item_totals_are_calculated_from_product_and_counts(self):
        my_till = self.generate_dummy_till()
        my_sack_request = SackRequest("../data/example_sack.csv", my_till)

        expected = {"TOP": 20,
                    "HOOP": 140,
                    "HULA HOOP": 105}

        self.assertEqual(expected, my_sack_request.gift_total_costs)
