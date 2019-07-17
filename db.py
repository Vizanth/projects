import cx_Oracle 
import re
con=cx_Oracle.connect("vizuu/hq@127.0.0.1/XE")
cur=con.cursor()
class UserError(Exception):
    def Error(self):
        print("User already Exist")
def login():
    usm=fun7()
    pasw=fun8()
    cur.execute("select * from useid3 where rollno='" + usm +"' and password='" + pasw +"'")
    login_data=cur.fetchall()
    print(login_data)
    if login_data == []:
        print("You need  user id")
        newuser()
    else:
        while(True):
            print("1.ADD\n2.DELETE\n3.SEARCH\n4.MODIFY\n5.Display")
            print("*"*20)
            print("--"*30)
            ch=int(input("Enter the choice="))
            if ch==1:
                add()
            elif ch==2:
                delete()
            elif ch==3:
                search()
            elif ch==4:
                modify()
            elif ch==5:
                display()
            else:
                print("(((  Successfully Stored in DataBase Oracle  )))")
                break
def newuser():
    try:
        name = re.match('[A-Z][a-z]{10}$',input("Enter the name within 10 characters="))
        while name == None:
            name = re.match('[A-Z||a-z]{10}$',input("Enter the name within 10 characters="))
        rollno =re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the rollno="))
        while rollno == None:
            rollno =re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the rollno="))
        email =re.match('[a-z,.,0-9]+[@]{1}[a-z]+[.][a-z]{3}',input("Enter the email="))
        while name == None:
            email =re.match('[a-z]+[.]{1}[a-z,0-9]+[@]{1}[a-z]+[.][a-z]{3}',input("Enter the email="))
        college = re.match('[A-Z,a-z]{3}$',input("Enter the college within 3 characters="))
        while college==None:
            college =re.match('[A-Z,a-z]{3}$',input("Enter the college within 3 characters="))
        us=re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the userid="))
        while us==None:
            us=re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the userid="))
        ps=re.match('[0-9]{8}$',input("Enter the password="))
        while ps==None:
            ps=re.match('[0-9]{8}$',input("Enter the password as DOB only numbers="))
        print("Please check given info. correct or Not")
        print(name.group(0),'\n',rollno.group(0),'\n',email.group(0),'\n',college.group(0),'\n',us.group(0),'\n',ps.group(0))
        in_data={"1":name.group(0),"2":rollno.group(0),"3":email.group(0),"4":college.group(0),"5":us.group(0),"6":ps.group(0)}
        cur.execute("insert into useid3 values(:1,:2,:3,:4,:5,:6)",in_data)
        con.commit()
        print("User Login Created")
        login()
    except UserError as us:
        us.Error()
        
def add():
    code=fun1()
    name=fun2()
    year=fun3()
    city=fun4()
    rate=fun5()
    cors_con=fun6()
    input_data={
                "college_code":code,
                "college_name":name,
                "est_year":year,
                "city":city,
                "rate":rate,
                "course_count":cors_con
                }
    cur.execute("insert into tncollege3 values(:college_code, :college_name, :est_year, :city, :rate, :course_count)",input_data)
    con.commit()
    print("Inserted")
def delete():
    code1=fun1()
    chg={"clg_code1":code1}
    cur.execute("delete from tncollege3 where college_code=(:clg_code1)",chg)
    con.commit()
    print("Deletion completed")
def search():
    code2=fun1()
    chg1={"clg_code2":code2}
    cur.execute("select * from tncollege3 where college_code=(:clg_code2)",chg1)
    items=cur.fetchone()
    print(list(items))
    con.commit()
