from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


def default_key(buttons: list, row: int = 2) -> ReplyKeyboardMarkup:
    key_buttons = list()
    for button in buttons:
        key_buttons.append(KeyboardButton(str(button)))
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=row).add(*key_buttons)


def inline_key(buttons: list, row: int = 2) -> InlineKeyboardMarkup:
    key_buttons = list()
    for button in buttons:
        key_buttons.append(InlineKeyboardButton(
            button[0], callback_data=button[1]))
    return InlineKeyboardMarkup(row_width=row).add(*key_buttons)


def url_key(buttons: list, row: int = 2) -> InlineKeyboardMarkup:
    key_buttons = list()
    for button in buttons:
        key_buttons.append(InlineKeyboardButton(
            button[0], url=button[1]))
    return InlineKeyboardMarkup(row_width=row).add(*key_buttons)
