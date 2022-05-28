import PySimpleGUI as sg

sg.theme('Dark2')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Instructions', button_color='black'),],
            [sg.Text('Start Date UTC: '), sg.InputText(default_text="YYYY-MM-DD"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d")],
            [sg.Text('End Date UTC: '), sg.InputText(default_text="YYYY-MM-DD"), sg.CalendarButton(button_text="Choose Date", format = "%Y-%m-%d")],
            [sg.Text('Select Drives NOT to query: '), sg.Checkbox(text="C:", text_color="white"), sg.Checkbox(text="D:", text_color="white"), sg.Checkbox(text="E:", text_color="white")],
            [sg.Text('Node Dump Location: '), sg.InputText(default_text=""), sg.FolderBrowse(button_text = "Browse")],
            [sg.Button('Start Querying', button_color='dark green'), sg.Button('Stop Querying', button_color='dark orange'), sg.Button('Finish Copying & Exit', button_color='dark red')] ]

# Create the Window
window = sg.Window('DIAS Automated Manual Dumping', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Start Querying':
        print("Starting Query")
    if event == 'Stop Querying':
        print("Stopping Query")
    if event == sg.WIN_CLOSED or event == 'Finish Copying & Exit': # if user closes window or clicks cancel

        break

window.close()
