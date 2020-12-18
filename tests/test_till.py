from unittest import TestCase
import till


class Test(TestCase):
    def test_echo(self):
        expected = "tests tests"
        actual = till.echo("tests")
        self.assertEqual(expected, actual)
