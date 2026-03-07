# task_1_modules

def plus(num_1: float, num_2: float)-> float:
    return num_1 + num_2

def minus(num_1: float, num_2: float)-> float:
    return num_1 - num_2

def division(num_1: float, num_2: float)-> float:
    return num_1 / num_2
    
def multiply(num_1: float, num_2: float)-> float:
    return num_1 * num_2

# task_2_modules

def word_upper(word: str)-> str:
    return word.upper()

def is_palindrom(word: str)-> bool:
    return word == word[::-1]

# task_3_modules

def multiply_list_by_7(nums: list)-> list:
    result = []
    for num in nums:
        result.append(multiply(num, 7))
    return result

# task_4_modules

def sum_dict(dict_1: dict, dict_2: dict)-> dict:
    result = dict_1
    for key, value in dict_2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value   
    return result     

# task_5_modules

def is_positive_num(num: float)-> bool:
    if num < 0:
        raise ValueError("число менше нуля")
    else:
        return True