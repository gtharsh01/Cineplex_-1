from tkinter import *
import cx_Oracle
import webbrowser
from tkinter import messagebox as msg
import ast##for file handling
from PIL import Image,ImageTk
import cv2
import signup
import cx_Oracle
import random
import connection
from connection import Connect
import view_admin

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="black")
root.resizable(False,False)

###browsers
def openlink(n):
    if n==1:
        webbrowser.open("https://in.bookmyshow.com/explore/home")
    if n==2:

        webbrowser.open("https://www.youtube.com/results?search_query=standup+up+comedy")
    if n==3:
        webbrowser.open("https://www.jiocinema.com")
    if n==4:
        webbrowser.open("https://open.spotify.com")
    if n==5:
        webbrowser.open("https://www.imdb.com")
        

#3.
def signin():
    username=user.get()
    password=code.get()
    
    conn = connection.Connect()
    cr = conn.cursor()

    q = f"select * from admin where empname='{username}' and emppass='{password}'"

    # q = "select * from admin where email='"+email+"' and password='"+password+"'"
    cr.execute(q)
    result = cr.fetchall()
    for i in result:
        print(i)
        
    if username=="username" and password=="password":
        msg.showwarning("","invalid Email/Password")
    elif result==():
        msg.showwarning("","invalid Email/Password")
    elif username==result[0][1]:
        if password!=result[0][4]:
            msg.showwarning("","invalid Password")
        elif password==result[0][4]:
            if result[0][5]=="Super Admin":
                msg.showinfo("", "Login Successful")
                command=view_admin.Main()
            else:
                msg.showinfo("", "Login Successful")
                command=page2('root')
        ###else:
        ###    msg.showwarning("","invalid Password")
        
            
    ###elif username:
    ###    msg.showwarning("","invalid Email/Password")
        
global img
img = PhotoImage(file='cinema1.png')

Label(root,image=img,bg='white').place(x=50,y=50)
Label(root,text='Hello Everyone',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=130,y=350)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#######.........................
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user= Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#######.........................
#1.
def on_enter(e):
    code.delete(0,'end')


def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')

code= Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=130)
code.insert(0,'password')

