#SDD 2024
import tkinter as tk 
import customtkinter as ctk
import random

#Set up appearance and colour theme
ctk.set_appearance_mode("Dark") #Options are: System, Light, Dark
ctk.set_default_color_theme("blue") #Options are: Blue, Green, Dark Blue

class MultiplicationApp(ctk.CTk):
    def __innit__(self_)
        super().__innit__()
        self.title("Multiplication Learning App")
        self.geometry("800x800")
        