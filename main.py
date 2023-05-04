from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from youtubesearchpython import VideosSearch
from youtubesearchpython.__future__ import Search,VideosSearch

from async_lru import alru_cache
from models import Video

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search")
@alru_cache(maxsize=128)
async def search(query: str, limit: int = 10):
    if not query:
        raise HTTPException(
            status_code=400, detail="Query parameter is required")

    if limit < 1 or limit > 20:
        raise HTTPException(
            status_code=400, detail="Limit must be between 1 and 20")

    # videosSearch = VideosSearch(query, limit=limit)
    try:
        # videosResult = await videosSearch.next()
        # return [Video(
        #     title=result['title'],
        #     url_suffix=result['url_suffix'],
        #     channel=result['channel']['name'],
        #     duration=result['duration'],
        #     views=result['viewCount']['short'],
        #     thumbnail=result['thumbnails'][0]['url']
        # )
        # for result in videosResult['result']]
        search = VideosSearch('NoCopyrightSounds', limit = limit)
        # search = Search('NoCopyrightSounds', limit = 1)
        result = await search.next()
        # print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
