from PySimpleGUI import PySimpleGUI as sg
import biblioteca as b

h = 6
w = 2
visor = '0'
sg.theme('BlueMono')

layout = [
    [sg.Text(visor, size=(39,w), justification='right', background_color='white', key='tela')],
    [sg.Button('C', size=(h,w), enable_events=True), sg.Button('x²', size=(h,w), enable_events=True), sg.Button('√x', size=(h,w), enable_events=True), sg.Button('/', size=(h,w), enable_events=True), sg.Button('←', size=(h,w), enable_events=True)],
    [sg.Button('7', size=(h,w), enable_events=True), sg.Button('8', size=(h,w), enable_events=True), sg.Button('9', size=(h,w), enable_events=True), sg.Button('*', size=(h,w), enable_events=True), sg.Button('sin(x)', size=(h,w), enable_events=True)],
    [sg.Button('4', size=(h,w), enable_events=True), sg.Button('5', size=(h,w), enable_events=True), sg.Button('6', size=(h,w), enable_events=True), sg.Button('+', size=(h,w), enable_events=True), sg.Button('cos(x)', size=(h,w), enable_events=True)],
    [sg.Button('1', size=(h,w), enable_events=True), sg.Button('2', size=(h,w), enable_events=True), sg.Button('3', size=(h,w), enable_events=True), sg.Button('-', size=(h,w), enable_events=True), sg.Button('tan(x)', size=(h,w), enable_events=True)],
    [sg.Button('+/-', size=(h,w), enable_events=True), sg.Button('0', size=(h,w), enable_events=True), sg.Button(',', size=(h,w), enable_events=True), sg.Button('=', size=(14,w), enable_events=True)]
]

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    elif event == '1' or event == '2' or event == '3' or event == '4' or event == '5' or event == '6' or event == '7' or event == '8' or event == '9' or event == '0':
        if visor == '0':
            visor = event
        else:
            visor += event

    elif event == 'C':
        visor = b.resetaVisor()

    elif event == '+/-':
        visor = b.trocaSinalVisor(visor)

    elif event == '←':
        visor = b.apagaVisor(visor)
    
    window['tela'].update(visor)


window.close()