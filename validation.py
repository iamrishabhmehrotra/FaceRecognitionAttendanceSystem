a="shreesh"
b="Shreesh"
if a==b:
    print("yess")
else:
    print("No")

    open_main = messagebox.askyesno("YesNo", "Access only admin!")
    if open_main:
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)
        self.root.withdraw()

        app_password = "vslnaiaddetaejsr"  # Replace with your app password

        email = "sender@gmail.com"  # Replace with the sender's email address

        subject = "Allert Login Notification"
        message = "Face Recognition Student Management\n\n\nLogin to your account was successful.\nSuccessfully login into Face Recognition Student Menagement\n\n(If these is not you then immediatly report in admin office\nChange your userid and password also change Security question)"

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

        else:
        if not open_main:
            return