#!
from tkinter import *
import smtplib
import time
from validate_email import validate_email
import datetime


###################################################################################

    

  


def login():
    def main():
        def lesson1():
            print('\n')
            print('Stopwatch Game Lesson:')
            print('Importing:')
            print('To make this project we need to import a built in module called time.This module allows us to work with time.You may have heard of the function datetime , and these built in modules are very similar you can check this module out by clicking on project:ALARM CLOCK.As I said this module is built in so all you have to do is type (import time) ')
        def game1():
            print('\n')
            print('Stopwatch game:')
            print('Press enter')
            while True:
                try:
                    input('')
                    st=time.time()
                    print('Started')
                    while True:
                        print(round(time.time()-st,0))
                        time.sleep(1)
                except KeyboardInterrupt:
                    et=time.time()
                    print('')
                    print('Final time: ',round(et-st,2))
                    break
        #Lesson
        def lesson2():
            print('\n')
            print('Stopwatch Game Lesson:')
            print('Importing:')
            print('')
        def game2():
            h=str(datetime.datetime.now().hour)
            m=(datetime.datetime.now().minute)
            m=m+1
            m=str(m)
            print('ALARM CLOCK')
            print('Hour:What hour do you want to set the alarm to?    Minute:What minute do you want to set the alarm to? \n    Tip:Set the hour to '+h+' and the minute to '+m)
            print('\n')
            alarmHour=int(input("HOUR"))
            alarmMinute=int(input("MINUTE"))
            ampm=str(input("am or pm"))
            if ampm=="pm":
                alarmHour=alarmHour+12
                while(1==1):
                    if(alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
                      print("TIMES UP")
                    break
        def lesson3():
            print('\n')
            print('Turtle Graphiics:')
            print('Importing:')
            print('')
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

       
           #Game
        game1=Toplevel(screen2)
        game1.title('Magnitudo Free:Python:Game develoupment')
        game1.geometry('500x500')
        headin=Label(game1,text='Games & Lesson:Free',bg='blue',fg='red')
        headin.pack()
        lesson1=Button(game1,text='lesson1:Stopwatch game',bg='powder blue',fg='black',width='50',bd='3',command=lesson1)
        lesson1.pack()
        game11=Button(game1,text='Game1:Stopwatch:Game',bg='powder blue',fg='black',width='50',bd='3',command=game1)
        game11.pack()
        lesson2=Button(game1,text='lesson2:Alarm Clock',bg='powder blue',fg='black',width='50',bd='3',command=lesson2)
        lesson2.pack()
        game2=Button(game1,text='Game2:Alarm Clock',bg='powder blue',fg='black',width='50',bd='3',command=game2)
        game2.pack()
        lesson3=Button(game1,text='Lesson(Special):Turtle Graphics!',bg='red',fg='dark blue',width='50',bd='3',command=lesson3)
        lesson3.pack()
        game1.mainloop()

        print('Stopwatch game:')
        print('Press enter')
        while True:
            try:
                input('')
                st=time.time()
                print('Started')
                while True:
                    print(round(time.time()-st,0))
                    time.sleep(1)
            except KeyboardInterrupt:
                et=time.time()
                print('')
                print('Final time: ',round(et-st,2))
                break


    def i_d():
        print('Validating please wait one moment...')
        g_info=g.get()
        print('Checking info..')
        if g_info=="2011":
          main()
        else:
            error()
 


    def error():
        warning3=Label(screen2,text='All fields need to be valid',bg="red",fg="yellow").pack()
    def save():
        print("Validating...Please wait one moment")
    

        f=0
        g_info=g.get()
        valid=validate_email(g_info,verify=True)
        valid
        print("99% done...")
    
        file=open("user.txt","r")
        content=file.read()
        file.close()
        a=g_info in content
        tf=a
        if valid=='False':
            print('Email is not valid')
            f=1
            error()
        if g_info =='':
            f=1
            error()
        if f==0 and valid==None and g_info in content :
            main()
    
        else:
            print('Please sign in first')
            error()    


            
    screen2=Toplevel(screen)
    screen2.title('Login Page')
    screen2.geometry("500x500")
    heading=Label(screen2,text='Form',bg="yellow",fg="blue",width="500",height="3")
    heading.pack()
    gmail=Label(screen2,text="Gmail")
    gmail.pack()
    gmail=StringVar()


    g=Entry(screen2,textvariable=gmail,width="30")
    g.pack()


    save3=Button(screen2,text="Log-in with email",width="20",height="2",bg='powder blue',fg="black",command=save)
    save3.pack()


    i_d=Button(screen2,text="Log-in with id",width="20",height="2",bg='powder blue',fg="black",command=i_d)
    i_d.pack()


















##################################################################################






def error1():
    screen1=Toplevel(screen1)
    screen1.geometry('150x90')
    screen1.title('Warning')
    warning=Label(screen1,text='All fields need to be valid',bg="red",fg="yellow").pack()
def save1():
    f=0
    print("Validating...")
    fe_info=fe.get()
    le_info=le.get()
    g_info=g.get()
    valid=validate_email(g_info,verify=True)
    valid
    print(valid)
    if fe_info=='':
        error1()
    if le_info=='':
        error()

    if g_info=='':
        error1()
    print('50% done')
    if valid==False:
        print("75% done")
        error1()
        print("Failed")
        f=1
    if valid==None:
        print('Please wait one moment...')
        file=open("user.txt","a")
        file.write('\n')
        file.write(fe_info)
        file.write('\n')
        file.write(le_info)
        file.write('\n')
        file.write(g_info)
        file.write("\n")
        file.close()
        print("You are signed in!You will recive an email in a few seconds with the information to the lesson")
        gmailaddress = 'pranavS31899@gmail.com'
        gmailpassword = 'PRANAVSAI'
        mailto = g_info

        msg = 'You are signed up, your id is 2011'
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , msg)
        mailServer.quit()
