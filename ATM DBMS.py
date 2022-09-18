from ast import While
from distutils.command.build_scripts import first_line_re
from email.headerregistry import Address
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="thamarai790",
    database="atm"
    
    
)
mycursor=mydb.cursor()
#------------------------------------------
#mycursor.execute("create database atm")
#------------------------------------------



#mycursor.execute("create table atm_data (FIRST_NAME varchar(255),LAST_NAME varchar(255),BRANCH varchar(255),ACCOUNT_NO int,BALANCE int)")
#mydb.commit()
#print("table created successfully")

#-------------------------------------------------------------------------------------



def insert_data():
    sql ="insert into atm_data (FIRST_NAME,LAST_NAME,BRANCH,ACCOUNT_NO,BALANCE) values(%s,%s,%s,%s,%s)"
    FIRST_NAME=input("Enter first name : ")
    LAST_NAME=input("Enter last name : ")
    BRANCH=input("Enter act type : ")
    ACCOUNT_NO=int(input("Enter Account.no : "))
    BALANCE=int(input("Enter the balance : "))
    val =(FIRST_NAME,LAST_NAME,BRANCH,ACCOUNT_NO,BALANCE)
    mycursor.execute(sql,val)
    mydb.commit()
    print(" data inserted successfully :) ")

def view_data():
    mycursor.execute("select * from atm_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def update_data():
    sql="update from atm_data address where address"
    address=input("enter your update address")
    val=(address)
    mycursor.execute(sql,val)
    print("data update succwssfully")


def delect_data():
    sql="delect from atm_data where address"
    adress=input("Address :")
    val=(adress)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data deleted success ")

def exit_atm():
    print(exit)

while True:
    print(" 1.Insert Data ")
    print(" 2.View Data ")
    print(" 3.Update Data ")
    print( "4.Delect Data ")
    print ( "5.Exit ")
    
    user=int(input("enter your number : "))
    if user==1:
        insert_data()
    if user==2:
        view_data()
    if user==3:
        update_data()
    if user==4:
        delect_data()
    if user==5:
        exit_atm()