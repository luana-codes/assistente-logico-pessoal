from prolog import consultar, verdade, atomo, BASE


def mostrar(titulo, itens):
    print(f"\n== {titulo} ==")
    if not itens:
        print("  (nada encontrado)")
    for item in itens:
        print("  -", item)


def minhas_disciplinas():
    r = consultar("cursa(D, Dia, Turno)", ["D", "Dia", "Turno"])
    mostrar("Minhas disciplinas", [f"{x['D']} ({x['Dia']}, {x['Turno']})" for x in r])

def agenda_do_dia():
    dia = atomo(input("Qual dia? (segunda, terca, quarta, quinta, sexta, sabado): "))
    r = consultar(f"o_que_faco({dia}, T, A)", ["T", "A"])
    mostrar(f"Agenda de {dia}", [f"{x['T']}: {x['A']}" for x in r])


def horarios_livres():
    r = consultar("livre(D, T)", ["D", "T"])
    mostrar("Horários livres", [f"{x['D']} de {x['T']}" for x in r])


def estou_livre():
    dia = atomo(input("Dia: "))
    turno = atomo(input("Turno (manha, tarde, noite): "))
    if verdade(f"livre({dia}, {turno})"):
        print(f"\nSim! {dia} de {turno} está livre.")
    else:
        print(f"\nNão: {dia} de {turno} está ocupado (ou dia/turno inválido).")


def posso_ensinar():
    r = consultar("pode_ensinar(L)", ["L"])
    mostrar("Linguagens que posso ensinar", [x["L"].upper() for x in r])


def meus_gostos():
    categoria = atomo(input("Categoria (serie, comida, hobby, musica...): "))
    r = consultar(f"gosta({categoria}, I)", ["I"])
    mostrar(f"Gosto de ({categoria})", [x["I"].replace("_", " ") for x in r])


def dias_cheios():
    r = consultar("dia_cheio(D)", ["D"])
    mostrar("Dias cheios (2 turnos ou mais ocupados)", [x["D"] for x in r])

def minha_regra():
    # R6: disciplinas que curso à noite em dias em que estou livre à tarde
    r = consultar("dupla_de_estudo(D)", ["D"])
    mostrar("Disciplinas para dupla de estudo", [x["D"].replace("_", " ") for x in r])

def cadastrar_gosto():
    categoria = atomo(input("Categoria: "))
    item = atomo(input("Item: "))
    with open(BASE, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\ngosta({categoria}, {item}).")
    print(f"Aprendi: você gosta de {item.replace('_', ' ')} ({categoria}).")

OPCOES = {
    "1": ("Minhas disciplinas", minhas_disciplinas),
    "2": ("Agenda de um dia", agenda_do_dia),
    "3": ("Horários livres", horarios_livres),
    "4": ("Estou livre em...?", estou_livre),
    "5": ("Linguagens que posso ensinar", posso_ensinar),
    "6": ("Meus gostos por categoria", meus_gostos),
    "7": ("Dias cheios", dias_cheios),
    "8": ("Minha regra", minha_regra),
    "9": ("Cadastrar um gosto", cadastrar_gosto),
}

def menu():
    nome = consultar("eu(N)", ["N"])[0]["N"]
    while True:
        print(f"\n=== Assistente pessoal de {nome} ===")
        for chave, (titulo, _) in OPCOES.items():
            print(f"{chave}. {titulo}")
        print("0. Sair")
        op = input("> ").strip()
        if op == "0":
            print("Até mais!")
            break
        if op not in OPCOES:
            print("Opção inválida.")
            continue
        try:
            OPCOES[op][1]()
        except (ValueError, RuntimeError) as erro:
            print("Ops:", erro)


if __name__ == "__main__":
    menu()