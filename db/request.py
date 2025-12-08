from datetime import datetime
from calendar import monthrange
from db.models import asycn_session
from db.models import Expense
from sqlalchemy import select, and_, func

async def add(user_id, data):
    async with asycn_session() as session:
        session.add(Expense(
            user_id=user_id,
            sum=data["sum"],
            description=data["description"],
            date = datetime.now()
        ))
        await session.commit()

async def getYears(user_id):
    async with asycn_session() as session:
        result = await session.scalars(
            select(func.strftime("%Y", Expense.date))
            .where(Expense.user_id == user_id)
            .distinct()
            .order_by(func.strftime("%Y", Expense.date))
        )
        years = list(result)
        return years  

    
async def getAll(user_id, data):
    year = data['year']
    month = data['month']
    start_date = datetime(year,month,1)
    last_day = monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)

    async with asycn_session() as session:
        expenses = await session.scalars(
            select(Expense).where(
                and_(
                    Expense.user_id == user_id,
                    Expense.date >= start_date,
                    Expense.date <= end_date
                )
            )
        )
        return answerExpenses(expenses.all())

def answerExpenses(expenses):
    if not expenses:
        return "в этом месяце трат нет"
    sum = 0
    answer = []
    for exp in expenses:
        date = exp.date.strftime("%d.%m.%Y")
        answer.append(f"{date}\n {exp.sum}\n{exp.description}")
        sum +=exp.sum
    
    answer.append("-------------")
    answer.append(f"Всего: {sum} руб.")
    return "\n\n".join(answer)