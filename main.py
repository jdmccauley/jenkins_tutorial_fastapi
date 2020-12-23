from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/worldhello")
async def world_hello():
    return {"message": "World Hello"}