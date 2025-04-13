from tkinter import *
from PIL import Image, ImageTk
import winsound  # For sound notifications

class hatespeech:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False, False)
        self.root.title("Hate Speech Detection")

        # Background image
        bg1 = Image.open(r"registerpage.png")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=1366, height=768)

        # Title section
        title_lb1 = Label(
            bg_img,
            text="HATE SPEECH DETECTION",
            font=("calibri", 35, "bold"),
            bg="#003366",  # Dark blue background
            fg="#FFFFFF"   # White text
        )
        title_lb1.place(relx=0.5, y=50, anchor="center")

        Label(
            self.root,
            text="Enter Text",
            font=("calibri", 20),
            fg="#003366",
            bg="#FFFFFF"
        ).place(relx=0.5, y=150, anchor="center")
        
        self.text_entry = Text(self.root, font=("calibri", 15), bd=4, width=60, height=5)
        self.text_entry.place(relx=0.5, y=200, anchor="center")

        Button(
            self.root,
            text="Check",
            font=("calibri", 18),
            fg="#FFFFFF",
            bg="#003366",
            command=self.check_hate_speech
        ).place(relx=0.45, y=300, anchor="center")
        
        Button(
            self.root,
            text="Clear",
            font=("calibri", 18),
            fg="#FFFFFF",
            bg="#660000",
            command=self.clear_entry
        ).place(relx=0.55, y=300, anchor="center")

        # Output area for displaying results
        self.result_area = Text(
            self.root,
            width=80,
            height=4,
            font=("calibri", 14),
            state='disabled',
            bg="#F0F8FF",  # Light blue background
            fg="#003366"   # Dark blue text
        )
        self.result_area.place(relx=0.5, y=450, anchor="center")

        # Expanded list of hate speech keywords
        self.hate_speech_keywords = [
            "hate", "violence", "racism", "racist", "discrimination",
            "sexism", "sexist", "misogyny", "homophobia", "bigotry",
            "xenophobia", "phobia", "hate speech", "abuse", "bullying",
            "assault", "terrorist", "terrorism", "incitement",
            "persecution", "intolerance", "dehumanization", "slur",
            "derogatory", "offensive", "stereotype", "prejudice", 
            "hate group", "extremist", "radical", "insult", 
            "dysphemism", "hate crime", "injustice", "inequality",
            "marginalization", "stigma", "disparagement", "hostility", "kill"
        ]

    def play_sound(self):
        winsound.Beep(1000, 300)  # Frequency and duration in milliseconds

    def check_hate_speech(self):
        self.play_sound()  # Play sound on button click
        text = self.text_entry.get("1.0", END).strip()
        if not text:
            self.display_error("Error: Please enter some text.")
            return

        detected_keywords = []
        for keyword in self.hate_speech_keywords:
            if keyword in text.lower():
                detected_keywords.append(keyword)

        if detected_keywords:
            result_text = f"Hate Speech Detected! Keywords: {', '.join(detected_keywords)}"
        else:
            result_text = "No hate speech detected."

        # Clear previous results and display the results
        self.result_area.config(state='normal')  # Enable to update
        self.result_area.delete(1.0, END)  # Clear previous results
        self.result_area.insert(END, result_text)
        self.result_area.config(state='disabled')  # Make it read-only

    def clear_entry(self):
        self.play_sound()  # Play sound on button click
        self.text_entry.delete("1.0", END)  # Clear the input field
        self.result_area.config(state='normal') 
        self.result_area.delete(1.0, END)  # Clear the output area
        self.result_area.config(state='disabled')  # Make it read-only again

    def display_error(self, message):
        self.result_area.config(state='normal')  # Temporarily allow edits for error messages
        self.result_area.delete(1.0, END)
        self.result_area.insert(END, message)
        self.result_area.config(state='disabled')  # Make it read-only again

if __name__ == "__main__":
    root = Tk()
    obj = hatespeech(root)
    root.mainloop()
