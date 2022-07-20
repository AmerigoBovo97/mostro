import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import sqlitedict
from main import *
from DataSet import *
from UserClass import User

"""Qui ci sono tutte le funzioni che un utente può richiamre trammite comando"""

bot = telepot.Bot('5426218063:AAFPRWcBi7KMpHpP8mZOkGAWM4Z2yO0NVq4')


def start(msg):
    """crea un nuovo utente se già non è registrato"""

    new_id = msg['chat']['id']
    new_obj = user_creator
    new_obj['chat_id'] = new_id
    try:
        print('merda')
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
    text = msg['text']
    user = load(chat_id)

    match user['passaggio']:
        case 'nome':
            user['componenti']['nome'] = text
            l = []
            for x in tipo:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['tipo'], reply_markup=keyboard)
            user['passaggio'] = 'tipo'
            changer(user)

        case 'tipo':
            user['componenti']['tipo'] = text
            l = []
            for x in taglie:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['taglia'], reply_markup=keyboard)
            user['passaggio'] = 'taglia'
            changer(user)

        case 'taglia':
            user['componenti']['taglia'] = text
            l = []
            for x in descrittori:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['descrittore'], reply_markup=keyboard)
            user['passaggio'] = 'descrittore'
            changer(user)

        case 'descrittore':
            user['componenti']['descrittore'] = text
            l = []
            for x in allineamenti:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['allineamento'], reply_markup=keyboard)
            user['passaggio'] = 'allineamento'
            changer(user)

        case 'allineamento':
            user['componenti']['allineamento'] = text
            bot.sendMessage(chat_id, componenti['CA'])
            user['passaggio'] = 'CA'
            changer(user)

        case 'CA':
            user['componenti']['CA'] = text
            bot.sendMessage(chat_id, componenti['n_dadoVita'])
            user['passaggio'] = 'n_dadoVita'
            changer(user)

        case 'n_dadoVita':
            try:
                user['componenti']['n_dadoVita'] = int(text)
                if int(text) < 1:
                    raise Exception
                bot.sendMessage(chat_id, componenti['speed'])
                user['passaggio'] = 'speed'
                changer(user)
            except:
                bot.sendMessage(chat_id, 'Il numero di dadi vita deve essere un numero intero maggiore di 0')

        case 'speed':
            user['componenti']['speed'] = text
            bot.sendMessage(chat_id, componenti['stats'])
            user['passaggio'] = 'stats'
            changer(user)

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
                    user['componenti']['stats'] = text
                    bot.sendMessage(chat_id, componenti['TS'])
                    user['passaggio'] = 'TS'
                    changer(user)

            except ValueError:
                bot.sendMessage(chat_id, 'le statistiche devonon essere 6 numeri interi maggiori di 0 e possibilimente minori di 31')

        case 'TS':
            if text == 'Nessuno':
                user['componenti']['TS'] = ''
                bot.sendMessage(chat_id, componenti['skills'])
                user['passaggio'] = 'skills'
                changer(user)

            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in TS:
                            raise ValueError
                        else:
                            pass
                    user['componenti']['TS'] = text
                    bot.sendMessage(chat_id, componenti['skills'])
                    user['passaggio'] = 'skills'
                    changer(user)
                except ValueError:
                    bot.sendMessage(chat_id, 'i tiri salvezza devono essere questi: For Des Cos Int Sag Car')

        case 'skills':
            if text == 'nessuno':
                user['componenti']['skills'] = ''
                bot.sendMessage(chat_id, componenti['resDanni'])
                user['passaggio'] = 'resDanni'
                changer(user)

            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in skills:
                            raise ValueError
                        else:
                            pass
                    user['componenti']['skills'] = text
                    bot.sendMessage(chat_id, componenti['resDanni'])
                    user['passaggio'] = 'resDanni'
                    changer(user)
                except ValueError:
                    bot.sendMessage(chat_id, 'le skills che un mostro puo avere sono queste')

        case 'resDanni':
            if text == 'nessuno':
                user['componenti']['resDanni'] = ''
                bot.sendMessage(chat_id, componenti['immDanni'])
                user['passaggio'] = 'immDanni'
                changer(user)
            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in danni:
                            raise ValueError
                        else:
                            pass
                    user['componenti']['resDanni'] = text
                    bot.sendMessage(chat_id, componenti['immDanni'])
                    user['passaggio'] = 'immDanni'
                    changer(user)
                except ValueError:
                    bot.sendMessage(chat_id, 'i tipi di danni possibili sono questi')

        case 'immDanni':
            if text == 'nessuno':
                user['componenti']['immDanni'] = ''
                bot.sendMessage(chat_id, componenti['immCondizioni'])
                user['passaggio'] = 'immCondizioni'
                changer(user)
            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in danni:
                            raise ValueError
                        else:
                            pass
                    user['componenti']['immDanni'] = text
                    bot.sendMessage(chat_id, componenti['immCondizioni'])
                    user['passaggio'] = 'immCondizioni'
                    changer(user)
                except ValueError:
                    bot.sendMessage(chat_id, 'i tipi di danni possibili sono questi')

        case 'immCondizioni':
            if text == 'nessuno':
                user['componenti']['immCondizioni'] = ''
                bot.sendMessage(chat_id, componenti['sensi'])
                user['passaggio'] = 'sensi'
                changer(user)
            else:
                try:
                    text = text.split()
                    for i in text:
                        if i not in condizioni:
                            raise ValueError
                        else:
                            pass
                    user['componenti']['immCondizioni'] = text
                    bot.sendMessage(chat_id, componenti['sensi'])
                    user['passaggio'] = 'sensi'
                    changer(user)
                except ValueError:
                    bot.sendMessage(chat_id, 'le tipologie di condizioni sono queste')

        case 'sensi':
            if text == 'nessuno':
                user['componenti']['sensi'] = ''
                bot.sendMessage(chat_id, componenti['linguaggi'])
                changer(user)
            else:
                user['componenti']['sensi'] = text
                bot.sendMessage(chat_id, componenti['linguaggi'])
                changer(user)

        case 'linguaggi':
            if text == 'nessuno':
                user['componenti']['linguaggi'] = '--'
                bot.sendMessage(chat_id, componenti['sfida'])
                user['passaggio'] = 'sfida'
                changer(user)
            else:
                user['componenti']['linguaggi'] = text
                bot.sendMessage(chat_id, componenti['sfida'])
                user['passaggio'] = 'sfida'
                changer(user)

        case 'sfida':
            try:
                if text in PE:
                    user['componenti']['sfida'] = text
                    bot.sendMessage(chat_id, componenti['tratti'])
                    user['passaggio'] = 'tratti'
                    changer(user)
                else:
                    raise ValueError
            except ValueError:
                bot.sendMessage(chat_id, 'Igor ma ti sembra possibile che {} sia la sfida di un mostro?????')

        case 'tratti':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['tratti'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altri tratti fallo altrimenti scrivi: Basta')
                changer(user)
            else:
                bot.sendMessage(chat_id, componenti['azioni'])
                user['passaggio'] = 'azioni'
                changer(user)

        case 'azioni':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['azioni'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altre azioni fallo altrimenti scrivi: Basta')
                changer(user)
            else:
                bot.sendMessage(chat_id, componenti['azioni leggendarie'])
                user['passaggio'] = 'azioni leggendarie'
                changer(user)

        case 'azioni leggendarie':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['azioni leggendarie'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altre azioni leggendarie fallo altrimenti scrivi: Basta')
                changer(user)
            else:
                bot.sendMessage(chat_id, componenti[
                    'ottimo hai completato tutti i passaggi e ora ecco qui il tuo mostro personalizzato'])
