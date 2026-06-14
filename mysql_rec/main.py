from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lannisters@3000",
    database = "student"
)

class Student(BaseModel):
    name : str
    age : int

cursor = con.cursor(dictionary=True)
app = FastAPI()

@app.get("/name_age")
def getAllStudent():
    query = "select * from name_age"
    cursor.execute(query)
    students = cursor.fetchall()
    return students

@app.post("/name_age")
def addNewStudent(stud : Student):
    query = "insert into name_age(name, age) values(%s, %s)"
    values = (stud.name, stud.age)
    cursor.execute(query, values)
    con.commit()
    return {"message" : "data added"}