from fastapi import FastAPI
from pydantic import BaseModel
from calculate import calculate

app = FastAPI()

class User_input(BaseModel):
    operation: str
    x: float
    y: float

@app.get('/hello')
def hello():
    return {'message': 'hello'}

@app.post('/calculate')
def operate(input: User_input):
    result = calculate(input.operation, input.x, input.y)
    return result