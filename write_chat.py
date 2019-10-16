import asyncio
import common
import json
import logging


async def autorize(writer, reader, token):
    writer.write(f'{token}\n'.encode())
    data = await reader.readline()
    if data.decode() == 'null\n':
        logging.debug('Token is invalid')
        await register(writer, reader)
    else:
        account_info = json.loads(data.decode())
        logging.debug(account_info)
    return account_info


async def register(writer, reader):
    nickname = input('Enter preffered nickname: ').replace('\n', ' ')
    writer.write(f'{nickname}\n'.encode())
    data = await reader.readline()
    logging.debug(data.decode())
    return json.loads(data.decode())


async def submit_message(writer, history, nickname, message):
    message = message.replace('\n', ' ')
    writer.write(f'{message}\n\n'.encode())


async def main():
    logging.basicConfig(level=logging.DEBUG)
    args = common.get_parser_args()
    reader, writer = await asyncio.open_connection(args.host, args.oport)
    if await reader.readline():
        if args.token:
            account_info = await autorize(writer, reader, args.token)
        else:
            writer.write('\n'.encode())
            await reader.readline()
            account_info = await register(writer, reader)
        await submit_message(
            writer,
            args.history,
            account_info['nickname'],
            args.message
            )
    writer.close()


if __name__ == '__main__':
    asyncio.run(main())
