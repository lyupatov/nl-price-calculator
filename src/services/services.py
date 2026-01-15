from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models import CalcResults


async def commit_calc_materials(data, session: AsyncSession):
    total_cost_rub = sum(mat.qty * mat.price_rub for mat in data.materials)
    calc = CalcResults(total_cost_rub=total_cost_rub)
    session.add(calc)
    await session.commit()
    await session.refresh(calc)

    return total_cost_rub
