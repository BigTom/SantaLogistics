class SackRequest:

    def __init__(self, path, till):
        self.read_sack_request_contents(path)
        self.till = till
        self.gift_total_costs = {"TOP": 20,
                        "HOOP": 140,
                        "HULA HOOP": 105}

    def read_sack_request_contents(self, path_to_data_file):
        with open(path_to_data_file, "r") as req:
            lines = [line.strip().split(",") for line in req]

        item_dict = {item[0]: int(item[1]) for item in lines[2:]}
        self.workshop = lines[0][0]
        self.gifts = item_dict


class Till:
    def __init__(self, gift_prices, discount_rates):
        self.gift_prices = gift_prices
        self.discount_rates = discount_rates

