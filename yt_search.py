from typing import List
from fastapi import FastAPI
from youtubesearchpython import VideosSearch

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def search(query: str) -> List[dict]:
    videosSearch = VideosSearch(query, limit=10)
    videosResult = await app.async_task(videosSearch.next())
    return videosResult["result"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


# from typing import List
# from fastapi import FastAPI
# # from youtubesearchpython import VideosSearch
# from youtubesearchpython.__future__ import VideosSearch

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/search")
# async def search(query: str) -> List[dict]:
#     videosSearch = VideosSearch(query, limit=10)
#     videosResult =  videosSearch.next()
#     print(videosResult)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)