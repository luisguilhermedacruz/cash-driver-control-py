from models.transacao import Transacao

class Receita(Transacao):
    def impacto_no_saldo(self) -> float:
        return self.valor