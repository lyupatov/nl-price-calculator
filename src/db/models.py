from sqlalchemy import Column, Integer, Numeric, DateTime, func
from src.db.base import Base


class CalcResults(Base):
    __tablename__ = "calc_results"

    id = Column(Integer, primary_key=True, index=True)
    total_cost_rub = Column(Numeric(precision=12, scale=2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
