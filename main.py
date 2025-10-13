from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
import time
from jwt import ExpiredSignatureError, InvalidTokenError

app = FastAPI()

SECRET_KEY = "SUREProED"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 15  # 15 minutes

auth_scheme = HTTPBearer()

def create_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": int(time.time()) + ACCESS_TOKEN_EXPIRE_SECONDS
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    return username

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username

    if username != "Bhargav":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(username)
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> str:
    token = credentials.credentials
    return verify_token(token)

class Calcu(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate")
def calculate(req: Calcu, user: str = Depends(get_current_user)):
    op = req.operation.lower()

    if op == "add":
        result = req.a + req.b
    elif op == "sub":
        result = req.a - req.b
    elif op == "mul":
        result = req.a * req.b
    elif op == "div":
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = req.a / req.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"user": user, "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
