import csv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from CSV
students = []
with open('q-fastapi.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class_filter: List[str] = Query(None)):
    if class_filter:
        filtered_students = [student for student in students if student["class"] in class_filter]
    else:
        filtered_students = students
    return {"students": filtered_students}