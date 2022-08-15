from Mostri_definitivo.venv.script.SistemFuctions import *
from Mostri_definitivo.venv.script.bot import bot
from Mostri_definitivo.venv.script.theDatas import *
from telepot import flavor
from os import path

"""Qui ci sono tutte le funzioni che un utente può richiamre trammite comando"""


def start(msg):
    """Crea un nuovo utente se già non è registrato"""

    new_id = msg['chat']['id']
    new_user = user_creator
    new_user['chat_id'] = new_id
    if path.exists(f'utenti/{new_id}.json'):
        print('si esiste')
        bot.sendMessage(new_id, f'Bentornato J, {new_id}')
    else:
        print('non esiste')

        save(new_user)
        bot.sendMessage(new_id, f'Benvenuto J, {new_id}')


def new_mostro(msg):
    """Fa partire il procedimento per creare un nuovo mostro"""

    chat_id = msg['chat']['id']
    user = load(chat_id)
    bot.sendMessage(chat_id, 'questo è il primo passaggio per creare un nuovo mostro, dimmi il nome che gli vuoi dare')
    user['monster_creator'] = True
    user['componenti'] = componenti
    user['passaggio'] = 'nome'

    if user['inline_msg_id']:
        msg_id1, msg_id2 = user['inline_msg_id']
        bot.deleteMessage((msg_id1, msg_id2))

    user['inline_msg_id'] = False
    save(user)


def monster_step(msg):
    """Raccoglie dall'utente le informazioni del mostro"""

    if flavor(msg) == 'chat':
        chat_id = msg['chat']['id']
        text = msg['text']
    elif flavor(msg) == 'callback_query':
        chat_id = msg['message']['chat']['id']
        text = msg['data']
    else:
        raise Exception('il flavour è sbagliato')

    user = load(chat_id)
    step = user['passaggio']

    match step:
        case 'nome' | 'tipo' | 'allineamento' | 'CA' | 'n_dadoVita' | 'speed' | 'sfida':
            setter_requester(user, step, text, chat_id)

        case 'stats':
            if monster_steps[step]['condizione']:
                setter_requester(user, step, [int(i) for i in text.split()], chat_id)

        case 'TS' | 'skills' | 'resDanni' | 'immDanni' | 'immCondizioni':
            if text == 'Nessuno':
                setter_requester(user, step, '', chat_id)
            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in varie[step]:
                            raise ValueError
                    setter_requester(user, step, text, chat_id)
                except ValueError:
                    bot.sendMessage(chat_id, monster_steps[step]['errore'])

        case 'taglia':
            setter_requester(user, step, text, chat_id, modifier=['dio mega merda'])

        case 'sensi' | 'linguaggi' | 'descrittore':
            if text == 'nessuno':
                setter_requester(user, step, '', chat_id)
            else:
                setter_requester(user, step, text, chat_id)

        case 'tratti' | 'azioni' | 'azioni leggendarie':
            if text != 'Basta':
                text = text.split('!')
                user['componenti'][step]['text'].append({text[0]: text[1]})
                save(user)
                next_step(step)
                if step != 'azioni leggendarie':
                    bot.sendMessage(chat_id, monster_steps[next_step(step)]['richiesta'])
                else:
                    bot.sendMessage(chat_id,
                                    'ottimo hai completato tutti i passaggi e ora ecco qui il tuo mostro personalizzato')
            else:
                bot.sendMessage(chat_id, monster_steps['azioni'])
                next_step(step)
                bot.sendMessage(chat_id, monster_steps[next_step(step)]['richiesta'])

    # table_creator(user)


def query_set_list(query_step, query_text, user):
    modifier = []
    if user['inline_msg_id']:
        msg_id1, mag_id2 = user['inline_msg_id']

        if query_text != 'nessuno' and query_text != 'basta':
            if query_text in user['componenti'][query_step]:
                user['componenti'][query_step].remove(query_text)
                save(user)
            else:
                setter(user, query_step, query_text)

            bot.editMessageText((msg_id1, mag_id2), monster_steps[query_step]['richiesta'],
                                reply_markup=monster_steps[query_step]['keyboard_bottom'](user, modifier))
        else:
            bot.deleteMessage((msg_id1, mag_id2))
            step_setter(user, query_step)
            requester(user, user['chat_id'], query_step, modifier)


funcs = {  # lista di funzioni richiamabili dall'utente
    '/start': start,
    '/nuovo': new_mostro,
    '/query_set_list': query_set_list
}
