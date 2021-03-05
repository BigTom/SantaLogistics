class SackRequest:
    """
    From a user perspective:
        Take a filepath and till, and provide invoice and shipping content
    SackRequest should read from file, get workshop from till,
            hold data and provide calculated invoice and shipping note on request

    Collaborators: FileReader, Till, Workshop
    """

    def __init__(self, sack_request_content, till):
        """
        Content is currently in the form
        {'workshop':workshopName,
          'gifts':{'giftName:giftCount}
        """
        self.workshop_name = sack_request_content['workshop']
        self.gifts = sack_request_content['gifts']
        self.workshop = till.workshops[self.workshop_name]

    def read_sack_request_contents(self, path_to_data_file):
        with open(path_to_data_file, "r") as req:
            lines = [line.strip().split(",") for line in req]
        item_dict = {item[0]: int(item[1]) for item in lines[2:]}
        self.workshop_name = lines[0][0]
        self.gifts = item_dict

    def calculate_lines_items(self):
        self.line_items = {gift_name: count * self.workshop.gift_prices[gift_name]
                           for gift_name, count in self.gifts.items()}

    def calculate_net_invoice_price(self):
        return sum(self.line_items.values())

    def calculate_summary_data(self):
        self.summary_data = {"total": sum(self.line_items.values()),
                             "discount_rate": 5}

    def __generate_invoice_data(self):
        self.calculate_lines_items()
        self.calculate_summary_data()
        self.invoice_data = {"line_items": self.line_items,
                             "summary": self.summary_data}

    def __generate_footer(self):
        self.footer = "Total:                 ₻{total:.2f}\n".format(total=self.summary_data['total']) + \
                      "Discount:                 {discount:.1f}%".format(discount=self.summary_data["discount_rate"])

    def __generate_invoice_lines(self):
        lines = [self.__generate_invoice_line(gift) for gift in self.gifts.keys()]
        self.invoice_lines = '\n'.join(lines)

    def __generate_invoice_line(self, gift):
        return "{name:10}| {count}    |".format(name=gift, count=self.gifts[gift]) + \
               "₻{total:.2f}".format(total=self.invoice_data['line_items'][gift]).rjust(11, " ")

    def generate_invoice(self):
        self.__generate_invoice_data()
        self.__generate_invoice_lines()
        self.__generate_footer()

        self.invoice = self.workshop_name + "\n\n" + \
        self.invoice_lines + "\n\n" + \
        self.footer


class Workshop:
    """
    Workshop should hold gift_prices and discount_rates,
    it should calculate the applicable discount and something shipping when relevant

    Collaborators: FileReader?
    """

    def __init__(self, gift_prices, discount_rates):
        self.gift_prices = gift_prices
        self.discount_rates = discount_rates


class Till:
    """
    Provides the correct workshop to a sackrequest.
    Knows the name of workshop and associated workshop object. Does not know about sack requests
    Long term builds workshop dictionary from file.
    Possibly rename to exchange?

    Collaborators: FileReader, Workshop
    """

    def __init__(self, workshops):
        # Currently takes a dictionary of {workshopName:workshopObj}
        self.workshops = workshops
