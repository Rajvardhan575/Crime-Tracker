from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Criminal:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1530x830+0+0")
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False,False)
        self.root.title("Criminal Details Management")

        self.var_section=StringVar()
        self.var_crime=StringVar()
        self.var_year=StringVar() 
        self.var_month=StringVar()
        self.var_criminal_id=StringVar()
        self.var_criminal_name=StringVar()
        self.var_jail=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_jailer=StringVar()

        bg1=Image.open(r"secondpage.png")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="CRIMINAL DETAILS MANAGEMENT",font=("calibri",35,"bold"),bg="yellow",fg="red")
        title_lb1.place(x=200,y=30,width=900,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="RED") 
        #main_frame.place(x=5,y=100,width=1355,height=510)
        main_frame.place(x=5,y=100,width=1355,height=610)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Save Criminal Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=1320,height=280)

        current_crime_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Crime",font=("verdana",12,"bold"),fg="navyblue")
        current_crime_frame.place(x=10,y=5,width=635,height=150)

        section_label=Label(current_crime_frame,text="Section",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        section_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        section_combo=ttk.Combobox(current_crime_frame,textvariable=self.var_section,width=15,font=("verdana",12,"bold"),state="readonly")
        section_combo["values"]=("Select Section","Section 1","Section 2","Section 3","Section 4","Section 5")
        section_combo.current(0)
        section_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        #label Course
        cou_label=Label(current_crime_frame,text="Crime",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_crime_frame,textvariable=self.var_crime,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("Select Crime","Murder","Extortion","Rape","Cyber Crime","Scam")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #label Year
        year_label=Label(current_crime_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_crime_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2015","2016","2017","2019","2020","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #label Semester --- Month 
        year_label=Label(current_crime_frame,text="Month",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_crime_frame,textvariable=self.var_month,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Month","January","February","March","April","May","June","July","August","September","October","November","December")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)
        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        class_Criminal_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Criminal_frame.place(x=660,y=0,width=635,height=230)

        #Criminal ID
        criminalID_label = Label(class_Criminal_frame,text="Criminal-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminalID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        criminalID_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_criminal_id,width=15,font=("verdana",12,"bold"))
        criminalID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Criminal Name
        crimianl_name_label = Label(class_Criminal_frame,text="Criminal-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        crimianl_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        crimianl_name_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_criminal_name,width=15,font=("verdana",12,"bold"))
        crimianl_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Jail
        criminal_jail_label = Label(class_Criminal_frame,text="Jail:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_jail_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        jail_combo=ttk.Combobox(class_Criminal_frame,textvariable=self.var_jail,width=13,font=("verdana",12,"bold"),state="readonly")
        jail_combo["values"]=("Select Jail","Yerwada","Yerwada Sec 2","Yerwada Sec 3","Yerwada Sec 4","Yerwada Sec 5","Tihar Sec 1","Tihar Sec 2","Tihar Sec 3","Mumbai","Pune","Kolhapur","Satara","Vashim","Delhi","Noida","Ahmdabad","Sangli")
        jail_combo.current(0)
        jail_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Roll No
        criminal_roll_label = Label(class_Criminal_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        criminal_roll_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        criminal_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Gender
        criminal_gender_label = Label(class_Criminal_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Criminal_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Date of Birth
        criminal_dob_label = Label(class_Criminal_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        criminal_dob_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        criminal_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        #Email
        criminal_email_label = Label(class_Criminal_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        criminal_email_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        criminal_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Phone Number
        criminal_mob_label = Label(class_Criminal_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        criminal_mob_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        criminal_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Address
        criminal_address_label = Label(class_Criminal_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        criminal_address_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        criminal_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Jailer
        criminal_jailer_label = Label(class_Criminal_frame,text="Jiler Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        criminal_jailer_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        criminal_jailer_entry = ttk.Entry(class_Criminal_frame,textvariable=self.var_jailer,width=15,font=("verdana",12,"bold"))
        criminal_jailer_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Criminal_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Criminal_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=170,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="red")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="blue")
        update_btn.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="red")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="blue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Details and Saved Information",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=10,y=290,width=1320,height=300)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=10,width=1300,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_lable1=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_lable1["values"]=("ID")
        search_lable1.current(0)
        search_lable1.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=1300,height=160)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.criminal_table = ttk.Treeview(table_frame,column=("ID","Name","Section","Crime","Year","Month","Jail","Gender","DOB","Mob-No","Address","Roll-No","Email","Jailer","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("ID",text="CriminalID")
        self.criminal_table.heading("Name",text="Name")
        self.criminal_table.heading("Section",text="Section")
        self.criminal_table.heading("Crime",text="Crime")
        self.criminal_table.heading("Year",text="Year")
        self.criminal_table.heading("Month",text="Month")
        self.criminal_table.heading("Jail",text="Jail")
        self.criminal_table.heading("Gender",text="Gender")
        self.criminal_table.heading("DOB",text="DOB")
        self.criminal_table.heading("Mob-No",text="Mob-No")
        self.criminal_table.heading("Address",text="Address")
        self.criminal_table.heading("Roll-No",text="Roll-No")
        self.criminal_table.heading("Email",text="Email")
        self.criminal_table.heading("Jailer",text="Jailer")
        self.criminal_table.heading("Photo",text="PhotoSample")
        self.criminal_table["show"]="headings"


        # Set Width of Colums 
        self.criminal_table.column("ID",width=100)
        self.criminal_table.column("Name",width=100)
        self.criminal_table.column("Section",width=100)
        self.criminal_table.column("Crime",width=100)
        self.criminal_table.column("Year",width=100)
        self.criminal_table.column("Month",width=100)
        self.criminal_table.column("Jail",width=100)
        self.criminal_table.column("Gender",width=100)
        self.criminal_table.column("DOB",width=100)
        self.criminal_table.column("Mob-No",width=100)
        self.criminal_table.column("Address",width=100)
        self.criminal_table.column("Roll-No",width=100)
        self.criminal_table.column("Email",width=100)
        self.criminal_table.column("Jailer",width=100)
        self.criminal_table.column("Photo",width=100)


        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_section.get()=="Select Section" or self.var_crime.get=="Select Crime" or self.var_year.get()=="Select Year" or self.var_month.get()=="Select Month" or self.var_criminal_id.get()=="" or self.var_criminal_name.get()=="" or self.var_jail.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_jailer.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_criminal_id.get(),
                self.var_criminal_name.get(),
                self.var_section.get(),
                self.var_crime.get(),
                self.var_year.get(),
                self.var_month.get(),
                self.var_jail.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_jailer.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from criminal")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_focus)
        data = content["values"]

        self.var_criminal_id.set(data[0]),
        self.var_criminal_name.set(data[1]),
        self.var_section.set(data[2]),
        self.var_crime.set(data[3]),
        self.var_year.set(data[4]),
        self.var_month.set(data[5]),
        self.var_jail.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_jailer.set(data[13]),
        self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_section.get()=="Select Section" or self.var_crime.get=="Select Crime" or self.var_year.get()=="Select Year" or self.var_month.get()=="Select Month" or self.var_criminal_id.get()=="" or self.var_criminal_name.get()=="" or self.var_jail.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_jailer.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Criminal Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update criminal set Name=%s,Section=%s,Crime=%s,Year=%s,Month=%s,Jail=%s,Gender=%s,DOB=%s,Mob=%s,Address=%s,Roll=%s,Emial=%s,Jailer=%s,Photo=%s where ID=%s",( 
                    self.var_criminal_name.get(),
                    self.var_section.get(),
                    self.var_crime.get(),
                    self.var_year.get(),
                    self.var_month.get(),
                    self.var_jail.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_jailer.get(),
                    self.var_radio1.get(),
                    self.var_criminal_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_criminal_id.get()=="":
            messagebox.showerror("Error","Criminal Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from criminal where ID=%s"
                    val=(self.var_criminal_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_criminal_id.set(""),
        self.var_criminal_name.set(""),
        self.var_section.set("Select Section"),
        self.var_crime.set("Select Crime"),
        self.var_year.set("Select Year"),
        self.var_month.set("Select Month"),
        self.var_jail.set("Select Jail"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_jailer.set(""),
        self.var_radio1.set("")
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT ID,Name,Section,Crime,Year,Month,Jail,Gender,DOB,MOB,Address,Roll,Emial,Jailer,Photo FROM criminal where ID='" +str(self.var_search.get()) + "'"
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================

    def generate_dataset(self):
        if self.var_section.get()=="Select Section" or self.var_crime.get=="Select Crime" or self.var_year.get()=="Select Year" or self.var_month.get()=="Select Month" or self.var_criminal_id.get()=="" or self.var_criminal_name.get()=="" or self.var_jail.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_jailer.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from criminal")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1
                mycursor.execute("update criminal set Name=%s,Section=%s,Crime=%s,Year=%s,Month=%s,Jail=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Jailer_Name=%s,PhotoSample=%s where Criminal_ID=%s",( 
                    self.var_criminal_name.get(),
                    self.var_section.get(),
                    self.var_crime.get(),
                    self.var_year.get(),
                    self.var_month.get(),
                    self.var_jail.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_jailer.get(),
                    self.var_radio1.get(),
                    self.var_criminal_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #part of opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/criminal."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

if __name__ == "__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()