from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .kb_cancel_fsm import btn_cancel
kb_g_type = ReplyKeyboardMarkup(resize_keyboard=True)

btn_jacket = KeyboardButton(text='jacket')
btn_shirt = KeyboardButton(text='shirt')
btn_jeans = KeyboardButton(text='jeans')
btn_shoes = KeyboardButton(text='shoes')

kb_g_type.add(btn_jacket, btn_shirt, btn_jeans, btn_shoes)
kb_g_type.add(btn_cancel)
