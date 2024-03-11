from pydantic import BaseModel


class UserInputValidation(BaseModel):
    name: str
