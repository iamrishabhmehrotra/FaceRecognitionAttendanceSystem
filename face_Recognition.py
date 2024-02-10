from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2


class face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title

        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Top Image
        img_Top = Image.open(
            r"college_images\istockphoto.jpg")
        img_Top = img_Top.resize((670, 600), Image.Resampling.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=670, height=600)

        # Bottom Image
        img_bottom = Image.open(
            r"college_images\face_recog_right.jpg")
        img_bottom = img_bottom.resize((670, 600), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=665, y=45, width=670, height=600)

        # button train Data
        b1 = Button(f_lbl, text="Face Recognition", cursor="hand2",command=self.face_recog,
                    font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1.place(x=228, y=530, width=200, height=40)

        quit_button = Button(f_lbl, text="Quit", command=self.quit_app,
                                font=("times new roman", 15, "bold"), bg="red", fg="white")
        quit_button.place(x=450, y=530, width=100, height=40)

        #===================attendence============================================

    def quit_app(self):
        # Function to quit the application
        self.root.destroy()

    # def mark_attendence(self,i,r,n,d):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDataLiist=f.readlines()
    #         name_list=[]
    #         last_date = ""
    #
    #         if myDataLiist:
    #             last_entry = myDataLiist[-1].split(",")
    #             last_date = last_entry[-2] if last_entry else ""
    #
    #         for line in myDataLiist:
    #             entry=line.split(",")
    #             if entry[0]:
    #                 name_list.append(entry[0])
    #             else:
    #                 name_list.append(entry[1])
    #
    #         now = datetime.now()
    #         d1 = now.strftime("%d/%m/%Y")
    #         dtString = now.strftime("%H:%M:%S")
    #
    #         count=0
    #         if (i not in name_list) and  (r not in name_list) and (d not in name_list):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             if count!=1:
    #                 f.writelines(f"\nStudentID,Roll_No,Name,Department,Timing,Date,Status")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")
    #
    #         elif (r in name_list)and (i in name_list) and (d1 != last_date):  # Check if Roll_No is present and date has changed
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")

    def mark_attendence(self, i, r, n, d):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="pass",
                database="face_recognizer"
            )

            cursor = conn.cursor()

            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")

            # Check if an attendance record already exists for the student and current date
            query = "SELECT * FROM attendance WHERE StudentID = %s AND Date = %s"
            values = (i, d1)

            cursor.execute(query, values)
            existing_record = cursor.fetchone()

            if not existing_record:
                # Insert attendance record if no record exists for the student and date
                insert_query = "INSERT INTO attendance (StudentID, Roll_No, Name, Department, Time, Date, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                insert_values = (i, r, n, d, dtString, d1, "present")

                cursor.execute(insert_query, insert_values)
                conn.commit()
                print("Attendance marked successfully.")

            cursor.close()
            conn.close()

        except Exception as e:
            print("Error:", e)

        # =======================Face recognition=================================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="pass",
                                               database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n = "+".join(n)
                # n=f"{+}{n}"

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                # r=f"{+}{r}"

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                # d=f"{+}{d}"

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break

            key = cv2.waitKey(1)

            # Exit the loop and close the application if the spacebar (' ') key is pressed
            if key == ord(' '):
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_Recognition(root)
    root.mainloop()
