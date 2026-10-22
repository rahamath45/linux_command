
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to recipe app"}

@app.get("/reciepes")
def get_reciepes():
    return {"reciepes" :[{
                            "id":1,
                            "title":"chicken"
                            },
                            {
                            "id":2,
                            "title":"beef"
                            }
                            ]
    }
@app.post("/reciepes")
def create_reciepes():
    return{"message":"recipes create successfully"}

class user(BaseModel):
    id: int
    name : str