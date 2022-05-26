import shutil
import os
import datetime
dt = datetime.datetime.now()
date = str(datetime.date(dt.year, dt.month, dt.day))
shutil.copy('NodeSD/ExampleData.dat','ExampleHardDrive')
if not os.path.isdir('NodeSD/DannoAutoTransfer_'+ date):
    os.mkdir('NodeSD/DannoAutoTransfer_'+ date)
shutil.copy('NodeSD/ExampleData.dat','NodeSD/DannoAutoTransfer_'+ date)