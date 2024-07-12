from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
def read_status():
    return {"message": "System is healthy"}
