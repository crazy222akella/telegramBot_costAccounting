from aiogram import Bot, Dispatcher
import asyncio
from router import router
from db.models import async_main

async def main():
    await async_main()
    with open("C:/Users/mrand/Documents/token_telegramBot_trat/token.txt", "r") as file: token = file.readline()
    bot = Bot(token="token")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот остановлен")