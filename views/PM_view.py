from models.private_messages_model import PM
import datetime


def show_PM_panel(user_login, receiver):
    messages = PM.get_recent_messages()

    if messages != []:
        print('========Private Message========')
        for message in messages:
            date_formatted = message.date.strftime('%d.%m.%y/%H:%M')
            if ((message.author == user_login and message.receiver == receiver) or
                (message.author == receiver and message.receiver == user_login)):
                print ('<{}> {}: {}'.format(date_formatted, message.author, message.message))


def enter_message(author, receiver):
    text = 'Enter message (or type ~ to exit): '
    message = input(text)
    max_length = 99
    while len(message) > max_length:
        print('Message has to be shorter than {} characters, try again!'.format(max_length))
        message = input(text)
    if message == '~':
        pass
    else:
        PM(datetime.datetime.now(), author, receiver, message)
