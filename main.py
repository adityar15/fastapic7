from fastapi import FastAPI
from schemas import UserSchemas

app = FastAPI()


users = [
        {"id": 1, "name": "Aditya"},
        {"id": 2, "name": "Adi"},
        {"id": 3, "name": "John Doe"},
        {"id": 4, "name": "Jane Doe"},
]



@app.get("/")
def rootFunction():
    name = "Aditya"
    lastname = "Kadam"

    return { "name": name, "lastname": lastname }




@app.get("/users")
def getUsers():
    return users


@app.post("/user")
def createUser(user: UserSchemas.UserInputValidation):
    users.append(user)
    return users
