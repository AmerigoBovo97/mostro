from sqlitedict import SqliteDict
from DataSet import *
import time

"""In questo file ci sono tutte le funzioni di sistema"""


def save(key, value, cache_file='utenti.sqlite3'):
    """Questa funzione permette di salvare ugni istanza su un file"""

    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value  # Using dict[key] to store
            mydict.commit()  # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data save (Possibly unsupported):", ex)


def load(key, cache_file='utenti.sqlite3'):
    """Questa funzione permette di scaricare un dizionario che rappresenta un'istanza salvata in precedenza"""

    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key]  # No need to use commit(), since we are only loading data!
        return vars(value)
    except Exception as ex:
        print("Error during loading data load:", ex)


def changer(dict):
    new_istance = User(dict)
    save(dict['chat_id'], new_istance)
    del new_istance


def on_chat_message(msg):
    """richiama una funzione dal messaggio testuale dell'utente"""

    chat_id = msg['chat']['id']
    text = msg['text']
    try:
        obj = load(chat_id)
        print(obj)
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
