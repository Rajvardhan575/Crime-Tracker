from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from fakenewsdetect import fakenewsdetect
from criminal import Criminal
from hatespeech import hatespeech
from searchdetails import searchdetails
from main import mainpage
from vehicle import vehicle
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("startpage")
        self.root.geometry("1366x768+70+30")

        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        bg1=Image.open(r"thirdpage.png")
        bg1=bg1.resize((1366,768))
        self.root.resizable(False,False)
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        frame1= Frame(self.root,bg="#000000")
        frame1.place(x=950,y=160,width=340,height=450)

        title_lb1 = Label(bg_img,text="CRIME TRACKER - FOR SECURITY ENFORCEMENT AND CRIME CONTROL  \n \n Crime Tracker is an intelligence data-sharing, storing platform with common database. \n "
        "It was created to bolster national security and improve the coordination among various security and intelligence agencies.\n\n"
        "The Reason Behind CRIME TRACKER Development? \n\n"
        "CRIME TRACKER was developed in response to the increasing threat of terrorism and the need for better surveillance mechanisms. \n"
        "CRIME TRACKER was conceived to bridge security gaps by integrating information from multiple data sources and making it \n accessible to authorized agencies in real time.\n\n"
        "Problems tackled by CRIME TRACKER (The platform addresses several critical challenges):\n\n "
        "1. Can be tackled problem of Terrorism and Security Threats:\n By analyzing data patterns, CRIME TRACKER aids in identifying and preventing potential security risks.\n"
        "2. Coordination Gaps: It enhances collaboration and reduces delays in information sharing among agencies.\n"
        "3. Criminal Activities: CRIME TRACKER is designed to track and Criminal tackle activities and data.\n\n"
        "Functions of CRIME TRACKER (CRIME TRACKER integrates information from diverse sectors such as):\n\n"
        "This data is used by authorized security and law enforcement agencies to:\n"
        "1. Track suspects details and prevent unlawful activities effectively\n"
        "2. Improve decision-making during emergencies \n"
        "3. Can be Conduct real-time analysis of threats \n"
        "4. Immigration and visa details (Upcoming Update) \n"
        "5. Banking and financial transactions (Upcoming Update) \n"
        "6.Telecom records (Upcoming Update) \n"
        "7.Travel details, like rail and flight ticket bookings (Upcoming Update)  \n"
        "8.It acts as a crucial tool for national security while maintaining a strict focus on data privacy and access control. \n",font=("calibri",11,"bold"),bg="black",fg="yellow")
        title_lb1.place(x=40,y=100,width=850,height=600)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="red",bg="#000000")
        get_str.place(x=135,y=100)

        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="red",bg="#000000")
        username.place(x=30,y=160)

        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)

        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="red",bg="#000000")
        pwd.place(x=30,y=230)

        self.txtpwd=ttk.Entry(frame1,font=("times  new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)

        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="red",activeforeground="white",activebackground="#272e1f")
        loginbtn.place(x=33,y=320,width=270,height=35)

        Registerbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="red",bg="#000000",activeforeground="orange",activebackground="#272e1f")
        Registerbtn.place(x=33,y=370,width=50,height=20)

        forgetbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="red",bg="#000000",activeforeground="orange",activebackground="#272e1f")
        forgetbtn.place(x=90,y=370,width=50,height=20)

    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="" and self.txtpwd.get()==""):
            messagebox.showinfo("Welcome to Crime Tracker")
        else:
            conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from police where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=mainpage(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
# For Password Reset
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
            mycursor = conn.cursor()
            query=("select * from police where email=%s and ssq=%s and sa=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update police set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been reset, Please login with new Password!",parent=self.root2)
                
#Forgat Password
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='crime_tracker',port=3306)
            mycursor = conn.cursor()
            query=("select * from police where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)

                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)

                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)

class mainpage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False,False)
        self.root.title("Main")

        bg1=Image.open(r"secondpage.png")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lb1 = Label(bg_img,text="CRIME TRACKER",font=("calibri",35,"bold"),bg="YELLOW",fg="BLACK")
        title_lb1.place(x=450,y=20,width=500,height=45)

        title_lb1 = Label(bg_img,text="FOR SECURITY ENFORCEMENT AND CRIME CONTROL",font=("calibri",35,"bold"),bg="YELLOW",fg="BLACK")
        title_lb1.place(x=90,y=70,width=1200,height=45)

        criminal_b1_1 = Button(bg_img,command=self.criminal_panels,text="Criminal Detail \nManagement",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        criminal_b1_1.place(x=440,y=180,width=200,height=80)

        hatespeech_b1_1 = Button(bg_img,command=self.hatespeech,text="Hate Speech \n Detection",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        hatespeech_b1_1.place(x=340,y=340,width=200,height=80)

        phonenodetails_b1_1 = Button(bg_img,command=self.searchdetails,text="Criminal Detail \n Tracking",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        phonenodetails_b1_1.place(x=710,y=180,width=200,height=80)

        fakenewsdetect_b1_1 = Button(bg_img,command=self.fakenewsdetect,text="Fakenews\nDetection",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        fakenewsdetect_b1_1.place(x=440,y=500,width=200,height=80)

        vehicle_b1_1 = Button(bg_img,command=self.vehicle,text="Vehicle Details \n Tracking",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        vehicle_b1_1.place(x=820,y=340,width=200,height=80)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        exi_b1_1.place(x=710,y=500,width=200,height=80)

    def open_img(self):
        os.startfile("dataset")

    def criminal_panels(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal(self.new_window)

    def fakenewsdetect(self):
        self.new_window=Toplevel(self.root)
        self.app=fakenewsdetect(self.new_window)
    
    def hatespeech(self):
        self.new_window=Toplevel(self.root)
        self.app=hatespeech(self.new_window)

    def vehicle(self):
        self.new_window=Toplevel(self.root)
        self.app=vehicle(self.new_window)
    
    def searchdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=searchdetails(self.new_window)

    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()