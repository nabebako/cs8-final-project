from functions import *

# DEBUGGING - an example of what all_orders might look like

assert convert_yes_no('y') == True
assert convert_yes_no('z') == False
assert construct_discounts_dict({"Student": 30}, [False]) == {'Student': False}
assert construct_discounts_dict({"Student": 30, "First-responder": 25}, [
                                False, False]) == {'Student': False, 'First-responder': False}

test_user_student = {'age': 19, 'Student': True,
                     'Military': False, 'Teacher': False}
test_user_teacher = {'age': 33, 'Student': False,
                     'Military': False, 'Teacher': True}
test_user_basic = {'age': 33, 'Student': False,
                   'Military': False, 'Teacher': False}

discount_options_dict = {"Student": 30, "Military": 25, "Teacher": 20}
BASE_PRICE = 15.0

assert compute_price(BASE_PRICE, discount_options_dict,
                     test_user_basic) == BASE_PRICE

expected_discount = discount_options_dict["Teacher"]
expected_price = BASE_PRICE * (1-expected_discount/100)
assert compute_price(BASE_PRICE, discount_options_dict,
                     test_user_teacher) == expected_price

expected_discount = discount_options_dict["Student"]
expected_price = BASE_PRICE * (1-expected_discount/100)
assert compute_price(BASE_PRICE, discount_options_dict,
                     test_user_student) == expected_price


assert generate_ID({500: (16.5, None)}, 1000) == 501


test_user_student = {'age': 19, 'Student': True,
                     'Military': False, 'Teacher': False}
test_user_teacher = {'age': 33, 'Student': False,
                     'Military': False, 'Teacher': True}
BASE_PRICE = 15.0

assert add_order({10: (BASE_PRICE, test_user_student),
                  11: (BASE_PRICE, test_user_student)}, BASE_PRICE, test_user_teacher, 600) == {12: (15.0, {'age': 33, 'Student': False, 'Military': False, 'Teacher': True})}
