from fastapi import FastAPI
import requests


app = FastAPI()

@app.get("/trending_books")
def trending_books():
    pass

@app.get("/")
def home():
    return {"title": "LireApi"}

@app.get("/search/{title}")
def home(title: str):
    title = title.replace(" ", "-")
    url = "https://mangareader-api.vercel.app/api/v1/search/{title}"

    response = requests.get(url)
    return {"result": response.json()}
