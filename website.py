import streamlit as st
import os


password = 'pswd'

dev = {}
devs = {}
def get_usb():
    i = 0      
    for dev in os.listdir('/dev/disk/by-label'):
        if dev != "ESP" and dev != "EFI":
            i += 1
            # l = os.path.realpath('/dev/disk/by-label/'+dev)
            l = '/dev/disk/by-label/'+dev
            devs[i] = l

    return devs



st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():

    for i in range(len(get_usb())):
        # all_names = get_name()[i]
        st.write(get_usb()[i+1].split('/')[-1])
        st.container() # make a container for each device
        if st.button('Eject' + ' ' + get_usb()[i+1].split('/')[-1]):
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            if os.system('echo '+password+' | sudo -S eject -F '+get_usb()[i+1]) == 0: # if the command is successful maybe delete the if statement "sudo -S umount" on linux
                st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])
                st.write('Reload the page to see the changes')

if __name__ == "__main__":
    main()
