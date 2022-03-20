from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

with sqlite3.connect('DBmedsched') as db:
    cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS DBmedsched(MedName TEXT, StartDate TEXT, Until TEXT, IntakeDays TEXT, IntakeTime TEXT, Amount TEXT);""")

class win():
    def __init__(self,rt):
        self.rt = rt
        self.rt.title("MedSched")
        self.rt.geometry("1200x731")
        self.rt.resizable(width=False, height=False)


        def addMed():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            confirm = messagebox.askquestion("Confirmation", "Do you want to add this medicine?")
            if(confirm=="yes"):
                c.execute('INSERT INTO DBmedsched(MedName,StartDate,Until,IntakeDays,IntakeTime,Amount) VALUES(?,?,?,?,?,?)',(eName.get(),eStart.get(),eUntil.get(),eintkDate.get(),eintkTime.get(),eAmt.get()))
                conn.commit()
                eName.delete(0, END)
                eStart.delete(0, END)
                eUntil.delete(0, END)
                eintkDate.delete(0, END)
                eintkTime.delete(0, END)
                eAmt.delete(0, END)
                messagebox.showinfo("Entry Successful", "Entry Successful!, Press the refresh button to see it in the table")
            else:
                messagebox.showinfo("Action Cancelled", "Medicine not saved.")
            conn.commit()
            conn.close()

        def Query():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            c.execute("SELECT rowid, * FROM DBmedsched")
            rec = c.fetchall()
            global count
            count = 0
            for data in rec:
                if count % 2==0:
                    self.tbl_med.insert(parent='',index='end', iid=count, text='', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                else:
                    self.tbl_med.insert(parent='',index='end', iid=count, text='', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                count +=1
            conn.commit()
            conn.close()


        def display():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            c.execute("SELECT * FROM DBmedsched")
            rec2= c.fetchall()
            global count
            count = 0
            for j in self.tbl_med.get_children():
                self.tbl_med.delete(j)
            for data2 in rec2:
                if count %2 == 0:
                    self.tbl_med.insert(parent='', index='end', iid=count, text='',values=(data2[0],data2[1],data2[2],data2[3],data2[4], data2[5]))
                else:
                    self.tbl_med.insert(parent='', index='end', iid=count, text='',values=(data2[0],data2[1],data2[2],data2[3],data2[4],data2[5]))
                count+=1
            self.tbl_med.delete(*self.tbl_med.get_children())
            Query()
            conn.commit()

        def select():
            eId.delete(0, END)
            eName.delete(0, END)
            eStart.delete(0, END)
            eUntil.delete(0, END)
            eintkDate.delete(0, END)
            eintkTime.delete(0, END)
            eAmt.delete(0, END)

            selected = self.tbl_med.focus()
            val = self.tbl_med.item(selected, 'val')
            eId.insert(0, val[0])
            eName.insert(0, val[1])
            eStart.insert(0, val[2])
            eUntil.insert(0, val[3])
            eintkDate.insert(0, val[4])
            eintkTime.insert(0, val[5])
            eAmt.insert(0, val[6])

        def delete():
            permission = messagebox.askquestion("Confirmation", "Do you wish to delete this?")
            if permission =="yes":
                conn = sqlite3.connect('DBmedsched')
                c = conn.cursor()
                c.execute("DELETE FROM DBmedsched WHERE oid=" + eId.get())
                conn.commit()
                conn.close()
                messagebox.showinfo("Delete Successful","Delete Successful, Refresh to see changes.")
            else:
                messagebox.showinfo("Not Deleted", "Operation Cancelled or an error occured")

        def Update():
            ask = messagebox.askquestion("Confirmation", "Are you sure you want to update this?")
            if ask =="yes":
                select = self.tbl_med.focus()
                self.tbl_med.item(select, text="", values=(eId.get(),eName.get(),eStart.get(), eUntil.get(), eintkDate.get(),eintkTime.get(), eAmt.get(),))
                conn = sqlite3.connect('DBmedsched')
                c = conn.cursor()
                c.execute("UPDATE DBmedsched SET MedName = :mn, StartDate = :sd, Until = :u, IntakeDays = :ind, IntakeTime =:it, Amount =:am WHERE oid= :oid",{
                    'mn':eName.get(),
                    'sd':eStart.get(),
                    'u':eUntil.get(),
                    'ind':eintkDate.get(),
                    'it':eintkTime.get(),
                    'am':eAmt.get(),
                    'oid':eId.get(),
                })
                messagebox.showinfo("Success!", "Update Complete!")
            else:
                messagebox.showinfo("Update Incompelete", "Update Cancelled")

            conn.commit()
            conn.close()
        def about_us():
            messagebox.showinfo("About us","This application was made by group 4. Members:Tristan Tan, John lyndon Vasquez, Lance Pastrana, Chizel Diaz, April Nicole Martin")

#Frames
        mainFrame=Frame(self.rt, bd=10, width=1150, height=750, relief=RIDGE, bg='cyan')
        mainFrame.grid()
        titleframe=Frame(mainFrame, bd=5, width=1180, height=70, relief=FLAT,bg='#FFF89A')
        titleframe.grid()
        treeviewFrame=Frame(mainFrame, bd=5, width=1145, height=200, relief=RAISED)
        treeviewFrame.grid()
       # upperFrame2 = Frame(mainFrame, bd=5, width=1145, height=500, relief=RIDGE)
       # upperFrame2.grid(row=2, column=0)


        mainlabelFrame = Frame(mainFrame,bd =5, width=1130, height=480, relief=RAISED)
        mainlabelFrame.grid()

        xScroll = Scrollbar(treeviewFrame, orient=HORIZONTAL)
        yScroll = Scrollbar(treeviewFrame, orient=VERTICAL)
#labels
        titleLabel=Label(titleframe, font=('Arial', 30,'bold'), text="MEDSCHED", fg="#2D31FA", bg='#FFF89A')
        titleLabel.place(x=505, y=-1)
        nameLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Medicine Name:")
        nameLabel.grid(row=0,column=0)

        startLabel=Label(mainlabelFrame,font=('courier', 20,'bold'), text="Start Date:")
        startLabel.grid(row=1, column=0)

        untilLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Until:")
        untilLabel.grid(row=2, column=0)
        intkDatelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Day:")
        intkDatelbl.grid(row=3, column=0)
        intkTimelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Time:")
        intkTimelbl.grid(row=4, column=0)
        amtlbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Amount:")
        amtlbl.grid(row=5, column=0)

#Entry
        eId = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=5)
        eId.place(x=1000, y=1000)
        eName = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eName.grid(row=0, column=1)
        eStart = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eStart.grid(row=1, column=1)
        eUntil = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eUntil.grid(row=2, column=1)
        eintkDate= Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eintkDate.grid(row=3, column=1)
        eintkTime = Entry(mainlabelFrame, font=('arial', 20, 'bold'), width=30)
        eintkTime.grid(row=4, column=1)
        eAmt = Entry(mainlabelFrame, font=('arial', 20, 'bold'), width=30)
        eAmt.grid(row=5, column=1)
#buttons
        insertBtn= Button(mainlabelFrame, font=('arial', 20, 'bold'), text="Add Medicine", pady =1, bg='light blue', command=addMed)
        insertBtn.grid(row=0, column=2)
        updateBtn= Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Update", pady =1, padx=42,bg='yellow', command=Update)
        updateBtn.grid(row=1, column=2)
        deleteBtn = Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Delete", pady =1,padx=47, bg='red', command=delete)
        deleteBtn.grid(row=2, column=2)
        refreshBtn = Button(mainlabelFrame,font=('arial', 18, 'bold'), text="Refresh Table", pady =1,padx=10, bg='green', command=display)
        refreshBtn.grid(row=3, column=2)
        selectBtn = Button(mainlabelFrame,font=('arial', 18, 'bold'), text="Select Medicine", pady =1, bg='pink', command=select)
        selectBtn.grid(row=4, column=2)
        about_us = Button(mainFrame, font=('arial', 10, 'bold'), text="About us", pady =1,padx=1, command=about_us)
        about_us.place(x=1, y=672)

#treeview
        self.tbl_med = ttk.Treeview(treeviewFrame, height=13,
                               columns=("ID","MedName", "StartDate", "Until", "IntakeDays", "IntakeTime", "Amount"),
                               xscrollcommand=xScroll.set
                               , yscrollcommand=yScroll.set)
        xScroll.pack(side=BOTTOM, fill=X)
        yScroll.pack(side=RIGHT, fill=Y)

        self.tbl_med.heading("ID", text="No.")
        self.tbl_med.heading("MedName", text="MedName")
        self.tbl_med.heading("StartDate", text="StartDate")
        self.tbl_med.heading("Until", text="Until")
        self.tbl_med.heading("IntakeDays", text="IntakeDay/s")
        self.tbl_med.heading("IntakeTime", text="IntakeTime")
        self.tbl_med.heading("Amount", text="Amount")

        self.tbl_med['show'] = 'headings'

        self.tbl_med.column("ID", width=50)
        self.tbl_med.column("MedName", width=200)
        self.tbl_med.column("StartDate", width=200)
        self.tbl_med.column("Until", width=200)
        self.tbl_med.column("IntakeDays", width=200)
        self.tbl_med.column("IntakeTime", width=200)
        self.tbl_med.column("Amount", width=100)

        self.tbl_med.pack(fill=BOTH, expand=1)






if __name__=='__main__':
    rt = Tk()
    application = win(rt)
   # application = labels(rt)
    rt.mainloop()
#20/032020

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

with sqlite3.connect('DBmedsched') as db:
    cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS DBmedsched(MedName TEXT, StartDate TEXT, Until TEXT, IntakeDays TEXT, IntakeTime TEXT, Amount TEXT);""")

