import asyncio
import socket
import common
import logging


async def get_data_from_server(host, port):
    try:
        reader, _ = await asyncio.open_connection(host, port)
        data = await asyncio.wait_for(reader.readline(), timeout=5)
    except (asyncio.TimeoutError,
            ConnectionRefusedError,
            socket.gaierror):
        return None
    return data


async def check_answer_timeout(counter):
    if counter > 5 and counter < 10:
        common.write_message_to_file(
            'No connection. Trying to connect in 5 secs...\n'
            )
        await asyncio.sleep(5)
    elif counter >= 10:
        common.write_message_to_file(
            'No connection. Trying to connect in 20 secs...\n'
            )
        await asyncio.sleep(20)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    counter = 0
    args = common.get_parser_args()
    while True:
        data = await get_data_from_server(args.host, args.iport)
        if not data:
            logging.debug('No connection')
            await check_answer_timeout(counter)
            counter += 1
        else:
            common.write_message_to_file(args.history, data.decode())
            counter = 0


if __name__ == "__main__":
    asyncio.run(main())
