from io import BytesIO
from typing import Awaitable

from aiogram.types import Message

from settings import get_logger, bot

log = get_logger(__name__)


async def get_file(message: Message) -> Awaitable[BytesIO]:
    file = await bot.get_file(message.document.file_id)
    return await bot.download_file(file.file_path)
