from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",20,"bold"),bg="lightgreen",fg="Blue")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        # img_top=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re2.jpg")
        # img_top = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re2.jpg")
        img_top = Image.open(r"Images\re2.jpg")
        img_top=img_top.resize((1366, 700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=650)
        
        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="green",fg="white")
        b1_1.place(x=500,y=450,width=300,height=150)
        
        # img_bottom=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_bottom=img_bottom.resize((1366, 300),Image.LANCZOS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=390,width=1366,height=300)
        
    def train_classifier(self):
        # data_dir=(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\data")
        # data_dir = (r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\data")
        data_dir = (r"data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        speak_va("Training datasets completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        # self.root.destroy()



    
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()