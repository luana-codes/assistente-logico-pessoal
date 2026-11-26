# teste_ponte.py · confere se o Python conversa com o Prolog
from prolog import consultar, verdade

print("Quem sou eu:", consultar("eu(N)", ["N"]))
print("O que sei:", consultar("sabe(L, N)", ["L", "N"]))
print("Livre sexta à noite?", verdade("livre(sexta, noite)"))
