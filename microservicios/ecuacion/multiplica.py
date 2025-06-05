from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Input(BaseModel):
    a: float
    b: float
    c: float
    d: float

@app.post("/resolver")
def resolver(valores: Input):
    suma_resp = requests.post("http://suma:8000/sumar", json={"a": valores.a, "b": valores.b})
    resta_resp = requests.post("http://resta:8000/restar", json={"c": valores.c, "d": valores.d})
    
    suma = suma_resp.json()["resultado"]
    resta = resta_resp.json()["resultado"]
    
    resultado = suma * resta
    
    # Store the result in the database
    store_data = {
        "a": valores.a,
        "b": valores.b,
        "c": valores.c,
        "d": valores.d,
        "result": resultado
    }
    requests.post("http://database:8000/store_result", json=store_data)
    
    return {"resultado": resultado}