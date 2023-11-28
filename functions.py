# functions.py: YOUR NAME

def print_options(data):
    """
    Given a dictionary, print the keys
    and values as the formatted options:
     {key} - {value}
    """

    for k, d in data.items():
        print(f" {k} - {d}")


def print_orders(all_orders: dict, show_user=False):
    """
    param: all_orders (dict) - stores an orderID (key) that maps
            to a tuple with two elements: a price and a dictionary
            (the dictionary stores the user data such as age, etc.)
    param: show_user (bool) - indicates whether to print the
            user information dictionary

    Displays each order in the all_orders as follows:
    Order#..., $...
    if show_user = True, then after each order, the debugging print
    displays the dictionary.
    At the end of the output, the function prints 20 '.'
    followed by a "Total: $...", which displays the sum of all order
    prices.
    """

    if len(all_orders) == 0:
        print("WARNING: There is nothing to display!")
        print("....................")
        print("Total: $0.00")

    for order_id in all_orders:
        print(f"Order #{order_id}, {all_orders[order_id][0]}")
        if show_user:
            pass
            print(all_orders[order_id][1])


def convert_yes_no(inp: str):
    """
    If the input is "yes" or "y", return `True`;
    otherwise, return `False`.
    """

    return inp.upper() == "Y" or inp.upper() == "YES"


def construct_discounts_dict(keys_dict, values_list):
    """
    The function expects two objects of the same size:
    param: keys_dict (dict) - a dictionary with the
            necessary dictionary keys
    param: values_list (list) - a list with the returned
            dictionary values

    If the objects are not the same size, the function
    returns -1.
    Otherwise, it returns a dictionary where each KEY
    from the keys_dict is mapped to the corresponding
    item from the values_list. Return a NEW dictionary 
    instead of modifying the parameter keys_dict.

    For example, if the function is called with
    {"Student": 30, "Military": 25} , [True, False]
    the function returns
    {'Student': True, 'Military': False}
    """

    if len(keys_dict) != len(values_list):
        return -1

    res = {}
    i = 0
    for key in keys_dict:
        res[key] = values_list[i]
        i += 1

    return keys_dict


def compute_price_using_age(base_price, user_dict):
    """
    param: base_price (float) - the price without any discounts
    param: user_dict (dict) - contains the user information;
            expected to include a key "age"

    returns:
        -1 if the user_dict does not contain the key "age"
        Else, returns the updated price if the age is within the
        range needed for a discount:
        if age <= 12, reduce the base_price by 3
        if age >= 65, reduce the base_price by 2
        Otherwise, returns the original price.

    For example, calling the function with
    16.50 and {'age': 33} returns the original price of 16.50
    16.50 and {'age': 12} returns the discounted price of 13.50
    16.50 and {'age': 65} returns the discounted price of 14.50
    """
    if "age" not in user_dict:
        return -1

    if user_dict["age"] <= 12:
        base_price -= 3

    if user_dict["age"] >= 65:
        base_price -= 2

    return base_price


def compute_price_using_status_max(base_price, discount_options_dict, user_dict):
    """
    param: base_price (float) - the price without any discounts
    param: discount_options_dict (dict) - contains strings
            naming the different discounts, e.g., "Student", "Military",
            and the corresponding discount percentages, e.g., 30, 25,
            respectively.
    param: user_dict (dict) - contains the user information, where the
            keys include "age" and values from the discount_options_dict

    For each discount option in discount_options_dict, checks if the user_dict
    contains an entry for it and if it is True, then saves the corresponding
    discount percentage from the discount_options_dict.

    returns:
        the updated price based on the single maximum discount percentage
        (rounded to 2 decimal places).
        Otherwise, returns the original price.
    """
    discount_list = []
    for key in discount_options_dict:
        # print(..., end=": ") ### DEBUGGING
        if key in user_dict:
            # print(user_dict[...])  ### DEBUGGING
            if user_dict[key]:
                discount_list.append(discount_options_dict[key])

    if discount_list == []:
        return base_price
    else:
        discount = max(discount_list)
        return round(base_price * (1 - discount/100), 2)


