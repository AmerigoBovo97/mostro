from FunzioniUtente import *

"""Qui ci sono tutte le liste e i dizionari che mi servono"""

# =======================================================================================================================
"""DIZIONARI"""

funcs = {  # lista di funzioni richiamabili dall'utente
    '/start': start,
    '/nuovo': new_mostro
}

componenti = {
    # questo dizionario contiene tutti i valori del mostro, all'izio il valore delle chiavi è il messaggio che il bot invierà come richiesta, poi verrà sostituita dall'imput dell'utente
    'nome': 'Come si chiama il mostro? ',  # 0
    'tipo': 'Di che tipo è? ',  # 1
    'taglia': 'Dimmi la taglia ',  # 2
    'descrittore': 'Ha un descrittore particolare? ',  # 3
    'allineamento': 'Dimmi il suo allinemanto ',  # 4
    'CA': 'Dimmi la sua classe armatura ',  # 5
    'n_dadoVita': 'Dimmi quanti dadi vita ha ',  # 6
    'speed': 'Dimmi la sua velocità ',  # 7
    'stats': 'Dimmi le sue statistiche ',  # 8
    'TS': 'Ora dimmi se il mostro ha qualche competeneza nei tiri salvezza,\nusa questo tipo di formattazione:\nCos Int Sag\n oppure solamente:\nFor\n nel caso non ne avesse nessuno scrivi : Nessuno',
    # 9
    'skills': 'Dimmi in cosa ha competenza ',  # 10
    'resDanni': 'Ha qulche resistenza ai danni? ',  # 11
    'immDanni': 'Ha qualche immunità ai danni ',  # 12
    'immCondizioni': 'Ha qualche immunità alle condizioni? ',  # 13
    'sensi': 'Dimmi i suoi sensi ',  # 14
    'linguaggi': 'Dimmi i suoi linguaggi ',  # 15
    'sfida': 'Dimmi il suo grado sfida ',  # 16
    'tratti': 'dimmi che tratti ha con questo formato\ntitolo del tratto! descrizione del tratto',  # 17
    'azioni': 'dimmi che azioni ha con questo formato\ntitolo del azione! descrizione del azione',  # 18
    'azioniLeggendarie': 'dimmi che azioni leggendarie ha con questo formato\ntitolo dell\' azione leggendaria! descrizione dell\' azione leggendaria'
    # 19
}

taglia = {  # qui ci sono le varie taglie dei mostri con i loro dadi vita
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

taglie = [  # lista di taglie dei mostri
    'Minuscola',
    'Piccola',
    'Media',
    'Grande',
    'Enorme',
    'Mastodontica'
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

allineamenti = [  # qui ci sono tutti i vari allineamenti possibili
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
