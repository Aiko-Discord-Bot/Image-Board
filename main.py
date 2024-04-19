from typing import List
from uuid import uuid4
from fastapi import FastAPI 
app = FastAPI()

character = {
    1: {
        "name" : "Diluc",
        "url" : "https://s1.zerochan.net/Diluc.Ragnvindr.600.3129744.jpg",
    },
    2: {
        "name" : "Yelan",
        "url" : "https://s1.zerochan.net/Dororo.%28Character%29.600.2606598.jpg"
    },
    3: {
        "name" : "Dororo",
        "url" : "https://s1.zerochan.net/Dororo.%28Character%29.600.2606598.jpg"
    },
    4: {
        "name" : "Hyakkimaru",
        "url" : "https://s1.zerochan.net/Hyakkimaru.600.2474158.jpg"
    }

}

@app.get("/")
async def root():
    return {"hello":"Aiko"}

@app.get("/get-quiz/{char_id}")
async def get_actor(char_id: int):
    return character[char_id]

