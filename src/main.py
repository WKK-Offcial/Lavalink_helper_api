from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from dropbox_storage import DropboxManager
from pydantic import BaseModel
from pathlib import Path
import os
import uvicorn
import base64


load_dotenv()
app = FastAPI()

dropbox = DropboxManager()
dropbox.download_all()

class SoundModel(BaseModel):
    file_data: str
    file_name: str

@app.get('/')
async def test():
    return {"message": "Hello"}

@app.get('/sounds/{guild_id}')
async def get_sounds(guild_id: str):
    try:
        files = os.listdir(f'./sounds/{guild_id}/')
        files.sort()
        ret = {"files": files}
    except:
        raise HTTPException(status_code=418, detail="Wrong Guild Id")
    return ret

@app.post('/sounds/{guild_id}')
async def save_sound(guild_id: str, body: SoundModel):
    Path(f'./sounds/{guild_id}').mkdir(parents=True, exist_ok=True)
    print(body.file_name)
    if not body.file_name.endswith('.mp3'):
        raise HTTPException(status_code=418, detail="fsdfsdffs The fuck is this!? .mp3 only")
    file_data = base64.b64decode(body.file_data)
    with open(f'./sounds/{guild_id}/{body.file_name}', "wb") as f: # write binary to file
        f.write(file_data)
    dropbox.upload_file(f'./sounds/{guild_id}/{body.file_name}', f'{guild_id}')
    return {"message": "everything daijoubu"}
    
if __name__ == "__main__":
    load_dotenv()
    dropbox = DropboxManager()
    dropbox.download_all()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)