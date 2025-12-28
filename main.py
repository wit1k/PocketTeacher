import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from aiogram import Dispatcher, Bot

from Handlers.UserPrivate import UserPrivateRt

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(UserPrivateRt)

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        print('Бот запущен')  
        await dp.start_polling(bot)
    except Exception as e:
        print(f'Ошибка: {e}')
    finally:
        await bot.session.close()
asyncio.run(main())