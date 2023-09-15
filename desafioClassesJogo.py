class Heroi:
    ATAQUES = {
        "Mago": "magia",
        "Guerreiro": "espada",
        "Monge": "artes marciais",
        "Ninja": "shuriken",
    }

    def __init__(self, nome, idade, tipo):
        self.heroi = {"nome": nome, "idade": idade, "tipo": tipo}

    def atacar(self):
        tipo = self.heroi["tipo"]
        ataque = Heroi.ATAQUES.get(tipo, "realizou um ataque")
        print(f"O {self.heroi['tipo']} atacou usando {ataque}")

reiArthur = Heroi("Rei Arthur", 24, "Ninja")
Merlin = Heroi("Merlin", 112, "Mago")
Arlong = Heroi("Arlong - Peixe-Serra", 85, "Guerreiro")
DrEstranho = Heroi("DrEstranho", 47, "Monge")

reiArthur.atacar()
Merlin.atacar()
Arlong.atacar()
DrEstranho.atacar()
