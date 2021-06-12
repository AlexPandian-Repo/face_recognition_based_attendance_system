from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\fourth.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # FRAME
        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=600)

        img1 = Image.open(r"college_images\third.jpg")
        img1 = img1.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(main_frame, image=self.photoimg1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        
        # developer Info
        dep_label = Label(main_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.place(x=0,y=5)
        dep_label = Label(main_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.place(x=0, y=40)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()