from PySimpleGUI import PySimpleGUI as sg
from calculator import Calculator

class Interface:
    def __init__(self):
        h = 6
        w = 2
        sg.theme('BlueMono')
        self.calculator = Calculator()
        self.visor = sg.Text(self.calculator.visor, size=(39,1), justification='right', background_color='white', key='visor', text_color='black')
        self.zero = sg.Button('0', size=(h, w), enable_events=True)
        self.one = sg.Button('1', size=(h, w), enable_events=True)
        self.two = sg.Button('2', size=(h, w), enable_events=True)
        self.three = sg.Button('3', size=(h, w), enable_events=True)
        self.four = sg.Button('4', size=(h, w), enable_events=True)
        self.five = sg.Button('5', size=(h, w), enable_events=True)
        self.six = sg.Button('6', size=(h, w), enable_events=True)
        self.seven = sg.Button('7', size=(h, w), enable_events=True)
        self.eight = sg.Button('8', size=(h, w), enable_events=True)
        self.nine = sg.Button('9', size=(h, w), enable_events=True)
        self.reset = sg.Button('C', size=(h, w), enable_events=True)
        self.equals = sg.Button('=', size=(h, w), enable_events=True)
        self.sum = sg.Button('+', size=(h, w), enable_events=True)
        self.sub = sg.Button('-', size=(h, w), enable_events=True)
        self.mult = sg.Button('*', size=(h, w), enable_events=True)
        self.div = sg.Button('/', size=(h, w), enable_events=True)
        self.backspace = sg.Button('←', size=(h, w), enable_events=True)
        self.reverse = sg.Button('+/-', size=(h, w), enable_events=True)

        self.layout = [
            [self.visor],
            [self.seven, self.eight, self.nine, self.sum, self.reset], 
            [self.four, self.five, self.six, self.sub, self.backspace], 
            [self.one, self.two, self.three, self.mult], 
            [self.reverse, self.zero, self.equals, self.div]
        ]

    def run_calculator(self):
        window = sg.Window('Calculadora', self.layout)

        while True:
            event, values = window.read() # captura eventos

            if event == sg.WIN_CLOSED:
                break
            else:
                self.calculator.write_visor(event)
            
            window['visor'].update(self.calculator.visor)

        window.close()

interface = Interface()
interface.run_calculator()
