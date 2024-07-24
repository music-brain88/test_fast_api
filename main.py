from fastapi import FastAPI
from rust_module import sum_as_string

app = FastAPI()

@app.get("/sum/{a}/{b}")
async def get_sum(a: int, b: int):
    result = sum_as_string(a, b)
    return {"result": result}
