from fastapi import FastAPI, Response
import requests, redis

app = FastAPI()

r = redis.Redis(host="172.17.0.2", port=6379)


@app.get("/")
async def hello():
    return {"message": "Hello World"}

@app.get("/films")
async def get_films_list() -> Response:
    sw_url = "https://swapi.dev/api/films"
    try:
        response = requests.get(sw_url)

        if response.status_code == 200:
            return Response(str(response.json()), 200)
        else:
            return Response("Could not fetch data", response.status_code)
    except Exception as ex:
        return Response(f"Exception: {str(ex)}", 500)


@app.put("/setkv")
async def set_redis_kv(key: str) -> Response:
    try:
        if len(key) == 0 or key is None:
            return Response("Empty key provided", 400)
        
        r.set("key", key)

        v = r.get("key")

        return Response(f"Saved value to redis", 200)


    except Exception as ex:
        return Response(f"Exception: {str(ex)}", 500)


@app.get("/getkv")
async def get_redis_kv(key: str) -> Response:
    try:
        if len(key) == 0 or key is None:
            return Response("Empty key provided", 400)

        v = r.get(key)

        return Response(f"Value: {v}", 200)

    except Exception as ex:
        return Response(f"Exception: {str(ex)}", 500)