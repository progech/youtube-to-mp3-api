from typing import List
from pydantic import BaseModel


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class RichThumbnail(BaseModel):
    url: str
    width: int
    height: int


class DescriptionSnippet(BaseModel):
    text: str


class Channel(BaseModel):
    name: str
    id: str
    thumbnails: List[Thumbnail]
    link: str


class ViewCount(BaseModel):
    text: str
    short: str


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
    accessibility: dict
    link: str
    shelfTitle: str
