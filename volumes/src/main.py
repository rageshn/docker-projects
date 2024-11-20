from fastapi import FastAPI, Request, Response
import os

app = FastAPI()

base_path = "/app"
temp_path = "/app/temp"
feedback_path = "/app/feedback"


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.put("/post-feedback")
async def post_feedback(request: Request) -> Response:
    
    try:
        req = await request.json()
        print(req)
        title = req['title']
        desc = req['desc']
        temp_file_path = os.path.join(temp_path, title + ".txt")
        feedback_file_path = os.path.join(feedback_path, title + ".txt")
        if os.path.exists(temp_file_path):
            return Response("Feedback already exists", 500)

        with open(temp_file_path, '+a') as f:
            f.write(desc)
        with open(feedback_file_path, 'a+') as f:
            f.write(desc)
        return Response("Feedback recorded", 200)
    except Exception as ex:
        return Response(str(ex), 500)
    
@app.get("/read-feedback")
async def read_feedback(title: str) -> Response:
    try:
        print(title)
        feedback_file_path = os.path.join(feedback_path, title + ".txt")
        with open(feedback_file_path, 'r') as f:
            file_text = f.read()
        return Response(file_text, 200)

    except Exception as ex:
        return Response(str(ex), 500)