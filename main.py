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
def search(title: str):
    title = title.replace(" ", "-")
    url = f"https://mangareader-api.vercel.app/api/v1/search/{title}"
    response = requests.get(url)

    result = response.json()["data"]
    return {"query": title, "response": response.status_code, "result": result}
