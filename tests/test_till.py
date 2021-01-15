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
        actual = till.create_invoice_content("../data/example_sack.csv","../data/gifts.csv" )
        expected = {"workshop": "ELVES",
                    "items": [["TOP", 10,20],
                              ["HOOP", 40, 140],
                              ["HULA HOOP", 20, 105]],
                    "net_total": 265}
        self.assertEqual(expected, actual)