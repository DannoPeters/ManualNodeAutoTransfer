import PySimpleGUI as sg
import os
import platform

#Check OS of User
operatingSystem = platform.system()

if operatingSystem == 'Darwin': #Mac
    drives = os.listdir('/Volumes')
    print(drives)

if operatingSystem == 'Linux': #Linux
    print(os.listdir('/Volumes'))

if operatingSystem == 'Windows': #Windows
    import os.path
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    print(drives)

driveCheckboxes = [sg.Checkbox(drives[i], key=drives[i], background_color = "grey25", text_color = "snow") for i in range(len(drives))]

sg.theme('Dark2')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Instructions', button_color='black'), sg.Text('       Select Language', key='selectLanguageLabel'), sg.Button('🇬🇧English', button_color='grey30'), sg.Button('🇪🇸Español', button_color='grey30'),],
            [sg.Text('Start Date UTC: ', key='startDateLabel'), sg.InputText(default_text="YYYY-MM-DD", key="startDate"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d", button_color='orange red', locale = 'fr_FR'), sg.Text('', key='startDateError')],
            [sg.Text('End Date UTC: ', key='endDateLabel'), sg.InputText(default_text="YYYY-MM-DD", key="endDate"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d", button_color='orange red', locale = 'es_ES'), sg.Text('', key='endDateError')],
            [sg.Text('Select Drives NOT to query: ', key='drivesLabel')],
            [driveCheckboxes],
            [sg.Text('Node Dump Location: ', key='outputLocLabel'), sg.InputText(default_text="", key="outputLoc"), sg.FolderBrowse(button_text = "Browse", button_color='orange red'), sg.Text('', key='outputLocError')],
            [sg.Button('Start Querying', button_color='dark green', key='startButton'), sg.Button('Stop Querying', button_color='dark orange', key='stopButton'), sg.Button('Finish Copying & Exit', button_color='dark red', key='exitButton')],
            [sg.Text('')],
            [sg.ProgressBar(100, orientation='horizontal', key="progressSD"), sg.Text('Files on SD')],
            [sg.ProgressBar(100, orientation='horizontal', key="progressFile"), sg.Text('Specific File')],
            [sg.Text('E: Drive Complete')]
            ]

# Create the Window
window = sg.Window('DIAS Automated Manual Dumping', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == '🇪🇸Español':
        window['selectLanguageLabel'].update('Seleccione El Idioma')
        window['startDateLabel'].update('Día Inicio UTC')
        if values['startDate'] == 'YYYY-MM-DD':
            window['startDate'].update("AAAA-MM-DD")
        window['endDateLabel'].update('Día Final UTC')
        if values['endDate'] == 'YYYY-MM-DD':
            window['endDate'].update("AAAA-MM-DD")
        window['drivesLabel'].update('Seleccionar discos miembros para NO buscar')
        window['outputLocLabel'].update('Ubicación De Transferencia De Archivos')


    if event == 'Instructions': #Maybe add this as a side panel, or include screenshot images in instructions
        print("Requested Instructions")
        sg.popup('Instructions')

    if event == 'Start Querying':
        print("Starting Query")
        inputErrorTxt = ""
        if values['startDate'] == 'YYYY-MM-DD':
            inputErrorTxt += "Please input a Start Date to Query from\n"
            window['startDate'].update(background_color='pink')
            window['startDateError'].update('Error: Please Enter a Start Date', text_color = 'red')
        else:
            window['startDate'].update(background_color='snow')
            window['startDateError'].update('')
        if values['endDate'] == 'YYYY-MM-DD':
            inputErrorTxt += "Please input a Start Date to Query up to\n"
            window['endDate'].update(background_color='pink')
            window['endDateError'].update('Error: Please Enter an End Date', text_color = 'red')
        else:
            window['endDate'].update(background_color='snow')
            window['endDateError'].update('')
        if values['outputLoc'] == '':
            inputErrorTxt += "Please input a destination to save node files to\n"
            window['outputLoc'].update(background_color='pink')
            window['outputLocError'].update('Error: Please Enter an Output Location', text_color = 'red')
        else:
            window['outputLoc'].update(background_color='snow')
            window['outputLocError'].update('')
        if inputErrorTxt != "":
            window.refresh()
            #sg.popup(inputErrorTxt) #Popup disabled and pink bacgrounds added
        print(values)

    if event == 'Stop Querying':
        print("Stopping Query")

    if event == 'Finish Copying & Exit':
        #Add code to graceful exit
        break

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()
