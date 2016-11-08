from pynput.keyboard import Key, Listener
import uploadImage

#定义一个热键  Shift+Alt+A
shift_flag = False
alt_flag = False
a_flag = False
already_upload = False
def on_press(key):
    #print('{0} pressed'.format(key))
    global shift_flag
    global alt_flag
    global a_flag
    global already_upload
    if str(key) == "Key.shift":
        shift_flag = True
    elif str(key) == "Key.alt_l":
        alt_flag = True
    elif str(key) == "a" or str(key) == "A":
        a_flag = True

    #下面这行表示按下快捷键
    if shift_flag==True and alt_flag==True and alt_flag==True and already_upload==False:
        print("监听到快捷键Shift+Alt+A,正在上传图片")
        uploadImage.upload()
        already_upload = True
    
def on_release(key):
    #print('{0} release'.format(key))
    #if key == Key.esc:
        # Stop listener
        #return False
    global shift_flag
    global alt_flag
    global a_flag
    global already_upload
    if str(key) == "Key.shift":
        shift_flag = False
    elif str(key) == "Key.alt_l":
        alt_flag = False
    elif str(key) == "a" or str(key) == "A":
        a_flag = False
    if shift_flag==False or alt_flag==False or a_flag==False:
        already_upload = False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
