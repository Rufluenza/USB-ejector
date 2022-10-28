import sys
import os
import platform
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QFont


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('USB Ejector')

        self.layout = QVBoxLayout()

        self.usb_list = self.get_usb_devices()

        for usb in self.usb_list:
            self.layout.addWidget(self.make_usb_box(usb))

        self.setLayout(self.layout)

        self.show()

    def get_usb_devices(self):
        devices = []
        if platform.system() == 'Linux':
            for device in os.listdir('/dev'):
                if device.startswith('sd'):
                    # if device is not in blacklist.txt then add it to devices list
                    read_blacklist = open('blacklist.txt', 'r')
                    blacklist = read_blacklist.readlines()
                    read_blacklist.close()
                    if device not in blacklist:
                        devices.append((device, '/dev/'+device))
                    #devices.append((device, '/dev/'+device))
        elif platform.system() == 'Windows':
            for device in os.listdir('/media'):
                devices.append((device, '/media/'+device))
        elif platform.system() == 'Darwin':
            for device in os.listdir('/Volumes'):
                if device != 'Macintosh HD' and device != 'Time Machine Backups':
                    devices.append((device, '/Volumes/'+device))
        return devices

    def make_usb_box(self, usb):
        box = QWidget()
        box_layout = QVBoxLayout()
        
        name = QLabel(usb[0])
        size_used = QLabel(str(os.path.getsize(usb[1])))

        # convert size_used to human readable format
        size_used.setText('{:.2f} MB'.format(int(size_used.text())/1024/1024))
        eject_button = QPushButton('Eject')

        box_layout.addWidget(name)
        box_layout.addWidget(size_used)
        box_layout.addWidget(eject_button)

        box.setLayout(box_layout)

        eject_button.clicked.connect(lambda: self.eject_usb(usb))

        return box
    
    def update_gui(self):
        self.layout = QVBoxLayout()
        for usb in self.usb_list:
            self.layout.addWidget(self.make_usb_box(usb))
        self.setLayout(self.layout)
        self.show()

    def eject_usb(self, usb):
        confirm = QMessageBox.question(self, 'Confirm', 'Are you sure you want to eject '+usb[0]+'?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            if platform.system() == 'Linux':
                os.system('eject '+usb[1])
            elif platform.system() == 'Windows':
                os.system('eject '+usb[1])
            elif platform.system() == 'Darwin':
                os.system('diskutil umount '+usb[1])

            QMessageBox.information(self, 'Success', usb[0]+' ejected successfully!')
            
            # update the list of usb devices and update the gui
            # first delete the old list of usb devices
            del self.usb_list[:]
            self.usb_list = self.get_usb_devices()
            # if the usb device is the last one then close the gui
            if len(self.usb_list) == 0:
                self.close()
            else:
                # remove all widgets from the layout
                for i in reversed(range(self.layout.count())):
                    self.layout.itemAt(i).widget().setParent(None)
                # then call the make_usb_box function to add the new list of usb devices
                for usb in self.usb_list:
                    self.layout.addWidget(self.make_usb_box(usb))
                
                self.update_gui()
            
        elif confirm == QMessageBox.No:
            QMessageBox.information(self, 'Cancelled', usb[0]+' not ejected.')
        else:
            QMessageBox.critical(self, 'Error', 'An error occured while ejecting '+usb[0]+'.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())