def compute_price(base_price, discount_options_dict, user_dict):
    """
    param: base_price (float) - the price without any discounts
    param: discount_options_dict (dict) - maps the strings that
            name the different discounts, e.g., ("Student", "Military"),
            to the corresponding discount percentages, e.g., (30, 20)
    param: user_dict (dict) - contains the user information, where the
            keys include "age" and values from discount_options_dict

    Custom helper functions:
    - compute_price_using_age
    - compute_price_using_status_max

    returns:
    a negative value if either of the helper functions resulted in an error;
    otherwise, returns the updated price with the applied discount:
    this price is the minimum of base_price, age_price and status_price
    """
    age_price = compute_price_using_age(base_price, user_dict)
    status_price = compute_price_using_status_max(
        base_price, discount_options_dict, user_dict)
    final_price = min(base_price, age_price, status_price)

    if age_price == -1:
        return -1

    # print("User info", user_dict) ### DEBUGGING
    # print("Discounts", discount_options_dict) ### DEBUGGING
    # print("Prices", base_price, age_price, status_price) ### DEBUGGING
    # print(final_price)

    return final_price


def generate_ID(collection, offset):
    """
    param: collection (dict) - a collection of items that works with max()
    param: offset (int) - an integer offset that's added to the first ID.

    If the collection is empty, then the first ID is the offset value.
    Otherwise, the function retrieves the max value from the collection,
    and returns its value+1.

    returns:
    The computed ID, based on the offset or the max element in the collection.
    If max value is not an integer, the function returns an error string:
    "Error, non-integer IDs"

    For example, calling the function with
    {} and 0 as the offset should return 0, since the collection is empty
    and 0 is the offset;
    {} and 1000 as the offset should return 1000.
    {500: (16.5, None)} and 1000 as the offset should return 501, since the
    collection is not empty and 500 (the dict key) is the max value.
    """
    if len(collection) == 0:
        return offset

    if type(max(collection)) != int:
        return "Error, non-integer IDs"

    return max(collection) + 1


def add_order(all_orders, price, user_dict, offset):
    """
    The function expects
    param: all_orders (dict) - a dictionary that contains ticket orders
    param: price (float) - a float that's >=0
    param: user_dict (dict) - stores the integer "age" and the status of
            the discount options
    param: offset (int) - an integer that's needed by the generate_ID()

    The function stores the offset as the key that maps to the tuple containing
    two elements: the price and the user_dict. The function should not modify
    the all_orders dictionary.

    Helper function:
    - generate_ID() to store the order ID

    returns: either an error from the generate_ID() or a NEW dictionary with
        the created order.
    """
    new_id = generate_ID(all_orders, offset)
    if type(new_id) == str:
        return new_id

    return {new_id: (price, user_dict)}


def input_user_info(discount_options_dict):
    """
    param: discount_options_dict (dict) - contains strings,
            naming the different discounts, e.g., ("Student", "Military")
            and the corresponding discount percentages

    Calls the input() to collect the user info:
    - age
    - string values for each discount in discount_options_dict

    Custom helper functions:
    - convert_yes_no
    - construct_discounts_dict

    returns:
    a dictionary, storing the "age" with the corresponding integer and
    boolean flags for each of the discount_options_dict.
    Otherwise, returns
    -1 if the age is an invalid integer;
    -2 if the number of discount flags does not match the number of
        options in discount_options_dict;
    """
    input_age = input("::: Enter the buyer's age (in years :-)): ")
    if not input_age.isdigit():
        print(f"WARNING: '{input_age}' is an invalid age.\n")
        return -1
    user_age = int(input_age)

    print("::: Enter y or n (separated by spaces) for the following fields:\n::: ", end="")
    for option in discount_options_dict:
        print(option, end="? ")
    print()
    discount_flags_str = input("> ")  # get and process the data into a list
    discount_flags_str_list = discount_flags_str.split()
    if len(discount_flags_str_list) != len(discount_options_dict):
        print(
            f"WARNING: you provided {len(discount_flags_str_list)} options instead of the expected {len(discount_options_dict)}.\n")
        return -2

    discount_flags_bool_list = []
    # Assume that there is no need to remove the excess whitespace
    for flag in discount_flags_str_list:  # flag.strip()
        discount_flags_bool_list.append(convert_yes_no(flag))

    discounts_dict = construct_discounts_dict(
        discount_options_dict, discount_flags_bool_list)

    user_dict = {"age": user_age}
    user_dict.update(discounts_dict)

    return user_dict
