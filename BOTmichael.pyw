# Бот 7 б класса расписание.....
import time
import json
import vk_api
import datetime
import os
import sys
try:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'r')
    inter = json.load(myfile)
    myfile.close()
except:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'w')
    clear = {
        'BOT':False,
        'configure':False,
        'power':False
    }
    json.dump(clear,myfile)
    myfile.close()
finally:
    filename = ("position.json")
    myfile  =  open(filename,mode = 'r')
    inter = json.load(myfile)
    myfile.close()
inter['BOT'] = True
print(inter)
filename = ("position.json")
myfile  =  open(filename,mode = 'w')
json.dump(inter,myfile)
myfile.close()

def read():
    global inte
    try:
        filename = ("posi.json")
        myfile  =  open(filename,mode = 'r')
        inte = json.load(myfile)
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
        inte = json.load(myfile)
        myfile.close()
try:
    
    def saven():
        global i  
        try:
            filename = ("save_ID_of_user.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        except:
            filename = ("save_ID_of_user.json")
            myfile  =  open(filename,mode = 'w')
            clear = []
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("save_ID_of_user.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
    saven()
    dataname = r'Messages_of_'+datetime.date.today().strftime("%d.%m")
    def Surveillance(data,filename):
        file = open(filename+'.log',mode = 'at')#открыть файл(название списка)
        file.write('# '+data+'\n')
        # file = open(filename+'.log',mode = 'r')#открыть файл(название списка)
        # print(file.read())
        file.close()
    vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество
    def save_id(us):
        conf = i.count (us)
        try:
            if conf == 0:
                filename = ("save_ID_of_user.json")
                myfile  =  open(filename,mode = 'w')
                i.append(us)
                json.dump(i,myfile)
                myfile.close()   
            else:
                pass 
        except:
            text = ''
            text+=sys.exc_info()[0]+' - '+sys.exc_info()[1]
            Surveillance(text+time.strftime("%d-%m-%Y  %H:%M:%S", time.localtime()),'Errors')
            os.startfile('BOTmichael.pyw')
    global sh
    def sh():
        os.system('shutdown /s /t 60 /c "Aдминистратор выключает ваш компьютер через 1 мин..."')
    def dz():
        global dae,fase
        try:
            dae = ''
            time = datetime.date.today().strftime("%d.%m")
            lowe = str(time)
            dae+=lowe[0]+lowe[1]
            dae = int(dae)+1
            fase = str(dae)+lowe[2]+lowe[3]+lowe[4]
            file = open('HOME_WORK.json',mode = 'r')
            f = json.load(file)
            print(f)
            
            
            DZ = ''
            da = ''
            for les in f:
                if les == 'Data':
                    low = str(f['Data'])
                    da+=low[0]+low[1]
                    da = int(da)+1
                    fas = str(da)+low[2]+low[3]+low[4]
                    # print('Дата домашнего задания {}'.format(f['Data']))
                    DZ+= 'Дата домашнего задания - ' + fas + '\n'
                if les =='HomeWork':
                    num = 1
                    for j in f['HomeWork']:
                        DZ+='- '
                        DZ+=j+' \n'
                        # print(num,j)
                        num+=1
            
            print(time+fas)
            if str(time)==str(fas):
                write_msg(item['user_id'],u'Домашнее задание на завтра на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
            if str(time)!=str(fas):
                if int(dae)>int(da):
                    write_msg(item['user_id'],u'Домашнее задание на завтра на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
                else:
                    write_msg(item['user_id'],DZ)
        except:
            write_msg(item['user_id'],u'Домашнее задание на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
    def write_msg(user_id, s):
        vk.method('messages.send', {'user_id':user_id,'message':s})
    def helpes():
        write_msg(item['user_id'],u'Список команд, доступных боту:\n 1 - Помощь 🌚\n 2 - Расписание на завтра ⏳\n 3 - Расписание на неделю ⏳\n 4 - Домашнее задание 📖\n\n\n\t\tЧтобы отправить сообщение администратору, вначале сообщения введите две точки ..\n\n\n\nПримечание. Если бот по не отвечает, обратитесь к администратору напрямую.')
    def ad():
        write_msg(item['user_id'],'Режим администратора\nComands:\n/reset\n/condition')
    def skid_all_week():
        try:
            file = open('All_Day_Of_Week.json',mode = 'r')
            fi = json.load(file)
            SKID = 'Стандартное расписание на неделю:\n\n'
            a = 0
            while a<6:
                j = fi[a]
                day = j.get('DayOfWeek')
                SKID+=str(day)+':\n\n'
                less = j.get('Lessons')
                countless = len(less)
                cirt = 0
                while cirt<countless:
                    cirt+=1
                    SKID+= str(cirt) +') ' + less[cirt-1]+'\n'
                    cirt-=1
                    cirt+=1
                SKID+='\n'
                a+=1
            write_msg(item['user_id'],SKID)
        except:
            write_msg(item['user_id'],u'Общее стандартное расписание отсутствует!!!')
            text = ''
            text+=str(sys.exc_info()[0])+' - '+str(sys.exc_info()[1])
            print(text)
            Surveillance(str(text)+' - '+time.strftime("%d-%m-%Y  %H:%M:%S", time.localtime()),'Errors')
            if str(sys.exc_info()[0])=="<class 'SystemExit'>":
                pass
            else:
                os.startfile('BOTmichael.pyw')
                exit()
                

    def sked():
        try:
            dae = ''
            time = datetime.date.today().strftime("%d.%m")
            lowe = str(time)
            dae+=lowe[0]+lowe[1]
            dae = int(dae)+1
            fase = str(dae)+lowe[2]+lowe[3]+lowe[4]
            file = open('Certain_Day_Of_Week.json',mode = 'r')
            f = json.load(file)
            file.close()
            print(f)
            LESSON = ''
            da = ''
            for les in f:
                if les == 'Data':
                    low = str(f['Data'])
                    da+=low[0]+low[1]
                    da = int(da)+1
                    fas = str(da)+low[2]+low[3]+low[4]


                    LESSON += 'Дата расписания - ' + str(fas) + '\n'
                if les =='Lessons':
                    num = 1
                    for j in f['Lessons']:
                        LESSON+=str(num)+') '
                        LESSON+=j+'; \n'
                        num+=1

            time = datetime.date.today().strftime("%d.%m")
            if str(time)==str(fas):
                write_msg(item['user_id'],u'Расписание на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
            if str(time)!=str(fas):
                if int(dae)>int(da):
                    write_msg(item['user_id'],u'Расписание на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
                else:
                    write_msg(item['user_id'],LESSON)
        except:
            text = ''
            text+=str(sys.exc_info()[0])+' - '+str(sys.exc_info()[1])
            print(text)
            write_msg(item['user_id'],u'Расписание на завтра отсутствует!\nНапишите позднее, когда оно будет добавленно администратором')
    def rite(hom):
        if hom['body']==[]:
            pass
        elif hom['id']==[]:
            pass
        else:
            Surveillance(str(hom)+'\n',dataname)
            save_id(int(hom['id'][0]))
    def reset():
        Surveillance('rebooting bot'+' - '+time.strftime("%d-%m-%Y  %H:%M:%S", time.localtime()),'Errors')
        os.startfile('BOTmichael.pyw')

        exit()
    def admin():
        try:
            file = open('config.json',mode = 'r')
            conf = json.load(file)
            file.close()
        except:
            file = open('config.json',mode = 'w')
            default = {
            'Config':True
            }
            json.dump(default,file)
            file.close()
        finally:
            file = open('config.json',mode = 'r')
            conf = json.load(file)
        if conf['Config']==True:
            pass
        if conf['Config']==False:
            print('exite')
            inter['BOT'] = False
            print(inter)
            filename = ("position.json")
            myfile  =  open(filename,mode = 'w')
            json.dump(inter,myfile)
            myfile.close()
            exit()
    # def mail():
    #     home = {
    #             "body": [],
    #             "id": [] 
    #         }
    #     time.sleep(3)
    #     fo=0
    #     while True:
    #         fo+=1
    #         rite(home)
    #         admin()
    #         home = {
    #                 "body": [],
    #                 "id": [] 
    #             }
    #         send = ''
    #         ide = 0
    #         response = vk.method('messages.get', values)
    #         print(response)
    #         for item in response['items']:
    #             if item [u'body']:
    #                 send = item[u'body']
    #                 home['body'].append(send)
    #                 print(send)
    #             if item ['user_id']:
    #                 ide = item['user_id']
    #                 save_id(ide)
    #                 home['id'].append(ide)
    #                 print(ide)
            
    #         if str(send)=='/admin':
    #             ad()
    #             corect = True
    #             send = 0
    #             break
    #         if str(send)=='/reset':
    #             reset()
    #             corect = True
    #             send = 0
    #             break
    #         if str(send)=='.':
    #             corect = True
    #             send = 0
    #             break
    #         if str(send)!='':
    #             Surveillance(str(send),'Administration_messages')
    #             write_msg(445987860,send)
    #             write_msg(236981685,send)
    #             helpes()
    #             break
    #         if fo==20:
    #             break
    #         time.sleep(1)

                
    global home
    print('run programm')  
    os.startfile('admessage.pyw')
    home = {
                "body": [],
                "id": [] 
            }
    values = {'out': 0,'count': 1,'time_offset':1 }
    vk.method('messages.get', values)
    send = 0
    ide = 0
    corect = True
    while True:
        rite(home)
        admin()
        home = {
                "body": [],
                "id": [] 
            }
        send = 0
        ide = 0
        response = vk.method('messages.get', values)
        print(response)
        for item in response['items']:
            if item [u'body']:
                send = item[u'body']
                home['body'].append(send)
                print(send)
            if item ['user_id']:
                ide = item['user_id']
                save_id(ide)
                home['id'].append(ide)
                print(ide)
            
        # блок условий и проверок функций... 
        if str(send)=='Расписание на неделю' or str(send)=='3':
            skid_all_week()
            send = 0
            pass
        if str(send)=='Расписание на завтра'or str(send)=='2':
            sked()
            corect = True
            send = 0
        if str(send)=='/admin':
            ad()
            corect = True
            send = 0
        if str(send)=='/reset':
            reset()
            corect = True
            send = 0
        if str(send)=='Домашнее задание' or str(send)=='4':
            dz()
            corect = True
            send = 0
        if str(send)=='/condition':
            file = open(dataname+'.log',mode = 'r')
            sach = file.read()
            write_msg(int(ide),str(sach))
            file.close()
            corect = True
            send = 0
        if str(send) =='Помощь' or str(send)=='1':
            helpes()
            corect = True
            send = 0
        if str(send) =='@@':
            if ide == 445987860:
                os.startfile('admessage.pyw')
                time.sleep(2)
                print('ok')
                send = 0    
                ide = 0
            else:
                send = 0
                write_msg(int(ide),'Функция для вас недоступна')
        # if str(send) =='Сообщение администратору' or str(send)=='5':
        #     write_msg(int(ide),"Введите сообщение администратору (в течение 20 секунд): ")
        #     mail()
        #     corect = True
        #     send = 0
        if str(send)=='/del':
            if ide==445987860:
                h = {
                'Data':'',
                'Lessons':[]
                }
                he = {
                    "Data": "", 
                    "HomeWork":""
                }
                filename = ("Certain_Day_Of_Week.json")
                myfile  =  open(filename,mode = 'w')
                json.dump(h, myfile)
                myfile.close()
                filename = ("HOME_WORK.json")
                myfile  =  open(filename,mode = 'w')
                json.dump(he, myfile)
                myfile.close()
                ide = 0
                send = 0
                time.sleep(5)
        if str(send)=='/sh':
            sh()
            ide = 0
            send = 0
            time.sleep(5)
        if str(send)=='/a':
            os.system('Shutdown /a')
            ide = 0
            send = 0
            time.sleep(5)
        # if str(send)=='/ts':
        #     if ide==445987860:
        #         diro = os.getcwd()
        #         print(diro)
        #         os.system("tasklist /all >> d:\cmd.txt")
        #         time.sleep(4)
        #         f = open('d:\cmd.txt',mode = 'r')
        #         fo = f.read()
        #         print(fo)
        #         write_msg(445987860,fo)
        #         send = 0
        #         ide = 0
        #         fu = 0
                

        if str(send) != 'Расписание на завтра' or 'Помощь' or '/condition' or '@@' or '/reset' or 'Сообщение администратору' or '/admin' or 'Расписание на неделю' or 'Домашнее задание' or '1' or '2'  or '3'  or '4' or '5':
            if ide==0 or send == 0:
                ide = 0
                send = 0
                time.sleep(1)
                continue
            else:
                se = ''
                se+=send[0]
                try:
                    se+=send[1]
                except:
                    pass
                if se=='..':
                    time.sleep(3)
                read()
                if inte['Help']==False:
                    pass
                else:
                    helpes()
                ide = 0
                send = 0
                time.sleep(1)
                continue
                
except:
    text = ''
    text+=str(sys.exc_info()[0])+' - '+str(sys.exc_info()[1])
    print(text)
    Surveillance(str(text)+' - '+time.strftime("%d-%m-%Y  %H:%M:%S", time.localtime()),'Errors')
    if str(sys.exc_info()[0])=="<class 'SystemExit'>":
        exit()
    elif str(sys.exc_info()[0])=="<class 'requests.exceptions.ConnectionError'>":
        time.sleep(600)
    else:
        os.startfile('BOTmichael.pyw')
        