from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
import logging

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "").strip()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

if not TOKEN:
    logger.error("Ошибка: BOT_TOKEN не задан (проверьте .env)")
    raise SystemExit("Ошибка: BOT_TOKEN не задан (проверьте .env)")

logger.info("BOT_TOKEN set: %s", "yes")
logger.info("WEBAPP_URL: %s", WEBAPP_URL or "(не задан)")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
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

async def on_startup(dp):
    # Удаляем webhook, чтобы polling точно работал
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Webhook удалён (если был).")
    except Exception as e:
        logger.warning("Не удалось удалить webhook: %s", e)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
