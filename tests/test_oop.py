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


def generate_dummy_sack_request(till):
    request = {"workshop": "ELVES",
               "gifts": {"TOP": 10,
                         "HOOP": 40,
                         "HULA HOOP": 20}}
    return SackRequest(request, till)

def generate_another_dummy_sack_request(till):
    request = {"workshop": "ELVES",
               "gifts": {"TOP": 14,
                         "HULA HOOP": 25}}
    return SackRequest(request, till)


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

    def test_construct_till(self):
        my_till = Till({'ELVES': generate_dummy_workshop()})
        self.assertEqual(my_till.workshops['ELVES'].gift_prices,
                                              {"TOP": 2.00,
                                               "HOOP": 3.50,
                                               "DOLL": 4.65,
                                               "BLOCKS": 12.00,
                                               "HULA HOOP": 5.25})
        self.assertEqual(my_till.workshops['ELVES'].discount_rates,
                                              {"TOTALS": [10, 50, 100, 500, 1000],
                                                  "DISCOUNTS": [0.0, 2.5, 5.0, 7.5, 10.0]})

    def test_construct_sack_request(self):
        dummy_workshop = generate_dummy_workshop()
        dummy_till = Till({'ELVES': dummy_workshop})
        my_sack_request = SackRequest({"workshop": "ELVES",
               "gifts": {"TOP": 10,
                         "HOOP": 40,
                         "HULA HOOP": 20}}, dummy_till)
        self.assertEqual(my_sack_request.workshop, dummy_workshop)
        self.assertEqual(my_sack_request.workshop_name, "ELVES")
        self.assertEqual(my_sack_request.gifts, {"TOP": 10,
                         "HOOP": 40,
                         "HULA HOOP": 20})

    def test_till_produce_order_total_and_discount(self):
        my_till = Till({'ELVES': generate_dummy_workshop()})
        my_sack_request = generate_another_dummy_sack_request(my_till)

        expected = {"total": 28 + 131.25,
                    "discount_rate": 5}
        my_sack_request.calculate_lines_items()
        my_sack_request.calculate_summary_data()

        self.assertEqual(expected, my_sack_request.summary_data)

    def test_generate_invoice_data(self):
        # Generate a sack request and use it to generate invoice data
        my_till = Till({'ELVES': generate_dummy_workshop()})
        my_sack_request = generate_dummy_sack_request(my_till)
        my_sack_request.generate_invoice_data()
        expected = {"line_items": {"TOP": 20.0,
                                   "HOOP": 140.0,
                                   "HULA HOOP": 105.0},
                    "summary": {"total": 20.0 + 140.0 + 105.0,
                                "discount_rate": 5}}
        self.assertEqual(expected, my_sack_request.invoice_data)

    def test_create_output_header(self):
        my_till = Till({'ELVES': generate_dummy_workshop()})
        my_sack_request = generate_dummy_sack_request(my_till)
        my_sack_request.generate_invoice_data()
        expected = "ELVES"
        self.assertEqual(expected, my_sack_request.workshop_name)

    def test_create_output_footer(self):
        my_till = Till({'ELVES': generate_dummy_workshop()})
        my_sack_request = generate_dummy_sack_request(my_till)
        my_sack_request.generate_invoice_data()
        my_sack_request.generate_footer()
        expected = "Total:                 ₻265.00\n" + \
                   "Discount:                 5.0%"
        self.assertEqual(expected, my_sack_request.footer)

    def test_create_output_lines(self):
        my_till = Till({'ELVES': generate_dummy_workshop()})
        my_sack_request = generate_dummy_sack_request(my_till)
        my_sack_request.generate_invoice_data()
        my_sack_request.generate_invoice_lines()
        expected = """TOP       | 10    |     ₻20.00
HOOP      | 40    |    ₻140.00
HULA HOOP | 20    |    ₻105.00"""
        self.assertEqual(expected, my_sack_request.invoice_lines)