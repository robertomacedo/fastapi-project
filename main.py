from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def pegar():
    return {"msg": "Hello World Macedo"}

