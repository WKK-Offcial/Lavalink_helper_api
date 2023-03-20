from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from dropbox_storage import DropboxManager
import os
import uvicorn

load_dotenv()
app = FastAPI()

dropbox = DropboxManager()
dropbox.download_all()

@app.get('/')
async def test():
    return {"message": "Hello"}

@app.get('/getsounds/{guild_id}')
async def get_sounds(guild_id: str):
    try:
        files = os.listdir(f'./sounds/{guild_id}/')
        ret = {"files": files}
    except:
        raise HTTPException(status_code=404, detail="Wrong Guild Id")
    return ret

@app.post('/savesound/{guild_id}')
async def save_sound(guild_id: str):
    return {"message": "save sound"}
    
if __name__ == "__main__":
    load_dotenv()
    dropbox = DropboxManager()
    dropbox.download_all()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


#     """ Simple API module """
# import json
# import base64
# import falcon

# class Endpoints:
#     """
#     Class with endpoints required by discord bot
#     """
#     def on_get(self, req, res):
#         """
#         Handle GET requests.
#         """
#         test_dict = {'203114439468253184':['1','2', '3'], '1084958968302022805':['5','2', '4']}
#         res.text = json.dumps(test_dict) # Dictionary to json

#     def on_post(self, req, res):
#         """
#         Handle POST requests.
#         """
#         try:
#             mp3_data = req.get_media().get('mp3') # Get mp3 ecoded in base64 from json
#             guild_id = req.get_media().get('guild_id') # Get guild id
#             file_data = base64.b64decode(mp3_data) # decode b64 to binary
#             with open('aud.mp3', "wb") as file: # write binary to file
#                 file.write(file_data)
#             res.text = json.dumps({"message":"Done!"})
#         except Exception:
#             res.text = json.dumps({"message":"Failed!"})
#             res.status = falcon.HTTP_500

# app = falcon.App()
# app.add_route('/sounds', Endpoints())
