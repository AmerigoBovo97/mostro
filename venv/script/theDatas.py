from telepot.namedtuple import InlineKeyboardButton, ReplyKeyboardMarkup

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

allineamento = [  # qui ci sono tutti i vari allineamenti possibili
    'Legale Buono',
    'Legale Neutrale',
    'Legale Malvagio',
    'Neutrale Buono',
    'Neutrale Puro',
    'Neutrale Malvagio',
    'Caotico Buono',
    'Caotico Neutrale',
    'Caotico Malvagio',
    'Senza Allineamento'
]

TS = [  # qui ci sono i tiri salvezza dei mostri
    'For',
    'Des',
    'Cos',
    'Int',
    'Sag',
    'Car'
]

skills = [  # qui ci sono tutte le skills che un mostro puo avere
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

# =======================================================================================================================
"""DIZIONARI"""

varie = {
    'TS': [x for x in TS],
    'skills': [x for x in skills],
    'resDanni': [x for x in danni],
    'immDanni': [x for x in danni],
    'immCondizioni': [x for x in condizioni],

}

taglie = {  # qui ci sono le varie taglie dei mostri con i loro dadi vita
    'Minuscola': 4,
    'Piccola': 6,
    'Media': 8,
    'Grande': 10,
    'Enorme': 12,
    'Mastodontica': 20
}

PE = {  # questo è l'elenco di tutti i gradi sfida del mostro con annessi i PE gaudagnati e il bonus di competenza
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
    # questo dizionario contiene tutti i valori del mostro, all'izio il valore delle chiavi è il messaggio che il bot invierà come richiesta, poi verrà sostituita dall'imput dell'utente
    'nome': {  # 0
        'richiesta': 'Come si chiama il mostro? ',
        'errore': 'Il mostro deve avere un nome diverso dagli altri mostri che hai già crato',
        'keyboard_bottom': None
    },
    'tipo': {  # 1
        'richiesta': 'Di che tipo è? ',
        'errore': 'Il tipo di mostro deve essere uno di questi',
        'keyboard_bottom': ReplyKeyboardMarkup(
            keyboard=[p for p in [[InlineKeyboardButton(text=x, callback_data=x)] for x in tipo]],
            one_time_keyboard=True
        )
    },
    'taglia': {  # 2
        'richiesta': 'Dimmi la taglia ',
        'errore': 'La taglia deve essere una di queste',
        'keyboard_bottom': ReplyKeyboardMarkup(
            keyboard=[p for p in [[InlineKeyboardButton(text=x, callback_data=x)] for x in [taglie for taglie in taglie.keys()]]],
            one_time_keyboard=True
        )
    },
    'descrittore': {  # 3
        'richiesta': 'Ha un descrittore particolare? ',
        'errore': 'il descrittore defe essere uno di questi',
        'keyboard_bottom': ReplyKeyboardMarkup(
            keyboard=[p for p in [[InlineKeyboardButton(text=x, callback_data=x)] for x in descrittori]],
            one_time_keyboard=True
        )
    },
    'allineamento': {  # 4
        'richiesta': 'Dimmi il suo allinemanto ',
        'errore': 'L\'allineamento deve essere uno di questi',
        'keyboard_bottom': ReplyKeyboardMarkup(
            keyboard=[p for p in [[InlineKeyboardButton(text=x, callback_data=x)] for x in allineamento]],
            one_time_keyboard=True
        )
    },
    'CA': {  # 5
        'richiesta': 'Dimmi la sua classe armatura ',
        'errore': '',
        'keyboard_bottom': None
    },
    'n_dadoVita': {  # 6
        'richiesta': 'Dimmi quanti dadi vita ha ',
        'errore': 'Il numero dei dadi vita deve essere un numero naturale maggiore di 0',
        'keyboard_bottom': None
    },
    'speed': {  # 7
        'richiesta': 'Dimmi la sua velocità ',
        'errore': '',
        'keyboard_bottom': None
    },
    'stats': {  # 8
        'richiesta': 'Dimmi le sue statistiche ',
        'errore': 'Le statistiche devono essere 6 numeri naturali maggiori di 0',
        'keyboard_bottom': None
    },
    'TS': {  # 9
        'richiesta': 'Ora dimmi se il mostro ha qualche competeneza nei tiri salvezza,\nusa questo tipo di formattazione:\nCos Int Sag\n oppure solamente:\nFor\n nel caso non ne avesse nessuno scrivi : Nessuno',
        'errore': 'I tiri salvezza devono essere tra questi',
        'keyboard_bottom': None
    },
    'skills': {  # 10
        'richiesta': 'Dimmi in cosa ha competenza ',
        'errore': 'Le skills devono essere tra queste',
        'keyboard_bottom': None
    },
    'resDanni': {  # 11
        'richiesta': 'Ha qulche resistenza ai danni? ',
        'errore': 'Una resistenza deve riguardare un certo tipo di danno',
        'keyboard_bottom': None
    },
    'immDanni': {  # 12
        'richiesta': 'Ha qualche immunità ai danni ',
        'errore': 'U\'immunità deve riguardare un certo tipo di danno',
        'keyboard_bottom': None
    },
    'immCondizioni': {  # 13
        'richiesta': 'Ha qualche immunità alle condizioni? ',
        'errore': 'U\'immunità deve riguardare un certo tipo di condizione',
        'keyboard_bottom': None
    },
    'sensi': {  # 14
        'richiesta': 'Dimmi i suoi sensi ',
        'errore': '',
        'keyboard_bottom': None
    },
    'linguaggi': {  # 15
        'richiesta': 'Dimmi i suoi linguaggi ',
        'errore': '',
        'keyboard_bottom': None
    },
    'sfida': {  # 16
        'richiesta': 'Dimmi il suo grado sfida ',
        'errore': 'La sfida deve essere una di queste',
        'keyboard_bottom': None
    },
    'tratti': {  # 17
        'richiesta': 'dimmi che tratti ha con questo formato\ntitolo del tratto! descrizione del tratto',
        'errore': '',
        'keyboard_bottom': None
    },
    'azioni': {  # 18
        'richiesta': 'dimmi che azioni ha con questo formato\ntitolo del azione! descrizione del azione',
        'errore': '',
        'keyboard_bottom': None
    },
    'azioniLeggendarie': {  # 19
        'richiesta': 'dimmi che azioni leggendarie ha con questo formato\ntitolo dell\' azione leggendaria! descrizione dell\' azione leggendaria',
        'errore': '',
        'keyboard_bottom': None
    }
}

componenti = {
    # questo dizionario contiene tutti i valori del mostro, all'izio il valore delle chiavi è il messaggio che il bot invierà come richiesta, poi verrà sostituita dall'imput dell'utente
    'nome': '',
    'tipo': '',
    'taglia': '',
    'descrittore': '',
    'allineamento': '',
    'CA': '',
    'n_dadoVita': '',
    'speed': '',
    'stats': '',
    'TS': '',
    'skills': '',
    'resDanni': '',
    'immDanni': '',
    'immCondizioni': '',
    'sensi': '',
    'linguaggi': '',
    'sfida': '',
    'tratti': [],
    'azioni': [],
    'azioniLeggendarie': []
}

user_creator = {
    # Questo è il dizionario semi precompilato che viene passato alla classe User quando viene creato un nuovo utente
    'chat_id': '',  # questo valore è l'unico che viene modificato alla creazione dell'oggetto
    'mostri': {},
    # questo dizionario corrisponde alla lista di mostri che creerà ogni utente. Alla creazione è vuoto perchè devono ancora essere creato mostri
    'monster_creator': True,
    # questo attriuto rappresenta la variabile che permette al bot di sapere se è in esecuzione la creazione di un mostro opure no
    'componenti': componenti,  # questo è il dizionario che conterrà le statistiche del mostro
    'passaggio': 'nome'
    # ogni volta che un utente crea un mostro questa sarà la variabile che permette al bot di sapere a che punto è la creazione
}
