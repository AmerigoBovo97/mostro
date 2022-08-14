from telepot.namedtuple import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

"""Qui ci sono tutte le liste e i dizionari che mi servono"""

# =======================================================================================================================
"""LISTE"""

tipo = [
    # qui ci sono le tipologie dei mostri, in futuro implementerò la possibilità di aggiungerne alcuni personalizzati dall'utente
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

descrittori = [
    # qui ci sono tutti i descrittori dei mostri, in futuro implementerò la possibilità di aggiungerne alcuni personalizzati dall'utente
    'nessuno',
    'orco',
    'aarakocra',
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

allineamento = [  # qui ci sono tutti i vari allineamenti possibili
    'Senza Allineamento',
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

danni = [  # qui ci sono tutte le tipologie di danni
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

condizioni = [  # qui ci sono tutte le condizioni
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

lingue = [
    'comune',
    'elfico',
    'gigante',
    'gnomesco',
    'goblin',
    'halfling',
    'nanico',
    'orchesco',
    'abissale',
    'celestiale',
    'draconico',
    'gergo delle profondità',
    'infernale',
    'primordiale',
    'acquan (dialetto primordiale)',
    'auran (dialetto primordiale)',
    'ignan (dialetto primordiale)',
    'terran (dialetto primordiale)',
    'silvano',
    'sottocomune',
    'Daelkyr',
    'Gith',
    'Grung',
    'Kraul',
    'Loross',
    'Lossodontico',
    'Marinide',
    'Minotaurico',
    'Modron',
    'Netherese',
    'Otyugh',
    'Qualith',
    'Quori',
    'Riedran',
    'Sahuagin',
    'Slaad',
    'Thri-kreen',
    'Tlincalli',
    'Troglodita',
    'Umber Hulk',
    'Vedalken',
    'Worg',
    'Yeti',
    'Yikaria',
    'Zemnian'
]

# =======================================================================================================================
"""DIZIONARI"""

skills = {
    'For': [
        'Atletica'
    ],
    'Des': [
        'Acrobazia',
        'Furtività',
        'Rapidità di mano'
    ],
    'Cos': [

    ],
    'Int': [
        'Arcano',
        'Investigare',
        'Natura',
        'Religione',
        'Storia'
    ],
    'Sag': [
        'Empatia animale',
        'Intuizione',
        'Medicina',
        'Percezione',
        'Sopravvivenza'
    ],
    'Car': [
        'Intimidire',
        'Ingannare',
        'Intrattenere',
        'Persuadere'
    ],
}

varie = {
    'skills': (x for x in skills.values()),
    'resDanni': (x for x in danni),
    'immDanni': (x for x in danni),
    'immCondizioni': (x for x in condizioni),
    'TS': (x for x in skills.keys())

}

taglie = {  # qui ci sono le varie taglie dei mostri con i loro dadi vita
    'Minuscola': 4,
    'Piccola': 6,
    'Media': 8,
    'Grande': 10,
    'Enorme': 12,
    'Mastodontica': 20
}

PE = {  # questo è l'elenco di tutti i gradi sfida del mostro con annessi i PE guadagnati e il bonus di competenza
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

monster_steps = {
    # questo dizionario contiene tutti i valori del mostro, all'inizio il valore delle chiavi è il messaggio che il bot invierà come richiesta, poi verrà sostituita dall'input dell'utente
    'nome': {  # 0
        'richiesta': 'Come si chiama il mostro? ',
        'errore': 'Il mostro deve avere un nome diverso dagli altri mostri che hai già crato',
        'keyboard_bottom': lambda user, modifier: None,
        'condizione': lambda text, user: True if text not in user['mostri'] else False
    },
    'tipo': {  # 1
        'richiesta': 'Di che tipo è? ',
        'errore': 'Il tipo di mostro deve essere uno di questi',
        'keyboard_bottom': lambda user, modifier: ReplyKeyboardMarkup(
            keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in tipo],
            one_time_keyboard=True
        ),
        'condizione': lambda text, user: True if text in tipo else False
    },
    'taglia': {  # 2
        'richiesta': 'Dimmi la taglia',
        'errore': 'La taglia deve essere una di queste',
        'keyboard_bottom': lambda user, modifier: ReplyKeyboardMarkup(
            keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in taglie.keys()],
            one_time_keyboard=True
        ),
        'condizione': lambda text, user: True if text in taglie.keys() else False
    },
    'descrittore': {  # 3
        'richiesta': '<b>Ha un descrittore</b> particolare?',
        'errore': 'il descrittore defe essere uno di questi',
        'keyboard_bottom': lambda user, modifier: ReplyKeyboardMarkup(
            keyboard=[[InlineKeyboardButton(text=i, callback_data=i)] for i in (modifier + descrittori)]
        ),
        'condizione': lambda text, user: True if text in descrittori or text == 'nessuno' else False
    },
    'allineamento': {  # 4
        'richiesta': 'Dimmi il suo allineamento ',
        'errore': 'L\'allineamento deve essere uno di questi',
        'keyboard_bottom': lambda user, modifier: ReplyKeyboardMarkup(
            keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in allineamento],
            one_time_keyboard=True
        ),
        'condizione': lambda text, user: True if text in allineamento else False
    },
    'CA': {  # 5
        'richiesta': 'Dimmi la sua classe armatura ',
        'errore': '',
        'keyboard_bottom': lambda user, modifier: None,
        'condizione': lambda text, user: True
    },
    'n_dadoVita': {  # 6
        'richiesta': 'Dimmi quanti dadi vita ha ',
        'errore': 'Il numero dei dadi vita deve essere un numero naturale maggiore di 0',
        'keyboard_bottom': lambda user, modifier: None,
        'condizione': lambda text, user: True if int(text) > 0 else False
    },
    'speed': {  # 7
        'richiesta': 'Dimmi la sua velocità ',
        'errore': '',
        'keyboard_bottom': lambda user, modifier: None,
        'condizione': lambda text, user: True
    },
    'stats': {  # 8
        'richiesta': 'Dimmi le sue statistiche ',
        'errore': 'Le statistiche devono essere 6 numeri naturali maggiori di 0',
        'keyboard_bottom': lambda user, modifier: None,
        'condizione': lambda text, user: True if len(
            list(filter(lambda stat: (int(stat) > 0), text.split()))) == 6 else False
    },
    'TS': {  # 9
        'richiesta': 'Ora dimmi se il mostro ha qualche competenza nei tiri salvezza,\nusa questo tipo di formattazione:\nCos Int Sag\n oppure solamente:\nFor\n nel caso non ne avesse nessuno scrivi : Nessuno',
        'errore': 'I tiri salvezza devono essere tra questi',
        'keyboard_bottom': lambda user_ts, modifier_ts: InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text=f'{x.capitalize()} □' if x not in user_ts['componenti']['TS'] else f'{x.capitalize()} ☑️',
                    callback_data=f'/set!TS!{x}'
                )
            ]  for x in skills.keys()]),
        'condizione': lambda text, user: True
    },
    'skills': {  # 10
        'richiesta': 'Dimmi in cosa ha competenza ',
        'errore': 'Le skills devono essere tra queste',
        'keyboard_bottom': lambda user, x: lambda user, modifier: InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=i.capitalize(), callback_data=f'step {i}')] for i in
                             ([modifier + descrittori])]
        ),
        'condizione': lambda text, user: True
    },
    'resDanni': {  # 11
        'richiesta': 'Ha qualche resistenza ai danni? ',
        'errore': 'Una resistenza deve riguardare un certo tipo di danno',
        'keyboard_bottom': lambda x: InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in (['nessuno'] + danni)]
        ),
        'condizione': lambda text, user: True
    },
    'immDanni': {  # 12
        'richiesta': 'Ha qualche immunità ai danni ',
        'errore': 'U\'immunità deve riguardare un certo tipo di danno',
        'keyboard_bottom': lambda x: InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in (['nessuno'] + danni)]
        ),
        'condizione': lambda text, user: True
    },
    'immCondizioni': {  # 13
        'richiesta': 'Ha qualche immunità alle condizioni? ',
        'errore': 'U\'immunità deve riguardare un certo tipo di condizione',
        'keyboard_bottom': lambda x: InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in (['nessuno'] + condizioni)]
        ),
        'condizione': lambda text, user: True
    },
    'sensi': {  # 14
        'richiesta': 'Dimmi i suoi sensi ',
        'errore': '',
        'keyboard_bottom': lambda x: None,
        'condizione': lambda text, user: True
    },
    'linguaggi': {  # 15
        'richiesta': 'Dimmi i suoi linguaggi ',
        'errore': '',
        'keyboard_bottom': lambda x: None,
        'condizione': lambda text, user: True
    },
    'sfida': {  # 16
        'richiesta': 'Dimmi il suo grado sfida ',
        'errore': 'La sfida deve essere una di queste',
        'keyboard_bottom': lambda x: ReplyKeyboardMarkup(
            keyboard=[[InlineKeyboardButton(text=x, callback_data=x)] for x in PE],
            one_time_keyboard=True
        ),
        'condizione': lambda text, user: True if text in PE else False
    },
    'tratti': {  # 17
        'richiesta': 'dimmi che tratti ha con questo formato\ntitolo del tratto! descrizione del tratto',
        'errore': '',
        'keyboard_bottom': lambda x: None,
        'condizione': lambda text, user: True
    },
    'azioni': {  # 18
        'richiesta': 'dimmi che azioni ha con questo formato\ntitolo del azione! descrizione del azione',
        'errore': '',
        'keyboard_bottom': lambda x: None,
        'condizione': lambda text, user: True
    },
    'azioniLeggendarie': {  # 19
        'richiesta': 'dimmi che azioni leggendarie ha con questo formato\ntitolo dell\' azione leggendaria! descrizione dell\' azione leggendaria',
        'errore': '',
        'keyboard_bottom': lambda x: None,
        'condizione': lambda text, user: True
    }
}

