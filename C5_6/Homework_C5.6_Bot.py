'''
Имя бота  -  infomoneychange (@infomoneychangeBot).
Предоставляет курс конвертации для большинства известных валют.
Не округляет, если значение меньше 0,01.
Позволяет сравнить валюту саму с собой).
Бесплатный API позволяет делать конвертацию, только через базовый элемент(USD).

'''



import telebot
from extensions import APIException, Convert, list_of_cur
from config import TOKEN, money


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def helper(message):
    text = ''' Приветствую вас.
Чтобы узнать курс конвертации, необходимо сделать следующее -
ввести через пробел:\n
<имя валюты, цену которой надо узнать>
<имя валюты, в которой надо узнать цену первой валюты>
<количество первой валюты (если указывает дробное число, то в качестве разделителя используйте ".")>.\n
Можно еще ввести: /help и я повторю для вас это сообщение ещё раз
или /value и я покажу самые популярные валюты.
Ещё можно ввести - /value_all и я покажу все доступные валюты.
'''
    bot.reply_to(message,text)

@bot.message_handler(commands=['value'])
def list_value(message: telebot.types.Message):
    text = 'Список популярных валют: '
    for i in money.keys():
        text += '\n' + i
    bot.reply_to(message,text)

@bot.message_handler(commands=['value_all'])
def list_value_all(message: telebot.types.Message):
    list_cur ='Все доступные валюты:\n'
    for i,j in list_of_cur.items():
        list_cur += '\n'+ i + ' - ' + j
    list_cur +='\n\nВводить в формате "XXX YYY Q", где ХХХ и YYY международное обозначение валюты, а - Q сумма'
    bot.reply_to(message,list_cur)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    param = message.text.split(' ')
    try:

        if len(param) != 3:
            raise APIException('Необходимо ввести 3 параметра')
        quote, base, amount = param
        quote = quote.upper()
        base = base.upper()
        convers = Convert.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Возможно, вы где-то ошиблись\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Бот сломался, скоро починим\n{e}')

    else:
        if quote and base in money.keys():
            text = f'Цена {amount} {money[quote]} = {convers} {money[base]}'
        else:
            text = f'Цена {amount} {quote} = {convers} {base}'
        bot.send_message(message.chat.id, text)







bot.polling(none_stop=True)