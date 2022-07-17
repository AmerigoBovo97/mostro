"""IMPORT"""

import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
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

    taglie = {
        'Minuscola': 4,
        'Piccola': 6,
        'Media': 8,
        'Grande': 10,
        'Enorme': 12,
        'Mastodontica': 20
    }
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
        print('culo')
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
    text = msg['text']
    user = vars(load(chat_id))
    bot.sendMessage(chat_id, 'questo è il primo passaggio per creare un nuovo mostro, dimmi il nome che gli vuoi dare')
    user['monster_creator'] = False
    newIstance = User(user)
    save(chat_id, newIstance)
    del newIstance


def monster_step(msg):

    chat_id = msg['chat']['id']
    text = msg['text']
    user = vars(load(chat_id))

    match user['passaggio']:
        case 'nome':
            user['componenti'] = text
            user['passaggio'] = 'tipo'
            newIstance = User(user)
            save(chat_id, newIstance)
            del newIstance
            bot.sendMessage(chat_id, 'scelgi uno di questi')
            l = []
            for x in tipo:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = InlineKeyboardMarkup(inline_keyboard=[p for p in l])
            bot.sendMessage(chat_id, 'scegli uno di questi', reply_markup=keyboard)

        case 'tipo':
            l = []
            for x in tipo:
                l.append([InlineKeyboardButton(text=x, callback_data=x)])
                keyboard = InlineKeyboardMarkup(inline_keyboard=[p for p in l])
            bot.sendMessage(chat_id, 'scegli uno di questi', reply_markup=keyboard)


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
    'velocità': 'Dimmi la sua velocità ',  # 7
    'stats': 'Dimmi le sue statistiche ',  # 8
    'TS': 'Dimmi in che tiri salvezza ha competenza ',  # 9
    'abilità': 'Dimmi in cosa ha competenza ',  # 10
    'resDanni': 'Ha qulche resistenza ai danni? ',  # 11
    'immDanni': 'Ha qualche immunità ai danni ',  # 12
    'immCondizioni': 'Ha qualche immunità alle condizioni? ',  # 13
    'sensi': 'Dimmi i suoi sensi ',  # 14
    'linguaggi': 'Dimmi i suoi linguaggi ',  # 15
    'sfida': 'Dimmi il suo grado sfida ',  # 16
    'tratti': 'Dimmi che tratti ha ',  # 17
    'azioni': 'Dimmi che azioni fa ',  # 18
    'azioniLeggendarie': 'Dimmi che azioni leggendarie fa '  # 19
}

user_creator = {  # questo è il dizionario base che viene dato alla classe User come form predefinito
    'chat_id': '',
    'mostri': {},
    'monster_creator': True,
    'componenti': componenti,
    'passaggio': 'nome'
}

# =======================================================================================================================
"""LISTE"""

tipo = [
    'aberrazione',
    'bestia',
    'celestiale',
    'costrutto',
    'drago',
    'elementale',
    'fatato',
    'gigante',
    'immondo',
    'melma',
    'mostruosità',
    'non morto',
    'pianta',
    'umanoide',
    'vegetale'
]

# =======================================================================================================================
"""VARIABILI"""

# =======================================================================================================================
"""MAIN"""

runner()
