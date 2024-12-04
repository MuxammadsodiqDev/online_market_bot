from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

soni = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ozroq",callback_data="ozroq"), InlineKeyboardButton(text=f'{1}', callback_data="son"),InlineKeyboardButton(text="yana",callback_data="yana")]
    ]
)

accept_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ha",callback_data="ha"), InlineKeyboardButton(text=f"yo'q", callback_data="yoq")]
    ]
)

accept_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="albatta",callback_data="albatta"), InlineKeyboardButton(text=f"kerak emas", callback_data="kerak_emas")]
    ]
)