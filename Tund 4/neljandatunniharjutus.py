from kolmpind import kolmnurga_pind
from ruutpind import ruudu_pind
from ristpind import rist_pind

tehe = input("Kas sa soovid Kolmnurga, Ruudu või Ristküliku pindala teada? -")
print(tehe)
if tehe=="Kolmnurga":
    print(kolmnurga_pind())
if tehe=="Ruudu":
    print(ruudu_pind())
if tehe=="Ristküliku":
    print(rist_pind())

input()