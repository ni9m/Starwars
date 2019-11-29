class Acteurs:
    def __init__(self, nom="Nom", prenom="Prenom", duet=["pers1", "pers2"], nbperso=1):
        self.nom = nom
        self.prenom = prenom
        self.duet = duet
        self.nbperso = nbperso

    def get__nbperso(self):
        return self.nbperso

    def get__prenom(self):
        return self.prenom

    def get__nom(self):
        return self.nom

    def get__duet(self):
        return self.duet

    def set__prenom(self, prenom):
        self.prenom = prenom

    def set__nom(self, nom):
        self.nom = nom

    def set__duet(self, duet):
        self.duet = duet

    def set__nbperso(self, nbperso):
        self.nbperso = nbperso