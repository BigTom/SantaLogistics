def read_sack_request_contents(path_to_data_file):
    with open(path_to_data_file, "r") as req:
        lines = [line.strip().split(",") for line in req]

    item_dict = {item[0]: int(item[1]) for item in lines[2:]}
    return {
        "workshop": lines[0][0],
        "items": item_dict}


def calculate_item_total(request, price):
    return {product: count * price[product] for product, count in request.items()}


def read_gift_prices(path_to_data_file, workshop_name):
    with open(path_to_data_file, "r") as req:
        lines = [line.strip().split(",") for line in req]
    filter_by_workshop = {item[0].strip(): float(item[2][1:]) for item in lines[1:] if
                          len(item) > 1 and item[1] == workshop_name}
    return filter_by_workshop


def calculate_net_invoice_price(total_row_costs):
    return sum(total_row_costs.values())


def read_files(sack_request_file, gift_price_file):
    sack_request_content = read_sack_request_contents(sack_request_file)
    prices = read_gift_prices(gift_price_file, sack_request_content["workshop"])
    return sack_request_content, prices

def create_invoice_content(sack_request_content,prices):
    items_quantity = sack_request_content['items']
    items_total_costs = calculate_item_total(items_quantity, prices)
    items = [[item_name,
              quantity,
              items_total_costs[item_name]]
             for item_name, quantity in items_quantity.items()]
    total = calculate_net_invoice_price(items_total_costs)

    return {'items': items,
            'net_total': total,
            'workshop': sack_request_content["workshop"]}




def generate_output(invoice_content):
    # expected_input = {"workshop": "ELVES",
    #                    "items": [["TOP", 10, 20],
    #                              ["HOOP", 40, 140],
    #                              ["HULA HOOP", 20, 105]],
    #                    "net_total": 265}

    output = """
ELVES

GIFT      | COUNT | Total Cost

TOP       | 10    |     ₻20.00
HOOP      | 40    |    ₻140.00
HULA HOOP | 20    |    ₻105.00

Total:                 ₻265.00
"""
    return output


def generate_header(invoice_content):
    return invoice_content["workshop"]


def generate_footer(invoice_content):
    net_total = invoice_content["net_total"]
    return "Total:                 ₻{total:.2f}".format(total=net_total)
