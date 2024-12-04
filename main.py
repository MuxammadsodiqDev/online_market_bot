import asyncio
import logging

from aiogram import Bot, Dispatcher, html,F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import ContentType
from aiogram.types import Message ,CallbackQuery
from aiogram.fsm.context import FSMContext
from config import token
from defoult_buttons import sahifa,accept,accept1,user_sahifa,contact,location
from inline_buttons import accept_user,accept_admin
from states import Form_Cate,Form_Pro,From_User
from database import categoryAdd,categoryRead,productAdd,productRead
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder,InlineKeyboardButton,InlineKeyboardMarkup


TOKEN =token
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
product_count = 0  # Boshlang‘ich qiymat

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    telegram_id = message.from_user.id
    if telegram_id == 5072268247:
        await message.answer("Xush kelibsiz admin. ",reply_markup=sahifa)
    else:
        await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=cbb4cc0e6f5af2d07ac5517943d2d7419d010b13-10303576-images-thumbs&n=13",caption=f"Assalomu alaykum, {message.from_user.full_name}\nBizni online marketga xush kelibsiz",reply_markup=user_sahifa)

@dp.message(F.text == "category_add", F.from_user.id == 5072268247)
async def ProductAddbot(message: Message, state: FSMContext):
    await message.answer("Category nomini kiriting: ")
    await state.set_state(Form_Cate.category_state)

@dp.message(F.text, Form_Cate.category_state )
async def CategoryName(message: Message, state: FSMContext):
    CategoryName = message.text
    await state.update_data({
        "CategoryName":CategoryName
    })
    await message.answer(f"Haqiqatdan ham '{CategoryName}' category qo'shmoqchimiz?",reply_markup=accept)
    await state.set_state(Form_Cate.category_tasdiqlash)

@dp.message(F.text, Form_Cate.category_tasdiqlash)
async def TasdiqlashBot(message: Message, state: FSMContext):
    xabar = message.text
    data = await state.get_data()
    CategoryName = data.get("CategoryName")
    if "yes" == xabar.lower():
        categoryAdd(CategoryName)
        await message.answer("Category saqlandi")
        await message.answer("Yana nima qilamiz?",reply_markup=sahifa)
        await state.clear()
    elif "no" == xabar.lower():
        await state.clear()

@dp.message(F.text == "product_add", F.from_user.id == 5072268247)
async def ProductAddbot(message: Message, state: FSMContext):
    builder=ReplyKeyboardBuilder()
    categories = categoryRead()
    for i in categories:
        builder.add(types.KeyboardButton(text = F"{i[1]}"))
    builder.add(types.KeyboardButton(text ="⬅️ ortga"))
    builder.adjust(2)
    await message.answer("Category birini tanlang.",reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(Form_Pro.category_choice)

@dp.message(F.text ,  F.from_user.id == 5072268247,Form_Pro.category_choice)
async def categoryNameBot(message: Message, state: FSMContext):
    category_name = message.text
    categories = categoryRead()
    for i in categories:
        if i[1]==category_name:
            await state.update_data({
             "Category_id":i[0]
             })
            await state.set_state(Form_Pro.product_name)
            await message.answer("Mahsulot nomi kiriting: ")

@dp.message(F.text , F.from_user.id == 5072268247,Form_Pro.product_name)
async def ProductNameBot(message: Message,state: FSMContext):
    product_name = message.text
    await state.update_data({
        "product_name":product_name
    })
    await state.set_state(Form_Pro.product_price)
    await message.answer(f"{product_name} narxini kiriting: ")

@dp.message(F.text , F.from_user.id == 5072268247,Form_Pro.product_price)
async def ProductNameBot(message: Message,state: FSMContext):
    product_price = message.text
    await state.update_data({
        "product_price":product_price
    })
    data = await state.get_data()
    product_name = data.get("product_name")
    await state.set_state(Form_Pro.product_photo)
    await message.answer(f"{product_name} rasmini yuboring: ")

@dp.message(F.photo , F.from_user.id == 5072268247,Form_Pro.product_photo)
async def ProductNameBot(message: Message,state: FSMContext):
    product_photo = message.photo[-1].file_id
    await state.update_data({
        "product_photo":product_photo
    })
    data = await state.get_data()
    product_name = data.get("product_name")
    product_price = data.get("product_price")
    await state.set_state(Form_Pro.product_accept)
    await message.answer_photo(photo = f"{product_photo}" ,caption = f"{product_name}--{product_price} sum\n\nYuqoridagi malumotlarni saqlaysizmi?",reply_markup=accept1)

@dp.message(F.text , Form_Pro.product_accept)
async def FinishBot(message: Message, state: FSMContext):
    xabar = message.text
    data = await state.get_data()
    product_name = data.get("product_name")
    products_price = int(data.get("product_price"))
    product_photo = data.get("product_photo")
    category_id = int(data.get("Category_id"))

    if "yes"==xabar.lower():
        productAdd(product_name,products_price,product_photo,category_id)
        await message.answer("Mahsulot saqlandi.")
        await state.clear()
    elif 'no' == xabar.lower():
        await state.clear()

### USER
# class From_User(StatesGroup):
#     category_user = State()
#     product_name_user = State()
#     product_count_user = State()
#     contact
#     location
#     product_accept_user = State()

@dp.message(F.text == "products")
async def ProductAddbot(message: Message, state: FSMContext):
    builder=ReplyKeyboardBuilder()
    categories = categoryRead()
    for i in categories:
        builder.add(types.KeyboardButton(text = F"{i[1]}"))
    builder.add(types.KeyboardButton(text ="⬅️ ortga"))
    builder.adjust(2)
    await message.answer("Category birini tanlang.",reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(From_User.product_name_user)  

@dp.message(F.text, From_User.product_name_user)
async def ProductAddbot(message: Message, state: FSMContext):
    user_id = message.from_user.id
    category_name = message.text
    categories = categoryRead()
    for i in categories:
        if i[1]==category_name:
            await state.update_data({
             "Category_id":i[0],
             "Category_name":i[1],
             "user_id":user_id
             })
    data = await state.get_data()
    category = data.get("Category_id")
    builder=ReplyKeyboardBuilder()
    products = productRead(category)
    for i in products:
        builder.add(types.KeyboardButton(text = F"{i[1]}"))
    builder.add(types.KeyboardButton(text ="⬅️ ortga"))
    builder.adjust(2)
    await message.answer("Prooduct birini tanlang.",reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(From_User.product_count_user)  

def create_inline_keyboard(count: int) ->InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [  # Birinchi qator
            InlineKeyboardButton(text="⬅️ ozroq", callback_data="ozroq"),
            InlineKeyboardButton(text=f"📦 {count}", callback_data="count"),
            InlineKeyboardButton(text="➡️ yana", callback_data="yana")
        ],
        [  # Ikkinchi qator
            InlineKeyboardButton(text="buyurtma berish", callback_data="buyurtma")
        ]
    ])
    return keyboard

@dp.message(F.text, From_User.product_count_user)
async def ProductAddbot(message: Message, state: FSMContext):
    product_name = message.text
    data = await state.get_data()
    category = data.get("Category_id")
    products = productRead(category)
    for i in products:
        if i[1]==product_name:
            photo=f"{i[3]}"
            price=f"{i[2]}"
    global product_count
    product_count = 0  # Boshlang'ich qiymat
    await message.answer_photo(photo=photo,caption=f"{product_name} narxi-{price}\nMahsulot miqdorini tanlang!", reply_markup=create_inline_keyboard(product_count))
    await state.update_data({
        "product_name":product_name
    })

    builder=ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text ="⬅️ ortga"))

