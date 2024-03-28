from proj import *
i=50
def page2_1():
    screen=Toplevel(root)
    screen.title('cineplex')
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

    my=ImageTk.PhotoImage(photo3)
    Label(screen,image=my,bg='white').place(x=0,y=0)
    ###
    frame=Frame(screen,width=925,height=65,bg="white")

    frame.place(x=50,y=0)

    ##button1
    photo4=Image.open('dhamaka.png')
    photo4=photo4.resize((46,46))

    my1=ImageTk.PhotoImage(photo4)
        
    Button(frame,width=50,pady=7,image=my1,border=0).place(x=40,y=0)
    Label(frame,text='Movies',bg='white',font=('Calbri(body)',8,'bold')).place(x=42,y=48)

    ##button2
    photo5=Image.open('mike-1-1.jpg')
    photo5=photo5.resize((46,46))

    my2=ImageTk.PhotoImage(photo5)
        
    Button(frame,width=50,pady=7,image=my2,border=0).place(x=110,y=0)
    Label(frame,text='comedy',bg='white',font=('Calbri(body)',8,'bold')).place(x=112,y=48)

    ##button3
    photo6=Image.open('tata-ipl-logo.png')
    photo6=photo6.resize((46,46))

    my3=ImageTk.PhotoImage(photo6)
        
    Button(frame,width=50,pady=7,image=my3,border=0).place(x=180,y=0)
    Label(frame,text='Cricket',bg='white',font=('Calbri(body)',8,'bold')).place(x=182,y=48)

    ##button4
    photo7=Image.open('spotify.png')
    photo7=photo7.resize((46,46))

    my4=ImageTk.PhotoImage(photo7)
        
    Button(frame,width=50,pady=7,image=my4,border=0).place(x=250,y=0)
    Label(frame,text='Spotify',bg='white',font=('Calbri(body)',8,'bold')).place(x=252,y=48)

    ##button5
    photo8=Image.open('home.png')
    photo8=photo8.resize((46,46))

    my5=ImageTk.PhotoImage(photo8)
        
    Button(frame,width=50,pady=7,image=my5,border=0,command=homeicon).place(x=320,y=0)
    Label(frame,text='Home',bg='white',font=('Calbri(body)',8,'bold')).place(x=322,y=48)

    

    def moving():
        global i
        i+=3
        btn.place(x=i,y=100)
        if i<900:
            screen.after(50,lambda:moving())
    
    btn= Label(screen,text="support us by your feedback",border=2,font=('Calbri(body)',15,'bold'))
    screen.after(50,lambda:moving())

    
    label=Label(screen,text="Available Shows This Weekend",bg='magenta',fg='black',font=('Microsoft YaHei UI Light',18))
    label.place(x=250,y=125)
    ##movie1
    photo9=Image.open('avengers.jpeg')
    photo9=photo9.resize((100,150))

    my6=ImageTk.PhotoImage(photo9)
        
    Button(screen,width=100,pady=7,image=my6,border=0).place(x=150,y=200)
    Label(screen,text='Avengers:endgame',bg='white',font=('Calbri(body)',8,'bold')).place(x=150,y=365)

    #movie2
    photo10=Image.open('mazerunner.jpeg')
    photo10=photo10.resize((100,150))

    my7=ImageTk.PhotoImage(photo10)
        
    Button(screen,width=100,pady=7,image=my7,border=0).place(x=300,y=200)
    Label(screen,text='Maze Runner:3',bg='white',font=('Calbri(body)',8,'bold')).place(x=300,y=365)

    #movie3
    photo12=Image.open('shehzada.jpg')
    photo12=photo12.resize((100,150))

    my9=ImageTk.PhotoImage(photo12)
        
    Button(screen,width=100,pady=7,image=my9,border=0).place(x=450,y=200)
    Label(screen,text='Shehzada',bg='white',font=('Calbri(body)',8,'bold')).place(x=470,y=365)

    #movie4
    photo11=Image.open('war.jpg')
    photo11=photo11.resize((100,150))

    my8=ImageTk.PhotoImage(photo11)
        
    Button(screen,width=100,pady=7,image=my8,border=0).place(x=600,y=200)
    Label(screen,text='War',bg='white',font=('Calbri(body)',8,'bold')).place(x=630,y=365)    

    #movie5
    photo12=Image.open('The_Royal_Treatment.jpg')
    photo12=photo12.resize((100,150))

    my10=ImageTk.PhotoImage(photo12)
        
    Button(screen,width=100,pady=7,image=my10,border=0).place(x=150,y=500)
    Label(screen,text='The Royal Treatment',bg='white',font=('Calbri(body)',8,'bold')).place(x=150,y=665)    

    #movie6
    photo13=Image.open('avatar2.jpg')
    photo13=photo13.resize((100,150))

    my11=ImageTk.PhotoImage(photo13)
        
    Button(screen,width=100,pady=7,image=my11,border=0).place(x=300,y=500)
    Label(screen,text='Avatar:The Way Of Water',bg='white',font=('Calbri(body)',8,'bold')).place(x=300,y=665)    

    #movie7
    photo14=Image.open('Pathaan.jpg')
    photo14=photo14.resize((100,150))

    my12=ImageTk.PhotoImage(photo14)
        
    Button(screen,width=100,pady=7,image=my12,border=0).place(x=450,y=500)
    Label(screen,text='Pathaan',bg='white',font=('Calbri(body)',8,'bold')).place(x=470,y=665)    
       
    #movie8
    photo15=Image.open('chalmera.jpg')
    photo15=photo15.resize((100,150))

    my13=ImageTk.PhotoImage(photo15)
        
    Button(screen,width=100,pady=7,image=my13,border=0).place(x=600,y=500)
    Label(screen,text='Chal Mera Putt 2',bg='white',font=('Calbri(body)',8,'bold')).place(x=600,y=665)


    screen.mainloop()
