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


def create_invoice_content(sack_request_content, prices, discount_table):
    items_quantity = sack_request_content['items']
    items_total_costs = calculate_item_total(items_quantity, prices)
    items = [[item_name,
              quantity,
              items_total_costs[item_name]]
             for item_name, quantity in items_quantity.items()]
    total = calculate_net_invoice_price(items_total_costs)
    discount = get_discount(sack_request_content['workshop'], total, discount_table)

    return {'items': items,
            'net_total': total,
            'workshop': sack_request_content["workshop"],
            'discount':discount}


def generate_output(invoice_content):
    item_header = "GIFT      | COUNT | Total Cost"
    return "\n\n".join([generate_header(invoice_content["workshop"]),
                        item_header,
                        generate_invoice_lines(invoice_content["items"]),
                        generate_footer((invoice_content["net_total"], invoice_content["discount"]))
                        ])


def generate_header(header):
    return header


def generate_footer(footer_content):
    return "Total:                 ₻{total:.2f}\n".format(total=footer_content[0]) + \
           "Discount:                 {discount:.1f}%".format(discount=footer_content[1])


def generate_invoice_lines(gifts):
    lines = [generate_invoice_line(gift) for gift in gifts]
    return '\n'.join(lines)


def generate_invoice_line(gift):
    return "{name:10}| {count}    |".format(name=gift[0], count=gift[1]) + \
           "₻{total:.2f}".format(total=gift[2]).rjust(11, " ")


def get_discount(workshop, total, discounts):
    total_gifts = discounts["TOTAL"]
    for index, amount in enumerate(total_gifts):
        if amount > total:
            discount_index = index-1
            break
    return discounts[workshop][discount_index]