import telebot
from conf import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Для начала работы, введите команду в формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты \n Список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        
        if len(values) != 3:
            raise ConvertionException('слишком много параметров.')
        
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
        amount = float(amount)
        total_cost = total_base * amount

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')

    else:
        text = f'Цена {amount} {quote} в {base} - {total_cost}'
        bot.send_message(message.chat.id, text)

# Добавить вывод total_base с учетом amount

bot.polling(none_stop=True)
