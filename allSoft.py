import time
import json
import vk_api
import datetime
import os
import sys

class allLesson():
    day_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    All_Lessons = []

    def __init__(self):
        self.lessons = []
        self.allsked = {
            "Data": "",
            "Lessons": ""
        }
        print("==================================================================================================================")
        print("\nDatabase maintenance program for users connected to the BMT\n")
        print("==================================================================================================================\n")
        
    def files_load_Certain_Day_Of_Week(self):
        try:
            filename = ("Certain_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'r')
            self.allsked = json.load(myfile)
            myfile.close()
        except:
            filename = ("Certain_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'w')
            clear = []
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("Certain_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'r')
            self.allsked = json.load(myfile)
            myfile.close()

    def files_load_all_Day_Of_Week(self):
        try:
            filename = ("All_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'r')
            allLesson.All_Lessons = json.load(myfile)
            myfile.close()
        except:
            filename = ("All_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'w')
            clear = []
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("All_Day_Of_Week.json")
            myfile  =  open(filename,mode = 'r')
            allLesson.All_Lessons = json.load(myfile)
            myfile.close()

    def files_load_Home_Work(self):
        try:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            self.home_work = json.load(myfile)
            myfile.close()
        except:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'w')
            clear = []
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            self.home_work = json.load(myfile)
            myfile.close()
    
    def job_program(self):
        
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
        if inter['BOT']==True:
            bot = 'Включен'
        else:
            bot = 'Выключен'
        if inter['configure']==True:
            con = 'Включен'
        else:
            con = 'Выключен'
        if inter['power']==True:
            powe = 'Включен'
        else:
            powe = 'Выключен'
        os.system('cls')
        print("==================================================================================================================")
        print("\nDatabase maintenance program for users connected to the BMT\n")
        print("==================================================================================================================\n")
        
        print("\nФункции администрирования в случае ЧП: ")
        print('\t- 101 - Введите чтобы обнулить настройки программы')
        print('\t- 14 - Внеплановая остановка всех приложений программы\n')
        print('Состаяние файлов программы на текущий момент:')
        print('\t- Программа бота    --> ',bot)
        print('\t- Файл конфигурации --> ',con)
        print('\t- Программа таймера --> ',powe)
        print("\nФункции администрирования расписание и Д/З:")
        print("     1) Сделать расписание на следущий день")
        print("     2) Сделать стандартное расписание на всю неделю")
        print("     3) Записать домашнее задание на следущиё день")
        print("     4) Вывести информацию о расписании на следущий день")
        print("     5) Вывести информацию о всём расписании на неделю")
        print("     6) Вывести информация о домашнем задании")
        print('\n')
        print('Функции администрирования бота:')
        print('     7) Прочитать сообщения, отправленные боту')
        print('     8) Сделать рассылку сообщения подключенным пользователям')
        print('     9) Просмотреть пользователей подключенных к боту')
        print('    10) Остановить бота, перевести его в режим ожидания')
        print('    11) Прочитать отчет об ошибках')
        print('    12) Очистить данные')
        print('    13) - exit')
        print('    15) Архивировать, заполненные сегодня дз и уроки на завтра')
        print('    16) Написать сообщение на стене сообщества')
        
        


        try:
            self.variant = int(input("Введите номер варианта: "))
            while (self.variant != 1) and (self.variant != 2) and (self.variant != 16)and (self.variant != 3)and (self.variant != 14)and (self.variant != 15) and (self.variant != 101) and (self.variant != 4) and (self.variant != 5) and (self.variant != 6) and (self.variant != 7)and (self.variant != 8)and (self.variant != 9)and (self.variant != 10)and (self.variant != 11)and (self.variant != 12)and (self.variant != 13)and (self.variant != 0):
                print("\nНекорректный ввод данных!\nВы не следуете условию задачи!\n")
                self.variant = int(input("Введите номер варианта: "))

        except ValueError:
            pass

    def creat_Certain_sked(self):
        os.system('cls')
        self.files_load_Certain_Day_Of_Week()
        self.allsked = {
            "Data": "",
            "Lessons": ""
        }

        self.allsked["Data"] = datetime.date.today().strftime("%d.%m")

        print("\n")


        print("\nЗаполните уроки:\n")
        num_les = 1
        lesson = str(input("   {})".format(num_les)))
        self.lessons.append(lesson)
        k = str(" ")
        while k != "f":
            num_les += 1
            lesson = str(input("   {})".format(num_les)))
            if lesson != "":
                self.lessons.append(lesson)
                k = str(lesson) + "f"
            else:
                k = str(lesson) + "f"
        
        self.allsked["Lessons"] = self.lessons

        #ДЛЯ ТЕСТОВ
        print(self.allsked)

    def creat_All_sked(self):
        os.system('cls')
        self.miha=[]
        self.files_load_all_Day_Of_Week()
        allLesson.All_Lessons = []


        for Day in allLesson.day_of_week:
            self.files_load_all_Day_Of_Week()
            self.allsked = {
                "DayOfWeek": "",
                "Lessons": ""
            }


            print("\n\n-------------------------------------\nСоздание расписания на {}\n".format(Day))
            

            self.allsked["DayOfWeek"] = str(Day)

            print("\n")


            print("\nЗаполните уроки:\n")
            num_les = 1
            lesson = str(input("   {})".format(num_les)))
            self.lessons.append(lesson)
            k = str(" ")
            while k != "f":
                num_les += 1
                lesson = str(input("   {})".format(num_les)))
                if lesson != "":
                    self.lessons.append(lesson)
                    k = str(lesson) + "f"
                else:
                    k = str(lesson) + "f"
            
            self.allsked["Lessons"] = self.lessons
            print(self.miha)
            print(self.allsked)
            self.miha.append(self.allsked)
          
           

            print(allLesson.All_Lessons)
            self.lessons = []
            allLesson.All_Lessons.append(self.allsked)


    def creat_home_work(self):
        os.system('cls')
        self.files_load_Home_Work()
        self.home_work = {
            "Data": "",
            "HomeWork": [] 
        }

        self.home_work["Data"] = datetime.date.today().strftime("%d.%m")

        row = int(0)
        print("\nДомашнее задание на {}\n".format(datetime.date.today().strftime("%d.%m")))
        print("Информация:")
        print("     1)Введите точное и понятное домашнее задание, если вы не знаете,")
        print("       что заданно по определённому предмету, то опишите это!")
        print("     2)Всегда описывайте уроки по которым не заданно!\n")

        row_text = str(input("(Д/З) ... "))
        self.home_work["HomeWork"].append(row_text)
        k = str(" ")
        while k != "f":
            row_text = str(input("      ... "))
            if row_text != "":
                self.home_work["HomeWork"].append(row_text)
                k = str(row_text) + "f"
            else:
                k = str(row_text) + "f"

 
    def save_Certain_Day_Of_Week(self):
        filename = ("Certain_Day_Of_Week.json")
        myfile  =  open(filename,mode = 'w')

        json.dump(self.allsked, myfile)

        myfile.close()

    def save_All_sked(self):
        filename = ("All_Day_Of_Week.json")
        myfile  =  open(filename,mode = 'w')

        json.dump(self.miha, myfile)

        myfile.close()

    def save_home_work(self):
        filename = ("HOME_WORK.json")
        myfile = open(filename, mode="w")

        json.dump(self.home_work, myfile)

        myfile.close()


    def show_Certain_Day_Of_Week(self):
        os.system('cls')
        self.files_load_Certain_Day_Of_Week()
        for pattern in self.allsked:
            if pattern == "Data":
                da = ''
                file = open('Certain_Day_Of_Week.json',mode = 'r')
                f = json.load(file)
                file.close()
                low = str(f['Data'])
                da+=low[0]+low[1]
                da = int(da)+1
                fas = str(da)+low[2]+low[3]+low[4]
                
                print("\n========================================\nРасписание уроков на {}:".format(fas))

            else:
                
                num_lesson = int(1)

                print("\nУроки: ")
                for lessons in self.allsked[pattern]:
                    print(" {}) {}".format(num_lesson, self.allsked[pattern][num_lesson-1]))
                    num_lesson += 1

        print("\n========================================\n")

    def show_All_Day_Of_Week(self):
        os.system('cls')
        self.files_load_all_Day_Of_Week()
        for days in allLesson.All_Lessons:
            self.files_load_all_Day_Of_Week()
            c_les = int(1)
            for pattern in days:
                if pattern == "DayOfWeek":
                    
                    print("\n========================================\nРасписание на {}:\n".format(days[pattern]))

                elif pattern == "Lessons":
                    for lesson in days[pattern]:
                        print("{}){}".format(c_les, lesson))
                        c_les += 1

            days = []
    def show_Homework(self):
        os.system('cls')
        i = 0
        try:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        except:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'w')
            clear = {
            "Data": "",
            "HomeWork": [] 
            }
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        if i["Data"]=="":
            print('Домашнее задание отсутствует!!!')
        else:
            da = ''
            print('Информация о домашнем задании:\n')
            low = str(i['Data'])
            da+=low[0]+low[1]
            da = int(da)+1
            fas = str(da)+low[2]+low[3]+low[4]
            print('Дата домашнего задания - ',fas)
            print('Домашнее задание: ')
            countable = len(i["HomeWork"])
            print()
            g = 0
            while g<countable:
                print('# '+ i['HomeWork'][g])
                g+=1
    def admin_messages(self):
        os.system('cls')
        def watch(msg,num):
            os.system('cls')
            print('\n')
            if msg == []:
                pass
            else:
                num_count = len(num)
                d = 0
                while d<num_count:
                    d+=1
                    print(str(d)+') '+num[int(d-1)])
                    d-=1
                    d+=1
                try: 
                    isis = int(input('\nВведите номер варианта: '))
                    print(msg[isis-1])
                except:
                    print('Неверный формат')
                    watch(messages,number)
        try:
            isi = input('\nВведите с какого числа вы хотите посмотреть сообщения: ')
        except ValueError:
                 print('Неверный формат ввода!')

        messages = []
        number = []
        fas = isi
        da = ''
        sa = 0
        xser = False
        while sa<20:
            try:
                
                sa+=1
                try:
                    file = open('Messages_of_'+str(fas)+'.log',mode = 'r')
                except:
                    if xser==True:
                        continue
                        
                    else:
                        print('Файла не существует')
                        i = input('-')
                        break
                    
                sach = file.read()
                messages.append(sach)
                number.append(fas)
                xser = True
                low = str(fas)
                da = low[0]+low[1]
                da = int(da)+1
                fas = str(da)+low[2]+low[3]+low[4]
            except:
                continue
        watch(messages,number)
    def admin_distribution(self):
        pass
    def admin_Errors(self):
        os.system('cls')
        try:
            print('\nОтчет об ошибках BMT:\n')
            file = open('Errors.log',mode = 'r')
            errors = file.read()
            print(errors+'\n')

        except:
            print('Ошибки отсутствуют!!!')
    def admin_Deleted_data(self):
        print('\nВыберите, какие данные нужно удалить:')
        print('1) Очет об ошибках')
        print('2) Данные сообщений от пользователей')
        print('     Прочие данные расписания нельзя удалить, \nих можно только перезаписать\n\n')
        var = int(input('Выберите вариант:'))
        if var==1:
            os.remove('Errors.log')
        elif var==2:
            def watchу(msg,num):
                os.system('cls')
                print('\n')
                if msg == []:
                    pass
                else:
                    num_count = len(num)
                    d = 0
                    while d<num_count:
                        d+=1
                        print(str(d)+') '+num[int(d-1)])
                        d-=1
                        d+=1
                    try:
                        isis = int(input('\nВведите номер варианта: '))
                        try:
                            os.remove('Messages_of_'+num[int(isis-1)]+'.log')
                        except:
                            print('\nНеполучилось удалить файл\n')
                    except:
                        print('Неверный формат')
                        watchу(messages,number)
            try:
                isi = input('\nВведите с какого числа вы хотите удалить сообщения: ')
            except ValueError:
                 print('Неверный формат ввода!')

            messages = []
            number = []
            fas = isi
            da = ''
            sa = 0
            xser = False
            while sa<20:
                try:
                    sa+=1
                    try:
                        file = open('Messages_of_'+str(fas)+'.log',mode = 'r')
                    except:
                        if xser==True:
                            continue
                            
                        else:
                            print('Файла не существует')
                            i = input('-')
                            break
                        
                    sach = file.read()
                    messages.append(sach)
                    number.append(fas)
                    xser = True
                    low = str(fas)
                    da =low[0]+low[1]
                    da = int(da)+1
                    fas = str(da)+low[2]+low[3]+low[4]
                except:
                    continue
            watchу(messages,number)
                
    def admin_operating_mode(self):
        os.system('cls')
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
        if conf['Config'] == True:
            print('\nВ данный момент бот работает\n')
        elif conf['Config']== False:
            print('\nВ данный момент бот отключен(в режиме ожидания)\n')
        print('Варианты действий:\n')
        print('1) Перевести бота в режим ожидания')
        print('2) Вывести бота из режима ожидания')
        can = int(input('Введите вариант: '))
        if can==1:
            file = open('config.json',mode = 'w')
            default = {
            'Config':False
            }
            json.dump(default,file)
            file.close()
            print('\nБот переведён в режим ожидания')
        elif can==2:
            file = open('config.json',mode = 'w')
            default = {
            'Config':True
            }
            json.dump(default,file)
            file.close()
            print('\nБот выведен из режима ожидания')
        else:
            print('\nERROR!!! действия не выполнены')

    def admin_restore(self):
        t = int()
        # while tys<5:
        #     print('Loading: ',time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||",time.sleep(0.2),"||")
        #     tys+=1
        print("Настройки состаяния обнулены")
        filename = ("position.json")
        myfile  =  open(filename,mode = 'w')
        clear = {
            'BOT':False,
            'configure':False,
            'power':False
        }
        json.dump(clear,myfile)
        myfile.close()
        time.sleep(1)
            
    def stopping_the_program(self):
        print('В этом случае остановятся процессы программы "BMT"')
        u = input()
        os.system('Taskkill /IM pythonw.exe /F')

    def users_connected_to_the_bot(self):
        vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество        
        def watchuc(user_od):
            global full_name
            a = vk.method('users.get',{'user_ids':user_od})
            nam = a[0]['first_name']
            fam = a[0]['last_name']
            full_name = nam+' '+fam
            return full_name
        os.system('cls')
        file = open('save_ID_of_user.json',mode ='r')
        g = json.load(file)
        print('\nПользователи подключенные к боту:')
        h = len(g)
        uc = 0
        while uc<h:
            print(str(g[uc])+' - '+ watchuc(g[uc])+'\n')
            uc+=1
    def archive(self):
        try:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        except:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'w')
            clear = {
            "Data": "",
            "HomeWork": [] 
            }
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("HOME_WORK.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        file = open('Certain_Day_Of_Week.json',mode = 'r')
        f = json.load(file)
        file.close()
        a = {
            'HW':'',
            'Les':''
        }
        try:
            filename = ("BIG_ARCHIVE.json")
            myfile  =  open(filename,mode = 'r')
            arch = json.load(myfile)
            myfile.close()
        except:
            filename = ("BIG_ARCHIVE.json")
            myfile  =  open(filename,mode = 'w')
            clear = []
            json.dump(clear,myfile)
            myfile.close()
        finally:
            filename = ("BIG_ARCHIVE.json")
            myfile  =  open(filename,mode = 'r')
            arch = json.load(myfile)
            myfile.close()
        print('Архивируем ваши файлы')
        a['HW'] = i
        a['Les'] = f
        # print(a)
        # print(arch)
        arch.append(a)
        filename = ("BIG_ARCHIVE.json")
        myfile  =  open(filename,mode = 'w')
        json.dump(arch,myfile)
        myfile.close()
        filename = ("BIG_ARCHIVE.json")
        myfile  =  open(filename,mode = 'r')
        arch = json.load(myfile)
        myfile.close()
        de = len(arch)
        fp = 0
        print('\t--DT--\t--HW--\t--LS--\t')
        while fp<de:
            print(str(arch[fp]['HW']['Data'])+'\t\n\n'+str(arch[fp]['HW']['HomeWork'])+'\t\n\n'+str(arch[fp]['Les']['Lessons'])+'\n=================================================')
            fp+=1
    def admin_distribution(self):
        def write_msg(user_id, s):
            vk.method('messages.send', {'user_id':user_id,'message':s})
        os.system('cls')
        vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество        
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
            print('Data NONE!!!')
        finally:
            filename = ("save_ID_of_user.json")
            myfile  =  open(filename,mode = 'r')
            i = json.load(myfile)
            myfile.close()
        print('\nНаписать рассылку пользователям:')
        inyu = str(input('\n\t|>>Сообщение<<|--->>'))
        print('\n\t -1 Отправить всем')
        print('\n\t -2 Отправить одному\n\t <|\t\t\t|>')
        iny = str(input("\n|>"))
        if iny=='1':
            print(i)
            ino  = 0
            while ino<len(i):
                write_msg(i[ino],inyu)
                ino+=1
            print('Завершено')
            
        elif  iny=='2':
            def watchuc(user_od):
                global full_name
                a = vk.method('users.get',{'user_ids':user_od})
                nam = a[0]['first_name']
                fam = a[0]['last_name']
                full_name = nam+' '+fam
                return full_name
            file = open('save_ID_of_user.json',mode ='r')
            g = json.load(file)
            print('\nПользователи подключенные к боту:')
            h = len(g)
            uc = 0
            while uc<h:
                print(str(uc+1)+') '+str(g[uc])+' - '+ watchuc(g[uc])+'\n')
                uc+=1
            iu = int(input('Кому |> '))
            write_msg(i[iu-1],inyu)
            print('Завершено')
        else:
            print('Huila')
    def wall_post(self):
        os.system('cls')
        print('\n\tВведите сообщение которое вы хотите запостить\t')
        asd = str(input('|>> '))
        podz = int(input('Подтвердите отправку 1-2: '))
        if podz==1:
            vk = vk_api.VkApi(token = '30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54') #Авторизоваться как сообщество        
            #Внимание, как можете видеть никакие данные паролей и логинов не сохраняют и не отправляются, желаем приятных переписок.....
            
            import vk
            my_app_id = 6491135
            user_login = str(input('Логин|>'))

            user_password =str(input('Пароль|>'))

            session = vk.AuthSession(scope='wall', app_id=my_app_id, user_login=user_login, user_password=user_password)
            vk.api.access_token="30f6f68153a738287f04ed48a7bf0e260bd5c2b0903670710d1077e7c347d3b95c8f361e9b14efba36d54"
            api = vk.API(session)
            api.wall.post(owner_id='-165128029',message=asd,v = '3.0')
        
        else:
            pass

        

class Main(allLesson):

    repeat = int(1)
    while repeat == 1:
        print("\n")
        os.system('cls')
        sked = allLesson()
        sked.job_program()

        if sked.variant == 1:
            sked.creat_Certain_sked()
            sked.save_Certain_Day_Of_Week()
        elif sked.variant == 2:
            sked.creat_All_sked()
            print(allLesson.All_Lessons)
            sked.save_All_sked()
        elif sked.variant == 3:
            sked.creat_home_work()
            sked.save_home_work()
        elif sked.variant == 4:
            sked.show_Certain_Day_Of_Week()
        elif sked.variant == 5: 
            sked.show_All_Day_Of_Week()
        elif sked.variant == 6:
            sked.show_Homework()
        elif sked.variant == 13:
            exit()
        elif sked.variant == 7:
            sked.admin_messages()
        elif sked.variant == 8:
            sked.admin_distribution()
        elif sked.variant == 9:
            sked.users_connected_to_the_bot()
        elif sked.variant == 10:
            sked.admin_operating_mode()
        elif sked.variant == 11:
            sked.admin_Errors()
        elif sked.variant == 12:
            sked.admin_Deleted_data()
        elif sked.variant == 0:
            sked.job_program()
        elif sked.variant == 101:
            sked.admin_restore()
        elif sked.variant == 14:
            sked.stopping_the_program()
        elif sked.variant == 15:
            sked.archive()
        elif sked.variant == 16:
            sked.wall_post()
        
        
        def repeat_input():
            try:
                repeat = int(input("\nПродолжить работать с программой?\n1(Да) 2(Нет)\nВведите число: "))
                while (repeat != 1) and (repeat != 2):
                    print("\nНекорректный ввод данных!\nВы не следуете условию задачи!\n")
                    repeat = int(input("Продолжить работать с программой?\n1(Да) 2(Нет)\nВведите число: "))           
                
                return repeat

            except ValueError:
                print("\nОшибка в системе!\nНеверный формат ввода данных!")
                print("Вы не следуете условию задачи!")
                repeat_input()

        repeat = repeat_input()
