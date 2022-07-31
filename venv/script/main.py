import time
from UserFunctions import *
"""In questo file ci sono le funzioni principali del bot"""


def on_chat_message(msg):
    """richiama una funzione dal messaggio testuale dell'utente"""

    chat_id = msg['chat']['id']
    text = msg['text']
    try:
        obj = load(chat_id)
    except:
        print('Errore nel loading')
    if text in funcs:
        funcs[msg['text']](msg)
    elif not obj['monster_creator']:
        monster_step(msg)
    else:
        bot.sendMessage(chat_id, 'questo comando non esiste')


def on_callback_query(msg):
    print('sasso')


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


runner()






