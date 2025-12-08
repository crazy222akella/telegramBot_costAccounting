from aiogram import Bot, Dispatcher
import asyncio
from router import router
from db.models import async_main

async def main():
    await async_main()
    bot = Bot(token="8395321646:AAGP5ID7JzS4REpvBtvtONV_PgkLKXfAamI")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот остановлен")