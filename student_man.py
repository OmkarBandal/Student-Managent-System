from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Mangement System")
        self.root.geometry("1350x700+0+0")

    


        Title=Label(self.root,text="Student Mangement System",bd=10,relief="groove",font=("times new roman",40,"bold"),bg="yellow",fg="red")
        Title.pack(side="top",fill=X)

        #================ variable ======================
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.s_by=StringVar()
        self.search_txt=StringVar()





        #===================manage frame===================


        man_frame=Frame(self.root,bd=4,relief="ridge",bg="crimson")
        man_frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(man_frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        l_roll=Label(man_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        l_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        t_roll=Entry(man_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief="groove")
        t_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        l_name = Label(man_frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        t_name = Entry(man_frame,textvariable=self.name_var,  font=("times new roman", 15, "bold"),bd=5, relief="groove")
        t_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        l_email = Label(man_frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        t_email = Entry(man_frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        t_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        l_gender = Label(man_frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(man_frame,text="Contact",textvariable=self.gender_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)



        l_con = Label(man_frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"),)
        l_con.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        t_con = Entry(man_frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        t_con.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        l_dob = Label(man_frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        t_dob = Entry(man_frame, textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief="groove")
        t_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        l_add = Label(man_frame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")


        self.t_add=Text(man_frame,width=30,height=4,font=("times new roman", 10, "bold"))
        self.t_add.grid(row=7,column=1,pady=10, padx=20, sticky="w")

  #=========================button =================================================

        btn_frame = Frame(man_frame, bd=4, relief="ridge", bg="crimson")
        btn_frame.place(x=10, y=520, width=420)


        addbtn=Button(btn_frame,text="Add",width=10,command=self.add_stu).grid(row=0,column=0,padx=10,pady=10)

        upbtn = Button(btn_frame, text="Update", width=10,command=self.up_data12).grid(row=0, column=1, padx=10, pady=10)

        delbtn = Button(btn_frame, text="Delete", width=10,command=self.del_data).grid(row=0, column=2, padx=10, pady=10)

        clrbtn = Button(btn_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)











        # ===================detail frame===================

        de_frame = Frame(self.root, bd=4, relief="ridge", bg="crimson")
        de_frame.place(x=500, y=100, width=820, height=600)


        l_search = Label(de_frame, text="Search By ", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        l_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")


        combo_search=ttk.Combobox(de_frame,textvariable=self.s_by,width=10,font=("times new roman", 13, "bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        t_search = Entry(de_frame,textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5, relief="groove")
        t_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")


        searchbtn = Button(de_frame, text="Search", width=11,command=self.s_data).grid(row=0, column=3, padx=10, pady=10)

        showbtn = Button(de_frame, text="Show All", width=11,command=self.up_data12).grid(row=0, column=4, padx=10, pady=10)


        #================== tabel ===================================

        Tabel_frame=Frame(de_frame, bd=4, relief="ridge", bg="crimson")
        Tabel_frame.place(x=20, y=70, width=760, height=500)

        scrllx=Scrollbar(Tabel_frame,orient=HORIZONTAL)
        scrlly=Scrollbar(Tabel_frame,orient=VERTICAL)
        self.stu_t=ttk.Treeview(Tabel_frame,column=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scrllx.set,yscrollcommand=scrlly.set)
        scrllx.pack(side=BOTTOM,fill=X)
        scrlly.pack(side=RIGHT,fill=Y)
        scrllx.config(command=self.stu_t.xview)
        scrlly.config(command=self.stu_t.yview)

        self.stu_t.heading("email",text="E-Mail")
        self.stu_t.heading("name",text="Name")
        self.stu_t.heading("gender",text="Gender")
        self.stu_t.heading("roll",text="Roll No.")
        self.stu_t.heading("contact",text="Contact")
        self.stu_t.heading("dob",text="D.O.B")
        self.stu_t.heading("address",text="Address")
        self.stu_t['show']='headings'

        self.stu_t.column("roll",width=50)
        self.stu_t.column("name",width=100)
        self.stu_t.column("email",width=100)
        self.stu_t.column("gender",width=100)
        self.stu_t.column("contact",width=100)
        self.stu_t.column("dob",width=100)
        self.stu_t.column("address",width=200)
        
        self.stu_t.pack(fill="both",expand=1)
        self.stu_t.bind("<ButtonRelease-1>",self.get_cur)


        self.fetch_data()

    def add_stu(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("Error","All Feild Are Required!!!")
        else:

            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.t_add.get('1.0',END)
                                                                            )
                                                                            )
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()  
            messagebox.showinfo("Success","Record has been inserted.")
                  

     # ==================INSERT INTO `students`(`roll_no`, `name`, `email`, `gender`, `contact`, `dob`, `address`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7])


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from `students`")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.stu_t.delete(*self.stu_t.get_children())
            for row in rows:
                self.stu_t.insert('',END,values=row)
        con.commit()
        con.close()
    

    def clear(self):
        self.roll_no_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.t_add.delete('1.0',END)
    
    def get_cur(self,ev):
        cur_row=self.stu_t.focus()
        content1=self.stu_t.item(cur_row)
        row=content1['values']
        
        self.roll_no_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[6]),
        self.t_add.delete('1.0',END)
        self.t_add.insert(END,row[6])

    def up_data12(self):
        
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.t_add.get('1.0',END),
                                                                            self.roll_no_var.get()
                                                                            )
                                                                            )
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()  

    def del_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    
    def s_data(self):
        if self.search_txt.get()=="":
            messagebox.showerror("Error","Enter Something For Search!!! ")
        else:




        
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
        
            cur.execute("select * from `students` where  "+str(self.s_by.get())+" like '%"+str(self.search_txt.get())+"%'")
        
            rows=cur.fetchall()
        if len(rows)!=0:
            self.stu_t.delete(*self.stu_t.get_children())
            for row in rows:
                self.stu_t.insert('',END,values=row)
        con.commit()
        con.close()














root=Tk()
ob=Student(root)
root.mainloop()