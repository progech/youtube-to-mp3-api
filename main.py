from typing import List
from fastapi import FastAPI, HTTPException
from youtubesearchpython.__future__ import Search, VideosSearch
from async_lru import alru_cache
from models import Video, Thumbnail, RichThumbnail, DescriptionSnippet, Channel, ViewCount

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

    try:
        search = VideosSearch(query, limit=limit)

        videos_result = await search.next()

        if videos_result is None:
            return []

        videos = []

        # for result in videos_result['result']:
        #     video = Video(
        #         type='video',
        #         id=result['id'],
        #         title=result['title'],
        #         publishedTime=result['publishedTime'],
        #         duration=result['duration'],
        #         # viewCount=ViewCount(text=result['viewCount']['text'], short=result['viewCount']['short']),
        #         # thumbnails=[Thumbnail(url=thumbnail['url'], width=thumbnail['width'], height=thumbnail['height']) for thumbnail in result['thumbnails']],
        #         # richThumbnail=RichThumbnail(url=result['richThumbnail']['url'], width=result['richThumbnail']['width'], height=result['richThumbnail']['height']),
        #         # descriptionSnippet=[DescriptionSnippet(text=snippet['text']) for snippet in result['descriptionSnippet']],
        #         # channel=Channel(name=result['channel']['name'], id=result['channel']['id'], thumbnails=[Thumbnail(url=thumbnail['url'], width=thumbnail['width'], height=thumbnail['height']) for thumbnail in result['channel']['thumbnails']], link=result['channel']['link']),
        #         # accessibility=result['accessibility'],
        #         # link=result['link'],
        #         # shelfTitle=result['shelfTitle']
        #     )
        result = videos_result['result'][0]
        l = Video(
            type='video',
            id=result['id'],
            title=result['title'],
            publishedTime=result['publishedTime'],
            duration=result['duration'],
            viewCount=ViewCount(
                text=result['viewCount']['text'], short=result['viewCount']['short']),
            thumbnails=[Thumbnail(url=thumbnail['url'], width=thumbnail['width'],
                                  height=thumbnail['height']) for thumbnail in result['thumbnails']],
            richThumbnail=RichThumbnail(
                url=result['richThumbnail']['url'], width=result['richThumbnail']['width'], height=result['richThumbnail']['height']),
            descriptionSnippet=[DescriptionSnippet(
                text=snippet['text']) for snippet in result['descriptionSnippet']],
            channel=Channel(name=result['channel']['name'], id=result['channel']['id'], thumbnails=[Thumbnail(
                url=thumbnail['url'], width=thumbnail['width'], height=thumbnail['height']) for thumbnail in result['channel']['thumbnails']], link=result['channel']['link']),
            accessibility=result['accessibility'],
            link=result['link'],
            shelfTitle=result['shelfTitle']
        )
        print(l)
        return l

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
