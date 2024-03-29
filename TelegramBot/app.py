import asyncio
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())
from handlers.user_private import user_private_router

bot =Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

dp.include_routers(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())