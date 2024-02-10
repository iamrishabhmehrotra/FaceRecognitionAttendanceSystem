import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from login import Login_Window
from tkinter import messagebox
import mysql.connector
from loginAdmin import Login_Admin
import re
import cv2
import random
import smtplib
from main import Face_Recognition_System
from email.message import EmailMessage
from time import sleep


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #variable
        self.var_email=StringVar()
        self.var_pass=StringVar()

        bg=Image.open(r"college_images\login_bg.jpg")
        bg = bg.resize((1366, 710), Image.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        lbl_bg=Label(self.root,image=self.photoimgbg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=140,width=340,height=450)

        img1=Image.open(r"college_images\login-icon-3060.png") #login-icon-3039.gif
        img1=img1.resize((70,70),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        lbl_img1.place(x=640,y=175,width=70,height=70)

        get_str=Label(frame,text="Get Started",font=("time new roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=96,y=105)

        # label username
        username=lbl=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=Entry(frame,textvariable=self.var_email,font=("time new roman",15,"bold"))
        self.txtuser.place(x=60,y=187,width=240)

        #label password
        password = lbl = Label(frame, text="Password", font=("time new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=228)

        self.txtpass = Entry(frame, textvariable=self.var_pass,font=("time new roman", 15, "bold"))
        self.txtpass.place(x=60, y=260, width=240)


        # ==========================================================

        img2 = Image.open(r"college_images\login-icon-3060.png")  # login-icon-3039.gif
        img2 = img2.resize((30, 30), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img1 = Label(image=self.photoimage2, bg='black', borderwidth=0)
        lbl_img1.place(x=550, y=295, width=30, height=30)

        img3 = Image.open(r"college_images\login-icon-3060.png")  # login-icon-3039.gif
        img3 = img3.resize((30, 30), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img1 = Label(image=self.photoimage3, bg='black', borderwidth=0)
        lbl_img1.place(x=550, y=368, width=30, height=30)

        # ============================Buttons======================================

        # Login button
        loginbtn= Button(frame,text="Login",command=self.login,font=("time new roman", 15, "bold"),relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("time new roman", 10, "bold"),borderwidth=0,  relief=RIDGE, fg="red",
                          bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forgate password button
        forgetpassbtn = Button(frame, text="Forget Password",command=self.forgate_password_window, font=("time new roman", 10, "bold"),borderwidth=0,  relief=RIDGE, fg="red",
                             bg="black", activeforeground="white", activebackground="black")
        forgetpassbtn.place(x=10, y=380, width=160)

        # forgate password button
        adminlogin = Button(frame, text="Admin Login", command = self.adminLogins ,
                               font=("time new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="red",
                               bg="black", activeforeground="white", activebackground="black")
        adminlogin.place(x=10, y=410, width=160)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="pass", database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT email, password FROM register WHERE email = %s",
                    (self.var_email.get(),)
                )

                row = my_cursor.fetchone()
                if row is not None:
                    email, stored_password = row
                    entered_password = self.txtpass.get()

                    if entered_password == stored_password:
                        open_main = messagebox.askyesno("YesNo", "Access only admin!",parent=self.root)
                        if open_main:
                            self.new_window = Toplevel(self.root)
                            self.app = Face_Recognition_System(self.new_window)
                            self.root.withdraw()

                            app_password = "vslnaiaddetaejsr"  # Replace with your app password

                            email = "sender@gmail.com"  # Replace with the sender's email address

                            subject = "Allert Login Notification"
                            message = "Face Recognition Student Management\n\n\nLogin to your account was successful.\nSuccessfully login into Face Recognition Student Menagement\n\n(If these is not you then immediatly report in admin office\nChange your password)"

                            msg = EmailMessage()
                            msg.set_content(message)
                            msg["Subject"] = subject
                            msg["From"] = "bibmarkets@gmail.com"  # Replace with your email address
                            msg["To"] = self.var_email.get()  # Replace with recipient's email address

                            server = smtplib.SMTP("smtp.gmail.com", 587)
                            server.starttls()
                            server.login("bibmarkets@gmail.com", app_password)
                            server.send_message(msg)
                            server.quit()
                        else:
                            if not open_main:
                                return

                        # Additional code for sending an email notification can go here
                    else:
                        messagebox.showerror("Error", "Invalid password",parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid user name and password",parent=self.root)

                conn.commit()
                conn.close()
            except mysql.connector.Error as e:
                # print(e)
                messagebox.showerror("Database Error", f"Error: {e}")


    #======================================reset========================================
    def reset_pass(self):
        if self.combo_sequrity_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_sequrity.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="pass", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value= (self.txtuser.get(),self.combo_sequrity_Q.get(),self.txt_sequrity.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get(),)
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Successfully","Your Password changed successfully",parent=self.root2)



    #=====================forgate pass=====================================================

    def forgate_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email to reset the password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="pass",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid user name!",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("time new roman", 10, "bold"),borderwidth=0,  relief=RIDGE, fg="red",
                             bg="black")
                l.place(x=0,y=10,relwidth=1,height=40)

                sequrity_Q = Label(self.root2, text="Security Question", font=("time new roman", 15, "bold"), bg="white")
                sequrity_Q.place(x=50, y=80)

                self.combo_sequrity_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly", width=20)
                self.combo_sequrity_Q["values"] = (
                "Select", "Your Birth Place", "Your Wife/Husband Name", "Your Pet Name", "Your Netive Place")
                self.combo_sequrity_Q.current(0)
                self.combo_sequrity_Q.place(x=50, y=110, width=250)

                sequrity_A = Label(self.root2, text="Security Answer", font=("time new roman", 15, "bold"), bg="white")
                sequrity_A.place(x=50, y=150)

                self.txt_sequrity = ttk.Entry(self.root2,
                                              font=("time new roman", 15, "bold"))
                self.txt_sequrity.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("time new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,
                                              font=("time new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                #shreesht99@gmail.com

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("time new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=100,y=300,width=150)










    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def adminLogins(self):
        self.new_window =Toplevel(self.root)
        self.app = Login_Admin(self.new_window)









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





if __name__ == "__main__":
    main()
