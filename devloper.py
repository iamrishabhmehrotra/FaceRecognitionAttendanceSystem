from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Devloper:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title

        title_lbl = Label(self.root, text="DEVLOPER",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # bg Image
        img_Top = Image.open(
            r"college_images\background.jpg")
        img_Top = img_Top.resize((1366, 600), Image.Resampling.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=1366, height=600)



        # Frame

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=500)

        img_side = Image.open(
            r"college_images\devloper.jpg")
        img_side = img_side.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg_side = ImageTk.PhotoImage(img_side)

        f_lbl = Label(self.root, image=self.photoimg_side)
        f_lbl.place(x=1120, y=50, width=150, height=150)

        #Devloper info
        dev_label=Label(main_frame,text="Hello these shreesh",font=("times new roman", 20, "bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am full stack devloper", font = ("times new roman", 20, "bold"), fg = "blue", bg = "white")
        dev_label.place(x=0, y=40)

        # frame image
        img2 = Image.open(
            r"college_images\devloper.jpg")
        img2 = img2.resize((500, 350), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=160, width=500, height=350)

        # Main Frame

        left_frame = Frame(self.root, bd=2)
        left_frame.place(x=30, y=80, width=700, height=540)

        # Blog Section
        blog_label = Label(left_frame, text="Software Info", font=("times new roman", 25, "bold"))
        blog_label.pack(pady=10)

        # Scrollbar for Blog Content
        blog_scrollbar = Scrollbar(left_frame)
        blog_scrollbar.pack(side=RIGHT, fill=Y)

        # Text Widget for Blog Content
        self.blog_text = Text(left_frame, yscrollcommand=blog_scrollbar.set, wrap=WORD, font=("times new roman", 14))
        self.blog_text.pack(fill=BOTH, expand=True)

        blog_scrollbar.config(command=self.blog_text.yview)

        # Enable text widget for authorized user (developer)
        self.authorized_user = True  # Change this to True for authorized user
        if not self.authorized_user:
            self.blog_text.config(state=DISABLED)  # Disable the text widget for non-authorized users
        else:
            self.blog_text.config(state=NORMAL)  # Enable the text widget for authorized users

        # Add sample blog content
        sample_blog = """STUDENT DETAIL:\nTeacher or Admin are fill your form\n and make you eligible to give attendance.\n\n
FACE DETECTOR:\nFace detector is used for getting attendance of student just click Face Recognition button.\nIf you want to exist from face detector page just press space bar and hold for a second.\n\n
ATTENDANCE:\nAttendance page only access by teacher or admin\nImport CSV button can import the attendance file.\nExport button is used to save that attendance file with different name in your system.\nUpdate Button is for update the student present or absent manualy.\nReset is for clear all fields.\n\n
HELP DESK:\nYou can directly able to contact with support team if any thing wrong happens in system.\n\n
TRAIN DATA:\nAfter filling all the details of the student photo, name etc.\nTraining of inserted photo image is mendatory because its AI based system\n\n
PHOTOS:\nYou can see all the photos of the students here.\n\nDEVLOPER:\nYou are here now you can see some details about devloper and SYSTEM INFORMATION.\n\n
EXIT:\nThese button is used for exit from application, Say buy to application!"""
        self.blog_text.insert("1.0", sample_blog)


if __name__ == "__main__":
    root = Tk()
    obj = Devloper(root)
    root.mainloop()