import uvicorn
from fastapi import FastAPI, Body, Depends

from app.model import UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT


users = []

app = FastAPI()



def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False



@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(default=None)):
    users.append(user) 
    return {'Done':"User added sucssfully"}


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)#{'Done':"User Loged In sucssfully"}
    return {
        "error": "Wrong login details!"
    }
