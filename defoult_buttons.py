from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo

sahifa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'category_add'), KeyboardButton(text = 'product_add')]
    ],
    resize_keyboard=True
)

accept = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="yes"),KeyboardButton(text='no')]
    ],
    resize_keyboard=True
)

accept1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="yes"),KeyboardButton(text='no')]
    ],
    resize_keyboard=True
)

user_sahifa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'basket'), KeyboardButton(text = 'products')]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'contact',request_contact=True)]
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'location',request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)