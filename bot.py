import logging
from aiogram import Bot, Dispatcher, executor,types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import *
from botky import *

logging.basicConfig(level=logging.INFO)
TOKEN = "6342261010:AAEVKpRp1kxH9gyUwGbqQaEwdRlriJFPTrE"

bot = Bot(token=TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)


async def  on_start_bot(dp):
    await create_tables()

@dp.message_handler(CommandStart())
async def start_bot(message:types.Message):
    await message.answer("Salom")

@dp.message_handler(content_types=["audio"])
async def get_music(message:types.Message):
    music_name = message.audio.performer + " " + message.audio.title
    await insert_data(music_name,message.audio.file_id)


@dp.message_handler(commands=["top"]) 
async def get_all(message: types.Message):
    musics = await get_all_music()
    print(musics)
    music_list = []
    
    for music in musics:
        music_list.append(
            musics[0][1]
        )
    
    for music in music_list:
        await message.answer_audio(music)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_bot)