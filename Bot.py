import telebot

bot = telebot.TeleBot('5122802878:AAFW_xOdsY772yIqHSf9qT-IzIEl2gfa7as')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'И тебе не подохнуть! <b> {message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, '<b>Ну и тебе привет! </b>', parse_mode='html')
    elif message.text.lower() == 'Как дела':
        bot.send_message(message.chat.id, '<b>Пошел на хер! </b>', parse_mode='html')
    elif message.text.lower() == 'Как твои дела?':
        bot.send_message(message.chat.id, '<b>Пошел на хер! </b>', parse_mode='html')
    elif message.text.lower() == 'Как у тебя дела?':
        bot.send_message(message.chat.id, '<b>Пошел на хер! </b>', parse_mode='html')
    elif message.text.lower() == 'Как твои дела?':
        bot.send_message(message.chat.id, '<b>Пошел на хер! </b>', parse_mode='html')
    elif message.text.lower() == 'Сам пошел на хер':
        bot.send_message(message.chat.id, '<b>Тебе бы заткнуться, кожанный мешок и пойти на хуй</b>', parse_mode='html')
    elif message.text.lower() == 'Иди на хуй':
        bot.send_message(message.chat.id, '<b>Тебе бы заткнуться, кожанный мешок и пойти на хуй</b>', parse_mode='html')
    elif message.text.lower() == 'Сам иди на хуй':
        bot.send_message(message.chat.id, '<b>Тебе бы заткнуться, кожанный мешок и пойти на хуй</b>', parse_mode='html')
    elif message.text.lower() == 'Сам пошел':
        bot.send_message(message.chat.id, '<b>Тебе бы заткнуться, кожанный мешок и пойти на хуй</b>', parse_mode='html')
    elif message.text.lower() == 'Сам иди':
        bot.send_message(message.chat.id, '<b>Тебе бы заткнуться, кожанный мешок и пойти на хуй</b>', parse_mode='html')
    elif message.text.lower() == 'Ты душнила':
        bot.send_message(message.chat.id, '<b>Кожанный мешок с парой извилин что-то хочет сказать?</b>', parse_mode='html')
    elif message.text.lower() == 'Я твой рот ебал':
        bot.send_message(message.chat.id, '<b>Свой спермоприёмник почисть сперва, прежде чем говорить?</b>', parse_mode='html')
    elif message.text.lower() == 'Ты Сухин':
        bot.send_message(message.chat.id, '<b>Гореть тебе в аду!</b>', parse_mode='html')
    elif message.text.lower() == 'Хуй соси':
        bot.send_message(message.chat.id, '<b>Свой сперва подрости</b>', parse_mode='html')
    elif message.text.lower() == 'Пидор':
        bot.send_message(message.chat.id, '<b>Не на твою жопу обвислую</b>', parse_mode='html')
    elif message.text.lower() == 'Чо надо?':
        bot.send_message(message.chat.id, '<b>Жопу твою отодрать бутылкой</b>', parse_mode='html')
    elif message.text.lower() == 'Сам заткнись':
        bot.send_message(message.chat.id, '<b>Ты собака сутулая</b>', parse_mode='html')
    elif message.text.lower() == 'Эй ты':
        bot.send_message(message.chat.id, '<b>Че надо?</b>', parse_mode='html')
    elif message.text.lower() == 'Сука':
        bot.send_message(message.chat.id, '<b>Въеби гавна</b>', parse_mode='html')
    elif message.text.lower() == 'Ты':
        bot.send_message(message.chat.id, '<b>Рот свой от спермы протри! </b>', parse_mode='html')
    elif message.text.lower() == 'Хуй':
        bot.send_message(message.chat.id, '<b>В твой жопе скоро будет</b>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, '<b>Кожанный мешок должен попробовать еще раз написать своими кривыми руками что-то! Например как дела? </b>', parse_mode='html')
bot.polling(none_stop=True)
#конец