from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from func import ocr

app = FastAPI()


@app.post('/ocr-pdf')
async def create_upload_files(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail='Bad file type')
    filepath = await ocr.scan(file)
    return FileResponse(filepath)
