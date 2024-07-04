from fastapi import FastAPI
import requests


app = FastAPI()

@app.get("/trending_books")
def trending_books():
    pass

@app.get("/")
async def home():
    return {"title": "LireApi", "message": "Use /docs to see the documentation."}

@app.get("/search/{title}")
async def search(title: str):
    return {"query": title}
