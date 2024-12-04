from aiogram.fsm.state import State, StatesGroup

class Form_Cate(StatesGroup):
    category_state = State()
    category_tasdiqlash = State()

class Form_Pro(StatesGroup):
    category_choice = State()
    product_name = State()
    product_price =State()
    product_photo = State()
    product_accept = State()

class From_User(StatesGroup):
    category_user = State()
    product_name_user = State()
    product_count_user = State()
    product_contact_user = State()
    product_location_user = State()
    product_accept_user = State()
    admin_state = State()
    
