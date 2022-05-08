import time

import telebot

bot = telebot.TeleBot("5293310216:AAEiH3uQStJe9sLLaWWNIQ4MShR_UGMbLgk")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat_id, "Привет! Я бот, сделланный на python3")
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, здесь ты можешь пройти викторину на знание Истории России")
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         'Напиши: \n Викторина, чтобы проверить свои знания'
                         '\n Помощь — для получение информации о том, что нужно сделать)')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Викторина':
        bot.send_message(message.chat.id, 'Итак, это викторина создана для проверки ваших исторических знаний.'
                                          'Желаю удачи!!!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Ну чтож, начнем нашу викторину.')
        time.sleep(1.5)
        bot.send_message(message.chat.id, 'Итак первый вопрос!!!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Кто из правителей России первым официально объявил себя императором?')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Иван Грозный')
        bot.send_message(message.chat.id, 'Петр I')
        bot.send_message(message.chat.id, 'Николай II')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(30)

    elif message.text == 'Иван Грозный':
        bot.send_message(message.chat.id, 'Отлично, у вас получилось')
        bot.send_message(message.chat.id, "Идем дальше")

        bot.send_message(message.chat.id, 'В каком году Пётр I изменил основной титул с «Государь,'
                                      ' Царь и Великий князь всея Руси» на «Император Всероссийский»?')
        bot.send_message(message.chat.id, '1721')
        bot.send_message(message.chat.id, '1723')
        bot.send_message(message.chat.id, '1739')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(15)

    elif message.text == '1721':
        bot.send_message(message.chat.id, 'Отлично, у вас получилось')
        bot.send_message(message.chat.id, "Следущий вопрос")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Кто из императоров России первым в истории направился с дипломатическим'
                                 ' визитом за границу (в Европу)?')
        bot.send_message(message.chat.id, 'Николай I')
        bot.send_message(message.chat.id, 'Александр II')
        bot.send_message(message.chat.id, 'Петр I')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(15)

    elif message.text == 'Петр I':
        bot.send_message(message.chat.id, 'класс')
        bot.send_message(message.chat.id, "Следущий вопрос")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Кому из императриц Российской империи верховный тайный совет попытался'
                                 ' навязать «Кондиции» связывающие императорскую власть?')
        bot.send_message(message.chat.id, 'Елизавета Петровна')
        bot.send_message(message.chat.id, 'Анна Иоанновна')
        bot.send_message(message.chat.id, 'Екатерина Великая')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(15)

    elif message.text == 'Анна Иоанновна':
        bot.send_message(message.chat.id, 'хорошо')
        bot.send_message(message.chat.id, "Следущий вопрос")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Какое событие произошло во время перехода власти от Александра I к Николаю I?')
        bot.send_message(message.chat.id, 'Восстание декабристов')
        bot.send_message(message.chat.id, 'Стрелецкий бунт')
        bot.send_message(message.chat.id, 'Пугачевщина')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(15)

    elif message.text == 'Восстание декабристов':
        bot.send_message(message.chat.id, 'хорошо')
        bot.send_message(message.chat.id, "Следущий вопрос")
        time.sleep(2)

        bot.send_message(message.chat.id, '«Распутная императрица» – кого так называли?')
        bot.send_message(message.chat.id, 'Екатерина II')
        bot.send_message(message.chat.id, 'Екатерина I')
        bot.send_message(message.chat.id, 'Елизавета Петровна')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(30)

    elif message.text == 'Екатерина II':
        bot.send_message(message.chat.id, 'у вас неплохо получается')
        bot.send_message(message.chat.id, "Остался последний вопрос")
        time.sleep(2)

        bot.send_message(message.chat.id, 'Кто из императоров стал последним? ')
        bot.send_message(message.chat.id, 'Павел I')
        bot.send_message(message.chat.id, 'Михаил II')
        bot.send_message(message.chat.id, 'Иван VI')
        bot.send_message(message.chat.id, "Ваш ответ?")
        time.sleep(30)

    elif message.text == 'Михаил II':
        bot.send_message(message.chat.id, 'Вы ответили правильно на все вопросы!!!')
        end_message()

    elif message.text.strip() == 'Помощь':
        bot.send_message(message.from_user.id, "Привет, тебе нужно пройти викторину чтобы проверить свои знания."
                                           "Надеюсь у тебя полится\n")
    else:
        end_message(message)
        time.sleep(20)
        bot.close()


@bot.message_handler(commands=['exit'])
def end_message(message):
    bot.send_message(message.from_user.id, "Пока!")


bot.polling(none_stop=True, interval=0)
exit()