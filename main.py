from fastapi import FastAPI, Depends
from schemas import UserSchemas
from sqlalchemy.orm import Session

import models
from dbconnection import engine, get_db
import UserService

app = FastAPI()

# create all the tables defined in models.py. It runs as soon as we run the uvicorn command and it doesn't create tables again.
models.Base.metadata.create_all(bind=engine)

# users = [
#         {"id": 1, "name": "Aditya"},
#         {"id": 2, "name": "Adi"},
#         {"id": 3, "name": "John Doe"},
#         {"id": 4, "name": "Jane Doe"},
# ]



@app.get("/")
def rootFunction():
    name = "Aditya"
    lastname = "Kadam"

    return { "name": name, "lastname": lastname }



@app.post("/signup", response_model=UserSchemas.UserModel)
def createUser(user: UserSchemas.UserInputValidation, db: Session = Depends(get_db)):
    response = UserService.createUser(user, db) 
    return response

# @app.get("/users")
# def getUsers():
#     return users


# @app.post("/user")
# def createUser(user: UserSchemas.UserInputValidation):
#     users.append(user)
#     return users
