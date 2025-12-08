from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Integer, BigInteger, String, DateTime
from datetime import datetime

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite")
asycn_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Expense(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    sum: Mapped[int] = mapped_column(Integer)
    description: Mapped[String] = mapped_column(String(255))
    date: Mapped[datetime] = mapped_column(DateTime)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)