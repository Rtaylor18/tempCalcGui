#temperature converter using PySimpleGUI to create a quick and dirty temperature converter

import PySimpleGUI as sg

sg.theme("Python")

layout = [[sg.Text('Choose to convert to Celsius or Fahrenheit'),sg.Radio('C', 1,default=True, key = '-IN-' ), sg.Radio('F', 1, key = '-IN2-')],
          [sg.Text('Temp to Convert'),sg.Input(s = 15, key = '-INPUT-')],
          [sg.Button('Convert'), sg.Button('Reset')]
        ]

window = sg.Window('Temperature Converter', layout)

running = True

while running:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        running = False
    
    if event == 'Reset':
        window['-INPUT-'].update('')

    if event == 'Convert':
        if values['-IN-'] == True:
            answer = values['-INPUT-']
            #(F - 32) * 5/9 = C
            newAnswer = (int(answer) - 32) * 5/9 
            window['-INPUT-'].update(newAnswer)
        if values['-IN2-'] ==  True:
            answer = values['-INPUT-']
            #(C * 9/5) + 32 = F
            newAnswer = (int(answer) * 9 / 5) + 32 
            window['-INPUT-'].update(newAnswer)