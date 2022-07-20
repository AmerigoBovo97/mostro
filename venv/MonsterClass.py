"""
Questo file  contiene la classe che verrà utilizzata per la creazione di ogni nuovo mostro, per adesso si può ignorare
"""


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
