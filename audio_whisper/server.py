from fastapi import FastAPI, UploadFile
import whisper
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE
import shutil



app = FastAPI()

@app.post("/uploadaudio/")
async def upload_audio_file(file: UploadFile):
    with open(file.filename, 'wb') as audiof:
        contents = await file.read()
        audiof.write(contents)
    await file.close()

    model = whisper.load_model("base")
    result = model.transcribe(file.filename)

    return {"transcriptions": result["text"]}

@app.get("/hello/")
async def hello():
    return {"message": "Hello"}    