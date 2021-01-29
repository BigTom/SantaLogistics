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
        discounts = {"TOTAL": [10, 50, 100, 500, 1000],
                     "ELVES": [0.0, 2.5, 5.0, 7.5, 10.0]}
        actual = till.create_invoice_content(sack_request, prices_fake, discounts)
        expected = {"workshop": "ELVES",
                    "items": [["TOP", 10, 20],
                              ["HOOP", 40, 140],
                              ["HULA HOOP", 20, 105]],
                    "net_total": 265,
                    "discount": 5}
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
                   "net_total": 265,
                   "discount": 5}
        actual = till.generate_output(invoice_content)
        expected = """ELVES

GIFT      | COUNT | Total Cost

TOP       | 10    |     ₻20.00
HOOP      | 40    |    ₻140.00
HULA HOOP | 20    |    ₻105.00

Total:                 ₻265.00
Discount:                 5.0%"""
        self.assertEqual(expected, actual)

    def test_create_output_header(self):
        invoice_content = {"workshop": "ELVES",
                           "items": [["TOP", 10, 20],
                                     ["HOOP", 40, 140],
                                     ["HULA HOOP", 20, 105]],
                           "net_total": 265}
        expected = "ELVES"
        actual = till.generate_header(invoice_content["workshop"])
        self.assertEqual(expected, actual)

    def test_create_output_footer(self):
        invoice_content = {"workshop": "ELVES",
                           "items": [["TOP", 10, 20],
                                     ["HOOP", 40, 140],
                                     ["HULA HOOP", 20, 105]],
                           "net_total": 265,
                           "discount": 5}
        expected = "Total:                 ₻265.00\n" + \
                   "Discount:                 5.0%"
        actual = till.generate_footer((invoice_content["net_total"], invoice_content["discount"]))
        self.assertEqual(expected, actual)

    def test_create_output_lines(self):
        invoice_content = {"workshop": "ELVES",
                           "items": [["TOP", 10, 20],
                                     ["HOOP", 40, 140],
                                     ["HULA HOOP", 20, 105]],
                           "net_total": 265}
        expected = """TOP       | 10    |     ₻20.00
HOOP      | 40    |    ₻140.00
HULA HOOP | 20    |    ₻105.00"""
        actual = till.generate_invoice_lines(invoice_content["items"])
        self.assertEqual(expected, actual)

    def test_get_discount(self):
        workshop = "ELVES"
        total = 265
        discounts = {"TOTAL": [10, 50, 100, 500, 1000],
                     "ELVES": [0.0, 2.5, 5.0, 7.5, 10.0]}
        expected = 5.0
        actual = till.get_discount(workshop, total, discounts)
        self.assertEqual(expected, actual)



# def test_read_the_discount_file(self):
#    # TOTAL, ELVES, DWARVES, GNOMES, PIXIES, TROLLS
#    # 10, 0.00 %, 0.00 %, 0.00 %, 0.00 %, 0.00 %
#    # 50, 2.50 %, 2.00 %, 2.00 %, 3.00 %, 5.00 %
#    # 100, 5.00 %, 4.00 %, 5.00 %, 6.00 %, 5.00 %
#    # 500, 7.50 %, 6.00 %, 7.00 %, 9.00 %, 5.00 %
#    # 1000, 10.00 %, 8.00 %, 9.00 %, 12.00 %, 5.00 %
#
#     expected = [["TOTAL","ELVES","DWARVES","GNOMES","PIXIES","TROLLS"],
#                 [],
#                 [],
#                 [],
#                 [],
#                 []]
#
#     actual = till.read_gift_prices("../data/gifts.csv", "ELVES")
#     self.assertEqual(expected, actual)