from importlib.resources import contents
from msilib.schema import ComboBox
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1400x700+50+40")
        self.root.resizable(width=False,height=False)


#-----------------------------------All Variables----------------------------------------#
        self.Roll_No=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


#-----------------------------------Title Bar--------------------------------------------#
        title=Label(root,text="Student Management System",font=("times new roman",30,"bold"),bd=7,relief=GROOVE,bg="lightgreen",fg="black")
        title.pack(side=TOP,fill=X)


#----------------------------------Frist Frame-------------------------------------------#
        F1=Frame(root,bd=5,relief=RIDGE,bg="lightblue")
        F1.place(x=18,y=67,width=460,height=622)

        f1_title=Label(F1,text="Manage Student Details",bg="lightblue",font=("times new roman",20,"bold"))
        f1_title.grid(row=0,columnspan=2,pady=15)

        lbl_roll=Label(F1,text="Roll No.",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(F1,textvariable=self.Roll_No,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=15,pady=10,sticky="w")

        lbl_name=Label(F1,text="Name",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(F1,textvariable=self.name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,padx=15,pady=10,sticky="w")

        lbl_mail=Label(F1,text="Email",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_mail.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_mail=Entry(F1,textvariable=self.email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_mail.grid(row=3,column=1,padx=15,pady=10,sticky="w")

        lbl_gender=Label(F1,text="Gender",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_gender=ttk.Combobox(F1,textvariable=self.gender,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=15,pady=10,sticky="w")

        lbl_contact=Label(F1,text="Contact No.",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact=Entry(F1,textvariable=self.contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,padx=15,pady=10,sticky="w")

        lbl_dob=Label(F1,text="D.O.B.",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_dob=Entry(F1,textvariable=self.dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,padx=15,pady=10,sticky="w")

        lbl_address=Label(F1,text="Address",bg="lightblue",font=("times new roman",18,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(F1,font="arial 12 bold",width=22,height=4,bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,padx=15,pady=10,sticky="w")


#-------------------------------Button Frame---------------------------------------------#
        F3=Frame(F1,bd=4,relief=RIDGE,bg="lightblue")
        F3.place(x=10,y=520,width=430)

        btn_add=Button(F3,text="Add",font=5,width=7,command=self.add_student).grid(row=0,column=0,padx=9,pady=10)

        btn_update=Button(F3,text="Update",font=5,width=7,command=self.update_data).grid(row=0,column=1,padx=9,pady=10)

        btn_delete=Button(F3,text="Delete",font=5,width=7,command=self.delete_data).grid(row=0,column=2,padx=9,pady=10)

        btn_clear=Button(F3,text="Clear",font=5,width=7,command=self.clear_btn).grid(row=0,column=3,padx=9,pady=10)


#---------------------------------Second Frame-------------------------------------------#
        F2=Frame(root,bd=5,relief=RIDGE,bg="white")
        F2.place(x=500,y=67,width=880,height=622)

        lbl_search=Label(F2,text="Search by",bg="white",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(F2,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=5,pady=10,sticky="w")

        txt_search=Entry(F2,textvariable=self.search_txt,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=3,padx=30,pady=10,sticky="w")

        btn_search=Button(F2,text="Search",width=13,pady=3,command=self.search_data).grid(row=0,column=4,padx=9,pady=10,sticky="e")

        btn_show_all=Button(F2,text="Show All",width=13,pady=3,command=self.fetch_data).grid(row=0,column=5,padx=9,pady=10,sticky="e")


#----------------------------------Table Frame-------------------------------------------#
        F4=Frame(F2,bd=3,relief=RIDGE,bg="white")
        F4.place(x=10,y=55,width=850,height=555)

        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.student_table=ttk.Treeview(F4,columns=("Roll No.","Name","Email","Gender","Contact","D.O.B.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("D.O.B.",text="D.O.B.")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("Roll No.",width=90)
        self.student_table.column("Name",width=200)
        self.student_table.column("Email",width=150)
        self.student_table.column("Gender",width=70)
        self.student_table.column("Contact",width=150)
        self.student_table.column("D.O.B.",width=100)
        self.student_table.column("Address",width=250)
        self.student_table.pack(fill="both",expand=1)

        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_student(self):
        if self.Roll_No.get()=="" or self.name.get()=="" or self.contact.get()=="" or len(self.txt_address.get('1.0',"end-1c"))==0 or self.dob.get()=="" :
            messagebox.showerror("Error","All field are must fill!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.Roll_No.get(),
                                                                                self.name.get(),
                                                                                self.email.get(),
                                                                                self.gender.get(),
                                                                                self.contact.get(),
                                                                                self.dob.get(),
                                                                                self.txt_address.get('1.0',END)                                                       
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Saved","Your data will be added successfully!")
            con.close()


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def clear(self):
            self.Roll_No.set("")
            self.name.set("")
            self.email.set("")
            self.gender.set("")
            self.contact.set("")
            self.dob.set("")
            self.txt_address.delete("1.0",END)


    def clear_btn(self):
        op=messagebox.askyesno("Clear","Do you want to clear the data")
        if op>0:
            self.Roll_No.set("")
            self.name.set("")
            self.email.set("")
            self.gender.set("")
            self.contact.set("")
            self.dob.set("")
            self.txt_address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents["values"]
        self.Roll_No.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])


    def update_data(self):
        op=messagebox.askyesno("Update","Do you want to update the data")
        if op>0:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                self.name.get(),
                                                                                self.email.get(),
                                                                                self.gender.get(),
                                                                                self.contact.get(),
                                                                                self.dob.get(),
                                                                                self.txt_address.get('1.0',END),
                                                                                self.Roll_No.get()                                                       
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Updated","Your data will be updated!")
            con.close()


    def delete_data(self):
        op=messagebox.askyesno("Delete","Do you want to delete the data")
        if op>0:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("delete from students where roll_no=%s",self.Roll_No.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()


    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=Student(root)
root.mainloop()
