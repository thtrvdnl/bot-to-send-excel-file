from aiogram.dispatcher.filters.state import State, StatesGroup


class SendFileForReview(StatesGroup):
    upload_file = State()
