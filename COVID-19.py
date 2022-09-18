import mysql.connector
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="thamarai790",
    database="covid_19"
)

mycursor=mydb.cursor()
#********************************************#
#mycursor.execute("create database covid_19")

#mycursor.execute("create table coviddatas(COUNTRYNAME varchar(100),TOTALPOPLE int,NEWCASES int,DEATHCASES int,ACTIVECASES int,TOTALCASES int)")

def insert_studentdata():
    x=datetime.datetime.now()
    today=x.strftime("%A")
    print(today)
    this_month=x.strftime("%B")
    print(this_month)
    this_year=x.strftime("%Y")
    print(this_year)
    current_time=int(x.strftime("%H"))
    print(current_time)
    current_minitue=x.strftime("%M")
    print(current_minitue)
    print(f"{current_time}:{current_minitue}")
    date=date.today()
    print(date)


def insert_coviddatas():
    sql="insert into coviddatas(COUNTRYNAME,TOTALPOPLE,NEWCASES,DEATHCASES,ACTIVECASES,TOTALCASES) values (%s,%s,%s,%s,%s,%s)"
    COUNTRYNAME=input("enter name:")
    TOTALPOPLE=int(input("TOTALPOPLE:"))
    NEWCASES=int(input("NEWCASES:"))
    DEATHCASES=int(input("DEATHCASES:"))
    ACTIVECASES=int(input("ACTIVECASES:"))
    TOTALCASES=(NEWCASES+DEATHCASES+ACTIVECASES)
    print(TOTALCASES,"TOTALCASES")
    val=(COUNTRYNAME,TOTALPOPLE,NEWCASES,DEATHCASES,ACTIVECASES,TOTALCASES)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\ntable created successfully")


def view_coviddatas():
    mycursor.execute("\nselect * from coviddatas")
    result=mycursor.fetchall()
    for i in result:
        print(i)


def update_coviddatas():
    sql="update from coviddatas address where address"
    address=input("enter your update address")
    val=(address)
    print("data update succwssfully")


def delete_covidtatas():
    sql="delete from coviddatas where address"
    address=input("enter")
    val=(address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data deleted succwssfully")


def exit_coviddatas():
    print(exit)


while True:
    print("\n-->1.Insert data <<")
    print("-->2.View data --<<")
    print("-->3.Update data <<")
    print("-->4.Delete data <<")
    print("-->5.Exit data --<<")

    user=int(input("\nenter your choice:"))
    if user==1:
        insert_coviddatas()
    elif user==2:
        view_coviddatas()
    elif user==3:
        update_coviddatas()
    elif user==4:
        delete_covidtatas()
    elif user==5:
        exit_coviddatas()
    else:
        print("please type 1 to 5")

    import datetime
    from datetime import date
    
    x=datetime.datetime.now()
    date=x.strftime("%D")
    print(f"\ndate {date}")

    today=x.strftime("%A")
    print(f"day {today}")

    month=x.strftime("%B")
    print(f"month {month}")

    year=x.strftime("%y")
    print(f"year {year}")

    hour=x.strftime("%H")
    minute=x.strftime("%S")
    print(f"time {hour}:{minute}")