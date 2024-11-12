@echo off
REM Создание виртуального окружения
python -m venv venv

REM Активация виртуального окружения
call venv\Scripts\activate

REM Обновление pip
python.exe -m pip install --upgrade pip

REM Установка зависимостей из requirements.txt
pip install -r requirements.txt

echo Установка завершена!
pause
