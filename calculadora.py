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
    
    elif event.isnumeric():
        if visor == '0':
            visor = event
        else:
            if visor == 'Entrada inválida': visor = ''
            visor += event

    elif event == 'C':
        visor = b.resetaVisor()

    elif event == '+/-' and visor != 'Entrada inválida':
        visor = b.trocaSinalVisor(visor)

    elif event == '←' and visor != 'Entrada inválida':
        visor = b.apagaVisor(visor)
    
    elif b.ehOperacaoTipo1(event) and visor != 'Entrada inválida':
        if event == 'sin(x)': funcao = b.seno
        elif event == 'cos(x)': funcao = b.cosseno
        elif event == 'tan(x)': funcao = b.tangente
        elif event == 'x²': funcao = b.quadrado
        elif event == '√x': funcao = b.raiz

        visor = b.operacaoTipo1(funcao, visor)

    window['tela'].update(visor)


window.close()