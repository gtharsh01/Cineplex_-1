
def l:
    window=Tk()

    window.title('signup')
    window.geometry('925x500+300+200')
    window.configure(bg="white")
    window.resizable(False,False)


    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm.get()
        if password==confirm_password:
            try:
                file=open('datasheet.txt','r')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))
                messagebox.showinfo('Signup','Sucessfully Login')

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showinfo('invalid','both password shoul')
        
            
        
    global img
    img = PhotoImage(file='login1.png')

    Label(window,image=img,bg='white').place(x=50,y=50)
    Label(window,text='Hello Everyone',bg='magenta',font=('Calbri(body)',14,'bold')).place(x=130,y=350)
    frame=Frame(window,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
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

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)
    #######.........................


    #2.
    def on_enter(e):
        confirm.delete(0,'end')


    def on_leave(e):
        name=confirm.get()
        if name=='':
            confirm.insert(0,'password')

    confirm= Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
    confirm.place(x=30,y=180)
    confirm.insert(0,'Confirm Password')
    confirm.bind('<FocusIn>',on_enter)
    confirm.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=207)
    #######.........................


    Button(frame,width=39,pady=7,text='Sign up',bg='blue',fg='white',border=0,command=signup).place(x=35,y=240)
    label=Label(frame,text="i have an account",bg='red',fg='black',font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=300)
    signup=Button(frame,width=6,text='Sign in',cursor="hand2",bg='white',fg='blue',border=0)
    signup.place(x=200,y=300)


    window.mainloop()

