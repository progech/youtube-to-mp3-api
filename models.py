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
