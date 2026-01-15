from fastapi import APIRouter, Depends, Request
from src.schemas.schemas import MaterialsData
from src.db.session import get_session
from src.services.services import commit_calc_materials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from src.db.models import CalcResults

router = APIRouter()


@router.post("/calc")
async def calc(data: MaterialsData, session: AsyncSession = Depends(get_session)):
    total_cost_rub = await commit_calc_materials(data, session)
    return {"total_cost_rub": total_cost_rub}


@router.get("/costs_list")
async def costs_list(request: Request, session: AsyncSession = Depends(get_session)):
    stmt = (
        select(
            CalcResults.created_at,
            CalcResults.total_cost_rub
        )
        .order_by(desc(CalcResults.created_at))
        .limit(10)
    )

    execution = await session.execute(stmt)
    result = execution.mappings().all()

    return result
