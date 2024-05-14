from tkinter import *
from PIL import Image, ImageTk


class QuizStarter:
    def __init__(self, parent):

        #background_color = "OldLace"
        background_color = "red"


        self.bg_image = Image.open("QuizQuestion.png") #need to use Image if need to resize
        #self.bg_image = self.bg_image.resize((450, 350), Image.LANCZOS)  # Resize the image with specified dimensions and using Image.LANCZOS

        width = 960
        height = 540
        self.resize_image = self.bg_image.resize((width, height))

        self.bg_image = ImageTk.PhotoImage(self.resize_image)


        #frame set up
        self.quiz_frame = Frame(parent, bg=background_color)
        self.quiz_frame.pack()

        #label for image
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        #self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
        self.image_label.pack()





#***********Starting point of the program***********#
if __name__ == '__main__':
    root = Tk()
    root.geometry("960x540")
    root.title("General Knowledge Quiz")
    quizstarter_object = QuizStarter(root)  
    root.mainloop() #So window won't disappear 