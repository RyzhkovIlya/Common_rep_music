# from flask import Flask
# from api.musicmatcher import rec_music
import logging
from dotenv import load_dotenv
import os
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import time
from static.text import START, INFO
from model_test import similar_artist
import nltk
from api.musicmatcher import read_text, tfidf
nltk.download('stopwords')
load_dotenv()
API_TOKEN = os.getenv('TOKEN_GENIUS')
# app = Flask(__name__)
# @app.route('/', methods=['GET'])
# def index():
#     return 'Привет', 200
#     # return render_template('index.html', header=HEADER), 200
#
# @app.route('/result', methods=['GET'])
# def user_match():
#     result = rec_music()
#     # return render_template('index.html', header=result), 200
#     return  result, 200
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8080) #debug-перезапуск сервера автоматически

logging.basicConfig(filename='log1.log',
                    # encoding='utf-8',
                    level=logging.INFO)

# Загрузка токена через env
load_dotenv()
TOKEN = os.getenv('TOKEN_TELEGRAM')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_id} запустил бота в {time.asctime()}')
    await message.reply(START % user_name, parse_mode='Markdown')


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)

text_dict = read_text(API_TOKEN)

artists_similarity = tfidf(text_dict)

dict_of_artist_similary = dict(zip(text_dict.keys(), artists_similarity))

@dp.message_handler()
async def echo_message(message: types.Message):
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type != 'text':
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, 'Пришлите текст - одно слово, другие типы данных не поддерживаются')
    # elif not txt.isalpha():
    #       logging.info(f'Нам написал {user_name}, его id = {user_id}')
    #     await bot.send_message(user_id, 'Пришлите одно слово, без цифр и специальных символов')
    elif len(txt) > 15:
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, 'Пришлите одно слово длиной не более 15 символов')
    else:
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(similar_artist(txt, dict_of_artist_similary, text_dict))


if __name__ == '__main__':
    executor.start_polling(dp)