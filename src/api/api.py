from fastapi import APIRouter

router = APIRouter()


@router.get("/calc")
async def calc():
    return {"result": 42}
