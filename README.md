# Telegram Web App (Python + aiogram)

Этот репозиторий содержит минимальный пример: Telegram‑бот на Python (aiogram) который отправляет кнопку открытия Web App и статическое мини‑приложение (Web App) для размещения на GitHub Pages.

Файлы в репозитории:
- main.py — бот на aiogram (polling).
- requirements.txt — зависимости.
- .env.example — пример переменных окружения.
- docs/webapp/index.html — статический Web App, доступный через GitHub Pages.
- .gitignore — стандартный.

Быстрый запуск локально (только бот):
1. Склонируйте репозиторий.
2. Создайте виртуальное окружение и установите зависимости:
   python -m venv venv
   source venv/bin/activate  # или venv\Scripts\activate на Windows
   pip install -r requirements.txt
3. Создайте файл .env на основе .env.example и заполните BOT_TOKEN.
4. (Опционально) Для локальной проверки Web App используйте ngrok и укажите WEBAPP_URL в .env: https://<your-ngrok>.ngrok.io/webapp/index.html
5. Запустите бота:
   python main.py
6. В Telegram откройте бота и отправьте /start — бот пришлёт кнопку для открытия Web App.

Развёртывание Web App на GitHub Pages:
1. Статические файлы мини‑приложения находятся в docs/webapp.
2. В GitHub → Settings → Pages выберите branch: main и folder: /docs. После этого Web App будет доступен по URL:
   https://<your-github-username>.github.io/<repo>/webapp/index.html
3. Установите WEBAPP_URL в .env вашего бота на этот URL и перезапустите бота.

Безопасность:
- Для продакшн: проверяйте подпись initData Web App на бэкенде (Telegram docs).