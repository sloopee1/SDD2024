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

        

        