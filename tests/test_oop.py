from unittest import TestCase
from till_oop import SackRequest, Till, Workshop

def generate_dummy_workshop():
    gift_prices = {"TOP": 2.00,
                   "HOOP": 3.50,
                   "DOLL": 4.65,
                   "BLOCKS": 12.00,
                   "HULA HOOP": 5.25}
    discount_rates = {"TOTALS": [10, 50, 100, 500, 1000],
                      "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]}
    return Workshop(gift_prices, discount_rates)


def generate_dummy_sack_request():
    request = {"workshop": "ELVES",
               "gifts": {"TOP": 10,
                         "HOOP": 40,
                         "HULA HOOP": 20}}
    return SackRequest(request)

class Test(TestCase):
    def test_construct_workshop(self):
        gift_prices = {"TOP": 2.00,
                       "HOOP": 3.50,
                       "DOLL": 4.65,
                       "BLOCKS": 12.00,
                       "HULA HOOP": 5.25}
        discount_rates = {"TOTALS": [10, 50, 100, 500, 1000],
                          "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]}
        my_workshop = Workshop(gift_prices, discount_rates)
        self.assertEqual(gift_prices, my_workshop.gift_prices)
        self.assertEqual(discount_rates, my_workshop.discount_rates)



    # def test_till_calculate_order_line_cost_from_a_sack_request(self):
    #     my_till = generate_dummy_workshop()
    #
    #     my_sack_request = generate_dummy_sack_request()
    #
    #     expected = {"TOP": 20,
    #                 "HOOP": 140,
    #                 "HULA HOOP": 105}
    #     self.assertEqual(expected, my_till.get_order(my_sack_request))


    # def test_till_calculate_order_line_cost_from_any_sack_request(self):
    #     my_till = generate_dummy_workshop()
    #
    #     my_sack_request = self.generate_another_dummy_sack_request()
    #     expected = {"TOP": 28,
    #                 "HULA HOOP": 131.25}
    #     self.assertEqual(expected, my_till.get_order(my_sack_request))
    #
    #
    # def test_till_produce_order_total_and_discount(self):
    #     my_till = generate_dummy_workshop()
    #
    #     my_sack_request = self.generate_another_dummy_sack_request()
    #     expected = {"total": 28+131.25,
    #                 "discount_rate": 5}
    #     self.assertEqual(expected, my_till.get_summary_data(my_sack_request))


    def test_generate_invoice_data(self):
        my_till = Till(generate_dummy_workshop(), generate_dummy_sack_request())
        my_till.generate_invoice_data()
        expected = {"line_items": {"TOP": 20.0,
                                   "HOOP": 140.0,
                                   "HULA HOOP": 105.0},
                    "summary": {"total": 20.0+140.0+105.0,
                                "discount_rate": 5}}
        self.assertEqual(expected, my_till.invoice_data)

    def generate_another_dummy_sack_request(self):
        request = {"workshop": "ELVES",
                   "gifts": {"TOP": 14,
                             "HULA HOOP": 25}}
        return SackRequest(request)

    def test_construct_till(self):
        my_till = Till(generate_dummy_workshop(), generate_dummy_sack_request())
        self.assertEqual(my_till.workshop_name, "ELVES")
        self.assertEqual(my_till.gift_prices, {"TOP": 2.00,
                                               "HOOP": 3.50,
                                               "DOLL": 4.65,
                                               "BLOCKS": 12.00,
                                               "HULA HOOP": 5.25})
        self.assertEqual(my_till.discount_rates, {"TOTALS": [10, 50, 100, 500, 1000],
                                                  "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]})
        self.assertEqual(my_till.requested_gifts, {"TOP": 10,
                                                   "HOOP": 40,
                                                   "HULA HOOP": 20})



