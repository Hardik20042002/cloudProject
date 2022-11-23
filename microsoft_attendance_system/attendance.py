import tkinter as tk
import csv
import cv2
import os
import numpy as np
from PIL import Image
import numpy as np
import pandas as pd
import datetime
import time
import glob
import shutil
import os

window = tk.Tk()
window.title("image capture")
window.geometry('920x720')


window.configure(background='light green')
window.grid_rowconfigure(1, weight=3)
window.grid_columnconfigure(1, weight=3)


def clear():
    std_name.delete(0, 'end')
    res = ""
    label4.configure(text=res)


def clear2():
    std_number.delete(0, 'end')
    res = ""
    label4.configure(text=res)


def takeImage():
    name = (std_name.get())
    Id = (std_number.get())
    if name.isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray,1.1, 1)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                # store each student picture with its name and id
                cv2.imwrite("ImagesAttendance\ " + name + '.' + "jpg",
                            gray)
                cv2.imshow('FACE RECOGNIZER', img)
                src_dir = "your/source/dir"
                dst_dir = "your/destination/dir"


            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # stop the camera when the number of picture exceed 50 pictures for each student
            if sampleNum > 0:
                break

        cam.release()
        cv2.destroyAllWindows()
        # print the student name and id after a successful face capturing
        res = 'Student details saved with: \n Matric number : '  ' and  Full Name: ' + name

        row = [Id, name]

        with open('studentDetailss.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        label4.configure(text=res)
    else:

        if name.isalpha():
            res = "Enter correct Matric Number"
            label4.configure(text=res)


def getImagesAndLabels(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

def cropimage():
    if __name__ == '__main__':
        name = (std_name.get())
        name1 = ".jpg"
        name2= name + name1
        path = r'C:\Users\piyush\Desktop\ms_project\FaceRecorgnitionProject\ImagesAttendance'
        #path = 'ImagesAttendance'
        # Read image
        im = cv2.imread(f'{path}/{name2}')

        # Select ROI
        r = cv2.selectROI(im)

        # Crop image
        imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        # Display cropped image

        cv2.imshow("Image", imCrop)
        path = r'C:\Users\piyush\Desktop\ms_project\FaceRecorgnitionProject\ImagesAttendance'

        cv2.imwrite(os.path.join(path,name2),imCrop)
        #cv2.imwrite(name ,imCrop)





label1 = tk.Label(window, background="light blue", fg="black", text="Name :", width=10, height=1,
                  font=('Helvetica', 16))
label1.place(x=183, y=140)
std_name = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_name.place(x=380, y=141)



label2 = tk.Label(window, background="light blue", fg="black", text="Matric Number :", width=14, height=1,
                  font=('Helvetica', 16))
label2.place(x=200, y=190)
std_number = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_number.place(x=380, y=191)

clearBtn1 = tk.Button(window, background="light blue", command=clear, fg="black", text="CLEAR", width=8, height=1,
                      activebackground="light blue", font=('Helvetica', 10))
clearBtn1.place(x=680, y=142)
clearBtn2 = tk.Button(window, background="light blue", command=clear2, fg="black", text="CLEAR", width=8,
                      activebackground="light blue", height=1, font=('Helvetica', 10))
clearBtn2.place(x=680, y=192)

label3 = tk.Label(window, background="light blue", fg="light blue", text="Notification", width=10, height=1,
                  font=('Helvetica', 20, 'underline'))
label3.place(x=420, y=255)
label4 = tk.Label(window, background="yellow", fg="black", width=55, height=4, font=('Helvetica', 14, 'italic'))
label4.place(x=195, y=305)

takeImageBtn = tk.Button(window, command=takeImage, background="yellow", fg="black", text="CAPTURE IMAGE",
                         activebackground="light blue",
                         width=15, height=3, font=('Helvetica', 12))
takeImageBtn.place(x=430, y=500)

cropimagebtn = tk.Button(window, command=cropimage, background="yellow", fg="black", text="CROP IMAGE",
                          activebackground="red",
                          width=15, height=3, font=('Helvetica', 12))
cropimagebtn.place(x=630, y=500)




window.mainloop()
