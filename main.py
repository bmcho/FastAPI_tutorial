from enum import Enum
from typing import Optional

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


class UserLevel(str, Enum):
    a = "a"
    b = "b"
    c = "c"


@app.get("/")
def hello():
    return "Hello, World!"


# 함수 내 매개변수로 들어오는 user_id의 타입을 알 수 없다.
# @app.get("/users-f/{user_id:int}")
# def get_user_Flask(user_id):
#     return {"user_id": user_id}

# FastAPI는  위에서 부터 아래로 엔드포인트 순서를 수행한다
# 만약 /me 엔드포인트가 {user_id}로 간다면 error가 난다
@app.get("/users/me")
def get_current_user():
    return {"user_id": 123}


@app.get("/users/{user_id}")
def get_user(user_id: int = 100):
    return {"user_id": user_id}


@app.get("/users-q")
def get_users_q(request: Request, limit: Optional[int] = None):
    return {"limit": limit, "q": request.query_params}


@app.get("/users-e")
def get_users_e(grade: UserLevel = UserLevel.a):
    return {"grade": grade}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
