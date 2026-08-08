from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CampusOS AI is running"}

@app.get("/tasks")
def get_tasks():
    with open("sample_data/student_data.json") as file:
        data = json.load(file)

    return data["tasks"]
@app.get("/priority")
def get_priority():
    return {
        "priority": "Artificial Intelligence",
        "reason": "The assignment is due today."
    }
