import time
from UserFunctions import *
from telepot.namedtuple import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
import time

"""In questo file ci sono le funzioni principali del bot"""


def on_chat_message(msg):
    """richiama una funzione dal messaggio testuale dell'utente"""

    chat_id = msg['chat']['id']
    text = msg['text']
    try:
        obj = load(chat_id)
    except:
        print('Errore nel loading')
    finally:
        if text in funcs:
            funcs[msg['text']](msg)
        elif obj['monster_creator']:
            monster_step(msg)
        else:
            bot.sendMessage(chat_id, 'questo comando non esiste')


def on_callback_query(msg):
    chat_id = msg['message']['chat']['id']
    text = msg['data']
    obj = load(chat_id)
    query_func, query_step, query_text = text.split('!')

    if query_func in funcs:
        funcs[query_func](query_step, query_text, obj)



def runner():
    """riceve i messaggi e reindirizza asseconda del flavour"""
    """il flavour di un messaggio è il tipo di contenuto, se è un testo allora il flavour è chat,
    se è una risposta predefinita ricevuta dopo la pressione di un tasto menù, per esempio, callback query"""

    while True:
        bot.message_loop({
            'chat': on_chat_message,
            'callback_query': on_callback_query
        })

        while True:
            time.sleep(1)


if __name__ == "__main__":
    runner()
