from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtubesearchpython.__future__ import VideosSearch
from async_lru import alru_cache
from fastapi.exceptions import HTTPException

app = FastAPI()

origins = [
    # "http://localhost",
    # "http://localhost:3000",
    # "https://yourdomain.com",
    # "https://www.yourdomain.com",
    "https://ytguru.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search")
@alru_cache(maxsize=128)
async def search(query: str, limit: int = 7):
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

        for result in videos_result['result']:

            videos.append(result)

        return videos

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# from fastapi import FastAPI, HTTPException
# from youtubesearchpython.__future__ import VideosSearch
# from async_lru import alru_cache


# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/search")
# @alru_cache(maxsize=128)
# async def search(query: str, limit: int = 7):
#     if not query:
#         raise HTTPException(
#             status_code=400, detail="Query parameter is required")

#     if limit < 1 or limit > 20:
#         raise HTTPException(
#             status_code=400, detail="Limit must be between 1 and 20")

#     try:
#         search = VideosSearch(query, limit=limit)

#         videos_result = await search.next()

#         if videos_result is None:
#             return []

#         videos = []

#         for result in videos_result['result']:

#             videos.append(result)

#         return videos

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