code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=167)
#######.........................
Button(frame,width=39,pady=7,text='Sign in',bg= 'blue',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="dont have an account",bg='red',fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

#######..........................
#2.
signupbtn=Button(frame,width=6,text='Sign up',cursor="hand2",bg='white',fg='blue',border=0,command=signup.Signup)
signupbtn.place(x=215,y=270)



i=50
def page2(dest):
    if dest=='screen1':
        print("page 3 destroyed")
        screen1.destroy()
    '''elif dest=='root':
        root.destroy()
       ''' 
    
    screen=Toplevel(root)     #signin toh baad page 2
    screen.title('cineplex')
    #screen.state("zoomed")
    screen.geometry('925x1025+300+200')
    screen.config(bg="white")
    screen.resizable(False,False)
    #Label(screen,text='Hello Everyone',bg='cyan',font=('Calbri(body)',50,'bold')).pack(expand=True)
    #i use PIL module in this case because photo is not getting access

    global photos1
    photos2 = PhotoImage(file='cinema2.png')
    Label(screen,image=photos2,bg='black',width=925,height=900).place(x=0,y=0)
    ###
    photo3=Image.open('dhamaka.png')
    photo3=photo3.resize((46,46))
    global my
    my=ImageTk.PhotoImage(photo3)
    Label(screen,image=my,bg='white').place(x=0,y=0)
    ###
    frame=Frame(screen,width=925,height=65,bg="white")

    frame.place(x=50,y=0)

    ##button1
    photo4=Image.open('dhamaka.png')
    photo4=photo4.resize((46,46))
    global my1
    my1=ImageTk.PhotoImage(photo4)
   
    Button(frame,width=50,pady=7,image=my1,border=0,command=lambda:openlink(1)).place(x=40,y=0)
    Label(frame,text='Movies',bg='white',font=('Calbri(body)',8,'bold')).place(x=42,y=48)

    ##button2
    photo5=Image.open('mike-1-1.jpg')
    photo5=photo5.resize((46,46))
    global my2
    my2=ImageTk.PhotoImage(photo5)
        
    Button(frame,width=50,pady=7,image=my2,border=0,command=lambda:openlink(2)).place(x=110,y=0)
    Label(frame,text='comedy',bg='white',font=('Calbri(body)',8,'bold')).place(x=112,y=48)

    ##button3
    photo6=Image.open('tata-ipl-logo.png')
    photo6=photo6.resize((46,46))
    global my3
    my3=ImageTk.PhotoImage(photo6)
    
    Button(frame,width=50,pady=7,image=my3,border=0,command=lambda:openlink(3)).place(x=180,y=0)
    Label(frame,text='Cricket',bg='white',font=('Calbri(body)',8,'bold')).place(x=182,y=48)

    ##button4
    photo7=Image.open('spotify.png')
    photo7=photo7.resize((46,46))
    global my4
    my4=ImageTk.PhotoImage(photo7)
    
    Button(frame,width=50,pady=7,image=my4,border=0,command=lambda:openlink(4)).place(x=250,y=0)
    Label(frame,text='Spotify',bg='white',font=('Calbri(body)',8,'bold')).place(x=252,y=48)

    ##button5
    photo8=Image.open('imdb_logo.png')
    photo8=photo8.resize((46,46))
    global my5
    my5=ImageTk.PhotoImage(photo8)
        
    Button(frame,width=50,pady=7,image=my5,border=0,command=lambda:openlink(5)).place(x=320,y=0)
    Label(frame,text='IMDB',bg='white',font=('Calbri(body)',8,'bold')).place(x=322,y=48)

    #button6
    photo9=Image.open('ser.png')
    photo9=photo9.resize((46,46))
    global my20
    my20=ImageTk.PhotoImage(photo9)
    Button(frame,width=50,pady=7,image=my20,border=0,command=lambda:search()).place(x=390,y=0)
    Label(frame,text='Search',bg='white',font=('Calbri(body)',8,'bold')).place(x=392,y=48)

    

    def moving():
        global i
        i+=3
        btn.place(x=i,y=100)
        if i<900:
            screen.after(50,lambda:moving())
    
    btn= Label(screen,text="Cineplex Management System",border=2,font=('Calbri(body)',15,'bold'))
    screen.after(50,lambda:moving())

    
    label=Label(screen,text="Available Shows This Weekend",bg='magenta',fg='black',font=('Microsoft YaHei UI Light',18))
    label.place(x=250,y=125)
    ##movie1
    photo9=Image.open('avengers.jpeg')
    photo9=photo9.resize((100,150))
    global my6
    my6=ImageTk.PhotoImage(photo9)
        
    Button(screen,width=100,pady=7,image=my6,border=0,command=lambda:page3('avengers',1)).place(x=150,y=200)
    Label(screen,text='Avengers:endgame',bg='white',font=('Calbri(body)',8,'bold')).place(x=150,y=365)

    #movie2
    photo10=Image.open('mazerunner.jpeg')
    photo10=photo10.resize((100,150))
    global my7
    my7=ImageTk.PhotoImage(photo10)
        
    Button(screen,width=100,pady=7,image=my7,border=0,command=lambda:page3('Maze Runner:3',2)).place(x=300,y=200)
    Label(screen,text='Maze Runner:3',bg='white',font=('Calbri(body)',8,'bold')).place(x=300,y=365)

    #movie3
    photo12=Image.open('shehzada.jpg')
    photo12=photo12.resize((100,150))
    global my9
    my9=ImageTk.PhotoImage(photo12)
        
    Button(screen,width=100,pady=7,image=my9,border=0,command=lambda:page3('shehzada',3)).place(x=450,y=200)
    Label(screen,text='Shehzada',bg='white',font=('Calbri(body)',8,'bold')).place(x=470,y=365)

    #movie4
    photo11=Image.open('war.jpg')
    photo11=photo11.resize((100,150))
    global  my8
    my8=ImageTk.PhotoImage(photo11)
        
    Button(screen,width=100,pady=7,image=my8,border=0,command=lambda:page3('War',4)).place(x=600,y=200)
    Label(screen,text='War',bg='white',font=('Calbri(body)',8,'bold')).place(x=630,y=365)    

    #movie5
    photo12=Image.open('The_Royal_Treatment.jpg')
    photo12=photo12.resize((100,150))
    global my10
    my10=ImageTk.PhotoImage(photo12)
        
    Button(screen,width=100,pady=7,image=my10,border=0,command=lambda:page3('The Royal Treatment',5)).place(x=150,y=500)
    Label(screen,text='The Royal Treatment',bg='white',font=('Calbri(body)',8,'bold')).place(x=150,y=665)    

    #movie6
    photo13=Image.open('avatar2.jpg')
    photo13=photo13.resize((100,150))
    global my11
    my11=ImageTk.PhotoImage(photo13)
        
    Button(screen,width=100,pady=7,image=my11,border=0,command=lambda:page3('Avatar:The Way Of Water',6)).place(x=300,y=500)
    Label(screen,text='Avatar:The Way Of Water',bg='white',font=('Calbri(body)',8,'bold')).place(x=300,y=665)    

    #movie7
    photo14=Image.open('Pathaan.jpg')
    photo14=photo14.resize((100,150))
    global my12
    my12=ImageTk.PhotoImage(photo14)
    #name=StringVar(value='pathaan')
    Button(screen,width=100,pady=7,image=my12,border=0,command=lambda:page3('pathaan',7)).place(x=450,y=500)
    Label(screen,text='Pathaan',bg='white',font=('Calbri(body)',8,'bold')).place(x=470,y=665)    
       
    #movie8
    photo15=Image.open('chalmera.jpg')
    photo15=photo15.resize((100,150))
    global my13
    my13=ImageTk.PhotoImage(photo15)
        
    Button(screen,width=100,pady=7,image=my13,border=0,command=lambda:page3('chal mera putt3',8)).place(x=600,y=500)
    Label(screen,text='Chal Mera Putt 2',bg='white',font=('Calbri(body)',8,'bold')).place(x=600,y=665)

    screen.mainloop()

def page3(movie,n):
    global screen1
    screen1=Toplevel(root)
    screen1.title('movie')
    screen1.geometry('925x1025+300+200')
    screen1.config(bg="white")
    screen1.resizable(False,False)
    #Label(screen,text='Hello Everyone',bg='cyan',font=('Calbri(body)',50,'bold')).pack(expand=True)
    #i use PIL module in this case because photo is not getting access

    global photos2
    photos2 = PhotoImage(file='cinema2.png')
    Label(screen1,image=photos2,bg='black',width=925,height=900).place(x=0,y=0)

    Label(screen1,image=my,bg='white').place(x=0,y=0)
    ###
    frame3=Frame(screen1,width=925,height=65,bg="white")

    frame3.place(x=50,y=0)

    ##button1
    Button(frame3,width=50,pady=7,image=my1,border=0,command=lambda:openlink(1)).place(x=40,y=0)
    Label(frame3,text='Movies',bg='white',font=('Calbri(body)',8,'bold')).place(x=42,y=48)

    ##button2
    Button(frame3,width=50,pady=7,image=my2,border=0,command=lambda:openlink(2)).place(x=110,y=0)
    Label(frame3,text='comedy',bg='white',font=('Calbri(body)',8,'bold')).place(x=112,y=48)

    ##button3
    Button(frame3,width=50,pady=7,image=my3,border=0,command=lambda:openlink(3)).place(x=180,y=0)
    Label(frame3,text='Cricket',bg='white',font=('Calbri(body)',8,'bold')).place(x=182,y=48)

    ##button4
    Button(frame3,width=50,pady=7,image=my4,border=0,command=lambda:openlink(4)).place(x=250,y=0)
    Label(frame3,text='Spotify',bg='white',font=('Calbri(body)',8,'bold')).place(x=252,y=48)

    ##button5
    Button(frame3,width=50,pady=7,image=my5,border=0,command=lambda:openlink(5)).place(x=320,y=0)
    Label(frame3,text='IMDB',bg='white',font=('Calbri(body)',8,'bold')).place(x=322,y=48)

    ##button6
    photo21=Image.open('home.png')
    photo21=photo21.resize((46,46))
    global my21
    my21=ImageTk.PhotoImage(photo21)
    Button(frame3,width=50,pady=7,image=my21,border=0,command=lambda:page2('screen1')).place(x=390,y=0)
    Label(frame3,text='Home',bg='white',font=('Calbri(body)',8,'bold')).place(x=392,y=48)

    frame4=Frame(screen1,width=500,height=300,bg="white")

    frame4.place(x=200,y=290)
    if n==1:
        Button(screen1,width=100,pady=7,image=my6,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Avengers:Endgame(2019))',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)    
    elif n==2:
        Button(screen1,width=100,pady=7,image=my7,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Maze Runner:3(2016)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)
    elif n==3:
        Button(screen1,width=100,pady=7,image=my9,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Shehzada(2023)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)
    elif n==4:
        Button(screen1,width=100,pady=7,image=my8,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='War(2020)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)
    elif n==5:
        Button(screen1,width=100,pady=7,image=my10,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='The Royal Treatment(2022)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)
    elif n==6:
        Button(screen1,width=100,pady=7,image=my11,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Avatar:2',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)
                  
    elif n==7:
        Button(screen1,width=100,pady=7,image=my12,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Pathaan(2023)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)       
    elif n==8:
        Button(screen1,width=100,pady=7,image=my13,border=0).place(x=400,y=100)
        Label(screen1,text=movie,bg='white',font=('Calbri(body)',8,'bold')).place(x=410,y=260)       

        ##info
        Label(frame4,text='Chal mera putt 3(2021)',bg='white',font=('Calbri(body)',12,'bold')).place(x=0,y=50)       


    user= Entry(frame4,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=100,y=80)
    Label(frame4,text='Name:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=80)

    Age= Entry(frame4,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    Age.place(x=100,y=110)
    Label(frame4,text='Age:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=110)

    email= Entry(frame4,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    email.place(x=100,y=140)
    Label(frame4,text='Email:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=140)

    venue= Entry(frame4,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    venue.place(x=100,y=170)
    Label(frame4,text='Venue:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=170)

    tickets= Entry(frame4,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    tickets.place(x=100,y=200)
    Label(frame4,text='Tickets:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=200)

    submit=Button(frame4,width=30,pady=7,bg='orange',text='Submit',border=0,command=lambda:ticket(user,Age,email,venue,tickets)).place(x=120,y=240)

    


 ##movie data entry
def ticket(us,ag,em,ve,ti):

    n=random.randint(1000,9999)
    name1=us.get()
    age1=ag.get()
    email2=em.get()
    timing=ve.get()
    ticket1=ti.get()
    
    '''con=cx_Oracle.connect(user='system',password='123456')
    print(con)'''
    conn = connection.Connect()
    cr = conn.cursor()
    q = f"insert into movies values(null, '{name1}', '{age1}','{email2}','{timing}','{ticket1}')"
    cr.execute(q)
    conn.commit()
    
    msg.showinfo("Congratulaions..!!","Your ticket is Booked..!!")
    '''cur=con.cursor()
    s='insert into movies values(:1,:2,:3,:4,:5,:6)'
    cur.execute(s,(n,user1,age1,email2,venue1,ticket1))
    con.commit()'''
        
    
def search():
    global screen2
    screen2=Toplevel(root)
    screen2.title('search')
    #screen.state("zoomed")
    screen2.geometry('500x600+300+200')
    screen2.config(bg="white")
    screen2.resizable(False,False)
    frame10=Frame(screen2,width=500,height=400,bg="white")

    frame10.place(x=50,y=0)
    sear= Entry(screen2,width=40,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    sear.place(x=200,y=200)
    Label(screen2,text='enter ticket number:',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=200)

    submit=Button(screen2,width=30,pady=7,bg='orange',text='Submit',border=0,command=lambda:search2(sear)).place(x=120,y=240)

    
def search2(s1):
    s11=s1.get()
    con=cx_Oracle.connect(user='system',password='123456')
    cur=con.cursor()
    s='select * from movies'
    cur.execute(s)
    m11=cur.fetchall()
    con.commit()
    for i in m11:
        Label(screen2,text=i[0],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=300)
        Label(screen2,text=i[1],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=330)
        Label(screen2,text=i[2],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=360)
        Label(screen2,text=i[3],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=390)     
        Label(screen2,text=i[4],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=420)
        Label(screen2,text=i[5],bg='magenta',font=('Calbri(body)',14,'bold')).place(x=5,y=450)                                                                            
                                                                                    
root.mainloop()
