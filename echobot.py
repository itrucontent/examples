from aiogram import Bot, Dispatcher
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from dotenv import load_dotenv
import os
load_dotenv()


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

@dp.message(F.content_type.in_({ContentType.PHOTO,ContentType.VOICE,ContentType.VIDEO}))
async def send_text(message: Message):
    await message.answer("Данный формат не поддерживается")

@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)




if __name__ == '__main__':
    dp.run_polling(bot)