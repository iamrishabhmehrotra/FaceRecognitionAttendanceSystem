from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from login import Login_Window
from tkinter import messagebox
import mysql.connector
import re
import random
import smtplib



class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        self.generated_otp = None
        # ==========================variables======================================

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






        bg = Image.open(r"college_images\login_bg.jpg")
        bg = bg.resize((1366, 710), Image.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        lbl_bg = Label(self.root, image=self.photoimgbg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        # ====================in frame========================================

        frame = Frame(self.root, bg="white")
        frame.place(x=250, y=80, width=800, height=490)

        register_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",15,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # =========================entry feels=======================================

        #-------------------------------1 row

        fname=Label(frame,text="First Name",font=("time new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame, text="Last Name", font=("time new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)


        # ----------------------------------------- row 2

        contact = Label(frame, text="Contact", font=("time new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("time new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("time new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        #--------------------------------------row 3

        sequrity_Q = Label(frame, text="Security Question", font=("time new roman", 15, "bold"), bg="white")
        sequrity_Q.place(x=50, y=240)

        self.combo_sequrity_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly", width=20)
        self.combo_sequrity_Q["values"] = ("Select", "Your Birth Place", "Your Wife/Husband Name", "Your Pet Name", "Your Netive Place")
        self.combo_sequrity_Q.current(0)
        self.combo_sequrity_Q.place(x=50,y=270,width=250)

        sequrity_A = Label(frame, text="Security Answer", font=("time new roman", 15, "bold"), bg="white")
        sequrity_A.place(x=370, y=240)

        self.txt_sequrity = ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman", 15, "bold"))
        self.txt_sequrity.place(x=370, y=270, width=250)

        # ----------------------------------------- row 4

        pswd = Label(frame, text="Password",font=("time new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass,font=("time new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("time new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("time new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #--------------------------------------------------row 5
        # ----------------------------------------- row 5 (Added for OTP)

        otp_label = Label(frame, text="OTP", font=("time new roman", 15, "bold"), bg="white")
        otp_label.place(x=50, y=380)

        self.txt_otp = ttk.Entry(frame,textvariable=self.var_otp, font=("time new roman", 15, "bold"))
        self.txt_otp.place(x=50, y=410, width=250)

        self.generate_otp_button = Button(frame, text="Generate OTP",command=self.generate_otp)
        self.generate_otp_button.place(x=320, y=410)

        #=========================Check Button=========================================

        checkbtn=Checkbutton(frame,variable=self.var_checkbtn,text="I Agree The Details",font=("time new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=445)

        #===================Buttons=======================================================

        img = Image.open(r"college_images\register-button-png-18462.png")
        img = img.resize((240, 150), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(frame, image=self.photoimg,borderwidth=0, cursor="hand2",command=self.register_data,font=("time new roman", 15, "bold"),bg="white")
        b1.place(x=430, y=400, width=150,height=50)

        img1 = Image.open(r"college_images\login-button-png-18020.png")
        img1 = img1.resize((180, 90), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b2 = Button(frame, image=self.photoimg1, borderwidth=0, cursor="hand2",command=self.login_page, font=("time new roman", 15, "bold"),bg="white")
        b2.place(x=600, y=400, width=150, height=50)








        #======================Functions=================================================


    def generate_otp(self):
        email_address = self.txt_email.get()  # Get the email address

        if not email_address:
            messagebox.showerror("Error", "Please enter your email address before generating OTP.",parent=self.root)
        self.generated_otp = random.randint(1000, 9999)
        email_address = self.txt_email.get()  # Get the email address

        # Call the function to send OTP to the email
        self.send_otp_to_email(email_address, self.generated_otp)



    def send_otp_to_email(self, email, otp):
        try:
            app_password = "vslnaiaddetaejsr"  # Replace with your app password

            # Set up the email server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Login using the app password
            server.login("bibmarkets@gmail.com", app_password)

            # Compose the email
            subject = "Your OTP Code"
            message = f"Your OTP code is: {otp}"
            body = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail("bibmarkets@gmail.com", email, body)

            # Close the server connection
            server.quit()

            # messagebox.showinfo("OTP Sent", "An OTP has been sent to your email.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}",parent=self.root)




    def register_data(self):

        self.pattern_pasw=r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
        self.pasw=re.match(self.pattern_pasw,self.var_pass.get())
        self.pattern_phone = r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
        self.Phone = re.match(self.pattern_phone, self.var_contact.get())
        self.pattern_email = r"^[A-Za-z]+[-_$.A-Za-z]*[0-9]*@[A-Za-z]*\.[A-Za-z]+$"
        self.Email = re.match(self.pattern_email, self.var_email.get())
        self.entered_otp = self.var_otp.get()

        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.Phone or self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter proper phone number!", parent=self.root)
        elif not self.Email or self.var_email.get() == "":
            messagebox.showerror("Error!", "Please enter proper email!", parent=self.root)
        elif self.var_pass.get()=="":
            messagebox.showerror("Error","Enter the password",parent=self.root)
        elif self.var_confpass.get()=="":
            messagebox.showerror("Error", "Confirm the password",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same",parent=self.root)
        elif  not self.pasw:
            messagebox.showerror("Error","A password contains at least eight characters, including at least one number and includes both lower and uppercase letters and special characters, for example #, ?, !",parent=self.root)
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please agree the feiled details",parent=self.root)
        elif not self.entered_otp:
            messagebox.showerror("Error", "Please enter the OTP.",parent=self.root)
        # elif self.var_email.get() and
        else:
            if int(self.entered_otp) == self.generated_otp:
                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist, Please try another email",parent=self.root)
                else:
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
                conn.close()
                messagebox.showinfo("Success", "Registered successfully!",parent=self.root)
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Incorrect OTP. Registration failed.",parent=self.root)



        # ====================================Linking==============================
    def login_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_Window(self.new_window)
        self.root.destroy()