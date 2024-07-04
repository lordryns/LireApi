from fastapi import FastAPI
import json 


with open("manga.json", "r") as fp:
    books = json.load(fp=fp)

app = FastAPI()

@app.get("/manga")
async def get_manga():
    return books

@app.get("/")
async def home():
    return {"title": "LireApi", "message": "Use /docs to see the documentation."}

@app.get("/search/{title}")
async def search(title: str):
    return {"query": title}