componenti = {
    # questo dizionario contiene tutti i valori del mostro, all'inizio il valore delle chiavi è il messaggio che il bot invierà come richiesta, poi verrà sostituita dal input dell'utente
    'nome': '',
    'tipo': '',
    'taglia': '',
    'descrittore': '',
    'allineamento': '',
    'CA': '',
    'n_dadoVita': '',
    'speed': [],
    'stats': [],
    'TS': [],
    'skills': [],
    'resDanni': [],
    'immDanni': [],
    'immCondizioni': [],
    'sensi': [],
    'linguaggi': [],
    'sfida': '',
    'tratti': [],
    'azioni': [],
    'azioniLeggendarie': []
}

user_creator = {
    # Questo è il dizionario semi precompilato che viene passato alla classe User al momento della creazione dell'utente
    'chat_id': '',  # questo valore è l'unico che viene modificato alla creazione dell'oggetto
    'mostri': {},  # Questo dizionario corrisponde alla lista di mostri che creerà ogni utente. Alla creazione è vuoto perchè devono ancora essere creato mostri
    'monster_creator': True,  # Questo attributo rappresenta la variabile che permette al bot di sapere se è in esecuzione la creazione di un mostro oppure no
    'componenti': componenti,  # questo è il dizionario che conterrà le statistiche del mostro
    'passaggio': 'nome',  # Ogni volta che un utente crea un mostro questa sarà la variabile che permette al bot di sapere a che punto è la creazione
    'inline_msg_identifier': False
}

