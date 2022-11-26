import streamlit as st
import os



dev = {}
devs = {}
def get_usb():
    i = 0
    for dev in os.listdir('/Volumes'):
        if dev != 'Macintosh HD' and dev != 'Time Machine Backups':
            i += 1
            devs[i] = '/Volumes/'+dev
   
    return devs


# st.write(get_usb())




st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():

    for i in range(len(get_usb())):
        # all_names = get_name()[i]
        st.write(get_usb()[i+1].split('/')[-1])
        st.container() # make a container for each device
        if st.button('Eject' + ' ' + get_usb()[i+1].split('/')[-1]):
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            if os.system('diskutil eject '+get_usb()[i+1]) == 0: # if the command is successful maybe delete the if statement "sudo -S umount" on linux
                st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])

if __name__ == "__main__":
    main()








# make a web page with all the devices listed

