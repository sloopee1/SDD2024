#SDD 2024
import tkinter as tk 
import customtkinter as ctk
import random

#Set up appearance and colour theme
ctk.set_appearance_mode("Dark") #Options are: System, Light, Dark
ctk.set_default_color_theme("blue") #Options are: Blue, Green, Dark Blue

class MultiplicationApp(ctk.CTk):
    def __innit__(self):
        super().__innit__()
        self.title("Multiplication Learning App")
        self.geometry("800x800")
        self.current_score = 0 
        self.high_score = 0

        self.FONT_LARGE = ("Arial", 16)
        self.FONT_SMALL - ("Arial", 12)
        self.font_size_options - ["10", "12", "14", "16", "18", "20"]

        self.dark_mode = tk.BooleanVar(value=True) #Keeping track of whether it is in dark mode or not

        #Main Menu Frame Setup
        self.menu_frame = ctk.CTkFrame(self, width=720, height=50, corner_radius=10)
        self.menu_frame.place(relx=0.5, rely=0.1, anchor=tk.N)
        \
        #Create Buttons For Lesson, Quiz, and Settings
        self.lesson_button = ctk.CTkButton(self.menu_frame, text="Lesson", command=self.show_lesson)
        self.quiz_button = ctk.CTkButton(self.menu_frame, text="Quiz", command=self.show_quiz)
        self.settings_button = ctk.CTkButton(self.menu_frame, text="Settings", command=self.show_settings)

        #Initialize frames for different parts of the app
        self.lesson_frame = self.create_lesson_frame()
        self.quiz_frame = self.create_quiz_frame()
        self.settings_frame = self.create_settings_frame()

        #Display the lesson frame initally
        self.show_lesson()

        def toggle_dark_mode(self):
            mode = "Dark" if self.dark_mode.get() else "Light"
            ctk.set_appearance_mode(mode)

        def create_lesson_frame(self):
            frame = ctk.CTkFrame(self, width=720, height=480, corner_radius=10)
            frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            label = ctk.CTkLabel(frame, text="Enter a number to see its' multiplication table:", font=self.FONT_LARGE)
            label.pack(pady=10)

            entry = ctk.CTkEntry(frame, font=self.FONT_SMALL)
            entry.pack(pady=10)

            table_label = ctk.CTkLabel(frame, text="", font=self.FONT_SMALL)
            table_label.pack(pady=10, fill=tk.BOTH, expand=True)

            button = ctk.CTkButton(frame, text="Show Table", command =lambda: self.show_multiplication_table(int(entry.get()), table_label), font=self.FONT_SMALL)
            button.pack(pady=10)

            return frame
        
        



        