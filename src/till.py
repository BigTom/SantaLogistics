def echo(name):
    return "{0} {1}".format(name, name)


def read_sack_contents(path_to_data_file):
    print(path_to_data_file)
    with open(path_to_data_file, "r") as req:
        lines = [line.strip().split(",") for line in req]

    item_dict = { item[0]: int(item[1]) for item in lines [2:]}
    return item_dict

def calculate_item_total(count, price):
    return { k:v * price[k] for k,v in count }