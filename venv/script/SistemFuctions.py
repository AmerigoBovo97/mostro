import telepot
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
    """Ritorna lo step successivo da assegnare a: user['passaggio']"""

    cul = [x for x in componenti.keys()]
    return cul[cul.index(step) + 1]


def step_setter(user, step):
    """Assegna il nuovo valore a user['passaggio'] per poi salvarlo"""

    user['passaggio'] = next_step(step)
    save(user)


def setter(user, step, text):
    """Assegna il nuovo valore a user['componenti'] per poi salvarlo"""

    if type(user['componenti'][step]) == list:
        user['componenti'][step].append(text)
    else:
        user['componenti'][step] = text
    save(user)


def table_creator(obj):
    """Crea uo oggetto tabella con gli attributi che interessano e li stampa"""

    obj_table = PrettyTable()
    obj_table.field_names = ['KEY', 'VALUE']
    obj_table.add_row(['monster_creator', obj['monster_creator']])
    obj_table.add_row(['passaggio', obj['passaggio']])
    for x in obj['componenti']:
        obj_table.add_row([x, obj['componenti'][x]])
    print(obj_table)


def requester(user, chat_id, step, modifier):
    """Invia anche all'utente il messaggio di richiesta per un nuovo"""

    last_msg = bot.sendMessage(chat_id, monster_steps[next_step(step)]['richiesta'],
                        reply_markup=monster_steps[next_step(step)]['keyboard_bottom'](user, modifier),
                        parse_mode='HTML')

    if 'reply_markup' in last_msg:
        msg_id = telepot.message_identifier(last_msg)
        user['inline_msg_id'] = msg_id
        print(msg_id)
        save(user)


def setter_requester(user, step, text, chat_id, modifier=[]):
    """Richiamre la modifica di un componente e ne richiede uno nuovo"""

    if modifier is None:
        modifier = []
    if monster_steps[step]['condizione'](text, user):
        setter(user, step, text)
        step_setter(user, step)
        last_msg = requester(user, chat_id, step, modifier)

    else:
        last_msg = requester(user, chat_id, step, modifier)



