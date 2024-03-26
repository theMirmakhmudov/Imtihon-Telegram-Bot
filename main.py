import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import types
from config import TOKEN
from buttons import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7
from inline_buttons import builder

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"""
Assalomu Alaykum, {message.from_user.full_name} !

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

O'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.

Toshkent bo'ylab yetkazib berish - 20 000 so'm.
O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, 🔥 Mahsulotlar bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.
""", reply_markup=keyboard1)


@dp.message(F.text == "🔥 Mahsulotlar")
async def cmd_product(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard2)


@dp.message(F.text == "🏠 Bosh Menu")
async def cmd_back(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard1)


@dp.message(F.text == "ℹ️ Ma'lumot")
async def cmd_info(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard3)


@dp.message(F.text == "💼 Hamkorlik")
async def cmd_partner(message: types.Message):
    await message.answer("""
Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.

Menejer bilan bog'lanish uchun: @all_hp
    """)


@dp.message(F.text == "🚀 Yetkazib berish shartlari")
async def cmd_delivery(message: types.Message):
    await message.answer("""
Yetkazib berish shartlari:
O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
Toshkent bo'ylab yetkazib berish - 20 USD.
O‘zbekiston bo'ylab yetkazib berish - 30 USD.

1 000 USD dan ortiq buyurtmalarni yetkazib berish - tekin!
    """)


@dp.message(F.text == "☎️ Kontaktlar")
async def cmd_contact(message: types.Message):
    user = "Mr.Mirmakhmudov"
    contact = "+998913483370"
    await message.answer_contact(contact, first_name=user)


@dp.message(F.text == "Phone")
async def cmd_phone(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard4)


@dp.message(F.text == "Watch")
async def cmd_watch(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard5)


@dp.message(F.text == "Laptop")
async def cmd_laptop(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard6)


@dp.message(F.text == "Keyboard")
async def cmd_keyboard(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=keyboard7)


@dp.message(F.text)
async def cmd_product_1(message: types.Message):
    if message.text == "Product 1" or message.text == "Product 2" or message.text == "Product 3" or message.text == "Product 4":
        await message.answer_photo(photo="https://elmakon.uz/images/detailed/37/photo_2022-12-28_12-42-32.jpg", caption="""
iPhone 14 Pro

Apple IPhone 14 Pro Max, Deep Purple, 128 GB✔️

Apple: 100% Phone

Apple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!

Product code: 54

Narxi: 1500 USD    
""", reply_markup=builder.as_markup())

    elif message.text == "Watch 1" or message.text == "Watch 2" or message.text == "Watch 3" or message.text == "Watch 4":
        await message.answer_photo(
            photo="https://fossil.scene7.com/is/image/FossilPartners/FS6029_main?$sfcc_fos_medium$", caption="""

iPhone 14 Pro

Apple IPhone 14 Pro Max, Deep Purple, 128 GB✔️

Apple: 100% Phone

Apple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!

Product code: 54

Narxi: 1500 USD    
""", reply_markup=builder.as_markup())

    elif message.text == "Laptop 1" or message.text == "Laptop 2" or message.text == "Laptop 3" or message.text == "Laptop 4":
        await message.answer_photo(
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST7PYyFVm-6WZkeRD7FsM8zlGa1G_NRA2EMl3eJoQOoPsqTP7k0bsoqXITGsRxdAof3b0&usqp=CAU",
            caption="""

iPhone 14 Pro

Apple IPhone 14 Pro Max, Deep Purple, 128 GB✔️

Apple: 100% Phone

Apple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!

Product code: 54

Narxi: 1500 USD    
""", reply_markup=builder.as_markup())

    elif message.text == "Keyboard 1" or message.text == "Keyboard 2" or message.text == "Keyboard 3" or message.text == "Keyboard 4":
        await message.answer_photo(
            photo="https://i.ebayimg.com/images/g/Ik8AAOSwdqJid-3l/s-l1600.jpg",
            caption="""

iPhone 14 Pro

Apple IPhone 14 Pro Max, Deep Purple, 128 GB✔️

Apple: 100% Phone

Apple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!

Product code: 54

Narxi: 1500 USD    
""", reply_markup=builder.as_markup())


@dp.callback_query(F.data == "batafsil")
async def send_batafsil(callback: types.CallbackQuery):
    await callback.answer(
        text="""
IOS : 16
IPhone 14 Pro Max
Display: 120 Gz
Video Format: 3840x2160
        """,
    show_alert=True
    )


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
