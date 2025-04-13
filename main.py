from tkinter import*
from tkinter import ttk
from fakenewsdetect import fakenewsdetect
from PIL import Image,ImageTk
from criminal import Criminal
from hatespeech import hatespeech
import os
from searchdetails import searchdetails
from vehicle import vehicle

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
    obj=mainpage(root)
    root.mainloop()