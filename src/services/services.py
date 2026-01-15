from sqlalchemy.ext.asyncio import AsyncSession
from src.core.logger import logger
from src.db.models import CalcResults


async def commit_calc_materials(data, session: AsyncSession):
    try:
        total_cost_rub = sum(mat.qty * mat.price_rub for mat in data.materials)
        calc = CalcResults(total_cost_rub=total_cost_rub)
        session.add(calc)
        await session.commit()
        await session.refresh(calc)

        return total_cost_rub
    except Exception as e:
        await session.rollback()
        logger.exception("Failed to save calc result")
        raise
