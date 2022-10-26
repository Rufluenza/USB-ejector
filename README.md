
<!-- USB Ejector -->
## Quick start

This is a USB ejector GUI, made for Windows, Linux and Mac
it detects the usb devices so you only have to click under the name of the device to eject it.
I have made sure that on mac it does not detect the Macintosh HD and Time Machine Backups

### Prerequisites

You will need the python library PyQt5.
To download it open terminal and type in:
* Terminal
  ```sh
  pip install PyQt5
  ```
if you have any errors try pip3 instead
* Terminal
  ```sh
  pip3 install PyQt5
  ```
### current known issues
python crashing after device is ejected, 
 - ie. only one device can be ejected before having to restart the program  -
No user readable name on device on linux (name of the device on linux is sdb)  
The size of the usb device shown is currently only the used space not the total space
