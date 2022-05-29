import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = os.getenv

API_TOKEN = env("TOKEN")

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s(%(funcName)s):%(lineno)d | %(message)s",
)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger


chat_id = env("CHAT_ID")
storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
