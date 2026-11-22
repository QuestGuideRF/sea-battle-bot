import asyncio
from aiogram import Bot ,Dispatcher
from app .handlers import register_handlers
from app .logger import setup_logger
from app .config import BOT_TOKEN
logger =setup_logger ("bot")
bot =Bot (token =BOT_TOKEN )
dp =Dispatcher ()
register_handlers (dp )
async def main ():
    logger .info ("✅ Sea-Battle-Bot запущен!")
    await dp .start_polling (bot )
if __name__ =="__main__":
    asyncio .run (main ())