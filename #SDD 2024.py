#SDD 2024
import tkinter as tk 
import customtkinter as ctk
import random

#Set up appearance and colour theme
ctk.set_appearance_mode("Dark") #Options are: System, Light, Dark
ctk.set_default_color_theme("blue") #Options are: Blue, Green, Dark Blue

class MultiplicationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multiplication Learning App")
        self.geometry("800x800")
       
        self.current_score = 0 
        self.high_score = 0

        self.FONT_LARGE = ("Arial", 16)
        self.FONT_SMALL = ("Arial", 12)
        self.font_size_options = ["10", "12", "14", "16", "18", "20"]

        self.dark_mode = tk.BooleanVar(value=True) #Keeping track of whether it is in dark mode or not

        #Main Menu Frame Setup
        self.menu_frame = ctk.CTkFrame(self, width=720, height=50, corner_radius=10)
        self.menu_frame.place(relx=0.5, rely=0.1, anchor=tk.N)
        
        #Create Buttons For Lesson, Quiz, and Settings
        self.lesson_button = ctk.CTkButton(self.menu_frame, text="Lesson", command=self.show_lesson)
        self.quiz_button = ctk.CTkButton(self.menu_frame, text="Quiz", command=self.start_quiz)
        self.settings_button = ctk.CTkButton(self.menu_frame, text="Settings", command=self.show_settings)

        self.lesson_button.grid(row=0, column=0, padx=10, sticky="ew")
        self.quiz_button.grid(row=0, column=1, padx=10, sticky="ew")
        self.settings_button.grid(row=0, column=2, padx=10, sticky="ew")

        #Initialize frames for different parts of the app
        self.lesson_frame = self.create_lesson_frame()
        self.quiz_frame = self.create_quiz_frame()
        self.settings_frame = self.create_settings_frame()

        #Display the lesson frame initally
        self.show_lesson()

    def toggle_dark_mode(self):
        mode = "Dark" if self.dark_mode.get() else "Light"
        ctk.set_appearance_mode(mode)

    def show_multiplication_table(self, number, label):
        if number <= 0:
            label.configure(text="Please enter a positive number.")
        else:

            table_text = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 11)])
            label.configure(text=table_text)


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
    
    def toggle_dark_mode(self):
        ctk.set_appearance_mode("Dark" if self.dark_mode.get() else "Light")

    def create_quiz_frame(self):
        frame = ctk.CTkFrame(self, width=720, height=480, corner_radius=10)
        frame.place_forget()

        self.question_label = ctk.CTkLabel(frame, text="", font=self.FONT_LARGE)
        self.question_label.pack(pady=20)
        
        self.answer_entry = ctk.CTkEntry(frame, font = self.FONT_SMALL)
        self.answer_entry.pack()

        submit_button = ctk.CTkButton(frame, text="Submit", command=self.check_quiz_answer, font=self.FONT_SMALL)
        submit_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(frame, text="", font=self.FONT_SMALL)
        self.result_label.pack(pady=10)

        self.current_score_label = ctk.CTkLabel(frame, text=f"Current Score: {self.current_score}", font=self.FONT_SMALL)
        self.current_score_label.pack(pady=10)

        self.high_score_label = ctk.CTkLabel(frame, text=f"High Score: {self.high_score}", font=self.FONT_SMALL)
        self.high_score_label.pack(pady=10)

        return frame


    def start_quiz(self):
        self.current_score = 0
        self.hide_all_frames()
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.generate_quiz_question()


    def generate_quiz_question(self):
        self.num1, self.num2 = random.randint(1,12), random.randint(1,12)
        self.correct_answer = self.num1 * self.num2
        self.question_label.configure(text=f"What is {self.num1} x {self.num2}?")
        self.answer_entry.delete(0, tk.END)
        self.result_label.configure(text="")

    def check_quiz_answer(self):
        try:
            user_answer=int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.current_score += 1
                self.result_label.configure(text="Correct!", text_color="green")
                if self.current_score > self.high_score:
                    self.high_score = self.current_score
                self.current_score_label.configure(text=f"Current Score: {self.current_score}")    
                self.high_score_label.configure(text=f"High Score: {self.high_score}")
                self.generate_quiz_question()
            else:
                self.result_label.configure(text="Incorrect. Try Again!", text_color="red")
                self.show_explanation_window()
                self.current_score = 0
                self.current_score_label.configure(text=f"Current Score: {self.current_score}")   
        except ValueError:
            self.result_label.configure(text="Please enter a valid number.")

    def show_explanation_window(self):
        explanation_window = ctk.CTkToplevel(self)
        explanation_window.title("Explanation")
        explanation_window.geometry("400x300")

        table_text = "\n".join([f"{self.num1} x {i} = {self.num1 * i}" if i != self.num2 else f"[*{self.num1} x {i} = {self.num1 * i}*]" for i in range(1,11)])
        explanation_label = ctk.CTkLabel(explanation_window, text=f"The correct was {self.correct_answer}. \n\nMultilication table for {self.num1}:\n\n{table_text}", wraplength=380, justify="left", font=self.FONT_SMALL)
        explanation_label.pack(pady=20)

        next_question_button = ctk.CTkButton(explanation_window, text="Next Question", command=lambda: [explanation_window.destroy(), self.generate_quiz_question()])
        next_question_button.pack(pady=10)

    def create_settings_frame(self):
        frame = ctk.CTkFrame(self, width=720, height=480, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Dark Mode Switch
        dark_mode_switch = ctk.CTkSwitch(frame, text="Dark Mode",variable=self.dark_mode, command=self.toggle_dark_mode)
        dark_mode_switch.pack(pady=20)

        #Font Size Changer
        font_size_label = ctk.CTkLabel(frame, text="Select Font Size:", font=self.FONT_SMALL)
        font_size_label.pack(pady=10)

        font_size_dropdown = ctk.CTkComboBox(frame, values=self.font_size_options, command=self.adjust_font_size)
        #Default Font Size
        font_size_dropdown.set(str(self.FONT_SMALL[1]))
        font_size_dropdown.pack(pady=10)

        return frame

    def adjust_font_size(self, font_size):
        font_size = int(font_size)
        self.FONT_LARGE = ("Arial", font_size)
        self.FONT_SMALL = ("Arial", font_size - 4)
        self.update_widget_fonts(self)

    def update_widget_fonts(self, parent):
        for widget in parent.winfo_children():
            widget_type = type(widget)
            if widget_type in [ctk.CTkLabel, ctk.CTkButton, ctk.CTkEntry]:
                widget.configure(font=self.FONT_LARGE if widget_type is ctk.CTkLabel else self.FONT_SMALL)
            if hasattr(widget, "winfo_children"):
                self.update_widget_fonts(widget)

    def show_lesson(self):
        self.hide_all_frames()
        self.lesson_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_settings(self):
        self.hide_all_frames()
        self.settings_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_all_frames(self):
        self.lesson_frame.place_forget()
        self.quiz_frame.place_forget()
        self.settings_frame.place_forget()

if __name__ == "__main__":
    app = MultiplicationApp()
    app.mainloop()



                


        
        



        