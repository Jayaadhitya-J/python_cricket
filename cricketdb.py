import mysql.connector as ms
import easygui as e
from tkinter import *
import pyttsx3
mycon=ms.connect(host='localhost',user='root',passwd='Jay1')
cur=mycon.cursor()

#CREATING DATABASE
cur.execute('create database cricket')
cur.execute('use cricket')

#CREATING REQUIRED TABLES
cur.execute("create table team_stats(t_id int(3) primary key,team_name varchar(25),total_matches int(4),total_players int(3),no_of_championships int(4))")
cur.execute("create table personal_info(p_id int(3) primary key,name varchar(25),age int(3),height_in_m float(3,1),weight_in_kg float(3,1),years_of_experience int(3),t_id int(3),date_of_join date,foreign key(t_id) references team_stats(t_id) on delete cascade on update cascade)")
cur.execute("create table player_stats(p_id int(3),t_id int(3),runs int(7),wickets int(7),catches int(3),matches int(4),boundries int(7),foreign key(p_id) references personal_info(p_id),foreign key(t_id) references team_stats(t_id) on delete cascade on update cascade)")
cur.execute("create table points_table(t_id int(3),team_name varchar(25),wins int(4),loses int(10),draws int(10),total_matches int(4),total_points int(10),foreign key(t_id) references team_stats(t_id) on delete cascade on update cascade)")

#DEFAULT VALUES
cur.execute("insert into team_stats values(1,'The Guardians',10,53,2)")
cur.execute("insert into team_stats values(2,'Fireballs',10,34,4)")
cur.execute("insert into team_stats values(3,'Vandals',10,47,1)")
cur.execute("insert into team_stats values(4,'Explorers',10,28,3)")

cur.execute("insert into personal_info values(1,'Krish',21,1.8,88.3,2,4,'2014-12-03')")
cur.execute("insert into personal_info values(2,'Zain',23,1.6,73.5,5,1,'2015-05-12')")
cur.execute("insert into personal_info values(3,'Akarsh',26,1.7,82.7,7,3,'2016-09-30')")
cur.execute("insert into personal_info values(4,'Shray',28,1.9,92.4,9,2,'2011-02-28')")

cur.execute("insert into player_stats values(1,4,2342,54,22,51,137)")
cur.execute("insert into player_stats values(2,1,3463,24,67,83,428)")
cur.execute("insert into player_stats values(3,3,1942,105,14,72,32)")
cur.execute("insert into player_stats values(4,2,5569,17,81,127,503)")


cur.execute("insert into points_table values(1,'The Guardians',10,5,1,16,15)")
cur.execute("insert into points_table values(2,'Fireballs',13,3,0,16,23)")
cur.execute("insert into points_table values(3,'Vandals',16,0,0,16,32)")
cur.execute("insert into points_table values(4,'Explorers',15,0,1,16,30)")

#MAIN
engine=pyttsx3.init()
text="welcome to cricket database management by aarav, abhinav and jayadithya"
engine.setProperty("rate",150)
engine.say(text)
engine.runAndWait()

