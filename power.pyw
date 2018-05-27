import datetime
import os
import time
import json
time.sleep(40)
os.startfile('configure.pyw')
try:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'r')
    inter = json.load(myfile)
    myfile.close()
except:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'w')
    clear = {
        'BOT':True,
        'configure':True,
        'power':True
    }
    json.dump(clear,myfile)
    myfile.close()
finally:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'r')
    inter = json.load(myfile)
    myfile.close()
inter['power'] = True
print(inter)
filename = ("position.json")
myfile  =  open(filename,mode = 'w')
json.dump(inter,myfile)
myfile.close()
while True:
    times = time.strftime("%H:%M:%S", time.localtime())
    print(times)
    if str(times)=='00:00:00':
        inter['power'] = False
        print(inter)
        filename = ("position.json")
        myfile  =  open(filename,mode = 'w')
        json.dump(inter,myfile)
        myfile.close()
        time.sleep(30)
        os.system('shutdown/s')
    else:
        time.sleep(1)
        continue
    time.sleep(1)


