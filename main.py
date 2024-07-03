from fastapi import FastAPI


app = FastAPI()

@app.get("/trending_books")
def trending_books():
    pass

@app.get("/")
def home():
    return {"title": "LireApi"}