#menu
while True:
    engine=pyttsx3.init()
    text="Please choose an option to perform"
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()
    l1=['1.NEW RECORDS','2.UPDATE RECORDS','3.RETRIEVE RECORDS','4.EXIT']
    n=e.buttonbox('------------------->> PLEASE CHOOSE AN OPTION TO PERFORM <<-------------------','CRICKET',l1)
    if n==l1[0]:#ADDING NEW RECORDS
        while True:
            engine=pyttsx3.init()
            text="please select a table to add record in"
            engine.setProperty("rate",150)
            engine.say(text)
            engine.runAndWait()
            l2=['PERSONAL INFO','PLAYER STATS','TEAM STATS','POINTS TABLE','RETURN TO PREVIOUS MENU']
            a=e.buttonbox('----------------->>> PLEASE SELECT A TABLE TO ADD RECORD IN <<<-----------------','CRICKET',l2)
            if a==l2[0]:
                def api():
                    l3=["PLAYER ID","NAME","AGE","HEIGHT(in metres)","WEIGHT(in kilograms)","YEARS OF EXPERIENCE","TEAM ID","DATE OF JOIN(YYYY-MM-DD"]
                    b=e.multenterbox('PLEASE ENTER INFORMATION IN ALL THE FIELDS','CRICKET - NEW PLAYER',l3)
                    p_id=int(b[0])
                    name=b[1]
                    age=int(b[2])
                    height=float(b[3])
                    weight=float(b[4])
                    years=int(b[5])
                    t_id=int(b[6])
                    date=b[7]
                    cur.execute("insert into personal_info values({},'{}',{},{},{},{},{},'{}')".format(p_id,name,age,height,weight,years,t_id,date))
                    mycon.commit()
                    engine=pyttsx3.init()
                    text="DATA ADDED SUCCESSFULLY"
                    engine.setProperty("rate",150)
                    engine.say(text)
                    engine.runAndWait()
                    e.msgbox('DATA ADDED SUCCESSFULLY','CRICKET')
                api()

            elif a==l2[1]:
                def aps():
                    l4=["PLAYER ID","TEAM ID","RUNS","WICKETS","CATCHES","MATCHES PLAYED","BOUNDARIES"]
                    c=e.multenterbox('PLEASE ENTER INFORMATION IN ALL THE FIELDS','CRICKET - NEW STAT',l4)
                    p_id=int(c[0])
                    t_id=int(c[1])
                    runs=int(c[2])
                    wickets=int(c[3])
                    catches=int(c[4])
                    matches=int(c[5])
                    boundaries=int(c[6])
                    cur.execute("insert into player_stats values({},{},{},{},{},{},{})".format(p_id,t_id,runs,wickets,catches,matches,boundaries))
                    mycon.commit()
                    engine=pyttsx3.init()
                    text="DATA ADDED SUCCESSFULLY"
                    engine.setProperty("rate",150)
                    engine.say(text)
                    engine.runAndWait()
                    e.msgbox('DATA ADDED SUCCESSFULLY','CRICKET')
                aps()

            elif a==l2[2]:
                def ats():
                    l5=["TEAM ID","TEAM NAME","TOTAL MATCHES PLAYED","TOTAL PLAYERS IN THE TEAM","NUMBER OF CHAMPIONSHIPS WON"]
                    f=e.multenterbox('PLEASE ENTER INFORMATION IN ALL THE FIELDS','CRICKET - NEW TEAM',l5)
                    t_id=int(f[0])
                    team_name=f[1]
                    total_matches=int(f[2])
                    total_players=int(f[3])
                    no_of_championships=int(f[4])
                    cur.execute("insert into team_stats values({},'{}',{},{},{})".format(t_id,team_name,total_matches,total_players,no_of_championships))
                    mycon.commit()
                    engine=pyttsx3.init()
                    text="DATA ADDED SUCCESSFULLY"
                    engine.setProperty("rate",150)
                    engine.say(text)
                    engine.runAndWait()
                    e.msgbox('DATA ADDED SUCCESSFULLY','CRICKET')
                ats()

            elif a==l2[3]:
                def apt():
                    l6=['TEAM ID','TEAM NAME','WINS','LOSES','DRAWS']
                    g=e.multenterbox('PLEASE ENTER INFORMATION IN ALL THE FIELDS','CRICKET - NEW ENTRY',l6)
                    t_id=int(g[0])
                    team_name=g[1]
                    wins=int(g[2])
                    loses=int(g[3])
                    draws=int(g[4])
                    tot=wins+loses+draws
                    points=2*(wins)-(loses)
                    cur.execute("insert into points_table values({},'{}',{},{},{},{},{})".format(t_id,team_name,wins,loses,draws,tot,points))
                    mycon.commit()
                    engine=pyttsx3.init()
                    text="DATA ADDED SUCCESSFULLY"
                    engine.setProperty("rate",150)
                    engine.say(text)
                    engine.runAndWait()
                    e.msgbox('DATA ADDED SUCCESSFULLY','CRICKET')
                apt()

            elif a==l2[4]:
                break

    elif n==l1[1]:#UPDATING NEW RECORDS
        while True:
            engine=pyttsx3.init()
            text="please select a table to update records in"
            engine.setProperty("rate",150)
            engine.say(text)
            engine.runAndWait()
            l2=['PERSONAL INFO','PLAYER STATS','TEAM STATS','POINTS TABLE','RETURN TO PREVIOUS MENU']
            a=e.buttonbox('------------->>> PLEASE SELECT A TABLE TO UPDATE RECORDS IN <<<-------------','CRICKET',l2)
            if a==l2[0]:
                while True:
                    engine=pyttsx3.init()
                    text="please select a field to update"
                    engine.setProperty("rate",150)
                    engine.say(text)
                    engine.runAndWait()
                    def upi():
                        l3=["AGE","HEIGHT(in metres)","WEIGHT(in kilograms)","YEARS OF EXPERIENCE","TEAM ID",'RETURN TO PREVIOUS MENU']
                        b=e.buttonbox('----------------------->>> PLEASE SELECT A FIELD TO UPDATE <<<-----------------------','CRICKET - UPDATE',l3)
                        a=e.multenterbox("PLEASE ENTER PLAYER ID OF RECORD TO BE UPDATED:","cricket update",["player id"])
                        while True:
                            if b==l3[0]:
                                h=e.multenterbox("PLEASE ENTER NEW AGE",'CRICKET - UPDATE',["AGE"])
                                cur.execute("update personal_info set age={} where p_id={}".format(h,a))
                                mycon.commit()
                                engine=pyttsx3.init()
                                text="RECORD UPDATED SUCCESSFULLY"
                                engine.setProperty("rate",150)
                                engine.say(text)
                                engine.runAndWait()
                                e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                            elif b==l3[1]:
                                g=e.multenterbox("PLEASE ENTER NEW HEIGHT",'CRICKET - UPDATE',["Height"])
                                cur.execute("update personal_info set height_in_m={} where p_id={}".format(g,a))
                                mycon.commit()
                                engine=pyttsx3.init()
                                text="RECORD UPDATED SUCCESSFULLY SUCCESSFULLY"
                                engine.setProperty("rate",150)
                                engine.say(text)
                                engine.runAndWait()
                                e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                            elif b==l3[2]:
                                j=e.multenterbox("PLEASE ENTER NEW WEIGHT",'CRICKET - UPDATE',["Weight"])
                                cur.execute("update personal_info set weight_in_kg={} where p_id={}".format(j,a))
                                mycon.commit()
                                engine=pyttsx3.init()
                                text="RECORD UPDATED SUCCESSFULLY"
                                engine.setProperty("rate",150)
                                engine.say(text)
                                engine.runAndWait()
                                e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                            elif b==l3[3]:
                                k=e.multenterbox("PLEASE ENTER UPDATED YEARS OF EXPERIENCE",'CRICKET - UPDATE',["Years of experience"])
                                cur.execute("update personal_info set years_of_experience={} where p_id={}".format(k,a))
                                mycon.commit()
                                engine=pyttsx3.init()
                                text="RECORD UPDATED SUCCESSFULLY"
                                engine.setProperty("rate",150)
                                engine.say(text)
                                engine.runAndWait()
                                e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                            elif b==l3[4]:
                                o=e.multenterbox("PLEASE ENTER UPDATED TEAM ID",'CRICKET - UPDATE',["Team Id"])
                                cur.execute("update personal_info set t_id={} where p_id={}".format(o,a))
                                mycon.commit()
                                engine=pyttsx3.init()
                                text="RECORD UPDATED SUCCESSFULLY"
                                engine.setProperty("rate",150)
                                engine.say(text)
                                engine.runAndWait()
                                e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                            elif b==l3[5]:
                                break
                    upi()

            elif a==l2[1]:
                def ups():
                    l4=["TEAM ID","RUNS","WICKETS","CATCHES","MATCHES PLAYED","BOUNDARIES",'RETURN TO PREVIOUS MENU']
                    c=e.buttonbox('---------------->>> PLEASE SELECT A FIELD TO UPDATE <<<----------------','CRICKET - UPDATE',l4)
                    a=e.multenterbox("PLEASE ENTER PLAYER ID OF RECORD TO BE UPDATED","CRICKET - UPDATE",["Player Id"])
                    while True:
                        if b==l4[0]:
                            h=e.multenterbox("PLEASE ENTER NEW TEAM ID",'CRICKET - UPDATE',["teamid"])
                            cur.execute("update player_stats set t_id={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[1]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF RUNS",'CRICKET - UPDATE',["runs"])
                            cur.execute("update player_stats set runs={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[2]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF WICKETS",'CRICKET - UPDATE',["wickets"])
                            cur.execute("update player_stats set wickets={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[3]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF CATCHES",'CRICKET - UPDATE',["catches"])
                            cur.execute("update player_stats set catches={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[4]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF MATCHES",'CRICKET - UPDATE',["matches"])
                            cur.execute("update player_stats set matches={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[5]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF BOUNDARIES",'CRICKET - UPDATE',["boundaries"])
                            cur.execute("update player_stats set boundaries={} where p_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l4[6]:
                            break

                ups()

            elif a==l2[2]:
                def uts():
                    l5=["TEAM NAME","TOTAL MATCHES","TOTAL PLAYERS","NUMBER OF CHAMPIONSHIPS","RETURN TO PREVIOUS MENU"]
                    c=e.buttonbox('---------------->>> PLEASE SELECT A FIELD TO UPDATE <<<----------------:','CRICKET - NEW STAT',l5)
                    a=e.multenterbox("PLEASE ENTER PLAYER ID OF RECORD TO BE UPDATED","CRICKET - UPDATE",["Team Id"])

                    while True:
                        if b==l5[0]:
                            h=e.multenterbox("PLEASE ENTER NEW TEAM NAME",'CRICKET - UPDATE',["Team Name"])
                            cur.execute("update team_stats set team name={} where ={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l5[1]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF TOTAL MATCHES",'CRICKET - UPDATE',["Total Matches"])
                            cur.execute("update team_stats set total matches={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l5[2]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF TOTAL PLAYERS",'CRICKET - UPDATE',["Total Players"])
                            cur.execute("update team_stats set total players={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l5[3]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF CHAMPIONSHIPS WON",'CRICKET - UPDATE',["number of championships"])
                            cur.execute("update team_stats set number of championships={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        else:
                            break
                uts()

            elif a==l2[3]:
                def upk():
                    l6=["TEAM NAME","WINS","LOSES","DRAWS","TOTAL MATCHES","RETURN TO PREVIOUS MENU"]
                    c=e.buttonbox('---------------->>> PLEASE SELECT A FIELD TO UPDATE <<<----------------','CRICKET - NEW STAT',l6)
                    a=e.multenterbox("PLEASE ENTER TEAM ID OF RECORD TO UPDATE:","cricket update",["Team Id"])
                    while True:
                        if b==l6[0]:
                            h=e.multenterbox("PLEASE ENTER NEW TEAM NAME",'CRICKET - UPDATE',["team name"])
                            cur.execute("update points_table set team name={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l6[1]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF WINS",'CRICKET - UPDATE',["wins"])
                            cur.execute("update points_table set wins{} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l6[2]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF LOSES",'CRICKET - UPDATE',["loses"])
                            cur.execute("update points_table set loses={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l6[3]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF DRAWS",'CRICKET - UPDATE',["draws"])
                            cur.execute("update points_table set draws={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l6[4]:
                            h=e.multenterbox("PLEASE ENTER UPDATED NUMBER OF TOTAL MATCHES",'CRICKET - UPDATE',["total matches"])
                            cur.execute("update points_table set total matches={} where t_id={}".format(h,a))
                            mycon.commit()
                            engine=pyttsx3.init()
                            text="RECORD UPDATED SUCCESSFULLY"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            e.msgbox("RECORD UPDATED SUCCESSFULLY",'CRICKET - UPDATE')

                        elif b==l6[5]:
                            break
                upk()

            elif a==l2[4]:
                break
    if n==l1[2]:#RETRIEVE RECORDS
        while True:
            l2=['PERSONAL INFO','PLAYER STATS','TEAM STATS','POINTS TABLE','RETURN TO PREVIOUS MENU']
            engine=pyttsx3.init()
            text="To view records click on any one of the buttons:"
            engine.setProperty("rate",150)
            engine.say(text)
            engine.runAndWait()
            z=e.buttonbox('------------>>> TO VIEW RECORDS CLICK ON ANY ONE OF THE BUTTONS <<<------------','CRICKET',l2)

            if z==l2[0]:
                engine=pyttsx3.init()
                text="This table shows you the personal info"
                engine.setProperty("rate",150)
                engine.say(text)
                engine.runAndWait()
                def display0():
                    class Table:
                        def __init__(self,root):
                            for i in range(total_rows):
                                for j in range(total_columns):
                                    self.e = Entry(root, width=13, fg='blue',font=('Courier New',14,'bold'))
                                    self.e.grid(row=i,column=j)
                                    self.e.insert(END,data[i][j])
                    cur.execute("select * from personal_info")
                    data=cur.fetchall()
                    data.append(('P_ID','T_ID','RUNS','WICKETS','WEIGHT','CATCHES','MATCHES','BOUNDARIES'))
                    data=data[-1:]+data[:-1]
                    total_rows = len(data)
                    total_columns = len(data[0])
                    root = Tk()
                    t = Table(root)
                    root.mainloop()
                display0()

            elif z==l2[1]:
                engine=pyttsx3.init()
                text="Click on any one of the following buttons to view records"
                engine.setProperty("rate",150)
                engine.say(text)
                engine.runAndWait()
                def display1():
                    while True:
                        l3=['HIGHEST RUNS','HIGHEST WICKETS','HIGHEST CATCHES','MOST NUMBER OF MATCHES','HIGHEST BOUNDARIES','ENTIRE TABLE','RETURN TO PREVIOUS MENU']
                        w=e.buttonbox('PLEASE SELECT AN OPTION TO VIEW:','cricket',l3)
                        if w==l3[0]:
                            engine=pyttsx3.init()
                            text="Maximum runs scored by any player"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1a():
                                cur.execute("select max(runs) from player_stats")
                                data=cur.fetchall()
                                e.msgbox(data[0],'CRICKET - HIGHEST RUNS SCORED')
                            display1a()

                        elif w==l3[1]:
                            engine=pyttsx3.init()
                            text="Maximum wickets taken by any player"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1b():
                                cur.execute("select max(wickets) from player_stats")
                                data=cur.fetchall()
                                e.msgbox(data[0],'CRICKET - MAXIMUM WICKETS')
                            display1b()

                        elif w==l3[2]:
                            engine=pyttsx3.init()
                            text="Maximum catches taken by any player"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1c():
                                cur.execute("select max(catches) from player_stats")
                                data=cur.fetchall()
                                e.msgbox(data[0],'CRICKET - MAXIMUM CATCHES TAKEN')
                            display1c()

                        elif w==l3[3]:
                            engine=pyttsx3.init()
                            text="Maximum matches played by any player"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1d():
                                cur.execute("select max(matches) from player_stats")
                                data=cur.fetchall()
                                e.msgbox(data[0],'CRICKET - MAXIMUM MATCHES')
                            display1d()

                        elif w==l3[4]:
                            engine=pyttsx3.init()
                            text="Maximum boundaries scored by any player"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1e():
                                cur.execute("select max(boundries) from player_stats")
                                data=cur.fetchall()
                                e.msgbox(data[0],'CRICKET - MAXIMUM BOUNDARIES')
                            display1e()

                        elif w==l3[5]:
                            engine=pyttsx3.init()
                            text="The above table shows you the player stats"
                            engine.setProperty("rate",150)
                            engine.say(text)
                            engine.runAndWait()
                            def display1f():
                                class Table:
                                    def __init__(self,root):
                                        for i in range(total_rows):
                                            for j in range(total_columns):
                                                self.e = Entry(root, width=13, fg='blue',font=('Courier New',14,'bold'))
                                                self.e.grid(row=i,column=j)
                                                self.e.insert(END,data[i][j])
                                cur.execute("select * from player_stats")
                                data=cur.fetchall()
                                data.append(('P_ID','NAME','AGE','HEIGHT','WEIGHT','YEARS OF EXPERIENCE','T_ID','DATE OF JOIN'))
                                data=data[-1:]+data[:-1]
                                total_rows = len(data)
                                total_columns = len(data[0])
                                root = Tk()
                                t = Table(root)
                                root.mainloop()
                            display1f()

                        elif w==l3[6]:
                            break

                display1()

            elif z==l2[2]:
                engine=pyttsx3.init()
                text="This table shows you the team stats"
                engine.setProperty("rate",150)
                engine.say(text)
                engine.runAndWait()
                class Table:
                    def __init__(self,root):
                        for i in range(total_rows):
                            for j in range(total_columns):
                                self.e = Entry(root, width=13, fg='blue',font=('Courier New',14,'bold'))
                                self.e.grid(row=i,column=j)
                                self.e.insert(END,data[i][j])
                cur.execute("select * from team_stats")
                data=cur.fetchall()
                data.append(('T_ID','TEAM NAME','TOTAL MATCHES','TOTAL PLAYERS','NUMBER OF CHAMPIONSHIPS'))
                data=data[-1:]+data[:-1]
                total_rows = len(data)
                total_columns = len(data[0])
                root = Tk()
                t = Table(root)
                root.mainloop()

            elif z==l2[3]:
                engine=pyttsx3.init()
                text="This table shows you the points"
                engine.setProperty("rate",150)
                engine.say(text)
                engine.runAndWait()
                def display3():
                    class Table:
                        def __init__(self,root):
                            for i in range(total_rows):
                                for j in range(total_columns):
                                    self.e = Entry(root, width=13, fg='blue',font=('Courier New',14,'bold'))
                                    self.e.grid(row=i,column=j)
                                    self.e.insert(END,data[i][j])
                    cur.execute("select * from points_table")
                    data=cur.fetchall()
                    data.append(('T_ID','TEAM NAME','WINS','LOSES','DRAWS','TOTAL MATCHES','TOTAL POINTS'))
                    data=data[-1:]+data[:-1]
                    total_rows = len(data)
                    total_columns = len(data[0])
                    root = Tk()
                    t = Table(root)
                    root.mainloop()
                display3()

            elif z==l2[4]:
                break

    elif n==l1[3]:
        engine=pyttsx3.init()
        text="thank you for using our program"
        engine.setProperty("rate",150)
        engine.say(text)
        engine.runAndWait()
        e.msgbox("THANK YOU FOR USING OUR CODE",'CRICKET')
        break
