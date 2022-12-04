import streamlit as st
import os

dev = {}
devs = {}
media_path = r'/media/ruben/'

def get_usb():
    i = 0
    if os.path.exists(media_path):
        for dev in os.listdir(media_path):
            i += 1
            dev = dev.strip(media_path)
            if " " in dev:
                # add "'" around the device name
                dev = r"'" + dev + r"'"
            dev = str((dev).replace(' ', r'\x20'))
            l = media_path+dev
            devs[i] = l

    return devs

def get_filesystem():
    for file in range(len(get_usb())):
        # get the file system of the usb device
        #file = os.popen("df -h " + get_usb()[file+1] + " | grep -v 'Filesystem' | awk '{print $1}'").read()
        print(file)
    
    return file

# get_filesystem()


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
            if r"\x" in path:
                os.system("udisksctl unmount --block-device "+media_path+"'"+path.split(media_path)[-1]+"'")
                if os.system("udisksctl power-off --block-device "+media_path+"'"+path.split(media_path)[-1]+"'") == 0:
                    st.write('Ejected'+ ' ' + get_usb()[i+1].split(media_path)[-1])
                    st.write('Reload the page to see the changes.  ')
            #path.replace(r' ', r'\\x') #Det her må jeg ikke. Kender du en løsning? Jeg ønsker at erstatte mellemrummet med \x, da det er det Ubuntu gør med mellemrum i diskenes navne i /dev/disk
            else:
                os.system("udisksctl unmount --block-device "+media_path+path.split(media_path)[-1])
                if os.system("udisksctl power-off --block-device "+media_path+path.split(media_path)[-1]) == 0:
                    st.write('Ejected'+ ' ' + get_usb()[i+1].split(media_path)[-1])
                    st.write('Reload the page to see the changes.  ')
                # refresh the page from the server side

    
if __name__ == "__main__":
    main()
