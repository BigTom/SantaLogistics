from unittest import TestCase
import till


class Test(TestCase):
    def test_read_the_sack_items(self):
        expected = {"workshop": "ELVES",
                    "items": {"TOP": 10,
                              "HOOP": 40,
                              "HULA HOOP": 20}}
        actual = till.read_sack_request_contents("../data/example_sack.csv")
        self.assertEqual(expected, actual)

    def test_read_the_gift_prices(self):
        expected = {"TOP": 2.00,
                    "HOOP": 3.50,
                    "DOLL": 4.65,
                    "BLOCKS": 12.00,
                    "HULA HOOP": 5.25}
        actual = till.read_gift_prices("../data/gifts.csv", "ELVES")
        self.assertEqual(expected, actual)

    def test_item_totals_are_calculated_from_product_and_counts(self):
        item_and_counts = {"TOP": 10, "HOOP": 40, "HULA HOOP": 20}
        prices_fake = {"TOP": 2.0, "HOOP": 3.5, "HULA HOOP": 5.25}

        actual = till.calculate_item_total(item_and_counts, prices_fake)
        expected = {"TOP": 20,
                    "HOOP": 140,
                    "HULA HOOP": 105}

        self.assertEqual(expected, actual)

    def test_calculate_net_invoice_price(self):
        total_row_costs = {"TOP": 20,
                           "HOOP": 140,
                           "HULA HOOP": 105}
        actual = till.calculate_net_invoice_price(total_row_costs)
        expected = 265
        self.assertEqual(expected, actual)

    def test_create_invoice_content(self):
        sack_request = {"workshop": "ELVES",
                        "items": {"TOP": 10,
                                  "HOOP": 40,
                                  "HULA HOOP": 20}}
        prices_fake = {"TOP": 2.0, "HOOP": 3.5, "HULA HOOP": 5.25}
        actual = till.create_invoice_content(sack_request, prices_fake)
        expected = {"workshop": "ELVES",
                    "items": [["TOP", 10, 20],
                              ["HOOP", 40, 140],
                              ["HULA HOOP", 20, 105]],
                    "net_total": 265}
        self.assertEqual(expected, actual)

    def test_read_files(self):
        expected_sack_request = {"workshop": "ELVES",
                        "items": {"TOP": 10,
                                  "HOOP": 40,
                                  "HULA HOOP": 20}}
        expected_prices = {'BLOCKS': 12.0, 'DOLL': 4.65, 'HOOP': 3.5, 'HULA HOOP': 5.25, 'TOP': 2.0}
        actual = till.read_files("../data/example_sack.csv", "../data/gifts.csv")
        self.assertEqual((expected_sack_request, expected_prices), actual)

    def test_create_output_string(self):
        invoice_content= {"workshop": "ELVES",
                   "items": [["TOP", 10, 20],
                             ["HOOP", 40, 140],
                             ["HULA HOOP", 20, 105]],
                   "net_total": 265}
        actual = till.generate_output(invoice_content)
        expected = """
ELVES

GIFT      | COUNT | Total Cost

TOP       | 10    |     ₻20.00
HOOP      | 40    |    ₻140.00
HULA HOOP | 20    |    ₻105.00

Total:                 ₻265.00
"""
        self.assertEqual(expected, actual)

    def test_create_output_header(self):
        invoice_content = {"workshop": "ELVES",
                           "items": [["TOP", 10, 20],
                                     ["HOOP", 40, 140],
                                     ["HULA HOOP", 20, 105]],
                           "net_total": 265}
        expected = "ELVES"
        actual = till.generate_header(invoice_content)
        self.assertEqual(expected, actual)

    def test_create_output_footer(self):
        invoice_content = {"workshop": "ELVES",
                           "items": [["TOP", 10, 20],
                                     ["HOOP", 40, 140],
                                     ["HULA HOOP", 20, 105]],
                           "net_total": 265}
        expected = "Total:                 ₻265.00"
        actual = till.generate_footer(invoice_content)
        self.assertEqual(expected, actual)

    def test_create_output_lines(self):
        self.fail("write code to generate invoice lines")