from aiogram .types import Message 
from aiogram.fsm.context import FSMContext
import asyncio
import logging
from bot_config import bot, dp, database

from handlers.start import start_router
from handlers.homework import homework_router

async def main():
    database.create_tables()
    dp.include_router(homework_router)
    dp.include_router(start_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

