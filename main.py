from fastapi import FastAPI

import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    # Leer el archivo CSV
    with open("contactos.csv", "r") as f:
        df = pd.read_csv(f)
    # JSON encode contactos.csv
    response = df.to_dict("records")
    return response
