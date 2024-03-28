from tkinter import *
from tkinter import messagebox as msg
import ast
from PIL import Image,ImageTk
from connection import *
##import user_login2


class Signup:
        def __init__(self):
                self.window=Toplevel()
                self.window.title('signup')
                self.window.geometry('925x500+300+200')
                self.window.configure(bg="white")
                self.window.resizable(False,False)

                self.conn=Connect()
                self.cr=self.conn.cursor()

                
                self.lb1=Label(self.window,text='Hello Everyone',bg='magenta',font=('Calbri(body)',14,'bold'))
                self.lb1.place(x=130,y=350)

                self.frame=Frame(self.window,width=350,height=430,bg="white")
                self.frame.place(x=480,y=25)
                
                self.imggg = PhotoImage(file='login1.png')

                self.img1=Label(self.window,image=self.imggg,bg='white')
                self.img1.place(x=50,y=50)

                self.heading=Label(self.frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
                self.heading.place(x=100,y=5)

                self.user = Entry(self.frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
                self.user.place(x=30,y=80)
                self.user.insert(0,'username')
                self.user.bind('<FocusIn>',self.on_enter1)
                self.user.bind('<FocusOut>',self.on_leave1)

                self.f1=Frame(self.frame,width=295,height=2,bg='black')###black lines
                self.f1.place(x=25,y=107)

                self.mail = Entry(self.frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
                self.mail.place(x=30,y=130)
                self.mail.insert(0,'Email')
                self.mail.bind('<FocusIn>',self.on_enter4)
                self.mail.bind('<FocusOut>',self.on_leave4)

                self.f1=Frame(self.frame,width=295,height=2,bg='black')###black lines
                self.f1.place(x=25,y=157)


                self.code= Entry(self.frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
                self.code.place(x=30,y=180)
                self.code.insert(0,'Password')
                self.code.bind('<FocusIn>',self.on_enter2)
                self.code.bind('<FocusOut>',self.on_leave2)

                self.f2=Frame(self.frame,width=295,height=2,bg='black')###black lines
                self.f2.place(x=25,y=207)
                
                self.confirm= Entry(self.frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
                self.confirm.place(x=30,y=230)
                self.confirm.insert(0,'Confirm Password')
                self.confirm.bind('<FocusIn>',self.on_enter3)
                self.confirm.bind('<FocusOut>',self.on_leave3)

                self.f3=Frame(self.frame,width=295,height=2,bg='black')###black lines
                self.f3.place(x=25,y=257)

                self.mobile= Entry(self.frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
                self.mobile.place(x=30,y=280)
                self.mobile.insert(0,'Mobile Number')
                self.mobile.bind('<FocusIn>',self.on_enter5)
                self.mobile.bind('<FocusOut>',self.on_leave5)

                self.f3=Frame(self.frame,width=295,height=2,bg='black')###black lines
                self.f3.place(x=25,y=307)

                        
                self.signBtn=Button(self.frame,width=39,pady=7,text='Sign up',bg=
                       'blue',fg='white',border=0,command=self.signupFnc)
                self.signBtn.place(x=35,y=340)
                self.label=Label(self.frame,text="i have an account",bg='red',fg='black',font=('Microsoft YaHei UI Light',9))
                self.label.place(x=90,y=400)
                self.signin=Button(self.frame,width=6,text='Sign in',cursor="hand2",bg='white',fg='blue',border=0,command=self.signinFnc)
                self.signin.place(x=200,y=400)

                self.window.mainloop()
        
        def signupFnc(self):
            username=self.user.get()
            mail=self.mail.get()
            password=self.code.get()
            confirm_password=self.confirm.get()
            mobile=self.mobile.get()
            #######
            p=f"select empid from admin where empname='{username}'"
            self.cr.execute(p)
            r1=self.cr.fetchall()
            #######
            q=f"select empid from admin where empmail='{mail}'"
            self.cr.execute(q)
            r2=self.cr.fetchall()
            if username == '' or mail == '' or mobile == '' or password == '' or confirm_password == '':
                    msg.showwarning("", "Please Enter All Data")
            #check1.username
            if len(r1)!=0:
                    msg.showwarning("","User Already Existed..")
            #check2.verify
            elif verifyMobile(mobile)!=True:
                    msg.showwarning("","Enter Valid Mobile Number..")
            #check3.verify
            elif verifyEmail(mail)==False:
                    msg.showwarning("","Enter Valid Email..")
            #check4.email
            elif len(r2)!=0:
                    msg.showwarning("","Email is Already Existed..")
            #check5.password
            elif password!=confirm_password:
                    msg.showwarning("","Password and Confirm Password is Not Same ..")
                    

            else:
                    msg.showinfo("", "Account created Successfully")

                    
                    q =f"insert into admin values(null, '{username}', '{mail}','{mobile}','{password}','User')"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Account",f"Username='{username}' and Password='{password}'")
                    


        def signinFnc(self):
                self.window.destroy()
        #######.........................
        #1.
        def on_enter1(self,e):
            self.user.delete(0,'end')

        def on_leave1(self,e):
            name=self.user.get()
            if name=='':
                    self.user.insert(0,'username')

        #2.
        def on_enter2(self,e):
            self.code.delete(0,'end')


        def on_leave2(self,e):
            name=self.code.get()
            if name=='':
                    self.code.insert(0,'password')

        #######.........................


        #3.
        def on_enter3(self,e):
            self.confirm.delete(0,'end')


        def on_leave3(self,e):
            name=self.confirm.get()
            if name=='':
                    self.confirm.insert(0,'password')

        #4.
        def on_enter4(self,e):
            self.mail.delete(0,'end')

        def on_leave4(self,e):
            name=self.mail.get()
            if name=='':
                    self.mail.insert(0,'Email')

        #5.
        def on_enter5(self,e):
            self.mobile.delete(0,'end')

        def on_leave5(self,e):
            name=self.mobile.get()
            if name=='':
                    self.mobile.insert(0,'Mobile Number')

#######.........................

