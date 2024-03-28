from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import Connect
from add_admin import *

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Admin')
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="View Admin", font=('', 30, 'bold'))
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root)

        self.searchLb = Label(self.searchFrame, text="Search By Name/Email/Mobile", font=('', 14))
        self.searchLb.grid(row=0, column=0, pady=10, padx=10)
        self.searchBox = Entry(self.searchFrame,font=('', 14), width=30)
        self.searchBox.grid(row=0, column=1, padx=10, pady=10)
        self.searchBtn = Button(self.searchFrame, text="Search", width=10, font=('',14),bg='red', command=self.search)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", width=10, font=('',14),bg='yellow', command=self.refresh)
        self.deleteBtn = Button(self.searchFrame, text="Delete", width=10, font=('',14),bg='green', command=self.deleteAdmin)
        self.addBtn = Button(self.searchFrame, text="Add Admin", width=10, font=('',14),bg='pink', command=Add1)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=10)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=10)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=10)
        self.addBtn.grid(row=0, column=5, padx=10, pady=10)

        self.searchFrame.pack(pady=20)

        self.adminTable = ttk.Treeview(self.root, columns=('id', 'name','pass', 'email', 'mobile', 'role'))
        self.adminTable.heading('id', text="Admin ID")
        self.adminTable.heading('name', text="Name")
        self.adminTable.heading('pass', text="Password")
        self.adminTable.heading('email', text="Email")
        self.adminTable.heading('mobile', text="Mobile")
        self.adminTable.heading('role', text="Role")

        self.adminTable.bind('<Double-1>', self.openUpdateWindow)

        self.adminTable['show'] = 'headings'

        self.adminTable.pack(pady=20, padx=20, expand=True, fill='both')
        self.getAdminValues()

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('', 14))
        style.configure('Treeview', font=('', 14), rowheight=40)

        self.root.mainloop()

    def openUpdateWindow(self,e):
        rowid = self.adminTable.selection()
        rowData = self.adminTable.item(rowid[0])
        admin = rowData['values']
        print(admin)

        self.updateWindow = Toplevel()
        self.updateWindow.geometry('700x600')
        self.updateWindow.title('Update Admin')

        self.mainLabel1 = Label(self.updateWindow, text='Update Admin', font=('', 24, 'bold'))
        self.mainLabel1.pack(pady=20)

        self.formFrame = Frame(self.updateWindow)
        self.formFrame.pack(pady=10)

        font = ('', 14)
        self.idLabel = Label(self.formFrame, text="Admin Id", font=font)
        self.idEntry = Entry(self.formFrame, width=30, font=font)
        self.idLabel.grid(row=0, column=0, pady=10, padx=10)
        self.idEntry.grid(row=0, column=1, pady=10, padx=10)
        self.idEntry.insert(0, admin[0])
        self.idEntry.configure(state='readonly')

        self.nameLabel = Label(self.formFrame, text="Admin Name", font=font)
        self.nameEntry = Entry(self.formFrame, width=30, font=font)
        self.nameLabel.grid(row=1, column=0, pady=10, padx=10)
        self.nameEntry.grid(row=1, column=1, pady=10, padx=10)
        self.nameEntry.insert(0, admin[1])

        self.emaillabel = Label(self.formFrame, text="Admin Email", font=font)
        self.emailEntry = Entry(self.formFrame, width=30, font=font)
        self.emaillabel.grid(row=2, column=0, pady=10, padx=10)
        self.emailEntry.grid(row=2, column=1, pady=10, padx=10)
        self.emailEntry.insert(0, admin[2])

        self.mobileLabel = Label(self.formFrame, text="Admin Mobile", font=font)
        self.mobileEntry = Entry(self.formFrame, width=30, font=font)
        self.mobileLabel.grid(row=3, column=0, pady=10, padx=10)
        self.mobileEntry.grid(row=3, column=1, pady=10, padx=10)
        self.mobileEntry.insert(0, admin[3])

        self.roleLabel = Label(self.formFrame, text="Admin Role", font=font)
        self.roleEntry = ttk.Combobox(self.formFrame, width=29, font=font, values=['Super Admin', 'Admin'],state='readonly')
        self.roleLabel.grid(row=4, column=0, pady=10, padx=10)
        self.roleEntry.grid(row=4, column=1, pady=10, padx=10)
        self.roleEntry.set(admin[4])

        self.updateBtn = Button(self.updateWindow, text="Update", width=10, font=font, command=self.updateAdmin)
        self.updateBtn.pack(pady=10)

        self.updateWindow.mainloop()

    def updateAdmin(self):
        id = self.idEntry.get()
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        mobile = self.mobileEntry.get()
        role = self.roleEntry.get()

        q = f"update admin set empname='{name}', empmail='{email}',empmobile='{mobile}', emprole='{role}' where empid='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('', 'Admin has been updated.', parent=self.updateWindow)
        self.getAdminValues()
        self.updateWindow.destroy()


    def deleteAdmin(self):
        rowid = self.adminTable.selection()
        if len(rowid) != 1:
            msg.showwarning("","Please Select a Single Admin..")
        else:
            rowData = self.adminTable.item(rowid[0])
            admin = rowData['values']
            q = f"delete from admin where empid='{admin[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("","Admin has been Deleted")
            self.getAdminValues()

    def search(self):
        text = self.searchBox.get()
        q = f"select empid,empname,emppass,empmail,empmobile,emprole from admin where empname like '%{text}%' or empmobile like '%{text}%' or empmail like '%{text}%'"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        count = 0
        for i in result:
            self.adminTable.insert('', index=count, values=i)
            count += 1

    def refresh(self):
        self.searchBox.delete(0, 'end')
        self.getAdminValues()

    def getAdminValues(self):
        q = f"select empid,empname,emppass,empmail,empmobile,emprole from admin"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        count = 0
        for i in result:
            self.adminTable.insert('', index=count, values=i)
            count += 1
