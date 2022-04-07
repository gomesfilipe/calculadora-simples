def number_int():
    return '\-?\d+'

def number_float():
    return '\-?\d+\.\d+'

def number():
    return '\-?\d+(\.\d+)?'

def operand():
    return '[\+\-*/]'

def number_and_operand():
    return number() + operand()

def number_and_operand_and_number():
    return number() + operand() + number()

def number_and_operand_and_int_number():
    return number_and_operand() + number_int()
