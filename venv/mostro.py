"""IMPORT"""

import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import time
from sqlitedict import SqliteDict
import pprint

# =======================================================================================================================
"""TOKEN"""

bot = telepot.Bot('5426218063:AAFPRWcBi7KMpHpP8mZOkGAWM4Z2yO0NVq4')

# =======================================================================================================================
"""CLASSI"""


class User():
    """Ogni utente di telegram è un oggetto di questa classe"""


    def __init__(self, dict):
        self.chat_id = dict['chat_id']
        self.mostri = dict['mostri']
        self.monster_creator = dict['monster_creator']
        self.componenti = dict['componenti']
        self.passaggio = dict['passaggio']



class Mostro():
    """Ogni mostro che viene creato è un oggetto di questa classe"""

    abilitys = {
        'FOR': [
            'Atletica'
        ],
        'DES': [
            'Acrobazia',
            'Furtività',
            'Rapidità di mano'
        ],
        'COS': [

        ],
        'INT': [
            'Arcano',
            'Investigare',
            'Natura',
            'Religione',
            'Storia'
        ],
        'SAG': [
            'Empatia animale',
            'Intuizione',
            'Medicina',
            'Percezione',
            'Sopravvivenza'
        ],
        'CAR': [
            'Intimidire',
            'Ingannare',
            'Intrattenere',
            'Persuadere'
        ],
    }
    PE = {
        '0': ['0', 2],
        '1 / 8': ['25', 2],
        '1 / 4': ['50', 2],
        '1 / 2': ['100', 2],
        '1': ['200', 2],
        '2': ['450', 2],
        '3': ['700', 2],
        '4': ['1100', 2],
        '5': ['1800', 3],
        '6': ['2300', 3],
        '7': ['2900', 3],
        '8': ['3900', 3],
        '9': ['5000', 4],
        '10': ['5900', 4],
        '11': ['7200', 4],
        '12': ['8400', 4],
        '13': ['10000', 5],
        '14': ['11500', 5],
        '15': ['13000', 5],
        '16': ['15000', 5],
        '17': ['18000', 6],
        '18': ['20000', 6],
        '19': ['22000', 6],
        '20': ['25000', 6],
        '21': ['33000', 7],
        '22': ['41000', 7],
        '23': ['50000', 7],
        '24': ['62000', 7],
        '25': ['75000', 8],
        '26': ['90000', 8],
        '27': ['105000', 8],
        '28': ['15000', 8],
        '29': ['135000', 9],
        '30': ['155000', 9],
    }

    def __init__(self, componenti):
        self.nome = componenti['nome']
        self.tipo = componenti['tipo']
        self.taglia = componenti['taglia']
        self.descrittore = componenti['descrittore']
        self.allineamento = componenti['allineamento']
        self.CA = componenti['CA']
        self.n_dadoVita = componenti['n_dadoVita']
        self.speed = componenti['velocità']
        self.stats = componenti['stats']
        self.TS = componenti['TS'].split()
        self.skills = componenti['abilità'].split()
        self.resDanni = componenti['resDanni'].split()
        self.immDanni = componenti['immDanni'].split()
        self.immCondizioni = componenti['immCondizioni'].split()
        self.sensi = componenti['sensi']
        if componenti['linguaggi'] == '':
            self.linguaggi = '--'
        else:
            self.linguaggi = componenti['linguaggi']
        self.sfida = componenti['sfida']
        self.tratti = componenti['tratti']
        self.azioni = componenti['azioni']
        self.azioniLeggendarie = componenti['azioniLeggendarie']

    def set_modificatori(self):
        self.modificatori = {'FOR': '', 'DES': '', 'COS': '', 'INT': '', 'SAG': '', 'CAR': ''}
        for i in self.stats:
            if self.stats[i] > 9:
                self.modificatori[i] = int((self.stats[i] - 10) / 2)
            else:
                self.modificatori[i] = int((self.stats[i] - 11) / 2)

    def set_str(self, mod, comp=0):
        if mod + comp > -1:
            return '+{n}'.format(n=str(mod + comp))
        else:
            return '{n}'.format(n=str(mod + comp))

    def set_dado_vita(self):
        self.dadoVita = self.taglie[self.taglia]
        cos_modificatore = self.modificatori['COS'] * self.n_dadoVita
        PF = self.n_dadoVita * self.dadoVita + cos_modificatore
        self.PF = '{PF} ({n_dadoVita}d{dadoVita} + {cos})'.format(PF=PF, n_dadoVita=self.n_dadoVita,
                                                                  dadoVita=self.dadoVita, cos=cos_modificatore)

    def set_TS(self):
        n = 0
        self.strTS = ''
        for i in self.TS:
            if n == 0:
                self.strTS += (
                    '{i} {mod}'.format(i=i, mod=self.set_str(self.modificatori[i], self.PE[str(self.sfida)][1])))
                n += 1
            else:
                self.strTS += (
                    ', {i} {mod}'.format(i=i, mod=self.set_str(self.modificatori[i], self.PE[str(self.sfida)][1])))
                n += 1

    def set_skills(self):
        n = 0
        self.strSkills = ''
        key_list = list(self.abilitys.keys())
        val_list = list(self.abilitys.values())
        for i in self.skills:
            for f in val_list:
                if i in f:
                    if n == 0:
                        position = val_list.index(f)
                        self.strSkills += '{i} {mod}'.format(i=i,
                                                             mod=self.set_str(self.modificatori[key_list[position]],
                                                                              self.PE[str(self.sfida)][1]))
                        n += 1
                    else:
                        position = val_list.index(f)
                        self.strSkills += ', {i} {mod}'.format(i=i,
                                                               mod=self.set_str(self.modificatori[key_list[position]],
                                                                                self.PE[str(self.sfida)][1]))
                        n += 1
                else:
                    pass

    def set_res_imm(self):
        self.strResDanni = ''
        a = 0
        b = 0
        c = 0
        for i in self.resDanni:
            if a == 0:
                self.strResDanni += i
                a += 1
            else:
                self.strResDanni += ", {i}".format(i=i)
                a += 1
        self.strImmDanni = ''
        for i in self.immDanni:
            if b == 0:
                self.strImmDanni += i
                b += 1
            else:
                self.strImmDanni += ", {i}".format(i=i)
                b += 1
        self.strImmCondizioni = ''
        for i in self.immCondizioni:
            if c == 0:
                self.strImmCondizioni += i
                c += 1
            else:
                self.strImmCondizioni += ", {i}".format(i=i)
                c += 1

    def set_sensi(self):
        if self.sensi == '':
            if 'Percezione' in self.skills:
                self.sensi += 'Percezione Passiva {mod}'.format(
                    mod=self.set_str(self.modificatori['SAG'], self.PE[str(self.sfida)][1]))
            else:
                self.sensi += 'Percezione Passiva {mod}'.format(mod=self.set_str(self.modificatori['SAG']))
        else:
            sensi = self.sensi
            self.sensi = ''
            if 'Percezione' in self.skills:
                self.sensi += 'Percezione Passiva {mod}'.format(
                    mod=self.set_str(self.modificatori['SAG'], self.PE[str(self.sfida)][1]))
            else:
                self.sensi += 'Percezione Passiva {mod}'.format(mod=self.set_str(self.modificatori['SAG']))

            self.sensi += ', {sensi}'.format(sensi=sensi)


