import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '1764226729:AAGNHGHzHE6rmOChPotBYTvikfJC8HROaGI'

logging.basicConfig(level=logging.INFO)

bot = Bot(bot=API_OKEN)

db = Dispatcher(bot)

@db.message_handler(cammands=['start', 'salom'])

async def send_welcome(message: types.Message) :
	
	await message.reply("Assalomu alaykum")
	
	
	

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

