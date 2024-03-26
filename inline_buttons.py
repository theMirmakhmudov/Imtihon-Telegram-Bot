from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

builder = InlineKeyboardBuilder()
builder.row(types.InlineKeyboardButton(
    text="Batafsil", callback_data="batafsil")
)
builder.row(types.InlineKeyboardButton(
    text="Buyurtma berish",
    url="https://t.me/all_hp")
)
