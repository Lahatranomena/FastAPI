from datetime import datetime
from typing import List
from xmlrpc.client import DateTime

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def get_ping():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.get("/home")
def get_home():
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return Response(content=html_content, status_code=200)

@app.get("")
def get_none():
    with open("erreur404.html", "r", encoding="utf-8") as filenone:
        html_content = filenone.read()
        return Response(content=html_content, status_code=404)

class Post(BaseModel):
    author: str
    title: str
    content: str

List_post: List[Post] = []
@app.post("/posts")
def post_posts(new_post: List[Post]):
    List_post.extend(new_post)

    data_response = []
    for post in List_post:
        post_json = {
            "author" : post.author,
            "title" : post.title,
            "content" : post.content
        }

        data_response.append(post_json)

    return JSONResponse(content=data_response, status_code=201)

@app.get("/posts")
def get_posts():
    data_response = []
    for post in List_post:
        post_json = {
            "author" : post.author,
            "title" : post.title,
            "content" : post.content
        }
        data_response.append(post_json)
    return JSONResponse(content=data_response, status_code=200)

@app.put("/posts")
def update_post(new_post: Post):
    for i, p in enumerate(List_post):
        if p.title == new_post.title:

            List_post[i] == new_post
            return JSONResponse(content=new_post.model_dump(), status_code=200)

    List_post.append(new_post)
    return JSONResponse(content=new_post.model_dump(), status_code=201)




