import asyncio
import socket
import logging
import datetime
import argparse
import os
from dotenv import load_dotenv

load_dotenv()


def get_reader_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '--host',
        help='Specify hostname. Default is minechat.dvmn.org',
        default=os.getenv('HOST')
    )
    parser.add_argument(
        '--port',
        help='Specify remote port to read data. Default is 5000',
        default=os.getenv('READER_PORT')
    )
    parser.add_argument(
        '--history',
        help='Specify file to save history. Default is history.txt',
        default=os.getenv('HISTORY_FILE')
    )
    parser.add_argument(
        '--debug',
        help='Enable debug',
        default=False,
        )
    return parser.parse_args()


def write_message_to_file(history, message):
    now = datetime.datetime.now()
    with open(history, 'a') as file:
        file.write(f'[{now.strftime("%d.%m.%y %H:%M")}] {message}')


async def get_data_from_server(host, port):
    reader, _ = await asyncio.open_connection(host, port)
    data = await asyncio.wait_for(reader.readline(), timeout=5)
    return data


async def count_reconnection_delay(connection_attempts):
    if connection_attempts < 5:
        return 3
    elif connection_attempts >= 5 and connection_attempts < 10:
        return 10
    elif connection_attempts >= 10:
        return 20


async def wait_before_reconnection(delay, history):
    if delay:
        write_message_to_file(
            history,
            f'No connection. Trying to connect in {delay} secs...\n'
            )
        await asyncio.sleep(delay)


async def main():
    args = get_reader_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    connection_attempts = 0

    while True:
        try:
            data = await get_data_from_server(args.host, args.port)
            write_message_to_file(args.history, data.decode())
            connection_attempts = 0
        except (asyncio.TimeoutError, ConnectionRefusedError, socket.gaierror):
            logging.debug('No connection')
            delay = await count_reconnection_delay(connection_attempts)
            await wait_before_reconnection(delay, args.history)
            connection_attempts += 1
            continue


if __name__ == "__main__":
    asyncio.run(main())
