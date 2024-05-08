from tkinter import * 


class QuizStarter:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #label widget for our heading
        self.heading_label = Label(
            self.quiz_frame,
            text="General Quiz",
            font=("Tw cen MT", 18, "bold")
        )
        self.heading_label.grid(row=0)                             



#**********************starting point of program**********************#
if __name__ == '__main__':
    root = Tk()
    root.title("General quiz")
    quizStarter_object = QuizStarter(root) #instantiation, making an intance of class quizstarter to createthe frame with its widgets, passing roots as a parameter
    root.mainloop()#so the windows doesn't dissapear