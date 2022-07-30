from telepot.namedtuple import InlineKeyboardButton, ReplyKeyboardMarkup
from SistemFuctons import *
from UserClass import User
from bot import bot

"""Qui ci sono tutte le funzioni che un utente può richiamre trammite comando"""



def start(msg):
    """crea un nuovo utente se già non è registrato"""

    from theDatas import user_creator
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

    import theDatas
    chat_id = msg['chat']['id']
    text = msg['text']
    user = load(chat_id)
    step = user['passaggio']

    try:
        match step:
            case 'nome'|'tipo'|'taglia'|'descrittore':
                setter(user, step, text)
                next_step(step)
                bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'], reply_markup=theDatas.keyboard_bottom[next_step(step)])

            case 'allineamento'|'CA'|'speed':
                setter(user, step, text)
                next_step(step)
                bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])

            case 'n_dadoVita':
                if int(text) > 0:
                    setter(user, step, text)
                    next_step(step)
                    bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                else:
                    bot.sendMessage(chat_id, theDatas.componenti[step]['errore'])

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
                        setter(user, step, text)
                        next_step(step)
                        bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                except ValueError:
                    bot.sendMessage(chat_id, theDatas.componenti[step]['errore'])

            case 'TS'|'skills'|'resDanni'|'immDanni'|'immCondizioni':
                if text == 'Nessuno':
                    setter(user, step, '')
                    next_step(step)
                    bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                else:
                    try:
                        text = text.split()
                        print(text)
                        for i in text:
                            if i not in theDatas.varie[step]:
                                raise ValueError
                        setter(user, step, text)
                        next_step(step)
                        bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                    except ValueError:
                        bot.sendMessage(chat_id, theDatas.componenti[step]['errore'])

            case 'sensi'|'linguaggi':
                if text == 'nessuno':
                    setter(user, step, '')
                else:
                    setter(user, step, text)
                next_step(step)
                bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])

            case 'sfida':
                try:
                    if text in theDatas.PE:
                        setter(user, step, text)
                        next_step(step)
                        bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                    else:
                        raise ValueError
                except ValueError:
                    bot.sendMessage(chat_id, theDatas.componenti[step]['errore'])

            case 'tratti'|'azioni'|'azioni leggendarie':
                if text != 'Basta':
                    text = text.split('!')
                    user['componenti'][step]['text'].append({text[0]: text[1]})
                    changer(user)
                    next_step(step)
                    if step != 'azioni leggendarie':
                        bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])
                    else:
                        bot.sendMessage(chat_id, 'ottimo hai completato tutti i passaggi e ora ecco qui il tuo mostro personalizzato')
                else:
                    bot.sendMessage(chat_id, theDatas.componenti['azioni'])
                    next_step(step)
                    bot.sendMessage(chat_id, theDatas.componenti[next_step(step)]['richiesta'])

    except Exception as x:
        print(x)
        pass
    table_creator(user)
