from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import re
import cv2
import os
import csv
from tkinter import filedialog

from mysql.connector import MySQLConnection, CMySQLConnection
from mysql.connector.pooling import PooledMySQLConnection

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=============== Self Variable ===================================

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance= StringVar()
        self.var_com_search = StringVar()

        # banner Image

        # First Banner Image
        img = Image.open(r"college_images\FirstBannerImg.jpg")
        img = img.resize((640, 80), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=640, height=80)

        # Second Banner Image
        img1 = Image.open(r"college_images\thiredbannerimg.jpg")
        img1 = img1.resize((640, 80), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=640, y=0, width=640, height=80)

        # Background Image
        img3 = Image.open(r"college_images\background.jpg")
        img3 = img3.resize((1366, 800), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=70, width=1366, height=800)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=25)

        # Main Frame

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=30, width=1265, height=540)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=620, height=515)

        # left side banner image

        img_left = Image.open(
            r"college_images\secondfacerecognitionbaner.png")
        img_left = img_left.resize((640, 150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=150)

        # Attendance in left frame
        left_inside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Data",
                                       font=("times new roman", 12, "bold"))
        left_inside_frame.place(x=5, y=150, width=605, height=330)

        # Labels and entry

        # attendance Id
        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 12, "bold"),
                                   bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,
                                       font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5)

        # Student roll

        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"),
                           bg="white")
        roll_label.grid(row=0, column=2,padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,
                               font=("times new roman", 12, "bold"))
        atten_roll.grid(row=0,column=3, pady=8)

        # student name
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,
                               font=("times new roman", 12, "bold"))
        atten_name.grid(row=1, column=1,  pady=8)

        # Department

        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,
                               font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,
                               font=("times new roman", 12, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # date
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                               font=("times new roman", 12, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # attendance

        attendancelabel = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        attendancelabel.grid(row=3, column=0, pady=8)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"),
                                         state="readonly", width=18,textvariable=self.var_atten_attendance)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)


        # Button Frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=220, width=590, height=37)

        # save button

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv ,width=15, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=2)

        # update button
        update_btn = Button(btn_frame, text="Export",command=self.exportCsv, width=15,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1, padx=0)

        # delete button
        delete_btn = Button(btn_frame, text="Update", command=self.update_data, width=15,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(btn_frame, text="Reset", width=15,command=self.reset_data,
                           font=("times new roman", 12, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)







        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=635, y=10, width=620, height=515)

        # Search frame

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=10, width=600, height=75)

        # Search selct
        self.var_com_search = StringVar()

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="Red",
                             fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, textvariable=self.var_com_search,
                                    font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Date", "StudentID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(Search_frame, textvariable=self.var_search, width=15,
                                 font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        # search button
        search_btn = Button(Search_frame, command=self.search_data, text="Search", width=12,
                            font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        # show all button
        showAll_btn = Button(Search_frame, command=self.fetch_data, text="Show All", width=12,
                             font=("times new roman", 10, "bold"), bg="blue",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=3)



        # Table frame

        # table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
        #                           font=("times new roman", 12, "bold"))
        # table_frame.place(x=5, y=3, width=600, height=480)

        #===========================scroll table==========================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=150, width=600, height=265)

        # Scroll bar bottom and horizontal scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_Y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Table content
        self.AttendanceReporttable = ttk.Treeview(table_frame, column=(
            'id','roll','name','department','time','date','attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_Y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReporttable.xview)
        scroll_Y.config(command=self.AttendanceReporttable.yview)

        # vilibale of table content
        self.AttendanceReporttable.heading("id", text="StudentID")
        self.AttendanceReporttable.heading("roll", text="Roll")
        self.AttendanceReporttable.heading("name", text="Name")
        self.AttendanceReporttable.heading("department", text="Department")
        self.AttendanceReporttable.heading("time", text="Time")
        self.AttendanceReporttable.heading("date", text="Date")
        self.AttendanceReporttable.heading("attendance", text="Attendance")
        self.AttendanceReporttable["show"] = "headings"

        # Adgestement of table content
        # 'dep','cursor','year','sem','id','name','div','roll','gender','dob','email','gender','phone','address','teacher','photo'
        self.AttendanceReporttable.column("id", width=100)  # do it for all names
        self.AttendanceReporttable.column("roll", width=100)
        self.AttendanceReporttable.column("name", width=100)
        self.AttendanceReporttable.column("department", width=100)
        self.AttendanceReporttable.column("time", width=100)
        self.AttendanceReporttable.column("date", width=100)
        self.AttendanceReporttable.column("attendance", width=100)
        self.AttendanceReporttable.pack(fill=BOTH, expand=1)
        self.AttendanceReporttable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # =======================fatch data==================================

    def fetchData(self, rows):
        self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
        for i in rows:
            self.AttendanceReporttable.insert("",END,values=i)

    #i import csv
    # def importCsv(self):
    #     global mydata
    #     mydata.clear()
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchData(mydata)



        # update function
    def update_data(self):
        # Check if all required fields are filled
        if (
                self.var_atten_id.get() == ""
                or self.var_atten_roll.get() == ""
                or self.var_atten_name.get() == ""
                or self.var_atten_dep.get() == ""
                or self.var_atten_attendance.get() == "Status"
                or self.var_atten_date.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required!", parent=self.root)
        else:
            try:
                # Confirm the update with a message box
                Update = messagebox.askyesno("Update", "Do you want to update these details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="pass",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()

                    # Update the record using SQL UPDATE statement
                    update_query = "UPDATE attendance SET Roll_No=%s, Name=%s, Department=%s, Time=%s, Date=%s, Status=%s WHERE StudentID=%s AND Date=%s"
                    data = (
                        self.var_atten_roll.get(),
                        self.var_atten_name.get(),
                        self.var_atten_dep.get(),
                        self.var_atten_time.get(),
                        self.var_atten_date.get(),
                        self.var_atten_attendance.get(),
                        self.var_atten_id.get(),
                        self.var_atten_date.get(),
                    )
                    my_cursor.execute(update_query, data)
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", "Attendance details successfully updated", parent=self.root)

                    # Refresh the table with updated data
                    self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




    def importCsv(self):
        # Open a file dialog to select a CSV file
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)

        if fln:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="pass",
                                               database="face_recognizer")
                cursor = mydb.cursor()

                with open(fln, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    next(csvreader)  # Skip the header row if it exists
                    for row in csvreader:
                        StudentID, Roll_No, Name, Department, Time, Date, Status = row
                        # Use the data to construct an INSERT query and execute it
                        insert_query = "INSERT INTO attendance (StudentID, Roll_No, Name, Department, Time, Date, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        data = (StudentID, Roll_No, Name, Department, Time, Date, Status)
                        cursor.execute(insert_query, data)

                    mydb.commit()
                    mydb.close()

                    messagebox.showinfo("Success", "Data imported and added to the database successfully.")
                    self.fetch_data()  # Refresh the displayed data
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showinfo("Info", "No CSV file selected.")




    # export csv
    # def exportCsv(self):
    #     try:
    #         if len(mydata)<1:
    #             messagebox.showerror("No Data","No Data found to export",parent=self.root)
    #             return False
    #         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
    #         with open(fln,mode="w",newline="") as myfile:
    #             exp_write=csv.writer(myfile,delimiter=",")
    #             for i in mydata:
    #                 exp_write.writerow(i)
    #             messagebox.showinfo("Data Exported","Your data exported to"+os.path.basename(fln)+"Successfully")
    #
    #     except Exception as es:
    #         messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def exportCsv(self):
        selected_items = self.AttendanceReporttable.selection()

        if len(selected_items) > 0:
            # Export only selected rows
            selected_data = []
            for item in selected_items:
                item_data = self.AttendanceReporttable.item(item, 'values')
                selected_data.append(item_data)

            # Define the file name for the selected data
            file_name = "selected_data.csv"

            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["StudentID", "Roll_No", "Name", "Department", "Time", "Date", "Status"])  # Header

                for data in selected_data:
                    writer.writerow(data)

            messagebox.showinfo("Data Exported", "Selected data has been exported to selected_data.csv successfully.")
        else:
            # Export all visible rows
            all_data = []
            for item in self.AttendanceReporttable.get_children():
                item_data = self.AttendanceReporttable.item(item, 'values')
                all_data.append(item_data)

            # Define the file name for all data
            file_name = "all_data.csv"

            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["StudentID", "Roll_No", "Name", "Department", "Time", "Date", "Status"])  # Header

                for data in all_data:
                    writer.writerow(data)

            messagebox.showinfo("Data Exported", "All visible data has been exported to all_data.csv successfully.")


    def get_cursor(self, event=""):
        cursor_rows = self.AttendanceReporttable.focus()
        content = self.AttendanceReporttable.item(cursor_rows)
        data = content["values"]

        if data:  # Check if data is not empty
            self.var_atten_id.set(data[0])
            self.var_atten_roll.set(data[1])
            self.var_atten_name.set(data[2])
            self.var_atten_dep.set(data[3])
            self.var_atten_time.set(data[4])
            self.var_atten_date.set(data[5])
            self.var_atten_attendance.set(data[6])
        else:
            # Handle the case when data is empty, e.g., when no row is selected.
            # You can clear the form fields or show an error message.
            self.reset_data()  # Example: Clear the form fields





    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("Status")
        self.var_com_search.set("Select")
        self.var_search.set("")




    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from attendance where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
                    for i in data:
                        self.AttendanceReporttable.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



    #fatch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                       database="face_recognizer")

        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendance")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
            for i in data:
                self.AttendanceReporttable.insert("", END, values=i)
            conn.commit()
            conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()