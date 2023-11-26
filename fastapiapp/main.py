from fastapi import FastAPI
from auth.model import PostSchema

posts = [
    {
        "id" : 1,
        "title" : "penguins",
        "text"  : "penguins are aquatic birds"
    },
    {
        "id" : 2,
        "title" : "tiger",
        "text"  : "tigers are carnivo animal"
    },
    {
        "id" : 3,
        "title" : "koalas",
        "text"  : "koalas are nice"
    }
]

users = []

app = FastAPI()

@app.get("/", tags=["test"] )
def greet():
    return {"hello":"World"}
