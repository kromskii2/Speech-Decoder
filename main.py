import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import speech_recognition as sr
from pydub import AudioSegment

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=[types.ContentType.VOICE])
async def handle_voice_message(message: types.Message):
    # Сохранение голосового сообщения
    file_info = await bot.get_file(message.voice.file_id)
    file_path = file_info.file_path
    voice_file = f"voice_{message.message_id}.oga"
    wav_file = f"voice_{message.message_id}.wav"

    await bot.download_file(file_path, voice_file)

    # Конвертация .oga в .wav
    audio = AudioSegment.from_ogg(voice_file)
    audio.export(wav_file, format="wav")

    # Распознавание речи
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(wav_file)
    with audio_file as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language='ru-RU')
        await message.answer(f"Распознанный текст: {text}")

        # Удаление голосового сообщения
        os.remove(voice_file)
        os.remove(wav_file)
    except sr.UnknownValueError:
        await message.answer("Не удалось распознать речь.")
    except sr.RequestError as e:
        await message.answer(f"Ошибка сервиса распознавания речи: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
