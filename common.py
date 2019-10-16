import asyncio
import datetime
import argparse
import os
from dotenv import load_dotenv

load_dotenv()


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--host',
        help='Specify hostname. Default is minechat.dvmn.org',
        default=os.getenv('HOST')
    )
    parser.add_argument(
        '--iport',
        help='Specify remote port to read data. Default is 5000',
        default=os.getenv('READER_PORT')
    )
    parser.add_argument(
        '--oport',
        help='Specify remote port to send data. Default is 5050',
        default=os.getenv('WRITER_PORT')
    )
    parser.add_argument(
        '--history',
        help='Specify file to save history. Default is history.txt',
        default=os.getenv('HISTORY_FILE')
    )
    parser.add_argument(
        '--message',
        help='Message to chat',
        type=str
    )
    parser.add_argument(
        '--token',
        help='Token for registered user',
        default=os.getenv('TOKEN'),
        type=str
    )
    return parser.parse_args()


def write_message_to_file(history, message, nickname=None):
    now = datetime.datetime.now()
    if not nickname:
        with open(history, 'a') as file:
            file.write(f'[{now.strftime("%d.%m.%y %H:%M")}] {message}')
    else:
        with open(history, 'a') as file:
            file.write(f'[{now.strftime("%d.%m.%y %H:%M")}] {nickname}: {message}\n')
