from sqlitedict import SqliteDict
from UserClass import User
from prettytable import PrettyTable



def save(key, value, cache_file='utenti.sqlite3'):
    """Questa funzione permette di salvare ugni istanza su un file"""

    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value  # Using dict[key] to store
            mydict.commit()  # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data save (Possibly unsupported):", ex)


def load(key, cache_file='utenti.sqlite3'):
    """Questa funzione permette di scaricare un dizionario che rappresenta un'istanza salvata in precedenza"""

    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key]  # No need to use commit(), since we are only loading data!
        return vars(value)
    except Exception as ex:
        print("Error during loading data load:", ex)


def changer(dict):
    new_istance = User(dict)
    save(dict['chat_id'], new_istance)
    del new_istance


def next_step(step):
    """ritorna lo step successivo da assegnare a: user['passaggio']"""

    from theDatas import componenti
    cul = [x for x in componenti.keys()]
    return cul[cul.index(step) + 1]


def setter(user, step, text):
    """assegna nuovi valori a user['conmponenti'] e user['passaggio'] per poi salvarli"""

    user['componenti'][step]['text'] = str(text)
    user['passaggio'] = next_step(step)
    changer(user)


def table_creator(obj):
    """crea uo oggetto tabella con gli attributi che interessano e li printa"""

    obj_table = PrettyTable()
    obj_table.field_names = ['KEY', 'VALUE']
    obj_table.add_row(['monster_creator', obj['monster_creator']])
    obj_table.add_row(['passaggio', obj['passaggio']])
    for x in obj['componenti']:
        obj_table.add_row([x, obj['componenti'][x]['text']])
    print(obj_table)