def signin():
    def save1():
        f=0
        print("Validating...")
        fe_info=fe.get()
        le_info=le.get()
        g_info=g.get()
        valid=validate_email(g_info,verify=True)
        valid
        print(valid)
        if fe_info=='':
            error1()
        if le_info=='':
            error()

        if g_info=='':
            error1()
        print('50% done')
        if valid==False:
            print("75% done")
            error1()
            print("Failed")
            f=1
        if valid==None:
            print('Please wait one moment...')
            file=open("user.txt","a")
            file.write('\n')
            file.write(fe_info)
            file.write('\n')
            file.write(le_info)
            file.write('\n')
            file.write(g_info)
            file.write("\n")
            file.close()
            print("You are signed in!You will recive an email in a few seconds with the information to the lesson")
            gmailaddress = 'pranavS31899@gmail.com'
            gmailpassword = 'PRANAVSAI'
            mailto = g_info

            msg = 'You are signed up, your id is 2011'
            mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
            mailServer.starttls()
            mailServer.login(gmailaddress , gmailpassword)
            mailServer.sendmail(gmailaddress, mailto , msg)
            mailServer.quit()
    screen1=Toplevel(screen)
    screen1.title('Form')
    screen1.geometry("500x500")
    heading=Label(screen1,text='Form',bg="yellow",fg="blue",width="500",height="3")
    heading.pack()
    firstname=Label(screen1,text="First Name",)
    firstname.place(x=15,y=70)
    lastname=Label(screen1,text="Last Name")
    lastname.place(x=15,y=140)
    gmail=Label(screen1,text="Gmail")
    gmail.place(x=15,y=210)
    firstname=StringVar()
    lastname=StringVar()
    gmail=StringVar()


    fe=Entry(screen1,textvariable=firstname,width="30")
    le=Entry(screen1,textvariable=lastname,width="30")
    g=Entry(screen1,textvariable=gmail,width="30")
    fe.place(x=15,y=100)
    le.place(x=15,y=180)
    g.place(x=15,y=250)


    save11=Button(screen1,text="Sign up",width="20",height="2",bg='powder blue',fg="black",command=save1)
    save11.place(x=15,y=300)





#####################################################################################

def chat():
    gmailaddress = input("what is your gmail address?  ")
    gmailpassword = input("what is the password for that email address?   ")
    mailto ='pranavS31899@gmail.com'
    msg = input("What is your message? \n ")
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Sent!")
    mailServer.quit()



    





screen=Tk()
screen.title('Magnitudo:Python , Game,lessons & code')
screen.geometry('750x750')
l=Label(screen,text="Chat Bot",bg="yellow",fg="blue")
l=Button(screen,text='Sign in',bg='powder blue',fg='black',width='250',command=signin)
s=Button(screen,text='Log-In',bg='powder blue',fg='black',width='250',command=login)
c=Button(screen,text='Message Creator',bg='powder blue',fg='black',width='250',command=chat)
l.pack()
s.pack()
c.pack()

