from prettytable import PrettyTable
from Mostri_definitivo.venv.script.bot import bot
from theDatas import *
import json


def save(user):
    chat_id = user['chat_id']
    with open(f'utenti/{chat_id}.json', 'w') as f:
        json.dump(user, f, indent=4)


def load(chat_id):
    with open(f'utenti/{chat_id}.json', 'r') as f:
        return dict(json.load(f))


def next_step(step):
    """ritorna lo step successivo da assegnare a: user['passaggio']"""

    cul = [x for x in componenti.keys()]
    return cul[cul.index(step) + 1]


def setter(user, step, text):
    """assegna nuovi valori a user['componenti'] e user['passaggio'] per poi salvarli"""

    user['componenti'][step] = text
    user['passaggio'] = next_step(step)
    save(user)


def table_creator(obj):
    """2crea uo oggetto tabella con gli attributi che interessano e li printa"""

    obj_table = PrettyTable()
    obj_table.field_names = ['KEY', 'VALUE']
    obj_table.add_row(['monster_creator', obj['monster_creator']])
    obj_table.add_row(['passaggio', obj['passaggio']])
    for x in obj['componenti']:
        obj_table.add_row([x, obj['componenti'][x]])
    print(obj_table)


def setter_requester(user, step, text, chat_id):
    """oltre che a richiamre la modifica di un componente invia anche all'utente il messaggio di richiesta nuovo componente"""

    if monster_steps[step]['condizione'](text, user):
        setter(user, step, text)
        bot.sendMessage(chat_id, monster_steps[next_step(step)]['richiesta'],
                        reply_markup=monster_steps[next_step(step)]['keyboard_bottom'])
    else:
        bot.sendMessage(chat_id, monster_steps[step]['errore'],
                        reply_markup=monster_steps[step]['keyboard_bottom'])



