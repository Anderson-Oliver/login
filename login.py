import PySimpleGUI as sg

# layout
sg.theme('TanBlue')
layout = [
    [sg.Text('Nome'),sg.Input(key='nome',size=(25,3))],
    [sg.Text('Senha'),sg.Input(key='senha',size=(25,3))],
    [sg.Button('Enter'),sg.Button('Sair')]
]

# janela
janela = sg.Window('Tela de login',layout)
# ler s eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break