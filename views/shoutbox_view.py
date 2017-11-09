from models.shoutbox_model import Shoutbox
import datetime


def show_shoutbox_panel():
    messages = Shoutbox.get_recent_messages()

    if messages != []:
        print('========SHOUTBOX========')
        for message in messages:
            date_formatted = message.date.strftime('%d.%m.%y/%H:%M')
            print ('<{}> {}: {}'.format(date_formatted, message.author, message.message))


def enter_message(author):
    text = 'Enter message (or type ~ to exit): '
    message = input(text)
    max_length = 40
    while len(message) > max_length:
        print('Message has to be adasdshorter than {} characters, try again!'.format(max_length))
        message = input(text)
    if message == '~':
        pass
    else:
        Shoutbox(datetime.datetime.now(), author, message)
swds
