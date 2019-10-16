# Async chat

Scripts for asynchronous reading/writing chat messages from CLI


## How to install

Python 3.7 has to be installed. You might have to run python3 instead of python depending on system if there is a conflict with Python2. Then use pip (or pip3) to install dependencies:

```commandline
pip install -r requirements.txt
```
## How to use

There are several parameters which can be specified in .env file. They will be used by default if script is run without any keys.

```
HOST=minechat.dvmn.org
READER_PORT=5000
WRITER_PORT=5050
HISTORY_FILE=history.txt
TOKEN=######################
```

Run `python read_chat.py` to read incoming messages or `python write_chat.py --message ' '` to send message to chat.

```
python3 read_chat.py --help
usage: read_chat.py [-h] [--host HOST] [--iport IPORT] [--oport OPORT]
                    [--history HISTORY] [--message MESSAGE] [--token TOKEN]

optional arguments:
  -h, --help         show this help message and exit
  --host HOST        Specify hostname. Default is minechat.dvmn.org
  --iport IPORT      Specify remote port to read data. Default is 5000
  --oport OPORT      Specify remote port to send data. Default is 5050
  --history HISTORY  Specify file to save history. Default is history.txt
  --message MESSAGE  Message to chat
  --token TOKEN      Token for registered user
```


## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
