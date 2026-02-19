from datetime import datetime


class Transacao:
    def __init__(self, valor: float, descricao: str, data: datetime | None = None):
        self.valor = float(valor)
        self.descricao = descricao.strip()
        self.data = data or datetime.now()

    def impacto_no_saldo(self) -> float:
        raise NotImplementedError("Implemente nas classes filhas.")

    def __repr__(self) -> str:
        data_br = self.data.strftime("%d/%m/%Y")
        return f"{data_br} | {self.__class__.__name__} | R$ {self.valor:.2f} | {self.descricao}"
