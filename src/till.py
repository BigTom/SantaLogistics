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


def create_invoice_content(sack_request_file, param1):
    sack_request_content = read_sack_request_contents(sack_request_file)

    return {'items': [['TOP', 10, 20], ['HOOP', 40, 140], ['HULA HOOP', 20, 105]],
            'net_total': "FIX ME NEXT",
            'workshop': sack_request_content["workshop"]}
