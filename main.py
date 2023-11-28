from functions import *

all_orders = {
    'L': 'List orders',
    'O': 'Order a ticket',
    'C': 'Compute statistics',
    'Q': 'Quit this program'
}

# Hard-coded sample values
discount_options_dict = {"Student": 30, "Military": 25, "First-responder": 20}
BASE_PRICE = 16.50
OFFSET = 1000  # used to generate the IDs for orders

opt = None

while True:
    print("What would you like to do?")
    print_options(all_orders)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper()  # to allow users to input lower- or upper-case letters

    if opt not in all_orders:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected {opt} to {all_orders[opt]}.")

    if opt == "Q":
        print("Goodbye!\n")
        break

    elif opt == 'L':
        print_orders(all_orders, show_user=True)

    elif opt == 'O':
        user_info = input_user_info(discount_options_dict)
        if type(user_info) == dict:
            result = compute_price(
                BASE_PRICE, discount_options_dict, user_info)
            if result < 0:
                print(
                    f"WARNING: something went wrong when saving this order.\nError code: {result}")
            else:
                print(f"::: Success! Sold for ${result:.2f}")
                result = add_order(all_orders, result, user_info, OFFSET)
                if type(result) == dict:
                    print("::: Successfully saved the order.")
                    print(result)  # DEBUGGING
                    all_orders.update(result)
                else:
                    # print the error
                    print(
                        f"WARNING: something went wrong when storing this order.\nError code: {result}")
                # print(all_orders) ### DEBUGGING - verify that it was updated
        else:
            print(f"WARNING: user info was not input correctly.\n"
                  f"Error code: {user_info}")

    # ----------------------------------------------------------------
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")
