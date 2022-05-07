import mysql.connector
import dbconfig as details

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



try:
    mydb = mysql.connector.connect(host=details.host,user=details.uname,password=details.upass,database=details.database)
    mycursor = mydb.cursor()

except:
    print("Error connecting database")
