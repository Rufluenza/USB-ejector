import streamlit as st
import os

dev = {}
devs = {}
media_path = r'/media/xmount/'

def get_usb():
    i = 0
    if os.path.exists(media_path):
        for dev in os.listdir(media_path):
            i += 1
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
            path.replace(' ', '\x') #Det her må jeg ikke. Kender du en løsning? Jeg ønsker at erstatte mellemrummet med \x, da det er det Ubuntu gør med mellemrum i diskenes navne i /dev/disk
            os.system('udisksctl unmount --block-device '+'/dev/disk/by-label/'+path.split(media_path)[-1])
            if os.system('udisksctl power-off --block-device '+'/dev/disk/by-label/'+path.split(media_path)[-1]) == 0:
                st.write('Ejected'+ ' ' + get_usb()[i+1].split(media_path)[-1])
                st.write('Reload the page to see the changes.  ')
                # refresh the page from the server side

    
if __name__ == "__main__":
    main()
