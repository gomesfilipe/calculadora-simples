import re
import regex as r
class Calculator:
    def __init__(self):
        self.degree = True
        self.visor = '0'
        self.last_buttom = None
        self.operation = None
        self.operations = {
            '+': self.op_sum,
            '-': self.op_sub,
            '*': self.op_mult,
            '/': self.op_div
        }

    def op_sum(self, a, b):
        self.visor = str(a + b)
        return a + b

    def op_sub(self, a, b):
        self.visor = str(a - b)
        return a - b

    def op_mult(self, a, b):
        self.visor = str(a * b)
        return a * b

    def op_div(self, a, b):
        self.visor = str(int(a / b))
        return int(a / b)

    def write_visor(self, char):
        if self.is_op(char): # se caractere é um operando
            if self.visor_only_number():
                self.visor = self.visor + char # concatenando operando com operador
                self.operation = char
                self.last_buttom = char

            elif self.visor_number_operation():
                self.visor = self.visor.replace(self.operation, char)
                self.operation = char
                self.last_buttom = char

        elif is_number(char): # se caractere é um numero
            if self.visor == '0' or self.last_buttom == '=':
                self.visor = char
                self.last_buttom = char
            else:
                self.visor = self.visor + char # concatenando operando com operador
                self.last_buttom = char
        
        elif char == 'C':
            self.reset_visor()
            self.last_buttom = char
        
        elif char == '=':
            self.result_visor()
            self.visor = clear_zeros(self.visor)
            self.last_buttom = char
        
        elif char == '←':
            if len(self.visor) == 1:
                self.reset_visor()
                self.last_buttom = char
            else:
                self.visor = self.visor[:len(self.visor) - 1]
                self.last_buttom = char
        
        elif char == '+/-':
            if self.visor_only_number():
                self.visor = str(float(self.visor) * (-1))
                self.last_buttom = char

        elif char == '.':
            if self.visor_only_int_number() or self.visor_number_operation_int_number():
                self.visor = self.visor + char
                self.last_buttom = char

    def reset_visor(self):
        self.visor = '0'

    def result_visor(self):
        if self.visor_number_operation_number():
            numbers = self.visor.split(self.operation)
            self.operations[self.operation](float(numbers[0]), float(numbers[1]))

    def is_op(self, char):
        if char in self.operations:
            return True
        return False

    def visor_only_int_number(self):
        regex = '^' + r.number_int() + '$'
        return bool(re.match(regex, self.visor))

    def visor_only_number(self):
        regex = '^' + r.number() + '$'
        return bool(re.match(regex, self.visor))

    def visor_number_operation(self):
        regex = '^' + r.number_and_operand() + '$'
        return bool(re.match(regex, self.visor))

    def visor_number_operation_number(self):
        regex = '^' + r.number_and_operand_and_number() + '$'
        return bool(re.match(regex, self.visor))

    def visor_number_operation_int_number(self):
        regex = '^' + r.number_and_operand_and_int_number() + '$'
        return bool(re.match(regex, self.visor))

def is_number(char):
    try:
        number = int(char)
        return 0 <= number and number <= 9

    except:
        return False

def clear_zeros(string):
    index = string.find('.')
    if index == -1:
        return string

    for i in string[index + 1:]:
        if i != '0':
            return string

    return string[:index]
