class SackRequest:
# sackRequest should read from file, hold data and provide data on request
    def __init__(self, sack_request_content):
        self.workshop = sack_request_content['workshop']
        self.gifts = sack_request_content['gifts']

    def read_sack_request_contents(self, path_to_data_file):
        with open(path_to_data_file, "r") as req:
            lines = [line.strip().split(",") for line in req]

        item_dict = {item[0]: int(item[1]) for item in lines[2:]}
        self.workshop = lines[0][0]
        self.gifts = item_dict

    # Workshop Class
    # Responsibility: providing pricing, discount, and shipping information for a specific workshop
    # Collaborators: FileReader
    # primary method: read workshop information from file and then provide information

    # SackRequest Class
    # Responsibility: provide gift quantities, workshop and destination
    # Collaborators: FileReader

    # Till Class
    # Responsibility: to calculate and create and invoice and a shipping note
    # Collaborators: Workshop, SackRequest
    # primary method: constructor that takes a workshop and a sackRequest
    # method: generate invoice
    # method: generate shipping note
    # note: may capture intermediate values as member variables

class Workshop:
    def __init__(self, gift_prices, discount_rates):
        self.gift_prices = gift_prices
        self.discount_rates = discount_rates


class Till:
    # Responsibility: providing pricing, discount, and shipping information for a specific workshop
    # Collaborators: FileReader, SackRequest
    def __init__(self, workshop, sack_request):
        self.workshop_name = sack_request.workshop
        self.gift_prices = workshop.gift_prices
        self.discount_rates = workshop.discount_rates
        self.requested_gifts = sack_request.gifts

    # method: generate invoice
    # method: generate shipping note
    # note: may capture intermediate values as member variables

    def get_order(self, my_sack_request):
        lines = self.get_order_lines(my_sack_request.gifts)
        return lines

    def calculate_lines_items(self):
        self.line_items = {gift_name: count * self.gift_prices[gift_name] for gift_name, count in self.requested_gifts.items()}

    def calculate_net_invoice_price(self):
        return sum(self.line_items.values())

    def calculate_summary_data(self):
        self.summary_data = {"total": sum(self.line_items.values()),
                            "discount_rate": 5}

    def generate_invoice_data(self):
        self.calculate_lines_items()
        self.calculate_summary_data()
        self.invoice_data = {"line_items": self.line_items,
                             "summary": self.summary_data}
