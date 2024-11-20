from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def hello():
    env_value = os.environ["ENV_PORT"]
    return {"message": f"Hello World and env_port: {env_value}"}