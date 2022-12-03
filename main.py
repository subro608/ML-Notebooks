from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data':{'name': "sarthak"}}



@app.get("/about")
def about():
    return {"data": "about_page"}