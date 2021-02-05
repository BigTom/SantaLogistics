from unittest import TestCase
from till_oop import SackRequest, Till


class Test(TestCase):

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

    def generate_dummy_sack_request(self):
        request = {"workshop": "ELVES",
                   "gifts": {"TOP": 10,
                             "HOOP": 40,
                             "HULA HOOP": 20}}
        return SackRequest(request)

    def test_till_calculate_order_line_cost_from_a_sack_request(self):
        my_till = self.generate_dummy_till()

        my_sack_request = self.generate_dummy_sack_request()

        expected = {"TOP": 20,
                    "HOOP": 140,
                    "HULA HOOP": 105}
        self.assertEqual(expected, my_till.get_order(my_sack_request))

    def test_till_calculate_order_line_cost_from_any_sack_request(self):
        my_till = self.generate_dummy_till()

        my_sack_request = self.generate_another_dummy_sack_request()
        expected = {"TOP": 28,
                    "HULA HOOP": 131.25}
        self.assertEqual(expected, my_till.get_order(my_sack_request))

    def generate_another_dummy_sack_request(self):
        request = {"workshop": "ELVES",
                   "gifts": {"TOP": 14,
                             "HULA HOOP": 25}}
        return SackRequest(request)
