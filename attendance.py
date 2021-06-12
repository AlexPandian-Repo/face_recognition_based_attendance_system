from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #================================================>Variables<=====================>
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        img1 = Image.open(r"college_images\second.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img2 = Image.open(r"college_images\second.jpg")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        title_lbl = Label(self.root, text="Attendance management system", font=("times new roman", 35, "bold"),
                          bg="white",
                          fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=200, width=1480, height=600)

        # left label Frame
        left_inside_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                       font=("times new roman", 12, "bold"), fg="black")
        left_inside_frame.place(x=3, y=10, width=650, height=580)

        # label and Entry===========
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 13, "bold"),
                                   bg="white", fg="green")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=3, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,
                                       font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=3, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll No:", bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_roll,
                               font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # NAme
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_name,
                               font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_time,
                               font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_date,
                               font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        attendanceLabel = Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance,
                                         font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # button frame============>
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=700, height=35)

        # Import button------>
        import_btn = Button(btn_frame, text="Import csv",command=self.importCSV, width=17,
                          font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)
        # Export button------>
        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=17,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)
        # update button----------->
        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=2)
        # Reset Button----------->
        reset_btn = Button(btn_frame, text="Reset", width=17,command=self.reset_data,
                           font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Frame=================================================================>

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"), fg="black")
        Right_frame.place(x=655, y=10, width=690, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=680, height=455)

        # **************scroll bar table************
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  column=(
                                                  "id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendace ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendace")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=======================Fetch Data===========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                                               parent=self.root)

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export",
                                    "Your Data Exported to" + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
