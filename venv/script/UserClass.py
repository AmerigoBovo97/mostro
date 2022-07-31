"""
Questo file contiene la classe User.
Ogni qualvolta un nuovo utente accede al bot e preme /start, viene creata una nuova istanza di questa classe.
"""



class User():
    """Quando viene creato un oggetto di questa classe, viene passato come argomento un dizionario."""


    def __init__(self, dict):
        self.chat_id = dict['chat_id']
        self.mostri = dict['mostri']
        self.monster_creator = dict['monster_creator']
        self.componenti = dict['componenti']
        self.passaggio = dict['passaggio']

