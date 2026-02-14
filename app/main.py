from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with uv (package manager)!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/xxx")
def post_item():
    return {"message": "Hello from FastAPI with uv (package manager)!"}

