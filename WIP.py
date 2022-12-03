# THIS IS THE WORK IN PROGRESS FILE
import streamlit as st
import os
import subprocess as sp

dev = {}
devs = {}
sdx = {}
sdx_list = {}

def get_usb():
    i = 0
    #tempo = sp.Popen("ls /dev/disk/by-label", shell=True).wait()
    #tempo = sp.Popen("ls /dev/disk/by-label", shell=True, stdout=sp.PIPE).communicate()[0].decode('utf-8').split(' ')
    list_of_usb = sp.Popen("ls /dev/disk/by-label | awk '{print $1}' > output.txt ", shell=True).wait()
    
    read_file = open(r'output.txt', 'r')
    
    for line in read_file:
        if line != r"ESP":
            i = i+1
            devs[i] = line
    #length = len(list_of_usb)
    

    return devs


# now we want to eject the file system to do that we need to find the sda or sdb or sdc etc we do that by using the os module
def get_sdx():
    i = 0
    # only get the file system from the devs device name and save it to a list
    for i in range(len(get_usb())):
        sdx_list[i] = get_usb()[i+1]
        #usb_name = get_usb()[i+1]
        #sdx = sp.Popen("df -h /dev/disk/by-label/"+usb_name+" | grep -v 'Filesystem' | awk '{print $1}'", shell=True).wait()
        #sdx = os.system("df -h /dev/disk/by-label/"+usb_name+" | grep -v 'Filesystem' | awk '{print $1}'")
        

        #print(sdx)
        sdx_list[i] = sdx
    return sdx_list
    



st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():
    for i in range(len(get_usb())):
        l = str(i)
        st.write(get_usb()[i+1].split('/')[-1])
        usb_eject = get_usb()[i+1]
        usb_eject = (usb_eject)
        
        st.container()
        l = st.button('Eject ' + 'Nr. '+l+' ' + get_usb()[i+1].split('/')[-1])
        if l:
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            os.system('udisksctl unmount --block-device /dev/disk/by-label/'+usb_eject)
            if os.system('udisksctl power-off --block-device /dev/disk/by-label/'+usb_eject) == 0:
                st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])
                st.write('Reload the page to see the changes.  ')
                # refresh the page from the server side

    
if __name__ == "__main__":
    main()
