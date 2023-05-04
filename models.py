from typing import List, Optional
from pydantic import BaseModel


class Thumbnail(BaseModel):
    url: str
    width: Optional[int]
    height: Optional[int]


class RichThumbnail(BaseModel):
    url: str
    width: Optional[int]
    height: Optional[int]


class DescriptionSnippet(BaseModel):
    text: Optional[str]


class Channel(BaseModel):
    name: str
    id: str
    thumbnails: List[Thumbnail]
    link: str


class ViewCount(BaseModel):
    text: Optional[str]
    short: Optional[str]


class Video(BaseModel):
    type: str
    id: str
    title: str
    publishedTime: str
    duration: str
    viewCount: ViewCount
    thumbnails: List[Thumbnail]
    richThumbnail: RichThumbnail
    descriptionSnippet: List[DescriptionSnippet]
    channel: Channel
    accessibility: Optional[dict]
    link: str
    shelfTitle: Optional[str]


#  result = videos_result['result'][0]
#         l = Video(
#             type='video',
#             id=result['id'],
#             title=result['title'],
#             publishedTime=result['publishedTime'],
#             duration=result['duration'],
#             viewCount=ViewCount(
#                 text=result['viewCount']['text'], short=result['viewCount']['short']),
#             thumbnails=[Thumbnail(url=thumbnail['url'], width=thumbnail['width'],
#                                   height=thumbnail['height']) for thumbnail in result['thumbnails']],
#             richThumbnail=RichThumbnail(
#                 url=result['richThumbnail']['url'], width=result['richThumbnail']['width'], height=result['richThumbnail']['height']),
#             descriptionSnippet=[DescriptionSnippet(
#                 text=snippet['text']) for snippet in result['descriptionSnippet']],
#             channel=Channel(name=result['channel']['name'], id=result['channel']['id'], thumbnails=[Thumbnail(
#                 url=thumbnail['url'], width=thumbnail['width'], height=thumbnail['height']) for thumbnail in result['channel']['thumbnails']], link=result['channel']['link']),
#             accessibility=result['accessibility'],
#             link=result['link'],
#             shelfTitle=result['shelfTitle']
#         )
#         print(l)
