import streamlit as st
import os

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
        l = str(i)
        st.write(get_usb()[i+1].split('/')[-1])
        st.container() # make a container for each device
        l = st.button('Eject' + ' ' + get_usb()[i+1].split('/')[-1])
        if l:
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            os.system('udisksctl unmount --block-device '+get_usb()[i+1])
            if os.system('udisksctl power-off --block-device '+get_usb()[i+1]) == 0:  # if os.system('echo '+password+' | sudo -S eject -F '+get_usb()[i+1]) == 0: 
                st.write('Ejected'+ ' ' + get_usb()[i+1].split('/')[-1])
                st.write('Reload the page to see the changes, currently there is shown an error.\n\n But it has nothing to do with the device media.  ')
                # refresh the page from the server side so no error is shown

    
if __name__ == "__main__":
    main()
