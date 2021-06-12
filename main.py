import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1 Image

        img1 = Image.open(r"college_images\second.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=100)

        # 2 Image

        img2 = Image.open(r"college_images\second.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=100)

        # 3 Image

        img3 = Image.open(r"college_images\second.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=100)

        # bg Image

        img4 = Image.open(r"college_images\scott-graham-5fNmWej4tAA-unsplash.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=100, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ===============time==========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 10, "bold"), bg="white", fg="blue")
        lbl.place(x=0, y=(-15), width=110, height=50)
        time()

        # Student button 
        img5 = Image.open(r"college_images\studentdetails.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

        # detect face
        img6 = Image.open(r"college_images\face-recognition.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, command=self.face_data, cursor="hand2")
        b1.place(x=400, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=400, y=300, width=220, height=40)

        # Attendence
        img7 = Image.open(r"college_images\attendance.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command=self.attendance_data, image=self.photoimg7, cursor="hand2")
        b1.place(x=700, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendence", cursor="hand2", command=self.attendance_data,
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=700, y=300, width=220, height=40)

        # HELP
        img8 = Image.open(r"college_images\help.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.help_data)
        b1.place(x=1000, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="HELP", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1000, y=300, width=220, height=40)

        # Training
        img9 = Image.open(r"college_images\download.jfif")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=100, y=550, width=220, height=40)

        # Photos

        img10 = Image.open(r"college_images\photos.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=400, y=550, width=220, height=40)

        # Developer
        img11 = Image.open(r"college_images\developer.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.developer_data)
        b1.place(x=700, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data,
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=700, y=550, width=220, height=40)

        # Exit button===============>

        img12 = Image.open(r"college_images\exit_PNG2.png")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.iExit)
        b1.place(x=1000, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1000, y=550, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit ?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

            # ===========================function button==============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
