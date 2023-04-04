from aiogram import Bot, Dispatcher, executor, types
from confing import token
import sqlite3
import time

bot = Bot(token)
dp = Dispatcher(bot)

db = sqlite3.connect('users.db')
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        id INTEGER,
        created VARCHAR(255)
    );
""")
cursor.connection.commit()

@dp.message_handler(commands=['start', 'go', 's'])
async def start(message:types.Message):
    cursor = db.cursor()
    cursor.execute(f"SELECT id FROM users WHERE id = {message.chat.id};")
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}', 
        '{message.from_user.first_name}', '{message.from_user.last_name}',
        {message.chat.id}, '{time.ctime()}');""")
    cursor.connection.commit()
    await message.answer(f"Привет {message.from_user.full_name} вот наши курсы: \n/android- информация о курсе андроид \n/frontend- информация о курсе фронтед \n/backend-информация о курсе бэкенд \n/uxui-инфрормац ия о ui дизайнера  \n/ios - инфориация о ios разработке ")

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer("Вот мои комманды\n/start - запустить бота \n/android- информация о курсе андроид \n/frontend- информация о курсе фронтед \n/backend-информация о курсе бэкенд \n/uxui-инфрормац ия о ui дизайнера  \n/ios - инфориация о ios разработке")

@dp.message_handler(text=["здравствуйте"])
async def hello(message:types.Message):
    await message.reply("Привет")

@dp.message_handler(commands=['android'])
async def test(message:types.Message):
    await message.reply("Что делает Android-разработчик Он создает и поддерживает приложения на операционной системе Android. На ней работают не только смартфоны, но и планшеты, умные часы, а также Smart TV. Именно от разработчика зависит, насколько удобным и функциональным будет приложение.обучения стоит 10 тысяч длительность обучения 5 месяцов")

@dp.message_handler(commands=['frontend'])
async def test(message:types.Message):
    await message.reply("Что делает Фронтенд разработчика? Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы. Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так, чтобы все работало правильно.обучение стоит 10 тысяч длительность обучения 7 месяцов")
    
@dp.message_handler(commands=['backend'])
async def test(message:types.Message):
    await message.reply("Back-end (бэкенд) разработка — это создание серверной части в веб-приложениях. То есть backend разработчики имеют дело со всем, что относится к базам данных, архитектуре, программной логике — в общем, со всем, что обычный пользователь не видит.стоимость обучения 8 тысяч длительность 6 месяцов") 

@dp.message_handler(commands=['uxui'])
async def test(message:types.Message):
    await message.reply("UX/UI дизайнер — специалист, который проектирует и рисует интерфейсы цифровых продуктов: мобильных и веб-приложений, сайтов. Такой дизайнер может участвовать как в создании новых продуктов, так и помогать дорабатывать те, что уже запущены.обучение стоит 8 тысяч длительность 5 месяцов")

@dp.message_handler(commands=['ios'])
async def test (message:types.Message):
    await message.reply("iOS-разработчик, или iOS developer, — это программист, который пишет сервисы и программы для айфонов. Из-за особенностей устройств Apple и их операционной системы для них нужно писать специальный код. Основной язык, на котором пишут код iOS-разработчики, — Swift.стоимость обучения 12 тысяч длительность курса 8 месяцув")
    

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)