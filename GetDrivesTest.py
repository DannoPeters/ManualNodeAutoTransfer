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