@dp.callback_query(F.data=="buyurtma")
async def process_callback(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({
        "product_count":product_count
        })
    await state.set_state(From_User.product_contact_user) 
    await call.message.answer(text =f"Contact yuboring!",reply_markup=contact)

@dp.message(lambda message: message.content_type == ContentType.CONTACT)
async def ContactBot(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data({
        "contact":contact
        })
    await message.answer(text="Location yuboring!",reply_markup=location)

@dp.message(lambda message: message.content_type == ContentType.LOCATION)
async def ContactBot(message: Message, state: FSMContext):
    latitude = message.location.latitude  # Latitude (Kenglik)
    longitude = message.location.longitude
    await state.update_data({
        "latitude":latitude,
        "longitude":longitude
        })
    data = await state.get_data()
    photo = data.get("photo")
    product_count = data.get("product_count")
    contact = data.get('contact')
    product_name= data.get("product_name")
    category_name = data.get("Category_name")
    await message.answer(text=f"{message.from_user.full_name} siz haqiqatdan ham quyidagini sotip olmoqchimisz!!!\ncategory: {category_name},\nproduct_name: {product_name},\nproduct_count: {product_count} ta",reply_markup=accept_user)
    await state.set_state(From_User.product_accept_user)


@dp.callback_query(F.data=="ha",From_User.product_accept_user)
async def process_callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.reply("Buyurtma adminga yuborildi,iltimos admin javobini kuting!")
    data = await state.get_data()
    product_count = data.get("product_count")
    contact = data.get('contact')
    product_name= data.get("product_name")
    category_name = data.get("Category_name")
    latitude=data.get('latitude')
    longitude=data.get('longitude')
    user_id =call.message.from_user.id
    await bot.send_message('5072268247',"YANGI BUYURTMA!!!")
    await bot.send_location("5072268247",latitude=latitude, longitude=longitude)
    await bot.send_message("5072268247",f"{call.message.from_user.full_name} ismli mijoz,\ncategory: {category_name},\nproduct_name: {product_name},\nproduct_count: {product_count} ta\ncontact: {contact},\nid: {user_id}\nBuyurtmani qabul qilamizmi?",reply_markup=accept_admin)
    # await state.set_state(From_User.admin_state)
    a=await state.get_state()
    print(a)



@dp.callback_query(F.data == "yoq", From_User.product_accept_user)
async def process_callback2(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("buyurtma bekor qilinda",reply_markup=user_sahifa)
    await state.clear()

@dp.callback_query(F.data == "albatta")
async def admin_accept_bot(call:types.CallbackQuery,state: FSMContext):
    print("ishladi")
    data = await state.get_data()
    user_id = call.message.from_user.id
    print("zo'r ishladi")
    print(user_id)
    await bot.send_message("6234035139",text="Zakas yo'lga chiqdi")
    print(call.message.text)

# @dp.callback_query(F.data == "albatta",F.from_user.id == 5072268247 )
# async def albatta_bot(call: types.CallbackQuery):
    


@dp.callback_query()
async def process_callback(call: types.CallbackQuery):
    global product_count
    if call.data == 'ozroq' and product_count > 0:  # Kamaytirish
        product_count -= 1
        await call.message.edit_reply_markup(reply_markup=create_inline_keyboard(product_count))
    elif call.data == 'yana':  # Ko‘paytirish
        product_count += 1
        await call.message.edit_reply_markup(reply_markup=create_inline_keyboard(product_count))



    
    
    






    







async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")