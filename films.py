class Films:
    def __init__(self, titre="Nom", annee=1900, numero=99, cout=100000, recette=300000,
                 col=["IronMan", "SipderMan", "AntMan"], col2=["Daniel Craig", "Samuel L. Jackson", "Brad Pitt"],
                 nbActeurs=3, nbPerso=5):
        self.titre = titre
        self.annee = annee
        self.numero = numero
        self.cout = cout
        self.recette = recette
        self.col = col
        self.col2 = col2
        self.nbActeurs = nbActeurs
        self.nbPerso = nbPerso

    def dico(self, titre, annee, benef):
        self.dictionnaire = {
            "titre": titre,
            "annee": annee,
            "benef": benef
        }

    def calcul(self, cout, recette):
        calcul = int(recette) - int(cout)

        if calcul >= 0:
            print("Le film a réalisé des bénéfices :")
        else:
            print("Le film a réalisé des pertes : ")
        return calcul

    def isbefore(self, anneesaisie):
        if anneesaisie < self.annee:
            k = False
        else:
            k = True
        return k

    def tri(self):
        return sorted(self.col2)

    def get__nbPerso(self):
        return self.nbPerso

    def get__nbActeurs(self):
        return self.nbActeurs

    def get__col(self):
        return self.col

    def get__titre(self):
        return self.titre

    def get__annee(self):
        return self.annee

    def get__numero(self):
        return self.numero

    def get__cout(self):
        return self.cout

    def get__recette(self):
        return self.recette

    def set__titre(self, titre):
        self.titre = titre

    def set__annee(self, annee):
        self.annee = annee

    def set__numero(self, numero):
        self.numero = numero

    def set__cout(self, cout):
        self.cout = cout

    def set__recette(self, recette):
        self.recette = recette
