import mysql.connector
import dbconfig as details
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

d = today.strftime("%d%b%y")

def checktoday():
    try:
        cmd = "Select * from "+d
        mycursor.execute(cmd)
    
    except:
        print("Creating attenance table for today...")
        cmd = "create table "+d+"(rollno varchar(6),1st int,2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)"
        mycursor.execute(cmd)
        rollnos = getstudlist()
        for i in rollnos:
            cmd = "insert into "+d+" values (%s,null,null,null,null,null,null,null,null);"
            mycursor.execute(cmd,(i,))

        mydb.commit()



def getstudlist():
    cmd = "select rollno from student"
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    data = []
    for i in res:
        data.append(i[0])
    print(data)
    return data


def scanstaff(tag):
    staff = 0
    cmd = "SELECT staffid FROM staff where uid=%s"
    mycursor.execute(cmd,(tag,))
    data = mycursor.fetchall()
    print(data)
    if(data == []):
        print("Please scan a staff id first")
    else:
        staff = data[0][0]
    return staff


def addattendance(tag,curr_staff):
    if(curr_staff==0):
        cmd = "SELECT staffid FROM staff where uid=%s"
        mycursor.execute(cmd,(tag,))
        data = mycursor.fetchall()
        print(data)
        if(data == []):
            print("Please scan a staff id first")
        else:
            curr_staff = data[0][0]
            print(curr_staff)
        mydb.commit()
    
    else:
        cmd = "SELECT staffid FROM staff where uid=%s"
        mycursor.execute(cmd,(tag,))
        data = mycursor.fetchall()
        print(data)
        if(data == []):
            cmd = "SELECT rollno,sname FROM student where uid=%s"
            mycursor.execute(cmd,(tag,))
            data = mycursor.fetchall()
            rollno = data[0][0]
            sname = data[0][1]
            cmd = "insert into attendance values (%s,%s,%s,%s);"
            mycursor.execute(cmd,(rollno,curr_staff,sname,1,))
        else:
            curr_staff = data[0][0]
            print(curr_staff)
        mydb.commit()



def insertnow(roll):
    current_time = now.strftime("%H:%M:%S")
    colnm = 0
    cmd = "update "+d+" set "+colnm+" 1 where rollno="+roll+";"
    mycursor.execute(cmd)
    pass



try:
    mydb = mysql.connector.connect(host=details.host,user=details.uname,password=details.upass,database=details.database)
    mycursor = mydb.cursor()

except:
    print("Error connecting database")

checktoday()
getstudlist()