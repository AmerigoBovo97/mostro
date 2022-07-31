from Mostri_definitivo.venv.script.SistemFuctions import *
from Mostri_definitivo.venv.script.UserClass import User
from Mostri_definitivo.venv.script.bot import bot
from Mostri_definitivo.venv.script.theDatas import *

"""Qui ci sono tutte le funzioni che un utente può richiamre trammite comando"""


def start(msg):
    """crea un nuovo utente se già non è registrato"""

    new_id = msg['chat']['id']
    new_obj = user_creator
    new_obj['chat_id'] = new_id
    try:
        with SqliteDict('utenti.sqlite3') as mydict:
            if new_id in mydict:
                print('utente gia esistente')
                bot.sendMessage(new_id, 'bentornato')
            else:
                user = User(new_obj)
                save(new_id, user)
                print('nuovo utente registrato')
                bot.sendMessage(new_id, 'benvenuto')
    except:
        user = User(new_obj)
        save(new_id, user)
        print('nuovo utente registrato')
        bot.sendMessage(new_id, 'benvenuto')


def new_mostro(msg):
    """fa partire il procedimento per creare un nuovo msotro"""

    chat_id = msg['chat']['id']
    user = load(chat_id)
    bot.sendMessage(chat_id, 'questo è il primo passaggio per creare un nuovo mostro, dimmi il nome che gli vuoi dare')
    user['monster_creator'] = False
    user['passaggio'] = 'nome'
    changer(user)


def monster_step(msg):
    """raccoglie dall'utente le informazioni del mostro"""

    chat_id = msg['chat']['id']
    user = load(chat_id)
    step = user['passaggio']
    text = msg['text']

    try:
        match step:
            case 'nome' | 'tipo' | 'taglia' | 'descrittore' | 'allineamento' | 'CA' | 'speed':
                setter_requester(user, step, text, chat_id)

            case 'n_dadoVita':
                try:
                    if int(text) > 0:
                        setter_requester(user, step, text, chat_id)
                    else:
                        raise ValueError
                except ValueError:
                    bot.sendMessage(chat_id, monster_steps[step]['errore'])

            case 'stats':
                try:
                    text = [int(i) for i in text.split()]
                    if len(text) != 6:
                        raise ValueError
                    else:
                        for i in text:
                            if i < 1:
                                raise ValueError
                            else:
                                pass
                        setter_requester(user, step, text, chat_id)
                except ValueError:
                    bot.sendMessage(chat_id, monster_steps[step]['errore'])

            case 'TS' | 'skills' | 'resDanni' | 'immDanni' | 'immCondizioni':
                if text == 'Nessuno':
                    setter_requester(user, step, '', chat_id)
                else:
                    try:
                        text = text.split()
                        print(text)
                        for i in text:
                            if i not in varie[step]:
                                raise ValueError
                        setter_requester(user, step, text, chat_id)
                    except ValueError:
                        bot.sendMessage(chat_id, monster_steps[step]['errore'])

            case 'sensi' | 'linguaggi':
                if text == 'nessuno':
                    setter_requester(user, step, 'text', chat_id)
                else:
                    setter_requester(user, step, text, chat_id)

            case 'sfida':
                try:
                    if text in PE:
                        setter_requester(user, step, text, chat_id)
                    else:
                        raise ValueError
                except ValueError:
                    bot.sendMessage(chat_id, monster_steps[step]['errore'])

            case 'tratti' | 'azioni' | 'azioni leggendarie':
                if text != 'Basta':
                    text = text.split('!')
                    user['componenti'][step]['text'].append({text[0]: text[1]})
                    changer(user)
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

    except Exception as x:
        print(x)
        pass
    table_creator(user)


funcs = {  # lista di funzioni richiamabili dall'utente
    '/start': start,
    '/nuovo': new_mostro
}
