from tkinter import *
import smtplib
import time
from validate_email import validate_email
import base64
def error():
    screen1=Toplevel(screen)
    screen1.geometry('150x90')
    screen1.title('Warning')
    warning=Label(screen1,text='All fields need to be valid',bg="red",fg="yellow").pack()



def error1():
    screen1=Toplevel(screen)
    screen1.geometry('150x90')
    screen1.title('Warning')
    warning=Label(screen1,text='Sorry,you dont have enough points to buy this product in your account'  ,bg="red",fg="yellow").pack()
def save():
    price=int(0)
    f=0
    a=0
    global p
    print("Validating...")
    le_info=le.get()
    u_info=u.get()
    p_info=p.get()
    encode=p_info.encode("utf-8")
    encoded=str(base64.b16encode(encode))
    #a=base64.b16decode(encoded.decode("utf-8"))
    f3=open('user.txt','r')
    contex=f3.read()
    ok=u_info and encoded in contex
    f3.close()
    if ok==False:
        error()
        f=1
        

    if le_info=='':
        error()
        f=1
    if p_info=='':
        error()
        f=1
    if u_info=='':
        error()
        f=1
    
    encode2=p_info.encode("utf-8")
    encoded2=base64.b16encode(encode2)
    encoded2=str(encoded2)
    #What the product is
    if le_info=='1':
        price=int(14.99)
        le_info='Paper 500 sheets'
    if le_info=='2':
        
        le_info=='The Deep End Book'
    
    print(encoded2)
    file=open(u_info+'.txt','r')
    content=file.read()
    content=int(content)
    for chr in content:
        a=int(a+1)
    print(content)
    file.close()    
    file1=open(u_info+'.txt','a') 
    print(content)
        
    if content<price:
        error1()
        f=1
 

    if content>price:
        file1.truncate(0)
        content1=content-price
        content1=str(content1)
        file1.write(content1)
        
    if f==0:
        a=Toplevel(screen)
        a.title('Validating')
        a.geometry("100x150")
        b=Label(a,text='You have purchased an item!You will recive your item in less than a week.Thankyou for ordering!.',bg='powder blue',fg='red')
        b.place()
        gmailaddress = 'pranavS31899@gmail.com'
        gmailpassword = 'PRANAVSAI'
        #gmailpassword=base64.b16decode(encoded.decode("utf-8"))

        mailto = 'pranavS31899@gmail.com'

        msg = 'Product'+p_info
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , msg)
        mailServer.quit()

screen=Tk()
screen.title('Form')
screen.geometry("500x500")
heading=Label(text='Form',bg="yellow",fg="blue",width="500",height="3")
heading.pack()

lastname=Label(text="Id of product")
lastname.place(x=15,y=140)
Username=Label(text='Username')
Username.place(x=15,y=200)
password=Label(text='Password')
password.place(x=15,y=280)
firstname=StringVar()
lastname=StringVar()
gmail=StringVar()



le=Entry(textvariable=lastname,width="30")
u=Entry(textvariable=gmail,width="30")
u.place(x=15,y=250)
p=Entry(text='Id of product',width='30')
p.place(x=15,y=315)
le.place(x=15,y=180)




save=Button(text="Buy",width="20",height="2",bg='powder blue',fg="black",command=save)
save.place(x=15,y=400)
