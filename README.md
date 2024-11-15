# Speech Decoder Bot

**Speech Decoder Bot** – это интеллектуальный Telegram-бот, который принимает голосовые сообщения, конвертирует их в текст и отправляет результат обратно в чат. Этот бот предназначен для облегчения взаимодействия с голосовыми сообщениями и повышения удобства пользователей. 🗣️➡️📜

## Установка

Для установки всех необходимых зависимостей и настройки окружения запустите скрипт `install.bat`:

### Как работает `install.bat`

1. Создаёт виртуальное окружение с помощью команды:
    ```bash
    python -m venv venv
    ```

2. Активирует виртуальное окружение:
    ```bash
    call venv\Scripts\activate
    ```

3. Обновляет pip до последней версии:
    ```bash
    python.exe -m pip install --upgrade pip
    ```

4. Устанавливает зависимости из файла `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

Запустите `install.bat` и дождитесь завершения установки всех зависимостей.

## Основной файл

Основной файл бота – `main.py`. В этом файле реализована логика обработки голосовых сообщений и их конвертации в текст.

### Где менять токен бота

Чтобы настроить токен вашего бота, откройте файл `main.py` и найдите строку:
```python
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
```
Замените `'YOUR_TELEGRAM_BOT_API_TOKEN'` на ваш токен, полученный от BotFather в Telegram.

## Запуск бота

Для запуска бота используйте скрипт `start.bat`:

1. Активирует виртуальное окружение:
    ```bash
    call venv\Scripts\activate
    ```

2. Запускает файл `main.py`:
    ```bash
    python main.py
    ```

Запустите `start.bat`, чтобы активировать виртуальное окружение и запустить бота.