# =======================================================================================================================
"""FUZIONI"""


def runner():
    """riceve i messaggi e reindirizza asseconda del flavour"""

    while True:
        bot.message_loop({
            'chat': on_chat_message,
            'callback_query': on_callback_query
        })

        while True:
            time.sleep(1)


def on_chat_message(msg):
    """richiama una funzione dal messaggio dell'utente"""

    chat_id = msg['chat']['id']
    text = msg['text']
    try:
         obj = vars(load(chat_id))
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
    chat_id = msg['chat']['id']
    user = vars(load(chat_id))
    bot.sendMessage(chat_id, 'questo è il primo passaggio per creare un nuovo mostro, dimmi il nome che gli vuoi dare')
    user['monster_creator'] = False
    user['passaggio'] = 'nome'
    newIstance = User(user)
    save(chat_id, newIstance)
    del newIstance


def monster_step(msg):

    chat_id = msg['chat']['id']
    text = msg['text']
    user = vars(load(chat_id))

    match user['passaggio']:
        case 'nome':
            user['componenti']['nome'] = text
            l = []
            for x in tipo:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard = True)
            bot.sendMessage(chat_id, componenti['tipo'],  reply_markup=keyboard)
            user['passaggio'] = 'tipo'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'tipo':
            user['componenti']['tipo'] = text
            l = []
            for x in taglie:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard = True)
            bot.sendMessage(chat_id, componenti['taglia'], reply_markup=keyboard)
            user['passaggio'] = 'taglia'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'taglia':
            user['componenti']['taglia'] = text
            l = []
            for x in descrittori:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['descrittore'], reply_markup=keyboard)
            user['passaggio'] = 'descrittore'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'descrittore':
            user['componenti']['descrittore'] = text
            l = []
            for x in allineamenti:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = ReplyKeyboardMarkup(keyboard=[p for p in l], one_time_keyboard=True)
            bot.sendMessage(chat_id, componenti['allineamento'], reply_markup=keyboard)
            user['passaggio'] = 'allineamento'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'allineamento':
            user['componenti']['allineamento'] = text
            bot.sendMessage(chat_id, componenti['CA'])
            user['passaggio'] = 'CA'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'CA':
            user['componenti']['CA'] = text
            bot.sendMessage(chat_id, componenti['n_dadoVita'])
            user['passaggio'] = 'n_dadoVita'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

        case 'n_dadoVita':
            try:
                user['componenti']['n_dadoVita'] = int(text)
                if int(text) < 1: raise Exception
                bot.sendMessage(chat_id, componenti['speed'])
                user['passaggio'] = 'speed'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
            except:
                bot.sendMessage(chat_id, 'Il numero di dadi vita deve essere un numero intero maggiore di 0')

        case 'speed':
            user['componenti']['speed'] = text
            bot.sendMessage(chat_id, componenti['stats'])
            user['passaggio'] = 'stats'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance

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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance

            except ValueError:
                bot.sendMessage(chat_id, 'le statistiche devonon essere 6 numeri interi maggiori di 0 e possibilimente minori di 31')

        case 'TS':
            if text == 'Nessuno':
                user['componenti']['TS'] = ''
                bot.sendMessage(chat_id, componenti['skills'])
                user['passaggio'] = 'skills'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance

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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                except ValueError:
                    bot.sendMessage(chat_id, 'i tiri salvezza devono essere questi: For Des Cos Int Sag Car')

        case 'skills':
            if text == 'nessuno':
                user['componenti']['skills'] = ''
                bot.sendMessage(chat_id, componenti['resDanni'])
                user['passaggio'] = 'resDanni'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance

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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                except ValueError:
                    bot.sendMessage(chat_id, 'le skills che un mostro puo avere sono queste')

        case 'resDanni':
            if text == 'nessuno':
                user['componenti']['resDanni'] = ''
                bot.sendMessage(chat_id, componenti['immDanni'])
                user['passaggio'] = 'immDanni'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                except ValueError:
                    bot.sendMessage(chat_id, 'i tipi di danni possibili sono questi')

        case 'immDanni':
            if text == 'nessuno':
                user['componenti']['immDanni'] = ''
                bot.sendMessage(chat_id, componenti['immCondizioni'])
                user['passaggio'] = 'immCondizioni'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                except ValueError:
                    bot.sendMessage(chat_id, 'i tipi di danni possibili sono questi')

        case 'immCondizioni':
            if text == 'nessuno':
                user['componenti']['immCondizioni'] = ''
                bot.sendMessage(chat_id, componenti['sensi'])
                user['passaggio'] = 'sensi'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
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
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                except ValueError:
                    bot.sendMessage(chat_id, 'le tipologie di condizioni sono queste')

        case 'sensi':
                if text == 'nessuno':
                    user['componenti']['sensi'] = ''
                    bot.sendMessage(chat_id, componenti['linguaggi'])
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                else:
                    user['componenti']['sensi'] = text
                    bot.sendMessage(chat_id, componenti['linguaggi'])
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance

        case 'linguaggi':
            if text == 'nessuno':
                user['componenti']['linguaggi'] = '--'
                bot.sendMessage(chat_id, componenti['sfida'])
                user['passaggio'] = 'sfida'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
            else:
                user['componenti']['linguaggi'] = text
                bot.sendMessage(chat_id, componenti['sfida'])
                user['passaggio'] = 'sfida'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance

        case 'sfida':
            try:
                if text in PE:
                    user['componenti']['sfida'] = text
                    bot.sendMessage(chat_id, componenti['tratti'])
                    user['passaggio'] = 'tratti'
                    newIstance = User(user)
                    save(chat_id, newIstance)
                    del newIstance
                else:
                    raise ValueError
            except ValueError:
                bot.sendMessage(chat_id, 'Igor ma ti sembra possibile che {} sia la sfida di un mostro?????')

        case 'tratti':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['tratti'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altri tratti fallo altrimenti scrivi: Basta')
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
            else:
                bot.sendMessage(chat_id, componenti['azioni'])
                user['passaggio'] = 'azioni'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance

        case 'azioni':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['azioni'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altre azioni fallo altrimenti scrivi: Basta')
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
            else:
                bot.sendMessage(chat_id, componenti['azioni leggendarie'])
                user['passaggio'] = 'azioni leggendarie'
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance

        case 'azioni leggendarie':
            if text != 'Basta':
                text = text.split('!')
                user['componenti']['azioni leggendarie'][text][0] = text[1]
                bot.sendMessage(chat_id, 'se vuoi aggiungere altre azioni leggendarie fallo altrimenti scrivi: Basta')
                newIstance = User(user)
                save(chat_id, newIstance)
                del newIstance
            else:
                bot.sendMessage(chat_id, componenti['ottimo hai completato tutti i passaggi e ora ecco qui il tuo mostro personalizzato'])




def save(key, value, cache_file='utenti.sqlite3'):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value  # Using dict[key] to store
            mydict.commit()  # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data save (Possibly unsupported):", ex)


def load(key, cache_file='utenti.sqlite3'):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key]  # No need to use commit(), since we are only loading data!
        return value
    except Exception as ex:
        print("Error during loading data load:", ex)


# =======================================================================================================================
"""DIZIONARI"""

funcs = {  # lista di funzioni richiamabili dall'utente
    '/start': start,
    '/nuovo': new_mostro
}

componenti = {
    'nome': 'Come si chiama il mostro? ',  # 0
    'tipo': 'Di che tipo è? ',  # 1
    'taglia': 'Dimmi la taglia ',  # 2
    'descrittore': 'Ha un descrittore particolare? ',  # 3
    'allineamento': 'Dimmi il suo allinemanto ',  # 4
    'CA': 'Dimmi la sua classe armatura ',  # 5
    'n_dadoVita': 'Dimmi quanti dadi vita ha ',  # 6
    'speed': 'Dimmi la sua velocità ',  # 7
    'stats': 'Dimmi le sue statistiche ',  # 8
    'TS': 'Ora dimmi se il mostro ha qualche competeneza nei tiri salvezza,\nusa questo tipo di formattazione:\nCos Int Sag\n oppure solamente:\nFor\n nel caso non ne avesse nessuno scrivi : Nessuno',  # 9
    'skills': 'Dimmi in cosa ha competenza ',  # 10
    'resDanni': 'Ha qulche resistenza ai danni? ',  # 11
    'immDanni': 'Ha qualche immunità ai danni ',  # 12
    'immCondizioni': 'Ha qualche immunità alle condizioni? ',  # 13
    'sensi': 'Dimmi i suoi sensi ',  # 14
    'linguaggi': 'Dimmi i suoi linguaggi ',  # 15
    'sfida': 'Dimmi il suo grado sfida ',  # 16
    'tratti': 'dimmi che tratti ha con questo formato\ntitolo del tratto! descrizione del tratto',  # 17
    'azioni': 'dimmi che azioni ha con questo formato\ntitolo del azione! descrizione del azione',  # 18
    'azioniLeggendarie': 'dimmi che azioni leggendarie ha con questo formato\ntitolo dell\' azione leggendaria! descrizione dell\' azione leggendaria'  # 19
}

user_creator = {  # questo è il dizionario base che viene dato alla classe User come form predefinito
    'chat_id': '',
    'mostri': {},
    'monster_creator': True,
    'componenti': componenti,
    'passaggio': 'nome'
}

taglia = {
    'Minuscola': 4,
    'Piccola': 6,
    'Media': 8,
    'Grande': 10,
    'Enorme': 12,
    'Mastodontica': 20
}

PE = {
    '0': ['0', 2],
    '1 / 8': ['25', 2],
    '1 / 4': ['50', 2],
    '1 / 2': ['100', 2],
    '1': ['200', 2],
    '2': ['450', 2],
    '3': ['700', 2],
    '4': ['1100', 2],
    '5': ['1800', 3],
    '6': ['2300', 3],
    '7': ['2900', 3],
    '8': ['3900', 3],
    '9': ['5000', 4],
    '10': ['5900', 4],
    '11': ['7200', 4],
    '12': ['8400', 4],
    '13': ['10000', 5],
    '14': ['11500', 5],
    '15': ['13000', 5],
    '16': ['15000', 5],
    '17': ['18000', 6],
    '18': ['20000', 6],
    '19': ['22000', 6],
    '20': ['25000', 6],
    '21': ['33000', 7],
    '22': ['41000', 7],
    '23': ['50000', 7],
    '24': ['62000', 7],
    '25': ['75000', 8],
    '26': ['90000', 8],
    '27': ['105000', 8],
    '28': ['15000', 8],
    '29': ['135000', 9],
    '30': ['155000', 9],
}

# =======================================================================================================================
"""LISTE"""

tipo = [
    'Aberrazione',
    'Bestia',
    'Celestiale',
    'Costrutto',
    'Drago',
    'Elementale',
    'Fatato',
    'Gigante',
    'Immondo',
    'Melma',
    'Mostruosità',
    'Non morto',
    'Pianta',
    'Umanoide',
    'Vegetale'
]

taglie = [
    'Minuscola',
    'Piccola',
    'Media',
    'Grande',
    'Enorme',
    'Mastodontica'
]

descrittori = [
    'orco',
    'aarakocra)',
    'goblinoide',
    'bullywug',
    'coboldo',
    'dmeone',
    'mutaforma',
    'diavolo',
    'nano',
    'elfo',
    'titano',
    'gith',
    'gnoll',
    'gnomo',
    'grimlock',
    'kenku',
    'kuo-toa',
    'umano',
    'lucertoloide',
    'marinide',
    'sahuagin',
    'thri-kreen',
    'troglodita',
    'yuan-ti',
    'yugoloth'
]

allineamenti = [
    'Legale Buono',
    'Legale Neutrale',
    'Legale Malvagio',
    'Neutrale Buono',
    'Neutrale Puro',
    'Neutrale Malvagio',
    'Caotico Buono',
    'Caotico Neutrale',
    'Caotico Malvagio'

]

tiri_salvezza = [
    'For',
    'Des',
    'Cos',
    'Int',
    'Sag',
    'Car'
]

TS = [
    'For',
    'Des',
    'Cos',
    'Int',
    'Sag',
    'Car'
]

skills = [
    'Atletica',
    'Acrobazia',
    'Furtività',
    'Rapidità do mano',
    'Arcano',
    'Investigare',
    'Natura',
    'Religione',
    'Storia',
    'Empatia animale',
    'intuizione',
    'Medicina',
    'Percezione',
    'Sopravvienza',
    'Intimidre',
    'Ingannare',
    'Intrattenere',
    'Persuadere'
]

danni = [
    'Taglienti',
    'Contundenti',
    'Perforanti',
    'Fuoco',
    'Ghiaccio',
    'Veleno',
    'Necrotici',
    'Radianti',
    'Fulmine',
    'Acido',
    'Psichici',
    'Tuono'
]

condizioni =[
    'Accecato',
    'Affascinato',
    'Afferrato',
    'Assordato',
    'Avvelenato',
    'Icapacitato',
    'Invisibilità',
    'Paralizzato',
    'Pietrificato',
    'Privo di sensi',
    'Prono',
    'Spaventato',
    'Stordito',
    'Trattenuto'
]

# =======================================================================================================================
"""VARIABILI"""

# =======================================================================================================================
"""MAIN"""

runner()
