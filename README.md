
<!-- USB Ejector -->
## Quick start

This is a USB ejector GUI, made for Windows, Linux and Mac.
It detects the USB devices so you only have to click under the name of the device to eject it.
I have made sure that on Mac it does not detect the Macintosh HD and Time Machine Backups.

### Prerequisites

You will need the python library PyQt5.
To download it open terminal and type in:
* Terminal
  ```sh
  pip install PyQt5
  ```
if you have any errors try pip3 instead.
* Terminal
  ```sh
  pip3 install PyQt5
  ```
### Location of scripts
You will also need to set the usb-eject.sh on your Desktop  
And the python script in Downloads  

## TO-DO
Blacklist drives so it only shows USB devices on linux.  
The size of the usb device shown is currently only the used space not the total space.  
Change the user script to find the python program by itself.

### Current known issues
python crashing after device is ejected,  
ie. only one device can be ejected before having to restart the program.  
