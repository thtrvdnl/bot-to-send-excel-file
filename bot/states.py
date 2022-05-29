from aiogram.dispatcher.filters.state import StatesGroup, State


class SendFileForReview(StatesGroup):
    upload_file = State()
