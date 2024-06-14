from fastapi import FastAPI

app = FastAPI()

EMPLOYEES = [{'firstname': 'John', 'lastname': 'Doe'},
             {'firstname': 'Jane', 'lastname': 'Nowak'},
             {'firstname': 'Monika', 'lastname': 'Smith'}]


@app.get("/")
async def index_api():
    return {"message": "The example API is working!"}

@app.get("/employees")
async def get_employees():
    return EMPLOYEES

@app.get("/employees/{name}")
async def get_one_employee(name: str):
    for emp in EMPLOYEES:
        if emp['lastname'] == name:
            return emp
        return{'employee': f'Employee with lastname {name} was not found!'}, 404