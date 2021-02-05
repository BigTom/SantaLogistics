class SackRequest:

    def __init__(self, sack_request_content):
        self.workshop = sack_request_content['workshop']
        self.gifts = sack_request_content['gifts']

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

    def get_order(self, my_sack_request):
        lines = self.get_order_lines(my_sack_request.gifts)
        return lines

    def get_order_lines(self, gifts):
        return {gift_name: count * self.gift_prices[gift_name] for gift_name, count in gifts.items()}
