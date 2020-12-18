from unittest import TestCase
import till


class Test(TestCase):
    def test_echo(self):
        expected = "tests tests"
        actual = till.echo("tests")
        self.assertEqual(expected, actual)

    def test_read_the_sack_items(self):
        expected = {"TOP": 10,
                    "HOOP": 40,
                    "HULA HOOP": 20}
        actual = till.read_sack_contents("../data/example_sack.csv")
        self.assertEqual(expected, actual)

#This test intends to show multiplying a count of item * the price of the item
# The implementation doesn't work and we didn't dig into why
    def test_item_count(self):
        # item_and_counts = till.read_sack_contents("../data/example_sack.csv")
        item_and_counts = {"TOP": 10, "HOOP": 40, "HULA HOOP": 20}
        prices_fake = {"TOP": 2.0, "HOOP": 3.5, "HULA HOOP": 5.25}

        actual = till.calculate_item_total(item_and_counts, prices_fake)
        expected = {"TOP": 20,
                    "HOOP": 140,
                    "HULA HOOP": 105}

        self.assertEqual(expected, actual)

#     def test_print_invoice(self):
#         expected = """
# WORKSHOP NAME
# GIFT COUNT Total Cost
# TOP 10 20.00
# HOOP 40 140.00
# HULA HOOP 20 105.00
#
# Total: 265.00
# Discount: 7.5%
# Total: 245.50
# """
#         # actual = till.print_invoice("../data/example_sack.csv")
#         actual = ""
#         self.assertEqual(expected, actual)
