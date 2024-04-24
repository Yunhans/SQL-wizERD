from fastapi import APIRouter

router = APIRouter()


router = APIRouter(
    prefix="/whiteboard",
    tags=["whiteboard"],
)