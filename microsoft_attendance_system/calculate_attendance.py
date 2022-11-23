import csv
from datetime import date
import os
from typing import TextIO

today = date.today()
d1 = today.strftime("%m/%d/%Y")


my_list=[]
print(d1)
f = open("studentDetailss.csv", 'r')
r = csv.reader(f, delimiter = ',')

for row in r :
    if row :
        my_list.append((row[1],'a',0,1))
f.close()



f = open("Attendance.csv", 'r')
r = csv.reader(f, delimiter = ',')
for row in r :
    if row:
        if d1==row[2] :
                for i in my_list :

                    if i[0]==row[0] :
                        my_list.remove(i)
f.close()

f = open("Attendance.csv", 'r')
r = csv.reader(f, delimiter = ',')
for row in r :
    if row:
        if d1==row[2] :
            my_list.append((row[0],'p',1,1))

f.close()

print(my_list)






my_list.clear()

f = open("percentage1.csv", 'r')
r = csv.reader(f, delimiter = ',')

for row in r :
    if row :
        my_list.append((row[0], row[1] ,int(row[2])+1 ,int(row[3])+1))
f.close()

f = open('percentage1.csv', 'w')
writer = csv.writer(f)
for i in my_list:
    if i[1] == 'p':
        writer.writerow((i[0],i[1],i[2]+1,i[3]+1))
    if i[1] == 'a':
        writer.writerow((i[0],i[1],i[2],i[3]+1))
f.close()

f = open('percentage.csv', 'r')
r = csv.reader(f, delimiter = ',')

my_attendance=[]
for i in my_list:
    p = int(i[2])
    d = int(i[3])
    pc =(p/d)*100
    my_attendance.append((i[0],p,d,pc))


print(my_attendance)


f = open('percentage.csv', 'w')
writer = csv.writer(f)
for i in my_attendance:
    writer.writerow((i[0],i[1],i[2],i[3]))