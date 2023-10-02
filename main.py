from fastapi import FastAPI
from fastapi import status

import pandas as pd

app = FastAPI()


@app.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Endpoint raíz"
        )
async def root():
    """
    # Endpoint raíz
    ## Status codes
    * 289 - Código de muestra
    * 334 - Otro status de prueba
    """
    return {"message": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    # Leer el archivo CSV
    with open("contactos.csv", "r") as f:
        df = pd.read_csv(f)
    # JSON encode contactos.csv
    response = df.to_dict("records")
    return response
