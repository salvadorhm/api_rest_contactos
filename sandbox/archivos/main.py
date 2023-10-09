from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.staticfiles import StaticFiles
import aiofiles
from PIL import Image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message":"Api ejemplo para manejar archivos"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"static/images/{file.filename}"
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    im = Image.open(file_location)
    out = im.rotate(45) # degrees counter-clockwise
    out.save("static/images/rot.png")
    out.show()
    return {"filename": file_location,"content/type":file.content_type,"message":"file saved"}
