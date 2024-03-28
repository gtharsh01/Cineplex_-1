from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

import connection
##import proj as p1




class Main:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('User Login')

        self.root.geometry('700x600')

        self.mainLabel = Label(self.root, text="User Login", font=('', 24, 'bold'))
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root)
        self.font = ('', 14)

        self.userLabel = Label(self.formFrame, text="Enter Username", font=self.font)
        self.userLabel.grid(row=0, column=0, padx=10, pady=10)
        self.userEntry = Entry(self.formFrame, font=self.font, width=30)
        self.userEntry.grid(row=0, column=1, padx=10, pady=10)

        self.passlabel = Label(self.formFrame, text="Enter Password", font=self.font)
        self.passlabel.grid(row=1, column=0, padx=10, pady=10)
        self.passEntry = Entry(self.formFrame, font=self.font, width=30, show='*')
        self.passEntry.grid(row=1, column=1, padx=10, pady=10)

        self.formFrame.pack(pady=10)

        self.btn = Button(self.root, text="Submit", font=('', 14), width=10, command=self.verifyUser)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def verifyUser(self):
        user = self.userEntry.get()
        password = self.passEntry.get()

        conn = connection.Connect()
        cr = conn.cursor()

        q = f"select * from admin where empname='{user}' and emppass='{password}'"

        # q = "select * from admin where email='"+email+"' and password='"+password+"'"
        cr.execute(q)
        result = cr.fetchall()
        if len(result) == 0:
            msg.showwarning("",'Invalid Email/Password')
        else:
            msg.showinfo("", "Login Successful")
            self.root.destroy()


