from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "").strip()

if not TOKEN:
    raise SystemExit("Ошибка: BOT_TOKEN не задан (проверьте .env)")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    # Если WEBAPP_URL пустой — покажем подсказку
    if WEBAPP_URL:
        btn = types.InlineKeyboardButton(
            text="Открыть мини‑приложение",
            web_app=types.WebAppInfo(url=WEBAPP_URL)
        )
        keyboard.add(btn)
        await message.answer("Нажмите кнопку, чтобы открыть мини‑приложение:", reply_markup=keyboard)
    else:
        await message.answer("WEBAPP_URL не настроен. Установите его в .env и перезапустите бота.")

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Отправьте /start чтобы получить кнопку Web App.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)