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
        



        