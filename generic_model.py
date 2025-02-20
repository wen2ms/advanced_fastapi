from fastapi import FastAPI
from typing import TypeVar, Generic, Optional
from pydantic import BaseModel
import uvicorn

class User(BaseModel):
    username: str
    password: str
    id: Optional[int] = None

class Role(BaseModel):
    rid: Optional[int] = None
    role: str
    user: User

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T]

    @staticmethod
    def success(data: Optional[T] = None, message: str = 'ok'):
        return Response(code=200, message=message, data=data)
    
    @staticmethod
    def fail(data: Optional[T] = None, message: str = 'fail'):
        return Response(code=400, message=message, data=data)
    
app = FastAPI()

@app.get('/ok', response_model=Response[User])
async def ok():
    user = User(username='Jucy', password='zxzx')

    return Response.success(data=user)

@app.get('/fail', response_model=Response[Role])
async def fail():
    user = User(username='Cuicy', password='123')

    role = Role(role='untitled', user=user)

    return Response.fail(data=role)

if __name__ == "__main__":
    uvicorn.run('generic_model:app', reload=True)