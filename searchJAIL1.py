from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class SearchJAIL1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False,False)
        self.root.title("Criminal Details Tracking Using Mobile Number")

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

        bg1=Image.open(r"registerpage.png")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="CRIMINAL IDENTITY AND DETAILS",font=("calibri",35,"bold"),bg="yellow",fg="red")
        title_lb1.place(x=0,y=30,width=800,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") 
        main_frame.place(x=5,y=100,width=1355,height=510)

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=30,y=10,width=1290,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=1265,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()

        #combo box
        search_label = Label(search_frame,text="Jail Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=1,padx=5,pady=15,sticky=W)
        self.var_searchTX=StringVar()

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Yerwada","Yerwada Sec 2","Yerwada Sec 3","Yerwada Sec 4","Yerwada Sec 5","Tihar Sec 1","Tihar Sec 2","Tihar Sec 3","Mumbai","Pune","Kolhapur","Satara","Vashim","Delhi","Noida","Ahmdabad","Sangli")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=1265,height=360)

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

    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT ID,Name,Section,Crime,Year,Month,Jail,Gender,DOB,MOB,Address,Roll,Emial,Jailer,Photo FROM criminal where Jail='" +str(self.var_search.get()) + "'"
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

if __name__ == "__main__":
    root=Tk()
    obj=SearchJAIL1(root)
    root.mainloop()