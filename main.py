from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

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
        if self.current_page == 1:
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
                self.back_button = Button(open_window, text="GO BACK", bg="dark blue", fg="white", 
                 font= ('Times New Roman',10,'bold'), command=self.goBack_pressed1)
                self.back_button.place(x=50, y=350)



      


    def goBack_pressed2(self):
        if self.current_page == 3:   
            self.change_background("QuizQuestion(2).png")
    


    
            
            





    

if __name__ == '__main__':
    open_window = Tk()
    open_window.geometry("650x400")
    open_window.title("General Knowledge Quiz")
    quizstarter_object = QuizStarter(open_window)
    open_window.mainloop()