import os
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_Recognition import face_Recognition
from attendance import Attendance
from devloper import Devloper
from datetime import datetime
from time import strftime
from LoginForButtons import Login_Windos,Login_Atten
from help import Help
from registration import Register


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # banner Image

        # First Banner Image
        img = Image.open(r"college_images\FirstBannerImg.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Banner Image
        img1 = Image.open(r"college_images\thiredbannerimg.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Thired Banner Image
        img2 = Image.open(r"college_images\secondfacerecognitionbaner.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=400, height=130)

        # Background Image
        img3 = Image.open(r"college_images\background.jpg")
        img3 = img3.resize((1366, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=710)

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        #=================================time===================================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman", 15, "bold"),background='white',fg='blue')
        lbl.place(x=0,y=(-2),width=110,height=45)
        time()

        # ================================Button=========================================

        # Student Button
        img4 = Image.open(r"college_images\studentimg.jpg")
        img4 = img4.resize((170, 140), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.loginStudent, cursor="hand2")
        b1.place(x=200, y=80, width=170, height=140)

        b1 = Button(bg_img, text="Student Details", command=self.loginStudent, cursor="hand2",
                    font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        b1.place(x=200, y=220, width=170, height=30)

        # Detect Face
        img5 = Image.open(r"college_images\FaceRecognition.jpg")
        img5 = img5.resize((170, 140), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_recognition)
        b1.place(x=400, y=80, width=170, height=140)

        b1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_recognition,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=400, y=220, width=170, height=30)

        # Attendance face button
        img6 = Image.open(r"college_images\Attendance.jpg")
        img6 = img6.resize((170, 140), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.loginAtten)
        b1.place(x=600, y=80, width=170, height=140)

        b1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.loginAtten,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=600, y=220, width=170, height=30)

        # Help face button
        img7 = Image.open(r"college_images\helpdesk.jpg")
        img7 = img7.resize((170, 140), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b1.place(x=800, y=80, width=170, height=140)

        b1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=800, y=220, width=170, height=30)

        # Train Face Button
        img8 = Image.open(r"college_images\Traindata.jpg")
        img8 = img8.resize((170, 140), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=320, width=170, height=140)

        b1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,
                    font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        b1.place(x=200, y=460, width=170, height=30)

        # Photo Face
        img9 = Image.open(r"college_images\photoface.jpg")
        img9 = img9.resize((170, 140), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=400, y=320, width=170, height=140)

        b1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=400, y=460, width=170, height=30)

        # Devloper button
        img10 = Image.open(r"college_images\devloper.jpg")
        img10 = img10.resize((170, 140), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.devloper_data)
        b1.place(x=600, y=320, width=170, height=140)

        b1 = Button(bg_img, text="Sys Info", cursor="hand2",command=self.devloper_data,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=600, y=460, width=170, height=30)

        # Exit button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((170, 140), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=800, y=320, width=170, height=140)

        b1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit,
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=800, y=460, width=170, height=30)

        # ==============================Photo Button===============================

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit the project!!!")
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        # ======================Function Buttons===================================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def devloper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Devloper(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def loginStudent(self):
        # Create the login window
        self.new_window = Toplevel(self.root)
        self.app = Login_Windos(self.new_window)

    def loginAtten(self):
        # Create the login window
        self.new_window = Toplevel(self.root)
        self.app = Login_Atten(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
