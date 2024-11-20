from fastapi import FastAPI, Response
import requests

app = FastAPI()


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
