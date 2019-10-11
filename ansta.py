# Zadanie 1

def post_code_generator(arg1, arg2):

    list_of_codes = []
    in_arg1 = int(arg1.replace('-', ''))
    in_arg2 = int(arg2.replace('-', ''))

    for i in range(in_arg1 + 1, in_arg2):
        result = str(i)
        result_with_dash = result[:2] + '-' + result[2:]
        list_of_codes.append(result_with_dash)

    return list_of_codes



# Zadanie 2

def what_is_missing(arg_list, n_el):

    input_set = set(arg_list)
    list_to_reference = set(range(1, n_el + 1))
    output_list = list(list_to_reference - input_set)

    return output_list



# Zadanie 3

from decimal import Decimal
import numpy as np

def list_of_decimals():

    generator_list_with_step = list(np.arange(2, 5.5, 0.5))
    result_list_with_decimals = [Decimal(x) for x in generator_list_with_step]

    return result_list_with_decimals
