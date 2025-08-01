"""
Конфигурационный файл для Telegram_bot.

Основные настройки, необходимые для работы бота

Attributes:
    TOKEN (str): Токен, полученный у BotFather, генерируется при регистрации нового бота
    keys (dict): Библиотека для взаимодействия с telegram API - словарь "ключ: тикер"
"""


TOKEN = '7885197025:AAGAfwvQtiHtDtVfSlGfWQE-Hbpu54zLmIM'

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'солана': 'SOL',
    'догкоин': 'DOGE',
    'доллар': 'USD',
    'евро': 'EUR'
}