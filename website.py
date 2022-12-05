import streamlit as st
import os
import time

dev = {}
devs = {}
media_path = r'/dev/disk/by-label/'

def get_usb():
    i = 0
    if os.path.exists(media_path):
        for dev in os.listdir(media_path):
            if dev != 'EFI' or dev != 'ESP':
                i += 1
                dev = dev.strip(media_path)
                if " " in dev:
                    dev = r"'" + dev + r"'"
                dev = str((dev).replace(' ', r'\x20'))
                l = media_path+dev
                devs[i] = l

    return devs


st.header("Xmount eject")
st.subheader("Eject your USB devices")
def main():
    for i in range(len(get_usb())):
        l = str(i)
        st.write(get_usb()[i+1].split(media_path)[-1])
        st.container()
        l = st.button('Eject ' + 'Nr. '+l+' ' + get_usb()[i+1].split(media_path)[-1])
        if l:
            st.write('ejecting'+ ' ' + get_usb()[i+1])
            path = get_usb()[i+1]
            print(path)
            if True:
                sd_path = os.popen("udisksctl unmount --block-device "+media_path+"'"+path.split(media_path)[-1]+"'").read()
                sd_path = str(sd_path)
                sd_path = sd_path.replace('Unmounted ', '')
                sd_path = sd_path.replace('.', '')
                sd_path = sd_path.replace(' ', '')
                sd_path = sd_path[:-1]
                for i in range(1, 7):
                    sd_path = sd_path[:-1]+str(i)
                    print(sd_path)
                    time.sleep(1)
                    if os.system("udisksctl unmount --block-device "+sd_path) == 0:
                        print('unmounted')
                        break
                print(sd_path)
                if os.system("udisksctl power-off --block-device "+ sd_path) == 0:
                    st.write('Ejected'+ ' ' + sd_path)
                    st.write('Reload the page to see the changes.  ')
            

    
if __name__ == "__main__":
    main()

