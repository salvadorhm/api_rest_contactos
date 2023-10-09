from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
import aiofiles

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Api ejemplo para manejar archivos"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"static/images/{file.filename}"
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"filename": file.filename,"content/type":file.content_type,"message":"file saved"}
