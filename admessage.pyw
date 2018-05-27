# Бот 7 б класса расписание.....
import time
import json
import vk_api
import datetime
import os
import sys
def read():
    global inter
    try:
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'r')
        inter = json.load(myfile)
        myfile.close()
    except:
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'w')
        clear = {
            'Help':True
        }
        json.dump(clear,myfile)
        myfile.close()
    finally:
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'r')
        inter = json.load(myfile)
        myfile.close()
def Surveillance(data,filename):
        file = open(filename+'.log',mode = 'at')#открыть файл(название списка)
        file.write('# '+data+'\n')
        # file = open(filename+'.log',mode = 'r')#открыть файл(название списка)
        # print(file.read())
        file.close()
vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество
values = {'out': 0,'count': 1,'time_offset':1 }
vk.method('messages.get', values)
def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})
def processing8():
    d = 0
    do = ''
    f = len(send)
    g = 2
    while g<f:
        do+=send[g]
        g+=1
    os.system('shutdown /s /t 60 /c "'+do+'"')
    time.sleep(8)
    os.system('Shutdown /a')
def processing():
    global send
    proposal='Пользователь - '
    user_od=ide
    a = vk.method('users.get',{'user_ids':user_od})
    nam = a[0]['first_name']
    fam = a[0]['last_name']
    full_name = nam+' '+fam
    proposal+=full_name
    proposal+=' отправил - '
    d = 0
    do = ''
    f = len(send)
    g = 2
    while g<f:
        do+=send[g]
        g+=1
    proposal+= do
    send = 0
    write_msg(445987860,proposal)
    write_msg(236981685,proposal)
    Surveillance(str(proposal),'Administration_messages')
    write_msg(ide,'Сообщение отправлено')
def up():
    print('up1'+str(h))
    h['Data']=datetime.date.today().strftime("%d.%m")
    h['Lessons'].append(send)
    print('up2'+str(h))
    time.sleep(1)
def skid():
    global h
    h = {
        'Data':'',
        'Lessons':[]
    }
    write_msg(ide,'Вводите уроки на завтра, дата поставится автоматически(перед уроком вводите - )\n Введите _ , чтобы закончить ввод расписания')
    read()
    print('skid'+str(h))
    inter['Help']=False
    filename = ("posi.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(inter,myfile)
    myfile.close()
def save():
    print('Save'+str(h))
    filename = ("Certain_Day_Of_Week.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(h,myfile)
    myfile.close()
def hw():
    global dz
    dz = {
        'Data':"",
        'HomeWork':[]
    }
    write_msg(ide,'Следующим сообщением отправте ВСЁ д/з, в начале напишите =\n Cтрока автоматически сохранится.')
    read()
    print('dz'+str(dz))
    inter['Help']=False
    filename = ("posi.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(inter,myfile)
    myfile.close()
def dze():
    print(send)
    t = ''
    j = 0
    te =''
    for t in send:
        if t == '=':
            if j!=1:
                t = ''
                
        te+=t
    dz['Data']=datetime.date.today().strftime("%d.%m")
    dz['HomeWork'].append(te)
    time.sleep(1)
    filename = ("HOME_WORK.json")
    myfile  =  open(filename,mode = 'w')
    json.dump(dz,myfile)
    myfile.close()  
    write_msg(ide,'Д/З записано')      
while True:
    se=''
    s = 0
    global h
    global ide,send
    send = ''
    ide = 0
    response = vk.method('messages.get', values)
    print(response)
    for item in response['items']:
        if item [u'body']:
            send = item[u'body']
            print(send)
        if item ['user_id']:
            ide = item['user_id']
            print(ide)
    if send != '':
        se=''
        se+=send[0]
        try:
            se+=send[1]
        except:
            pass
        s = send[0]
    if se=='..':
        print('ok')
        processing()
        send = 0
    if se=='//':
        print('ok')
        processing8()
        send = 0
    if se=='::':
        print('ok')
        skid()
        send = 0
    if se=='**':
        print('ok')
        hw()
        send = 0
    if s=='=':
        print('ok')
        print(send)
        dze()
        inter['Help']=True
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'w')
        json.dump(inter,myfile)
        myfile.close()
        send = 0
    if s=='_':
        write_msg(ide,'Ввод расписания на завтра окончен')
        save()
        h = {
        'Data':'',
        'Lessons':[]
        }
        read()
        inter['Help']=True
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'w')
        json.dump(inter,myfile)
        myfile.close()
        send = 0
    if s=='-':
        print('ok')
        up()
        send = 0
    if send=='@':
        if ide == 445987860:
            exit()
        else:
            write_msg(int(ide),'Функция для вас недоступна')
    time.sleep(1)