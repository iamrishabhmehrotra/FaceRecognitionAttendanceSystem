from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import re
import cv2

from mysql.connector import MySQLConnection, CMySQLConnection
from mysql.connector.pooling import PooledMySQLConnection


class Teacher:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ===============================Variables==============================================
        # 'dep','cursor','year','sem','id','name','div','roll','gender','dob','email','gender','phone','address','teacher','photo'

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_otp = StringVar()
        self.var_checkbtn = IntVar()

        # =================================================================================



        # ======================================================================



        # banner Image

        # First Banner Image
        img = Image.open(r"college_images\FirstBannerImg.jpg")
        img = img.resize((500, 80), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=80)

        # Second Banner Image
        img1 = Image.open(r"college_images\thiredbannerimg.jpg")
        img1 = img1.resize((500, 80), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=80)

        # Thired Banner Image
        img2 = Image.open(
            r"college_images\secondfacerecognitionbaner.png")
        img2 = img2.resize((500, 80), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=400, height=80)

        # Background Image
        img3 = Image.open(r"college_images\background.jpg")
        img3 = img3.resize((1366, 800), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=70, width=1366, height=800)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT  SYSTEM",
                          font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=25)

        # Main Frame

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=30, width=1265, height=540)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Staff Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=620, height=515)

        img_left = Image.open(
            r"college_images\secondfacerecognitionbaner.png")
        img_left = img_left.resize((640, 50), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=50)

        # current course in left frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current staff information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=50, width=605, height=430)

        # -------------------------------1 row

        studentName_label = Label(current_course_frame, text="First Name:", font=("times new roman", 12, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=0, padx=3, pady=5, sticky=W)

        studentName_entry = ttk.Entry(current_course_frame, textvariable=self.var_fname, width=20,
                                      font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=1, padx=3, pady=5, sticky=W)


        #Last name

        lastName_label = Label(current_course_frame, text="Last Name:", font=("times new roman", 12, "bold"),
                                  bg="white")
        lastName_label.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        lastName_entry = ttk.Entry(current_course_frame, textvariable=self.var_lname, width=20,
                                      font=("times new roman", 12, "bold"))
        lastName_entry.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        #Contact

        phone_label = Label(current_course_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=1, column=0, padx=3, pady=5, sticky=W)

        phone_entry = ttk.Entry(current_course_frame, textvariable=self.var_contact, width=20,
                                font=("times new roman", 12, "bold"))
        phone_entry.grid(row=1, column=1, padx=3, pady=5, sticky=W)

        # Email
        email_label = Label(current_course_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=1, column=2, padx=3, pady=5, sticky=W)

        email_entry = ttk.Entry(current_course_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=1, column=3, padx=3, pady=5, sticky=W)

        # Security Question

        securityQ_label = Label(current_course_frame, text="Security(Q)", font=("times new roman", 12, "bold"), bg="white")
        securityQ_label.grid(row=2, column=0, padx=3,pady=5, sticky=W)

        securityQ_combo = ttk.Combobox(current_course_frame, textvariable=self.var_securityQ,
                                  font=("times new roman", 12, "bold"), state="readonly", width=18)
        securityQ_combo["values"] = ("Select", "Your Birth Place", "Your Wife/Husband Name", "Your Pet Name", "Your Netive Place")
        securityQ_combo.current(0)
        securityQ_combo.grid(row=2, column=1, padx=3, pady=5, sticky=W)

        # Security Answer

        securityA_label = Label(current_course_frame, text="Security(A):", font=("times new roman", 12, "bold"), bg="white")
        securityA_label.grid(row=2, column=2, padx=3, pady=5, sticky=W)

        securityA_entry = ttk.Entry(current_course_frame, textvariable=self.var_securityA, width=20,
                                font=("times new roman", 12, "bold"))
        securityA_entry.grid(row=2, column=3, padx=3, pady=5, sticky=W)

        #password

        password_label = Label(current_course_frame, text="Password:", font=("times new roman", 12, "bold"), bg="white")
        password_label.grid(row=4, column=0, padx=3, pady=5, sticky=W)

        password_entry = ttk.Entry(current_course_frame, textvariable=self.var_pass, width=20,
                                font=("times new roman", 12, "bold"))
        password_entry.grid(row=4, column=1, padx=3, pady=5, sticky=W)

        # connferm password

        connpassword_label = Label(current_course_frame, text="Confirm Password:", font=("times new roman", 12, "bold"), bg="white")
        connpassword_label.grid(row=4, column=2, padx=3, pady=5, sticky=W)

        connpassword_entry = ttk.Entry(current_course_frame, textvariable=self.var_confpass, width=20,
                                   font=("times new roman", 12, "bold"))
        connpassword_entry.grid(row=4, column=3, padx=3, pady=5, sticky=W)







        # Button Frame

        btn_frame = Frame(current_course_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=220, width=590, height=37)

        # save button

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=15, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=2)

        # update button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=15,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1, padx=0)

        # delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15,
                           font=("times new roman", 12, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)



        # ==============Right Frame========================================================

        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=635, y=10, width=620, height=515)

        img_Right = Image.open(
            r"college_images\secondfacerecognitionbaner.png")
        img_Right = img_Right.resize((640, 50), Image.Resampling.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl = Label(Right_frame, image=self.photoimg_Right)
        f_lbl.place(x=5, y=0, width=640, height=50)

        # Search frame

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=60, width=600, height=75)

        # Search selct
        self.var_com_search = StringVar()

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="Red",
                             fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame,textvariable=self.var_com_search, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Email", "Phone","Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Search_frame,textvariable=self.var_search, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        # search button
        search_btn = Button(Search_frame, command=self.search_data ,text="Search", width=12, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        # show all button
        showAll_btn = Button(Search_frame, command=self.fetch_data ,text="Show All", width=12, font=("times new roman", 10, "bold"), bg="blue",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=3)

        # Table frame

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=150, width=600, height=250)
        # Scroll bar bottom and horizontal scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_Y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Table content
        self.student_table = ttk.Treeview(table_frame, column=(
            'fname', 'lname', 'phone','email', 'securityQ', 'securityA', 'password'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_Y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)

        # vilibale of table content
        self.student_table.heading("fname", text="First Name")
        self.student_table.heading("lname", text="Last Name")
        self.student_table.heading("phone", text="Contact")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("securityQ", text="Security Question")
        self.student_table.heading("securityA", text="Security Answer")
        self.student_table.heading("password", text="Password")
        self.student_table["show"] = "headings"

        # Adgestement of table content
        # 'dep','cursor','year','sem','id','name','div','roll','gender','dob','email','gender','phone','address','teacher','photo'
        self.student_table.column("fname", width=100)  # do it for all names
        self.student_table.column("lname", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("securityQ", width=100)
        self.student_table.column("securityA", width=100)
        self.student_table.column("password", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # self.student_table.column("dep",width=100)

        # =========================== Function Declaration Database  ========================================

        # ============================= Dont Touch Below Code Warning its a database code========================

    def add_data(self):

        self.pattern_pasw = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
        self.pasw = re.match(self.pattern_pasw, self.var_pass.get())
        self.pattern_phone = r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
        self.Phone = re.match(self.pattern_phone, self.var_contact.get())
        self.pattern_email = r"^[A-Za-z]+[-_$.A-Za-z]*[0-9]*@[A-Za-z]*\.[A-Za-z]+$"
        self.Email = re.match(self.pattern_email, self.var_email.get())

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.Phone or self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter proper phone number!", parent=self.root)
        elif not self.Email or self.var_email.get() == "":
            messagebox.showerror("Error!", "Please enter proper email!", parent=self.root)
        elif self.var_pass.get() == "":
            messagebox.showerror("Error", "Enter the password", parent=self.root)
        elif self.var_confpass.get() == "":
            messagebox.showerror("Error", "Confirm the password", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same", parent=self.root)
        elif not self.pasw:
            messagebox.showerror("Error", "A password contains at least eight characters, including at least",
                                 parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ==========================Fatch Data =====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                       database="face_recognizer")

        my_cursor = conn.cursor()
        my_cursor.execute("select * from register")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

        self.var_com_search.set("Select")

        # ===================== get cursor ============================================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_fname.set(data[0]),
        self.var_lname.set(data[1]),
        self.var_contact.set(data[2]),
        self.var_email.set(data[3]),
        self.var_securityQ.set(data[4]),
        self.var_securityA.set(data[5]),
        self.var_pass.set(data[6]),
        self.var_confpass.set(data[6])

    # update function
    def update_data(self):
        self.pattern_pasw = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
        self.pasw = re.match(self.pattern_pasw, self.var_pass.get())
        self.pattern_phone = r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
        self.Phone = re.match(self.pattern_phone, self.var_contact.get())
        self.pattern_email = r"^[A-Za-z]+[-_$.A-Za-z]*[0-9]*@[A-Za-z]*\.[A-Za-z]+$"
        self.Email = re.match(self.pattern_email, self.var_email.get())

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.Phone or self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter proper phone number!", parent=self.root)
        elif not self.Email or self.var_email.get() == "":
            messagebox.showerror("Error!", "Please enter proper email!", parent=self.root)
        elif self.var_pass.get() == "":
            messagebox.showerror("Error", "Enter the password", parent=self.root)
        elif self.var_confpass.get() == "":
            messagebox.showerror("Error", "Confirm the password", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same", parent=self.root)
        elif not self.pasw:
            messagebox.showerror("Error", "A password contains at least eight characters, including at least",parent=self.root)

        else:
            try:
                Upadate = messagebox.askyesno("Update", "Do you want to update these details", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update register set fname=%s,lname=%s, contact=%s,email=%s,securityQ=%s,securityA=%s,password=%s where email=%s",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get(),
                            self.var_email.get()
                        ))
                else:
                    if not Uapdate:
                        return
                messagebox.showinfo("Success", "Teacher details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                # print(e)

    # delete function
    def delete_data(self):
        if self.var_email.get == "":
            messagebox.showerror("Error", "Teacher email must be required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Teacher Delete Page", "Do you want to delete these teacher details!",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from register where email=%s"
                    val = (self.var_email.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully delete teacher details!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_securityQ.set("Select"),
        self.var_securityA.set(""),
        self.var_pass.set(""),
        self.var_confpass.set("")



    #     Search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from teacher where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


    # ==================== Genrate Data set or take photo samples ============================
    """
    def genrate_dataset(self):
        self.pattern_pasw = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
        self.pasw = re.match(self.pattern_pasw, self.var_pass.get())
        self.pattern_phone = r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
        self.Phone = re.match(self.pattern_phone, self.var_contact.get())
        self.pattern_email = r"^[A-Za-z]+[-_$.A-Za-z]*[0-9]*@[A-Za-z]*\.[A-Za-z]+$"
        self.Email = re.match(self.pattern_email, self.var_email.get())
        self.entered_otp = self.var_otp.get()

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.Phone or self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter proper phone number!", parent=self.root)
        elif not self.Email or self.var_email.get() == "":
            messagebox.showerror("Error!", "Please enter proper email!", parent=self.root)
        elif self.var_pass.get() == "":
            messagebox.showerror("Error", "Enter the password", parent=self.root)
        elif self.var_confpass.get() == "":
            messagebox.showerror("Error", "Confirm the password", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same", parent=self.root)
        elif not self.pasw:
            messagebox.showerror("Error","A password contains at least eight characters, including at least one number and includes both lower and uppercase letters and special characters, for example #, ?, !",
                                 parent=self.root)
        elif self.var_checkbtn.get() == 0:
            messagebox.showerror("Error", "Please agree the feiled details", parent=self.root)
        elif not self.entered_otp:
            messagebox.showerror("Error", "Please enter the OTP.", parent=self.root)

        else:
            try:
                take = messagebox.askyesno("Update", "Do you want to take a photo sample", parent=self.root)
                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from teacher")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update teacher set fname=%s,lname=%s,contact=%s,email=%s,securityQ=%s,securityA=%s,password=%s where email=%s",
                (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                    # ================= Load predifined data on face frontals from opencv  ===============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor=1.3
                        # Minimum Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", "Generating data sets complited!!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                """
    def fetch_student_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                       database="face_recognizer")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT fname, lname, contact, email, securityQ, securityA, password FROM teacher")
            student_data = cursor.fetchall()
            return student_data
        finally:
            conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = Teacher(root)
    root.mainloop()