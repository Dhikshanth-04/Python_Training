from fastapi import FastAPI
#pydantic and basemodel is the library file in fastapi, used to r=define the request and response
from pydantic import BaseModel

app = FastAPI()

# this block, would determine or enforces the type of date. 
# the input data should be the certain type
class Student(BaseModel):
    name : str
    age : int

student = {
    1 : {
        "name" : "SiiRii",
        "age" : 22

    },
    2 : {
        "name" : "Dhikshanth",
        "age" : 22
    }
}

#getting whole records
@app.get("/students")
def getStudents():
    return student

#getting according to student id
@app.get("/student/{student_id}")
def getStudent_id(student_id:int):
    return student[student_id]

#adding new student
@app.post("/student")
def addNewStudent(stud : Student):
    new_id = len(student)+1
    student[new_id] = {
        "name" : stud.name,
        "age" : stud.age
    }
    return {"message" : "Student record added"}

@app.put("/student/{student_id}")
def updateDetails(student_id : int, stud : Student):
    student[student_id] = {
        "name" : stud.name,
        "age" : stud.age
    }
    return {"meesage" : "Details updated"}

@app.delete("/student/{student_id}")
def deleteStudent(student_id : int):
    del student[student_id]
    return {"message" : "Record deleted"}
