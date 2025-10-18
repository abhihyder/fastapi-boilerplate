from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from app.requests.hashtag import HashtagRequest

route_config = {
    "prefix": "/api",
    "tags": ["API"]
}

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Fastapi app is Live"}


@router.get("/health")
def health_check():
    return {"message": "healthy"}