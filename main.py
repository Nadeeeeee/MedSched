from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

with sqlite3.connect('MedSchedDB') as db:
    cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS sched(MedName TEXT, StartDate TEXT, Until TEXT, IntakeDays TEXT, IntakeTime TEXT, Amount TEXT);""")
#conn = sqlite3.connect('MedSchedDB')
#c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS MedSchedDB(MedName TEXT, StartDate TEXT, Until TEXT, IntakeDays TEXT, IntakeTime TEXT, Amount TEXT)")
#conn.commit()
#conn.close()
class win():
    def __init__(self,rt):
        self.rt = rt
        self.rt.title("MedSched")
        self.rt.geometry("1160x710")
        self.rt.resizable(width=False, height=False)

        #MedName = StringVar()
       # StartDate = StringVar()
       # Until = StringVar()
       # IntakeDate = StringVar()
       # IntakeTime = StringVar()
       # Amount = StringVar()

        def addMed():
            conn = sqlite3.connect('MedSchedDB')
            c = conn.cursor()
            c.execute("INSERT INTO sched VALUES (:MedName, :StartDate,:Until,:IntakeDays,:IntakeTime,:Amount)",
                      {
                          'MedName': eName.get(),
                          'StartDate': eStart.get(),
                          'Until': eUntil.get(),
                          'IntakeDays': eintkDate.get(),
                          'IntakeTime': eintkTime.get(),
                          'Amount': eAmt.get(),
                      })
            conn.commit()
            conn.close()

#Frames
        mainFrame=Frame(self.rt, bd=10, width=1150, height=750, relief=RIDGE, bg='cyan')
        mainFrame.grid()
        titleframe=Frame(mainFrame, bd=5, width=1150, height=70, relief=RAISED,bg='blue')
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
        titleLabel=Label(titleframe, font=('courier', 30,'bold'), text="MEDSCHED", fg="White", bg='blue')
        titleLabel.place(x=505, y=-1)
        nameLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Medicine Name")
        nameLabel.grid(row=0,column=0)

        startLabel=Label(mainlabelFrame,font=('courier', 20,'bold'), text="Start Date")
        startLabel.grid(row=1, column=0)

        untilLabel=Label(mainlabelFrame, font=('courier', 20,'bold'), text="Until")
        untilLabel.grid(row=2, column=0)
        intkDatelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Date")
        intkDatelbl.grid(row=3, column=0)
        intkTimelbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Intake Time")
        intkTimelbl.grid(row=4, column=0)
        amtlbl = Label(mainlabelFrame, font=('courier', 20,'bold'), text="Amount")
        amtlbl.grid(row=5, column=0)
#Entry
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
        updateBtn= Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Update", pady =1, bg='yellow')
        updateBtn.grid(row=1, column=2)
        deleteBtn = Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Delete", pady =1, bg='red')
        deleteBtn.grid(row=2, column=2)
        refreshBtn = Button(mainlabelFrame,font=('arial', 20, 'bold'), text="Refresh", pady =1, bg='green')
        refreshBtn.grid(row=3, column=2)

#treeview
        self.tbl_med = ttk.Treeview(treeviewFrame, height=13,
                               columns=("MedName", "StartDate", "Until", "IntakeDays", "IntakeTime", "Amount"),
                               xscrollcommand=xScroll.set
                               , yscrollcommand=yScroll.set)
        xScroll.pack(side=BOTTOM, fill=X)
        yScroll.pack(side=RIGHT, fill=Y)

        self.tbl_med.heading("MedName", text="MedName")
        self.tbl_med.heading("StartDate", text="StartDate")
        self.tbl_med.heading("Until", text="Until")
        self.tbl_med.heading("IntakeDays", text="IntakeDay/s")
        self.tbl_med.heading("IntakeTime", text="IntakeTime")
        self.tbl_med.heading("Amount", text="Amount")

        self.tbl_med['show'] = 'headings'

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