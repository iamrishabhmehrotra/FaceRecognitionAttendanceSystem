from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # Title

        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Top Image
        img_Top = Image.open(
            r"college_images\secondfacerecognitionbaner.png")
        img_Top = img_Top.resize((1366, 275), Image.Resampling.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=1366, height=275)



        # Bottom Image
        img_bottom = Image.open(
            r"college_images\face-recognition-1.jpg")
        img_bottom = img_bottom.resize((1366, 265), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=360, width=1366, height=275)

        # button train Data
        b1 = Button(self.root, text="TRAIN DATA", cursor="hand2",command=self.train_classifier,
                    font=("times new roman", 28, "bold"), bg="red", fg="white")
        b1.place(x=0, y=320, width=1366, height=50)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") #gray scale image
            imageNp=np.array(img ,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13

        ids=np.array(ids)

        # =========================Train the classifier and save=============================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
