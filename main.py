from models.receita import Receita
from models.despesa import Despesa


r1 = Receita(200, "Corridas da manhã")
d1 = Despesa(80, "Gasolina")

lucroDoDia = r1 - d1

print(r1)
print(d1)
print(f"Lucro do dia foi: R$ {lucroDodia}")

print("Impacto Receita:", r1.impacto_no_saldo())
print("Impacto Despesa:", d1.impacto_no_saldo())
