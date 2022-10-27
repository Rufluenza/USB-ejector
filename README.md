
<!-- USB Ejector -->
## Quick start

This is a USB ejector GUI, made for Windows, Linux and Mac.
It detects the USB devices so you only have to click under the name of the device to eject it.
I have made sure that on Mac it does not detect the Macintosh HD and Time Machine Backups.  

### Screenshots
<img width="215" alt="Screenshot 2022-10-27 at 10 55 50" src="https://user-images.githubusercontent.com/39049727/198242006-3a068644-c410-4bf6-81db-77d437318b1c.png">
<img width="426" alt="Screenshot 2022-10-27 at 10 56 12" src="https://user-images.githubusercontent.com/39049727/198242012-a63ec82f-f19f-4555-9747-497352d656b2.png">
<img width="373" alt="Screenshot 2022-10-27 at 10 56 20" src="https://user-images.githubusercontent.com/39049727/198242013-8e99972d-fa82-4678-92b6-0bd9a7fb2af0.png">  


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
