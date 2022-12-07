import streamlit as st
import os
import time

dev = {}
devs = {}
media_path = r'/media/ruben/'

def get_usb():
    i = 0
    for dev in os.listdir(media_path):
        i += 1
        if " " in dev:
            dev = r"'" + dev + r"'"
        l = media_path+dev
        devs[i] = l

    return devs


st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():
    for i in range(len(get_usb())):
        l = str(i)
        button_name = get_usb()[i+1].split(media_path)[-1]
        if "'" in button_name:
            button_name = button_name.replace("'", '')
        st.write(button_name)
        st.container()
        l = st.button('Eject ' + 'Nr. '+l+' ' + button_name)
        if l:
            st.write('ejecting'+ ' ' + button_name)
            st.write('Please wait... ')
            path = get_usb()[i+1]
            sd_path = os.popen("df -h "+path+" | grep -v 'Filesystem'").read()
            sd_path = sd_path.split(' ')[0]
            sd_path = sd_path.replace(' ', '')
            sd_path = sd_path.replace('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0', '')
            os.system("udisksctl unmount --block-device "+sd_path)
            
            for i in range(1, 7):
                sd_path = sd_path+str(i)
                print(sd_path)
                if os.system("udisksctl unmount --block-device "+sd_path) == 0:
                    print('unmounted')
                sd_path = sd_path[:-1]
            print(sd_path)
            if os.system("udisksctl power-off --block-device "+ sd_path) == 0:
                st.write('Ejected'+ ' ' + button_name)
                st.write('Reload the page to see the changes.  ')
            

    
if __name__ == "__main__":
    main()