def modify():
    print("$"*20)
    print("1.Code\n2.college_name\n3.Established_year\n4.City\n5.Rating\n6.Course_count")
    print("$"*20)
    while(True):
        ch1=int(input("Enter the modify choice="))
        if ch1==1:
            code3=fun1()
            print("///// Enter the clg_code to be change /////")
            code4=fun1()
            chg2={"clg_code3":code3,
                          "clg_code4":code4
                          }
            cur.execute("update tncollege3 set college_code=(:clg_code4) where college_code=(:clg_code3)",chg2)
            print("*** UPDATION OF CLG_CODE SUCCESSFULL ***")
            con.commit()
        elif ch1==2:
            code4=fun1()
            print("///// Enter the clg_name to be change /////")
            name1=fun2()
            chg3={"clg_code3":code4,
                      "clg_name1":name1
                          }
            cur.execute("update tncollege3 set college_name=(:clg_name1) where college_code=(:clg_code3)",chg3)
            print("*** UPDATION OF CLG_NAME SUCCESSFULL ***")
            con.commit()
        elif ch1==3:
            code5=fun1()
            print("///// Enter the Year to be change /////")
            year1=fun3()
            chg2={"clg_code5":code5,
                          "clg_year1":year1
                          }
            cur.execute("update tncollege3 set establised_year=(:clg_year1) where college_code=(:clg_code5)",chg2)
            print("*** UPDATION OF YEAR SUCCESSFULL ***")
            con.commit()
        else:
            print("\n""&&  MODIFY COMPLETE &&""\n")
            break

def display():
    cur.execute("select * from tncollege3 order by college_code")
    items1=cur.fetchall()
    print(items1)
    
def fun1():
    c1=re.match('^[a-z][a-z][0-9]{3}$',input("Enter the clg_code="))
    while c1==None:
        c1=re.match('^[a-z]{2}[0-9]{3}$',input("Enter the clg_code="))
    return c1.group(0)
def fun2():
    c3=re.match('^[A-Z][a-z]{2}$',input("Enter the clg_name="))
    while c3==None:
        c3=re.match('^[A-Z][a-z]{2}$',input("Enter the clg_name="))
    return c3.group(0)
def fun3():
    c5=re.match('^(1|2)[0-9]{3}$',input("Enter the year="))
    while c5==None:
        c5=re.match('^[1-2][0-9]{3}$',input("Enter the year="))
    return int(c5.group(0))
def fun4():
    c7=re.match('^[A-Z][a-z]{2}$',input("Enter the city="))
    while c7==None:
        c7=re.match('^[A-Z][a-z]{2}$',input("Enter the city="))
    return c7.group(0)
def fun5():
    c9=re.match('^[0-9].[0-9]$',input("Enter the rating out of 10="))
    while c9==None:
       c9=re.match('^[0-9].[0-9]$',input("Enter the rating out of 10=")) 
    return float(c9.group(0))
def fun6():
    c11=re.match('^[1-9][0-9]*$',input("Enter the count="))
    while c11==None:
       c11=re.match('^[1-9][0-9]*$',input("Enter the count=")) 
    return int(c11.group(0))
def fun7():
    us=re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the userid="))
    while us==None:
        print("Plz check userid nd re-enter !!!")
        us=re.match('^[1-9][1-9][A-Z,a-z]{1}[1-9]{3}$',input("Enter the userid="))
    return us.group(0)
def fun8():
    ps=re.match('[0-9]{8}$',input("Enter the password="))
    while ps==None:
        print("Please check the password !!!")
        ps=re.match('[1-9]{8}$',input("Enter the password="))
    return ps.group(0)

print("Suceesful")
print("*"*20)
print("____Student College Rating Updation____")
print("1.USER LOGIN\t2.NEW USER\t")
ch1=int(input("Enter the choice="))
if ch1 == 1:
    try:
        cur.execute(""" create table useid3(name varchar2(20),rollno varchar2(10),gmail varchar2(40),college varchar2(4),username varchar2(10),password varchar2(8))""")
        cur.execute(""" create table tncollege3(college_code varchar2(20),college_name varchar2(20),establised_year number,city varchar2(20),rating number,no_course_count number)""")
        print("Login Table created")
        login()
    except:
        login()
elif ch1 == 2:
    newuser()
con.commit()
cur.close()
con.close()

