from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from states import SendFileForReview
from services import get_file
from settings import dp, bot, get_logger, chat_id

log = get_logger(__name__)


@dp.message_handler(commands=["upload_file"])
async def define_chat_id(message: types.Message):
    await message.answer(f"Привет {message.from_user.username}, отправь мне документ.")
    await SendFileForReview.upload_file.set()


@dp.message_handler(state=SendFileForReview.upload_file, content_types=ContentType.DOCUMENT)
async def get_document(message: types.Message):
    try:
        document = await get_file(message)
        await bot.send_document(chat_id, (message.document.file_name, document))
        await message.answer(f"Отлично ! Файл {message.document.file_name} был успешно отправлен.")
    except Exception as exp:
        log.exception(exp)
        await message.answer(f"Упс... произошла ошибка при отправке файл {message.document.file_name}")
