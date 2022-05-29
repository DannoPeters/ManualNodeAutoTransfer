import PySimpleGUI as sg
import os
import platform

#Check OS of User
operatingSystem = platform.system()
language = 'EN'

def checkInput(values):
    inputErrorTxt = ""
    if values['startDate'] == 'YYYY-MM-DD' or 'AAAA-MM-DD' or 'AAAA-MM-JJ':
        inputErrorTxt += "Please input a Start Date to Query from\n"
        window['startDate'].update(background_color='pink')
        errorMessage = 'Error: Please Enter a Start Date'
        if language == 'ES':
            errorMessage = 'Error: Ingrese Una Día De Inicio'
        elif language == 'FR':
            errorMessage = 'Erreur: Veuillez Saisir Une Date De Début'

        window['startDateError'].update(errorMessage, text_color='red')
    else:
        window['startDate'].update(background_color='snow')
        window['startDateError'].update('')
    if values['endDate'] == 'YYYY-MM-DD' or 'AAAA-MM-DD' or 'AAAA-MM-JJ':
        inputErrorTxt += "Please input a Start Date to Query up to\n"
        window['endDate'].update(background_color='pink')
        errorMessage = 'Error: Please Enter an End Date'
        if language == 'ES':
            errorMessage = 'Error: Ingrese Una Día De Final'
        elif language == 'FR':
            errorMessage = 'Erreur: Veuillez Saisir Une Date De Fin'
        window['endDateError'].update(errorMessage, text_color='red')
    else:
        window['endDate'].update(background_color='snow')
        window['endDateError'].update('')
    if values['outputLoc'] == '':
        inputErrorTxt += "Please input a destination to save node files to\n"
        window['outputLoc'].update(background_color='pink')
        errorMessage = 'Error: Please Enter an Output Location'
        if language == 'ES':
            errorMessage = 'Error: Ingrese Una Ubicación De Salida'
        elif language == 'FR':
            errorMessage = 'Erreur: Veuillez Saisir Un Emplacement De Sortie'
        window['outputLocError'].update(errorMessage, text_color='red')
    else:
        window['outputLoc'].update(background_color='snow')
        window['outputLocError'].update('')
    if inputErrorTxt != "":
        window.refresh()
        return False
    else:
        return True

def changeLanguage(window, code):
    if code == 'EN':
        window['instructions'].update('Instructions')
        window['selectLanguageLabel'].update('       Select Language')
        window['startDateLabel'].update('Start Date UTC: ')
        if values['startDate'] == 'AAAA-MM-JJ' or values['startDate'] == 'AAAA-MM-DD':
            window['startDate'].update("YYYY-MM-DD")
        window['endDateLabel'].update('End Date UTC: ')
        if values['endDate'] == 'AAAA-MM-JJ' or values['startDate'] == 'AAAA-MM-DD':
            window['endDate'].update("YYYY-MM-DD")
        window['drivesLabel'].update('Select Drives NOT to query: ')
        window['outputLocLabel'].update('Node Dump Location: ')
        window['startDateCal'].update('Choose Date')
        window['endDateCal'].update('Choose Date')
        window['browse'].update('Browse')
        window['startButton'].update('Start Query')
        window['stopButton'].update('Stop Query')
        window['exitButton'].update('Finish Copying & Exit')

    elif code == 'ES':
        window['instructions'].update('Instrucciones')
        window['selectLanguageLabel'].update('       Seleccione El Idioma')
        window['startDateLabel'].update('Día Inicio UTC: ')
        if values['startDate'] == 'YYYY-MM-DD':
            window['startDate'].update("AAAA-MM-DD")
        window['endDateLabel'].update('Día Final UTC: ')
        if values['endDate'] == 'YYYY-MM-DD':
            window['endDate'].update("AAAA-MM-DD")
        window['drivesLabel'].update('Seleccionar discos miembros para NO buscar: ')
        window['outputLocLabel'].update('Ubicación De Transferencia De Archivos: ')
        window['startDateCal'].update('Elige Fecha')
        window['endDateCal'].update('Elige Fecha')
        window['browse'].update('Navegar')
        window['startButton'].update('Iniciar Búsqueda')
        window['stopButton'].update('Detener Búsqueda')
        window['exitButton'].update('Finalizar Descarga & Salir')

    elif code == 'FR':
        window['instructions'].update('Instructions')
        window['selectLanguageLabel'].update('       Choisir La Langue')
        window['startDateLabel'].update('Date De Début UTC: ')
        if values['startDate'] == 'YYYY-MM-DD' or values['startDate'] == 'AAAA-MM-DD':
            window['startDate'].update("AAAA-MM-JJ")
        window['endDateLabel'].update('Date De Fin UTC: ')
        if values['endDate'] == 'YYYY-MM-DD' or values['startDate'] == 'AAAA-MM-DD':
            window['endDate'].update("AAAA-MM-JJ")
        window['drivesLabel'].update('Sélectionnez Les Disque Á Ne Pas Interroger: ')
        window['outputLocLabel'].update('Emplacement De Transfert De Fichiers: ')
        window['startDateCal'].update('Choisir Date')
        window['endDateCal'].update('Choisir Date')
        window['browse'].update('Naviguer')
        window['startButton'].update('Démarrer Requête')
        window['stopButton'].update('Arrêter Requête')
        window['exitButton'].update('Terminer La Copie & Quitter')

    window.refresh()
    return

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
layout = [  [sg.Button('Instructions', button_color='black', key="instructions"), sg.Text('       Select Language', key='selectLanguageLabel'), sg.Button('🇬🇧English', button_color='grey30'), sg.Button('🇪🇸Español', button_color='grey30'), sg.Button('🇫🇷Français', button_color='grey30')],
            [sg.Text('Start Date UTC: ', key='startDateLabel'), sg.InputText(default_text="YYYY-MM-DD", key="startDate"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d", button_color='orange red', locale = 'fr_FR', key="startDateCal"), sg.Text('', key='startDateError')],
            [sg.Text('End Date UTC: ', key='endDateLabel'), sg.InputText(default_text="YYYY-MM-DD", key="endDate"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d", button_color='orange red', locale = 'es_ES', key="endDateCal"), sg.Text('', key='endDateError')],
            [sg.Text('Select Drives NOT to query: ', key='drivesLabel')],
            [driveCheckboxes],
            [sg.Text('Node Dump Location: ', key='outputLocLabel'), sg.InputText(default_text="", key="outputLoc"), sg.FolderBrowse(button_text = "Browse", button_color='orange red', key='browse'), sg.Text('', key='outputLocError')],
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
    print(event)

    if event == '🇪🇸Español':
        language = 'ES'
        changeLanguage(window, language)

    elif event == '🇬🇧English':
        language = 'EN'
        changeLanguage(window, language)

    elif event == '🇫🇷Français':
        language = 'FR'
        changeLanguage(window, language)


    if event == 'Instructions': #Maybe add this as a side panel, or include screenshot images in instructions
        print("Requested Instructions")
        sg.popup('Instructions')

    if event == 'startButton':
        print("Starting Query")
        if checkInput(values):
            pass #if input is good
        else:
            pass #dont try to start
            #sg.popup(inputErrorTxt) #Popup disabled and pink bacgrounds added
        print(values)

    if event == 'stopButton':
        print("Stopping Query")

    if event == 'exitButton':
        #Add code to graceful exit
        break

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()
