from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from services import get_file
from settings import bot, chat_id, dp, get_logger
from states import SendFileForReview

from buttons import download_file_button

log = get_logger(__name__)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет {message.from_user.username}", reply_markup=download_file_button)


@dp.message_handler(lambda message: message.text and "Загрузить файл")
async def define_chat_id(message: types.Message):
    await message.reply(
        f"{message.from_user.username}, отправь мне документ.",
        reply_markup=download_file_button,
    )
    await SendFileForReview.upload_file.set()


@dp.message_handler(
    state=SendFileForReview.upload_file, content_types=ContentType.DOCUMENT
)
async def get_document(message: types.Message, state: FSMContext):
    try:
        document = await get_file(message)
        await bot.send_document(chat_id, (message.document.file_name, document))
        await message.answer(
            f"Отлично ! Файл {message.document.file_name} был успешно отправлен."
        )
    except Exception as exp:
        log.exception(exp)
        await message.answer(
            f"Упс... произошла ошибка при отправке файл {message.document.file_name}"
        )
    finally:
        await state.finish()
