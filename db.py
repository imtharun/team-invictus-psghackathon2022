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
    cmd = "select rollno from student;"
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    data = []
    for i in res:
        data.append(i[0])
    return data


def scanstaff(tag):
    staff = 0
    cmd = "SELECT staffid FROM staff where uid=%s"
    mycursor.execute(cmd,(tag,))
    data = mycursor.fetchall()
    if(data == []):
        print("Please scan a staff id first")
    else:
        staff = data[0][0]
    return staff


def addattendance(tag,curr_staff):
    cmd = "SELECT rollno FROM student where uid=%s"
    mycursor.execute(cmd,(tag,))
    data = mycursor.fetchall()
    rollno = data[0][0]
    insertnow(rollno)
    mydb.commit()


def insertnow(roll):
    current_time = now.strftime("%H:%M:%S")
    colnm = 0
    today830 = now.replace(hour=8, minute=30, second=0, microsecond=0)
    today920 = now.replace(hour=9, minute=20, second=0, microsecond=0)
    today930 = now.replace(hour=9, minute=30, second=0, microsecond=0)
    today110 = now.replace(hour=10, minute=10, second=0, microsecond=0)
    today1030 = now.replace(hour=10, minute=30, second=0, microsecond=0)
    today1120 = now.replace(hour=11, minute=20, second=0, microsecond=0)
    today1210 = now.replace(hour=12, minute=10, second=0, microsecond=0)
    today1340 = now.replace(hour=13, minute=40, second=0, microsecond=0)
    today1430 = now.replace(hour=14, minute=30, second=0, microsecond=0)
    today1520 = now.replace(hour=15, minute=20, second=0, microsecond=0)
    today1530 = now.replace(hour=15, minute=13, second=0, microsecond=0)
    today1620 = now.replace(hour=16, minute=20, second=0, microsecond=0)
    today1715 = now.replace(hour=17, minute=15, second=0, microsecond=0)

    if(now>today830 and now<today920):
        colnm="1st"
    if(now>today930 and now<today110):
        colnm="2nd"
    if(now>today1030 and now<today1120):
        colnm="3rd"
    if(now>today1120 and now<today1210):
        colnm="4th"
    if(now>today1340 and now<today1430):
        colnm="5th"
    if(now>today1430 and now<today1520):
        colnm="6th"
    if(now>today1530 and now<today1620):
        colnm="7th"
    if(now>today1620 and now<today1715):
        colnm="8th"
    cmd = "update "+str(d)+" set "+colnm+" = 1 where rollno="+str(roll)+";"
    mycursor.execute(cmd)
    mydb.commit()


try:
    mydb = mysql.connector.connect(host=details.host,user=details.uname,password=details.upass,database=details.database)
    mycursor = mydb.cursor(buffered=True)

except:
    print("Error connecting database")
