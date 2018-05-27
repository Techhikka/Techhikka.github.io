import time
import json
import vk_api
import datetime
import os
s = 0
import sys
#
vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество
#
try:
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
    inter['configure'] = True
    print(inter)
    filename = ("position.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(inter,myfile)
    myfile.close()

    def write_msg(user_id, s):
        vk.method('messages.send', {'user_id':user_id,'message':s})
    def start():
        while True:
            s = 0
            values = {'out': 0,'count': 1,'time_offset': 1}
            vk.method('messages.get', values)
            file = open('config.json',mode = 'r')
            conf = json.load(file)
            file.close()
            print(conf)
            response = vk.method('messages.get', values)
            if response['items']:
                values['last_message_id'] = response['items'][0]['id']
            for item in response['items']:
                write_msg(item[u'user_id'],u'На стороне сервера проходят технические работы, подождите')
            time.sleep(1)
            if conf['Config']==False:
                continue
            else:
                break
    while True:
        file = open('config.json',mode = 'r')
        confi = json.load(file)
        print(confi)
        file.close()
        if confi['Config']==False:
            start()
            s = 0
        else:
            if s==0:
                os.startfile('BOTmichael.pyw')
                s+=1
            else:
                continue
except:
    inter['configure'] = False
    print(inter)
    filename = ("position.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(inter,myfile)
    myfile.close()
    os.startfile('configure.pyw')