class win():
    def __init__(self,rt):
        self.rt = rt
        self.rt.title("MedSched")
        self.rt.geometry("1200x720")
        self.rt.resizable(width=False, height=False)


        def addMed():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            confirm = messagebox.askquestion("Confirmation", "Do you want to add this medicine?")
            if(confirm=="yes"):
                c.execute('INSERT INTO DBmedsched(MedName,StartDate,Until,IntakeDays,IntakeTime,Amount) VALUES(?,?,?,?,?,?)',(eName.get(),eStart.get(),eUntil.get(),eintkDate.get(),eintkTime.get(),eAmt.get()))
                conn.commit()
                eName.delete(0, END)
                eStart.delete(0, END)
                eUntil.delete(0, END)
                eintkDate.delete(0, END)
                eintkTime.delete(0, END)
                eAmt.delete(0, END)
                messagebox.showinfo("Entry Successful", "Entry Successful!, Press the refresh button to see it in the table")
            else:
                messagebox.showinfo("Action Cancelled", "Medicine not saved.")
            conn.commit()
            conn.close()

        def Query():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            c.execute("SELECT rowid, * FROM DBmedsched")
            rec = c.fetchall()
            global count
            count = 0
            for data in rec:
                if count % 2==0:
                    self.tbl_med.insert(parent='',index='end', iid=count, text='', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                else:
                    self.tbl_med.insert(parent='',index='end', iid=count, text='', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                count +=1
            conn.commit()
            conn.close()


        def display():
            conn = sqlite3.connect('DBmedsched')
            c = conn.cursor()
            c.execute("SELECT * FROM DBmedsched")
            rec2= c.fetchall()
            global count
            count = 0
            for j in self.tbl_med.get_children():
                self.tbl_med.delete(j)
            for data2 in rec2:
                if count %2 == 0:
                    self.tbl_med.insert(parent='', index='end', iid=count, text='',values=(data2[0],data2[1],data2[2],data2[3],data2[4], data2[5]))
                else:
                    self.tbl_med.insert(parent='', index='end', iid=count, text='',values=(data2[0],data2[1],data2[2],data2[3],data2[4],data2[5]))
                count+=1
            self.tbl_med.delete(*self.tbl_med.get_children())
            Query()
            conn.commit()

        def select():
            eId.delete(0, END)
            eName.delete(0, END)
            eStart.delete(0, END)
            eUntil.delete(0, END)
            eintkDate.delete(0, END)
            eintkTime.delete(0, END)
            eAmt.delete(0, END)

            selected = self.tbl_med.focus()
            val = self.tbl_med.item(selected, 'val')
            eId.insert(0, val[0])
            eName.insert(0, val[1])
            eStart.insert(0, val[2])
            eUntil.insert(0, val[3])
            eintkDate.insert(0, val[4])
            eintkTime.insert(0, val[5])
            eAmt.insert(0, val[6])

        def delete():
            permission = messagebox.askquestion("Confirmation", "Do you wish to delete this?")
            if permission =="yes":
                conn = sqlite3.connect('DBmedsched')
                c = conn.cursor()
                c.execute("DELETE FROM DBmedsched WHERE oid=" + eId.get())
                conn.commit()
                conn.close()
                messagebox.showinfo("Delete Successful","Delete Successful, Refresh to see changes.")
            else:
                messagebox.showinfo("Delete Failed", "Operation Cancelled or an error occured")

        def Update():
            ask = messagebox.askquestion("Confirmation", "Are you sure you want to update this?")
            if ask =="yes":
                select = self.tbl_med.focus()
                self.tbl_med.item(select, text="", values=(eId.get(),eName.get(),eStart.get(), eUntil.get(), eintkDate.get(),eintkTime.get(), eAmt.get(),))
                conn = sqlite3.connect('DBmedsched')
                c = conn.cursor()
                c.execute("UPDATE DBmedsched SET MedName = :mn, StartDate = :sd, Until = :u, IntakeDays = :ind, IntakeTime =:it, Amount =:am WHERE oid= :oid",{
                    'mn':eName.get(),
                    'sd':eStart.get(),
                    'u':eUntil.get(),
                    'ind':eintkDate.get(),
                    'it':eintkTime.get(),
                    'am':eAmt.get(),
                    'oid':eId.get(),
                })
                messagebox.showinfo("Success!", "Update Complete!")
            else:
                messagebox.showinfo("Update Failed", "Update Cancelled")

            conn.commit()
            conn.close()
        def about_us():
            messagebox.showinfo("About us","This application was made by group 4. Members:Tristan Tan, John lyndon Vasquez, Lance Pastrana, Chizel Diaz, April Nicole Martin")

#Frames
        mainFrame=Frame(self.rt, bd=10, width=1150, height=750, relief=RIDGE, bg='cyan')
        mainFrame.grid()
        titleframe=Frame(mainFrame, bd=5, width=1180, height=70, relief=FLAT,bg='#FFF89A')
        titleframe.grid()
        treeviewFrame=Frame(mainFrame, bd=5, width=1145, height=200, relief=RAISED)
        treeviewFrame.grid()
       # upperFrame2 = Frame(mainFrame, bd=5, width=1145, height=500, relief=RIDGE)
       # upperFrame2.grid(row=2, column=0)


        mainlabelFrame = Frame(mainFrame,bd =5, width=1130, height=480, relief=RAISED)
        mainlabelFrame.grid()

        xScroll = Scrollbar(treeviewFrame, orient=HORIZONTAL)
        yScroll = Scrollbar(treeviewFrame, orient=VERTICAL)
#labels
        titleLabel=Label(titleframe, font=('Arial', 30,'bold'), text="MEDSCHED", fg="#2D31FA", bg='#FFF89A')
        titleLabel.place(x=505, y=-1)
        nameLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Medicine Name:")
        nameLabel.grid(row=0,column=0)

        startLabel=Label(mainlabelFrame,font=('courier', 20,'bold'), text="Start Date:")
        startLabel.grid(row=1, column=0)

        untilLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Until:")
        untilLabel.grid(row=2, column=0)
        intkDatelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Day:")
        intkDatelbl.grid(row=3, column=0)
        intkTimelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Time:")
        intkTimelbl.grid(row=4, column=0)
        amtlbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Amount:")
        amtlbl.grid(row=5, column=0)

#Entry
        eId = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=5)
        eId.place(x=1000, y=1000)
        eName = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eName.grid(row=0, column=1)
        eStart = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eStart.grid(row=1, column=1)
        eUntil = Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eUntil.grid(row=2, column=1)
        eintkDate= Entry(mainlabelFrame, font=('courier', 20, 'bold'), width=30)
        eintkDate.grid(row=3, column=1)
        eintkTime = Entry(mainlabelFrame, font=('arial', 20, 'bold'), width=30)
        eintkTime.grid(row=4, column=1)
        eAmt = Entry(mainlabelFrame, font=('arial', 20, 'bold'), width=30)
        eAmt.grid(row=5, column=1)
#buttons
        insertBtn= Button(mainlabelFrame, font=('arial', 20, 'bold'), text="Add Medicine", pady =1, bg='light blue', command=addMed)
        insertBtn.grid(row=0, column=2)
        updateBtn= Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Update", pady =1, padx=42,bg='yellow', command=Update)
        updateBtn.grid(row=1, column=2)
        deleteBtn = Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Delete", pady =1,padx=47, bg='red', command=delete)
        deleteBtn.grid(row=2, column=2)
        refreshBtn = Button(mainlabelFrame,font=('arial', 18, 'bold'), text="Refresh Table", pady =1,padx=10, bg='green', command=display)
        refreshBtn.grid(row=3, column=2)
        selectBtn = Button(mainlabelFrame,font=('arial', 18, 'bold'), text="Select Medicine", pady =1, bg='pink', command=select)
        selectBtn.grid(row=4, column=2)
        about_us = Button(mainFrame, font=('arial', 10, 'bold'), text="About us", pady =1,padx=1, command=about_us)
        about_us.place(x=1, y=672)

#treeview
        self.tbl_med = ttk.Treeview(treeviewFrame, height=13,
                               columns=("ID","MedName", "StartDate", "Until", "IntakeDays", "IntakeTime", "Amount"),
                               xscrollcommand=xScroll.set
                               , yscrollcommand=yScroll.set)
        xScroll.pack(side=BOTTOM, fill=X)
        yScroll.pack(side=RIGHT, fill=Y)

        self.tbl_med.heading("ID", text="No.")
        self.tbl_med.heading("MedName", text="MedName")
        self.tbl_med.heading("StartDate", text="StartDate")
        self.tbl_med.heading("Until", text="Until")
        self.tbl_med.heading("IntakeDays", text="IntakeDay/s")
        self.tbl_med.heading("IntakeTime", text="IntakeTime")
        self.tbl_med.heading("Amount", text="Amount")

        self.tbl_med['show'] = 'headings'

        self.tbl_med.column("ID", width=50)
        self.tbl_med.column("MedName", width=200)
        self.tbl_med.column("StartDate", width=200)
        self.tbl_med.column("Until", width=200)
        self.tbl_med.column("IntakeDays", width=200)
        self.tbl_med.column("IntakeTime", width=200)
        self.tbl_med.column("Amount", width=100)

        self.tbl_med.pack(fill=BOTH, expand=1)






if __name__=='__main__':
    rt = Tk()
    application = win(rt)
   # application = labels(rt)
    rt.mainloop()

