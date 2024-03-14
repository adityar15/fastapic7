from schemas import UserSchemas
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def createUser(user: UserSchemas.UserInputValidation, db: Session):
    # select * from users where email = user.email limit 1
    currentUser  = db.query(models.User).filter(models.User.email == user.email).first()

    if currentUser:
        return {
            "status": "401",
            "message": "User already exists"
        }
    

    hashedPassword = passwordContext.hash(user.password)


    # insert into users (email, password) values (user.email, hashedPassword)
    newUser = models.User(email=user.email, password=hashedPassword)
    db.add(newUser)
    db.commit()

    # select * from users where id = newlyCreatedIdOftheUser  limit 1 
    db.refresh(newUser)

    return user

    