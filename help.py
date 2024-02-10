from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import smtplib
import ssl
import tkinter as tk
import re
import cv2
from email.message import EmailMessage
from tkinter import messagebox
from mysql.connector import MySQLConnection, CMySQLConnection
from mysql.connector.pooling import PooledMySQLConnection


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title

        title_lbl = Label(self.root, text="HELP DESK",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # bg Image
        img_Top = Image.open(
            r"college_images\background.jpg")
        img_Top = img_Top.resize((1366, 600), Image.Resampling.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=1366, height=600)

        # Help email
        dev_label = Label(f_lbl, text="Contact:Shreesht0@gmail.com", font=("times new roman", 15, "bold"), fg="blue",
                          bg="white")
        dev_label.place(x=580, y=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=250, y=80, width=800, height=490)


        # ==========================Variables======================================

        self.var_name=StringVar()
        self.var_email = StringVar()
        self.var_sub = StringVar()

        # =========================entry feels=======================================

        name = Label(frame, text="Name:", font=("time new roman", 20, "bold"), bg="white")
        name.place(x=180, y=55)

        name_entry = ttk.Entry(frame, textvariable=self.var_name, font=("time new roman", 15, "bold"))
        name_entry.place(x=280, y=60, width=280)

        #=============================email===========================================

        email = Label(frame, text="Email:", font=("time new roman", 20, "bold"), bg="white")
        email.place(x=180, y=125)

        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("time new roman", 15, "bold"))
        email_entry.place(x=280, y=130, width=280)

        #==============================Subject=========================================

        subject = Label(frame, text="Sub:", font=("time new roman", 20, "bold"), bg="white")
        subject.place(x=180, y=195)

        subject_entry = ttk.Entry(frame, textvariable=self.var_sub, font=("time new roman", 15, "bold"))
        subject_entry.place(x=280, y=200, width=280)

        #================================Message======================================

        message = Label(frame, text="Message:", font=("time new roman", 20, "bold"), bg="white")
        message.place(x=180, y=265)

        self.text_area = Text(frame, font=("times new roman", 15), wrap=WORD, borderwidth=1, relief="solid")
        self.text_area.place(x=280, y=300, width=280, height=170)

        img = Image.open(r"college_images\send.png")
        img = img.resize((70, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(frame, image=self.photoimg, borderwidth=0, cursor="hand2", command=self.submit_form,
                    font=("time new roman", 15, "bold"), bg="white")
        b1.place(x=580, y=400, width=70, height=70)

    def submit_form(self):
        self.pattern_email = r"^[A-Za-z]+[-_$.A-Za-z]*[0-9]*@[A-Za-z]*\.[A-Za-z]+$"
        self.Email = re.match(self.pattern_email, self.var_email.get())
        if self.var_name.get() == "" or self.var_email.get() == "" or self.text_area.get("1.0", "end-1c") == "":
            messagebox.showerror("Error", "All fields are required.",parent=self.root)
        elif not self.Email or self.var_email.get() == "":
            messagebox.showerror("Error!", "Please enter proper email!", parent=self.root)
        else:
            try:
                app_password = "vslnaiaddetaejsr"  # Replace with your app password

                email = "shreesht0@gmail.com"  # Replace with the recipient's email address

                subject = self.var_sub.get()
                message = f"""<html><body><b><h3><span style="color: red; background-color: yellow;">Face Recognition Student Management</span></h3></b><br><br><br>
                  <b>Name:</b> {self.var_name.get()}<br><br>
                  <b>From:</b> {self.var_email.get()}<br><br>
                  <b>Subject:</b> {self.var_sub.get()}<br><br>
                  <b>Message:</b><br>{self.text_area.get('1.0', 'end-1c')}</body></html>"""
                msg = EmailMessage()
                msg.set_content(message,subtype='html')
                msg["Subject"] = subject
                msg["From"] = self.var_email.get()   # Replace with your email address
                msg["To"] = "bibmarkets@gmail.com"

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("bibmarkets@gmail.com", app_password)
                server.send_message(msg)
                server.quit()

                messagebox.showinfo("Email Sent", "Email sent successfully.")
                self.reset()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
                self.reset()

    def reset(self):
        self.var_email.set(""),
        self.var_name.set(""),
        self.text_area.delete("1.0", tk.END),
        self.var_sub.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()