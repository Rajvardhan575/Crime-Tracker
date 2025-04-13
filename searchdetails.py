import os
from tkinter import *
from PIL import Image, ImageTk
from searchMOB1 import SearchMOB1
from searchNAME1 import SearchNAME1
from searchDOB1 import SearchDOB1
from searchJAILERNM import SearchJAILERNM1
from searchMONTH1 import SearchMONTH1
from searchYEAR1 import SearchYEAR1
from searchCRIME1 import SearchCRIME1
from searchJAIL1 import SearchJAIL1
from searchGENDER1 import SearchGENDER1
from searchLOCATION1 import SearchLOCATION1

class searchdetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False, False)
        self.root.title("Criminal Details Tracking")

        # Background image
        bg1 = Image.open(r"secondpage.png")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="CRIME AND CRIMINAL DETAILS TRACKING", font=("calibri", 35, "bold"), bg="yellow", fg="red")
        title_lb1.place(x=0, y=30, width=1360, height=45)

        SearchNAME1 = Button(bg_img,command=self.SearchNAME1,text="Details Tracking Using Criminal Name",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        SearchNAME1.place(x=350, y=100, width=660, height=45)

        SearchDOB1 = Button(bg_img,command=self.SearchDOB1,text="Details Tracking Using Date Of Birth",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        SearchDOB1.place(x=350, y=160, width=660, height=45)

        SearchMOB1 = Button(bg_img,command=self.SearchMOB1,text="Details Tracking Using Mobile Number",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        SearchMOB1.place(x=350, y=220, width=660, height=45)

        SearchJAILERNM1 = Button(bg_img,command=self.SearchJAILERNM1,text="In-Charge Jailers With Criminals",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        SearchJAILERNM1.place(x=350, y=280, width=660, height=45)

        SearchMONTH1 = Button(bg_img,command=self.SearchMONTH1,text="Month Wise Crimes",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        SearchMONTH1.place(x=350, y=340, width=660, height=45)

        SearchYEAR1 = Button(bg_img,command=self.SearchYEAR1,text="Year Wise Crimes",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        SearchYEAR1.place(x=350, y=400, width=660, height=45)

        SearchCRIME1 = Button(bg_img,command=self.SearchCRIME1,text="Crime Wise Criminal Details",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        SearchCRIME1.place(x=350, y=460, width=660, height=45)

        SearchJAIL1 = Button(bg_img,command=self.SearchJAIL1,text="Jail and Criminal Details",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        SearchJAIL1.place(x=350, y=520, width=660, height=45)

        SearchGENDER1 = Button(bg_img,command=self.SearchGENDER1,text="Gender Wise Details",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        SearchGENDER1.place(x=350, y=580, width=660, height=45)

        SearchLOCATION1 = Button(bg_img,command=self.SearchLOCATION1,text="Location Wise Crimes",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        SearchLOCATION1.place(x=350, y=640, width=660, height=45)

    def open_img(self):
        os.startfile("dataset")

    def SearchNAME1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchNAME1(self.new_window)

    def SearchJAILERNM1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchJAILERNM1(self.new_window)

    def SearchMONTH1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchMONTH1(self.new_window)

    def SearchYEAR1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchYEAR1(self.new_window)

    def SearchCRIME1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchCRIME1(self.new_window)

    def SearchJAIL1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchJAIL1(self.new_window)

    def SearchGENDER1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchGENDER1(self.new_window)

    def SearchLOCATION1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchLOCATION1(self.new_window)
    
    def SearchMOB1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchMOB1(self.new_window)

    
    def SearchDOB1(self):
        self.new_window=Toplevel(self.root)
        self.app=SearchDOB1(self.new_window)

    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = searchdetails(root)
    root.mainloop()