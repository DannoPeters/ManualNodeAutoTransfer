import pyudev
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink()
# For USB devices
monitor.filter_by(susbsytem='usb')
# OR specifically for most USB serial devices
monitor.filter_by(susbystem='tty')
for action, device in monitor:
    vendor_id = device.get('ID_VENDOR_ID')
    # I know the devices I am looking for have a vendor ID of '22fa'
    if vendor_id in ['22fa']:
        print('Detected {} for device with vendor ID {}'.format(action, vendor_id))