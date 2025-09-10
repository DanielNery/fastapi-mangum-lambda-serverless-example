from fastapi import FastAPI
from mangum import Mangum

# Cria a aplicação FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá do FastAPI no AWS Lambda com Mangum!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Olá, {name}!"}

# Cria o handler para AWS Lambda
handler = Mangum(app)
