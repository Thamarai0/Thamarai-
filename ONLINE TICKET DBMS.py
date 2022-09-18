from unittest import result
import mysql.connector
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user ="root",
    password="thamarai790",
    database="Train_booking"
)

mycursor=mydb.cursor()
#--------------------------------
#mycursor.execute("create database Train_booking ")
#---------------------------------
#mycursor.execute("create table place_info (PLACE_NAME varchar(255),TRAVEL_TIME varchar(255),TRAIN_NO varchar(255),DISTANCE int,COST int) ")
#mydb.commit()
#---------------------------------


def insert_data():
    sql="insert into place_info (PLACE_NAME,TRAVEL_TIME,TRAIN_NO ,DISTANCE,COST) values (%s,%s,%s,%s,%s)"
    PLACE_NAME=input("ENTER Place NAME  : ")
    TRAVEL_TIME=input("ENTER THE TIME : ")
    TRAIN_NO=input("Enter your Train.no : ")
    DISTANCE=int(input("Enter the distance : "))
    COST=int(input("Enter the Cost : "))
    val=(PLACE_NAME,TRAVEL_TIME,TRAIN_NO ,DISTANCE,COST)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Inserted Successfully :) ")

def view_data():
    mycursor.execute("select * from place_info ")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def delect_data():
    sql="delect from place_info where address"
    adress=input("Address :")
    val=(adress)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data deleted success ")

def update_data():
    sql="update from place_info address where address"
    address=input("enter your update address")
    val=(address)
    mycursor.execute(sql,val)
    print("data update succwssfully")

def exit():
    print(exit)

while True:
    print("\n1.Insert data")
    print("2.view data")
    print("3.delect data")
    print("4.update_data")
    print("5.exit")

    user=input("\nEnter your number : ")
    if user==1:
        insert_data()
    if user==2:
        view_data()
    if user==3:
        delect_data()
    if user==4:
        update_data()
    if user==5:
        exit()
    else:
        print("\nplease enter 1 to 5 ")

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
    
