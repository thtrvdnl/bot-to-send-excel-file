from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

download_file_button = ReplyKeyboardMarkup(resize_keyboard=True)
download_file_button.add(KeyboardButton("Загрузить файл"))
