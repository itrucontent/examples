from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from aiogram import F
from dotenv import load_dotenv
import os
load_dotenv()


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Функция для установки команд бота в меню
async def set_commands():
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь по использованию бота"),
        BotCommand(command="caps", description="Преобразовать текст в ЗАГЛАВНЫЕ буквы")
    ]
    await bot.set_my_commands(commands)


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

@dp.message(Command(commands=['caps']))
async def text_caps(message: Message):
    text_parts = message.text.split(maxsplit=1)
    if len(text_parts) > 1:
        text_change = text_parts[1].upper()
        await message.reply(text_change)
    else:
        await message.reply("Введите текст после команды /caps")

@dp.message(Command(commands=['reverse']))
async def text_reverse(message: Message):
    text_parts = message.text.split(maxsplit=1)
    if len(text_parts) > 1:
        text_change = text_parts[1][::-1]
        await message.reply(text_change)
    else:
        await message.reply("Введите текст после команды /reverse")

@dp.message(F.text.lower().in_(['hi', 'hello', 'салют']) | F.text.startswith("здрав") | F.text.startswith("привет"))
async def say_hello(message: Message):
    await message.answer("И вам здравствуйте!")

@dp.message(F.text.isdigit())
async def good_deel(message: Message):
    await message.reply("Похоже намечается серьезная сделка?")

@dp.message(F.text.endswith("?"))
async def send_question(message: Message):
    await message.reply("Похоже у вас серьезный вопрос")

@dp.message(F.photo)
async def send_photo(message: Message):
    if message.caption is not None:
        await message.reply(text=f'Что это за {message.caption}')
    else:
        await message.reply("Данный формат не поддерживается")


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)