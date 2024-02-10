from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from Admin import Admin
import smtplib
from email.message import EmailMessage
from registration import Register
from attendance import Attendance


def main():
    win=Tk()
    app=Login_Admin(win)
    win.mainloop()

class Login_Admin:
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
        lbl_img1=Label(self.root,image=self.photoimage1,bg='black',borderwidth=0)
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
        lbl_img1 = Label(self.root,image=self.photoimage2, bg='black', borderwidth=0)
        lbl_img1.place(x=550, y=295, width=30, height=30)

        img3 = Image.open(r"college_images\login-icon-3060.png")  # login-icon-3039.gif
        img3 = img3.resize((30, 30), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img1 = Label(self.root,image=self.photoimage3, bg='black', borderwidth=0)
        lbl_img1.place(x=550, y=368, width=30, height=30)

        # ============================Buttons======================================

        # Login button
        loginbtn= Button(frame,text="Login",command=self.adminLogin,font=("time new roman", 15, "bold"),relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # #register button
        # registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("time new roman", 10, "bold"),borderwidth=0,  relief=RIDGE, fg="red",
        #                   bg="black", activeforeground="white", activebackground="black")
        # registerbtn.place(x=15, y=350, width=160)

        # forgate password button
        # forgetpassbtn = Button(frame, text="Forget Password",command=self.forgate_password_window, font=("time new roman", 10, "bold"),borderwidth=0,  relief=RIDGE, fg="red",
        #                      bg="black", activeforeground="white", activebackground="black")
        # forgetpassbtn.place(x=10, y=380, width=160)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="pass", database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT email, password FROM admin WHERE email = %s",
                (self.var_email.get(),)
            )

            row = my_cursor.fetchone()
            if row is not None:
                email, stored_password = row
                entered_password = self.txtpass.get()

                if entered_password == stored_password:

                    self.new_window = Toplevel(self.root)
                    self.app = Student(self.new_window)
                    self.root.withdraw()

                else:
                    messagebox.showerror("Error", "Invalid password",parent=self.root)
            else:
                messagebox.showerror("Error", "Invalid user name and password",parent=self.root)

            conn.commit()
            conn.close()


    '''
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
    '''

    #=====================forgate pass=====================================================
    '''
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
    '''

    def adminLogin(self):
        self.new_window =Toplevel(self.root)
        self.app = Admin(self.new_window)
        self.root.withdraw()



if __name__ == "__main__":
    main()



