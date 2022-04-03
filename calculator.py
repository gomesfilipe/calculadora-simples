import re

class Calculator:
    def __init__(self):
        self.degree = True
        self.visor = '0'
        self.size = 1
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
        if is_op(char): # se caractere é um operando
            if bool(re.match('^\-?\d+$', self.visor)):
                self.visor = self.visor + char # concatenando operando com operador
                # self.size = self.size + 1
                self.operation = char

            elif bool(re.match('^\-?\d+[+\-*/]$', self.visor)):
                self.visor = self.visor.replace(self.operation, char)
                self.operation = char

        elif is_number(char): # se caractere é um numero
            if self.visor == '0':
                self.visor = char
            else:
                self.visor = self.visor + char # concatenando operando com operador
                # self.size = self.size + 1
        
        elif char == 'C':
            self.reset_visor()
        
        elif char == '=':
            self.result_visor()
        
        elif char == '←':
            if len(self.visor) == 1:
                self.reset_visor()
            else:
                self.visor = self.visor[:len(self.visor) - 1]
        
        elif char == '+/-':
            if bool(re.match('^\-?\d+$', self.visor)):
                self.visor = str(int(self.visor) * (-1))

    def reset_visor(self):
        self.visor = '0'

    def result_visor(self):
        if bool(re.match('^\-?\d+[+\-*/]\d+$', self.visor)):
            numbers = self.visor.split(self.operation)
            self.operations[self.operation](int(numbers[0]), int(numbers[1]))

def is_op(char):
        return char == '+' or char == '-' or char == '*' or char == '/'

def is_number(char):
    return char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'
        