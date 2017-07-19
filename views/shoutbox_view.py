from models.shoutbox_model import Shoutbox
import datetime


def show_shoutbox_panel():
    messages = Shoutbox.get_recent_messages()

    if messages != []:
        print('     SHOUTBOX')
        for message in messages:
            date_formatted = message.date.strftime('%d.%m.%y/%H:%M')
            print ('<{}> {}: {}'.format(date_formatted, message.author, message.message))


def enter_message(author):
    message = input('Enter message: ')
    max_length = 20
    while len(message) > max_length:
        print('Message has to be shorter than {} characters, try again!'.format(max_length))
        message = input('Enter message: ')
    Shoutbox(datetime.datetime.now(), author, message)
