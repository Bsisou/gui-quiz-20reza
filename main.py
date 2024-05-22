from tkinter import *
from PIL import Image, ImageTk

class QuizStarter:
    def __init__(self, open_window):
        self.open_window = open_window
        self.current_page = 1  # Keep track of the current page

        # Initial background image
        self.change_background("QuizQuestion.png")

        # Continue button
        self.continue_button = Button(open_window, text="Continue", bg="dark blue", fg="white", font=('Times New Roman',10,'bold'), command=self.continue_pressed)
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
            self.current_page = 1  # Keep track of the current page

            # Initial background image
            self.change_background("QuizQuestion(2).png")

            # Continue button
            self.continue_button = Button(open_window, text="Confirm", bg="#29BFA6", fg="white", font=('Times New Roman',10,'bold'), command=self.continue_pressed) 
            self.continue_button.place(x=520, y=310)
          
            self.continue_button = Button(open_window, text="GO BACK", bg="dark blue", fg="white", font=('Times New Roman',10,'bold'), command=self.continue_pressed)
            self.continue_button.place(x=100, y=315)
            self.entry_box = Entry(open_window, width=15, font=("Arial", 12))
            self.entry_box.place(x=310, y=210)

def open_second_window(self):
        second_window = Tk()
        second_window.geometry("650x400")
        second_window.title("General Knowledge Quiz")

    

if __name__ == '__main__':
    open_window = Tk()
    open_window.geometry("650x400")
    open_window.title("General Knowledge Quiz")
    quizstarter_object = QuizStarter(open_window)
    open_window.mainloop()