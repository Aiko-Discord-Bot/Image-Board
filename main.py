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
        "name": "",
        "url": "",
    },
    3: {
        "name": "",
        "url": "",
    },
     4: {
        "name": "",
        "url": "",
    },
     5: {
        "name": "",
        "url": "",
    },
     6: {
        "name": "",
        "url": "",
    },
     7: {
        "name": "",
        "url": "",
    },
     8: {
        "name": "",
        "url": "",
    },
     9: {
        "name": "",
        "url": "",
    },
     10: {
        "name": "",
        "url": "",
    },
     11: {
        "name": "",
        "url": "",
    },
     12: {
        "name": "",
        "url": "",
    },
     13: {
        "name": "",
        "url": "",
    },
     14: {
        "name": "",
        "url": "",
    },
     15: {
        "name": "",
        "url": "",
    },
     16: {
        "name": "",
        "url": "",
    },
     17: {
        "name": "",
        "url": "",
    },
     18: {
        "name": "",
        "url": "",
    },
     19: {
        "name": "",
        "url": "",
    },
     20: {
        "name": "",
        "url": "",
    },
     21: {
        "name": "",
        "url": "",
    },
     22: {
        "name": "",
        "url": "",
    },
     23: {
        "name": "",
        "url": "",
    },
     24: {
        "name": "",
        "url": "",
    },
     25: {
        "name": "",
        "url": "",
    },
     26: {
        "name": "",
        "url": "",
    },
     27: {
        "name": "",
        "url": "",
    },
     28: {
        "name": "",
        "url": "",
    },
     30: {
        "name": "",
        "url": "",
    },
     31: {
        "name": "",
        "url": "",
    },
     32: {
        "name": "",
        "url": "",
    },
     33: {
        "name": "",
        "url": "",
    },
     34: {
        "name": "",
        "url": "",
    },
     35: {
        "name": "",
        "url": "",
    },
     36: {
        "name": "",
        "url": "",
    },
     37: {
        "name": "",
        "url": "",
    },
     38: {
        "name": "",
        "url": "",
    },
     39: {
        "name": "",
        "url": "",
    },
     40: {
        "name": "",
        "url": "",
    },
     41: {
        "name": "",
        "url": "",
    },
     42: {
        "name": "",
        "url": "",
    },
     43: {
        "name": "",
        "url": "",
    },
     44: {
        "name": "",
        "url": "",
    },
     45: {
        "name": "",
        "url": "",
    },
     46: {
        "name": "",
        "url": "",
    },
     47: {
        "name": "",
        "url": "",
    },
     48: {
        "name": "",
        "url": "",
    },
     49: {
        "name": "",
        "url": "",
    },
     50: {
        "name": "",
        "url": "",
    }

}

@app.get("/")
async def root():
    return {"hello":"Aiko"}

@app.get("/get-quiz/{char_id}")
async def get_actor(char_id: int):
    return character[char_id]

