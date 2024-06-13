from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random


class QuizStarter:
    def __init__(self, open_window):
        self.open_window = open_window
        self.current_page = 1  # Keep track of the current page

        # Initial background image
        self.change_background("QuizQuestion.png")

        # Continue button
        self.continue_button = Button(open_window, text="Continue", bg="dark blue", fg="white", 
 font=('Times New Roman',10,'bold'), command=self.continue_pressed)
        self.continue_button.place(x=500, y=310)
    def change_background(self, image_path):
        # Load and display background image

        self.bg_image = Image.open(image_path)
        width = 650
        height = 400
        self.resize_image = self.bg_image.resize((width, height))
        self.bg_image = ImageTk.PhotoImage(self.resize_image)
        self.image_label = Label(self.open_window, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)


    
    def continue_pressed(self):
        if self.current_page == 1 or 3:
            # Change to the second page
            self.open_window = open_window
            self.current_page = 2  # Keep track of the current page

            # Initial background image
            self.change_background("QuizQuestion(2).png")

            # Continue button
            self.confirm_button = Button(open_window, text="Confirm", bg="#29BFA6", fg="white", 
 font=('Times New Roman',12,'bold'), command=self.confirm_pressed) 
            self.confirm_button.place(x=340, y=250)
            self.back_button = Button(open_window, text="GO BACK", bg="dark blue", fg="white", 
 font= ('Times New Roman',10,'bold'), command=self.goBack_pressed1)
            self.back_button.place(x=150, y=315)
            self.entry_box = Entry(open_window, width=15, font=("Arial", 12))
            self.entry_box.place(x=310, y=210)
            # dont go to the next page is they dont enter a name
            
            
            
    def goBack_pressed1(self):
        if self.current_page == 2:   
            self.change_background("QuizQuestion.png")
            self.continue_button = Button(open_window, text="Continue", bg="dark blue", fg="white", 
 font=('Times New Roman',10,'bold'), command=self.continue_pressed)
            self.continue_button.place(x=500, y=310)
             # Change to the first page
            self.current_page = 1 
            self.open_window = open_window


    
    def confirm_pressed(self):
        print(self.current_page)
        if self.current_page == 2:
            # Get the name entered by the user
            name = self.entry_box.get()
            print("Name entered:", name)
            
            
            if name == '':
                messagebox.showinfo("showinfo", "plz enter name")
            else:

                # Change to the third page
                self.current_page = 3
                self.change_background("QuizQuestion(3).png")
                print(self.current_page)
                self.back_button2 = Button(open_window, text="GO BACK", bg="dark blue", fg="white", 
                 font= ('Times New Roman',10,'bold'), command=self.goBack_pressed2)
                self.back_button2.place(x=50, y=350)
            self.next_button = Button(open_window, text="NEXT", bg="dark blue", fg="white", 
     font=('Times New Roman',10,'bold'), command=self.next_pressed)
            self.next_button.place(x=500, y=345)
            self.start_button = Button(open_window, text="START", bg="dark blue", fg="white",  font=('Times New Roman',10,'bold'), command=self.start_questions)
            self.start_button.place(x=200, y=345)

    def change_widgets(self):
        self.question_number += 1
        self.var1.set(0)
        self.question_label.config(text=self.questions[self.question_number][0])
        self.first_option.config(text=self.questions[self.question_number][1])
        self.second_option.config(text=self.questions[self.question_number][2])
        self.third_option.config(text=self.questions[self.question_number][3])
        self.forth_option.config(text=self.questions[self.question_number][4])

    def next_pressed(self):
        self.start_button.destroy()
        self.answer = self.var1.get()
        self.questions_list = []
        if len(self.questions_list) < 7:
            self.change_widgets()
        else:
            self.next_button.destroy()
            self.back_button2.destroy()
            

        
        
    def start_questions(self):
        self.questions = {
            1: ["Who is considered the final prophet in Islam?", "Prophet Isa (Jesus)", "Prophet Musa (Moses)", "Prophet Muhammad (PBUH)", "Prophet Ibrahim (Abraham)", 3],
            2: ["What is the holy book of Islam?", "Bible", "Torah", "Quran", "Gita", 3],
            3: ["In which city was Prophet Muhammad (PBUH) born?", "Jerusalem", "Mecca", "Medina", "Baghdad", 2],
            4: ["What is the name of the Islamic month of fasting?", "Ramadan", "Shawwal", "Dhul-Hijjah", "Rajab", 1],
            5: ["How many times a day are Muslims required to pray?", "Three", "Five", "Four", "Six", 2],
            6: ["What is the pilgrimage to Mecca called?", "Umrah", "Sawm", "Hajj", "Zakat", 3],
            7: ["Who was the first Caliph after Prophet Muhammad (PBUH)?", "Umar", "Ali", "Abu Bakr", "Uthman", 3],
            8: ["Which angel is believed to have brought revelations to Prophet Muhammad (PBUH)?", "Angel Michael (Mikail)", "Angel Gabriel (Jibril)", "Angel Raphael (Israfil)", "Angel Azrael (Izrail)", 2]
        }
      
        
        self.question_number = 1 
        self.question_label= Label (open_window, text=self.questions[self.question_number][0], font=("Arial", 12),padx=8, pady=35)
        self.question_label.place(x=160, y=80)

        # hold value of radio button
        self.var1 = IntVar()

        #radio button rb1
        self.first_option= Radiobutton(open_window, text= self.questions [self.question_number][1], font=("Helvetica", "12"), value=1, padx=35,pady=5, variable=self.var1) 
        self.first_option.place(x=54, y=215)


        # second radion button for option 2 - rb2
        self.second_option= Radiobutton(open_window, text= self.questions [self.question_number][1], font=("Helvetica", "12"), value=1, padx=35,pady=5, variable=self.var1) 
        self.second_option.place(x=345, y=215)

        # third radion button for option 3 - rb3
        self.third_option= Radiobutton(open_window, text= self.questions [self.question_number][1], font=("Helvetica", "12"), value=1, padx=35,pady=5, variable=self.var1) 
        self.third_option.place(x=54, y=287)

        # fourth radion button for option 4 - rb4
        self.forth_option= Radiobutton(open_window, text= self.questions [self.question_number][1], font=("Helvetica", "12"), value=1, padx=35,pady=5, variable=self.var1) 
        self.forth_option.place(x=345, y=287)
        


        


        

        


    def goBack_pressed2(self):
        if self.current_page == 3:  
            print(self.current_page)
            self.continue_pressed()
 
        
        
    

if __name__ == '__main__':
    open_window = Tk()
    open_window.geometry("650x400")
    open_window.title("Islamic Quiz")
    quizstarter_object = QuizStarter(open_window)
    open_window.mainloop()