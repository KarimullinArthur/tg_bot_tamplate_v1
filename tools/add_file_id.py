import logging
import sys

from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

sys.path.append('../src')

from loader import dp, db


logging.basicConfig(level=logging.INFO)


class State(StatesGroup):
    file_id = State()
    name = State()


@dp.message_handler(content_types=['photo', 'video'], state='*')
async def get_id(message: types.Message, state: FSMContext):
    await State.file_id.set()
    if message.content_type == 'photo':
        async with state.proxy() as data:
            data['file_id'] = message.photo[0].file_id
            await message.reply(data['file_id'])

    if message.content_type == 'video':
        async with state.proxy() as data:
            data['file_id'] = message.video.file_id
            await message.reply(data['file_id'])

    await message.reply('name')
    await State.next()


@dp.message_handler(content_types='text', state=State.name)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        db.add_img(data['file_id'], data['name'])

    await message.reply('save')


if __name__ == '__main__':
    logging.info("Send photo or video to your bot\n====")
    executor.start_polling(dp, skip_updates=True)
