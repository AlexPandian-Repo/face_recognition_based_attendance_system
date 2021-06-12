from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white",
                          fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=80)

        # Image 1===============================================================>

        img1 = Image.open(r"C:\Users\dwayn\Desktop\fras\FinalYearProject\college_images\scan-face1.jpg")
        img1 = img1.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1500, height=700)

        # button ================================================================>
        b1_1 = Button(self.root, text="Face Reconition")

        #img2 = Image.open(r"C:\Users\my\PycharmProjects\FinalYearProject\college_images\second.jpg")
        #img2 = img2.resize((950, 700), Image.ANTIALIAS)
        #self.photoimg2 = ImageTk.PhotoImage(img2)

        #f_lbl = Label(self.root, image=self.photoimg2)
        #f_lbl.place(x=650, y=55, width=950, height=700)

        # Button ====================>
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"),
                      bg="blue", fg="white")
        b1_1.place(x=1100, y=400, width=200, height=40)
    #==========
    def mark_attendance(self, i, r, n, d):
        with open("attendence_file.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")






    # =======
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                               database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                my_cursor.execute("select roll from student where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                my_cursor.execute("select dep from student where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                my_cursor.execute("select student_id from student where student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
