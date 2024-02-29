from aiogram import Router,types,F
from aiogram.filters import Command
from filters.chat_types import ChatTypeFilter
from string import punctuation

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group",'supergroup']))



bad_words = {'bad','word','badword','bad_word'}


def cleen_word(word:str):
    return word.translate(str.maketrans('', '', punctuation)).lower()


@user_group_router.message()
async def check_words(message: types.Message):
    if bad_words.intersection(message.text.lower().split()):
        cleen_word(message.text.lower())
        await message.answer('You used a bad word!')
        await message.delete()
        # await message.chat.ban(message.from_user.id)

    # await message.answer(message.text)

