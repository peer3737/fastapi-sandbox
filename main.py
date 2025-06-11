from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI(version='1.0', title='Je dikke moeder')

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # fetch list of blogs
    if published:
        return {'data': f'{limit} published blog(s) list', 'sort': sort}
    else:
        return {'data': f'{limit} blog(s) list'}


@app.get('/blog/unpublished')
def unpublished():

    # fetch unpublished blogs
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):

    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):

    #fetch comments of blog with id = id
    return {'data':[1, 2]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
