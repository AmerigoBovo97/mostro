from sqlitedict import SqliteDict
from UserClass import User



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
