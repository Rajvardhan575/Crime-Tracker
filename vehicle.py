from tkinter import *
from PIL import Image, ImageTk
import random

class vehicle:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+70+30")
        self.root.resizable(False, False)
        self.root.title("Vehicle Tracking System")

        # Background image
        bg1 = Image.open(r"thirdpage.png")
        bg1 = bg1.resize((1366, 868))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set background image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=8, width=1366, height=868)

        # Title section with enhanced style
        title_label = Label(
            bg_img,
            text="Vehicle Details Finding",
            font=("verdana", 30, "bold"),
            bg="#F0F0F0",  # Subtle grey background
            fg="#003366"  # Deep blue text
        )
        title_label.place(relx=0.5, rely=0.1, anchor="center", width=900, height=50)

        # Input Label
        input_label = Label(
            bg_img,
            text="Enter Vehicle Number:",
            font=("calibri", 20, "bold"),
            bg="#F0F0F0",
            fg="#003366"
        )
        input_label.place(relx=0.4, rely=0.25, anchor="center")

        # Input Entry
        self.vehicle_number_entry = Entry(bg_img, font=("calibri", 20), width=20, bd=4)
        self.vehicle_number_entry.place(relx=0.6, rely=0.25, anchor="center")

        # Button to Track
        track_button = Button(
            bg_img,
            text="Track Vehicle",
            font=("calibri", 18),
            fg="#FFFFFF",
            bg="#003366",
            command=self.generate_random_details
        )
        track_button.place(relx=0.5, rely=0.35, anchor="center")

        # Output Area
        self.result_area = Text(
            bg_img,
            width=80,
            height=15,
            font=("calibri", 14),
            bg="#F0F8FF",  # Light blue background
            fg="#003366",  # Dark blue text
            state='disabled'
        )
        self.result_area.place(relx=0.5, rely=0.65, anchor="center")

    def generate_random_details(self):
        vehicle_number = self.vehicle_number_entry.get().strip()
        if not vehicle_number:
            self.display_result("Error: Please enter a valid vehicle number!")
            return

        # Random details generation
        first_names = ["Aarav", "Vivaan", "Arjun", "Aditya", "Ishaan", "Rahul", "Kabir", "Manish", "Rohan", "Siddharth"]
        last_names = ["Sharma", "Verma", "Mehta", "Gupta", "Patel", "Joshi", "Reddy", "Nair", "Thakur", "Singh"]
        vehicle_names = ["Maruti Suzuki", "Hyundai", "Tata", "Toyota", "Honda", "Mahindra", "Kia", "Ford", "Volkswagen"]
        vehicle_models = ["Alto 800", "Creta", "Harrier", "Fortuner", "City", "XUV700", "Seltos", "Ecosport", "Polo"]
        colors = ["White", "Black", "Silver", "Blue", "Red", "Grey"]
        rc_numbers = [f"MH-{random.randint(10, 99)}-{random.randint(1000, 9999)}" for _ in range(5)]
        
        # Compile Randomized Output
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        vehicle = f"{random.choice(vehicle_names)} {random.choice(vehicle_models)}"
        rc_number = random.choice(rc_numbers)
        details = f"""
        Vehicle Number: {vehicle_number}
        Owner's Name: {name}
        Vehicle: {vehicle}
        Color: {random.choice(colors)}
        RC Number: {rc_number}
        Registered City: {random.choice(['Mumbai', 'Pune', 'Nagpur', 'Delhi', 'Bangalore', 'Hyderabad', 'Kolkata'])}
        """

        self.display_result(details)

    def display_result(self, message):
        self.result_area.config(state='normal')  # Temporarily enable editing
        self.result_area.delete(1.0, END)
        self.result_area.insert(END, message)
        self.result_area.config(state='disabled')  # Make it read-only again

if __name__ == "__main__":
    root = Tk()
    obj = vehicle(root)
    root.mainloop()
