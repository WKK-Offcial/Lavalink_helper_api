from fastapi import FastAPI

print("test")
app = FastAPI()

@app.get('/')
def test():
    return {"message": "Hello"}

@app.get('/getsounds/{guild_id}')
def get_sounds(guild_id: int):
    return {"message": "getsounds"}

@app.post('/savesound/{guild_id}')
def save_sound(guild_id: int):
    return {"message": "save sound"}