import random
from tkinter import *
from PIL import Image, ImageTk
import winsound  # For sound notifications

class fakenewsdetect:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False, False)
        self.root.title("Fake News Detection")

        # Background image
        bg1 = Image.open(r"thirdpage.png")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=1366, height=768)

        # Center container
        container = Frame(self.root, bg="#f0f0f0", bd=5, relief=RIDGE)
        container.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=500)

        # Title section
        title_lb1 = Label(container, text="FAKE NEWS DETECTOR", font=("calibri", 30, "bold"), bg="yellow", fg="red")
        title_lb1.pack(pady=20)

        # Article input label and text area
        input_frame = Frame(container, bg="#f0f0f0")
        input_frame.pack(pady=10)
        Label(input_frame, text="Enter News Article", font=("calibri", 16), bg="#f0f0f0").pack()
        self.article_entry = Text(input_frame, width=60, height=6, font=("calibri", 12), bd=2, relief=SUNKEN)
        self.article_entry.pack(pady=5)

        # Buttons section
        button_frame = Frame(container, bg="#f0f0f0")
        button_frame.pack(pady=10)
        Button(button_frame, text="Analyze", font=("calibri", 14), command=self.analyze_news, bg="green", fg="white", width=12).pack(side=LEFT, padx=20)
        Button(button_frame, text="Clear", font=("calibri", 14), command=self.clear_entry, bg="red", fg="white", width=12).pack(side=LEFT)

        # Output area for displaying results
        result_frame = Frame(container, bg="#f0f0f0")
        result_frame.pack(pady=10)
        Label(result_frame, text="Result", font=("calibri", 16), bg="#f0f0f0").pack()
        self.result_area = Text(result_frame, width=60, height=6, font=("calibri", 12), state='disabled', bd=2, relief=SUNKEN)
        self.result_area.pack(pady=5)

    def play_sound(self):
        # Play a simple beep sound when a button is clicked
        winsound.Beep(1000, 300)

    def analyze_news(self):
        self.play_sound()  # Play sound on button click
        article = self.article_entry.get("1.0", END).strip()
        if not article:
            self.display_error("Error: Please enter a news article.")
            return

        # Check if 'news' is at the end of the input (case-insensitive)
        if article.lower().endswith("india"):
            result_text = "REAL NEWS !"
        else:
            # Randomly choose a result
            result_choices = ["FAKE NEWS !", "REAL NEWS !", "UNDECIDED"]
            result_text = random.choice(result_choices)

        # Clear previous results and display the new result
        self.result_area.config(state='normal')  # Enable to update
        self.result_area.delete(1.0, END)  # Clear previous results
        self.result_area.insert(END, result_text)
        self.result_area.config(state='disabled')  # Make it read-only

    def clear_entry(self):
        self.play_sound()  # Play sound on button click
        self.article_entry.delete("1.0", END)  # Clear the input field
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
    obj = fakenewsdetect(root)
    root.mainloop()
