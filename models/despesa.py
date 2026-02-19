from models.transacao import Transacao


class Despesa(Transacao):
    def impacto_no_saldo(self) -> float:
        return -self.valor
