# prolog.py · ponte entre o Python e o SWI-Prolog (não precisa alterar)
import re
import subprocess

BASE = "meus_dados.pl"


def consultar(consulta, variaveis=()):
    """Faz uma consulta ao Prolog e devolve uma lista de dicionários.

    consultar("sabe(L, N)", ["L", "N"])
      -> [{"L": "python", "N": "intermediario"}, {"L": "sql", "N": "avancado"}]
    """
    variaveis = list(variaveis)
    if variaveis:
        molde = "\\t".join(["~w"] * len(variaveis)) + "~n"
    else:
        molde = "sim~n"
    objetivo = f'forall(({consulta}), format("{molde}", [{", ".join(variaveis)}]))'
    try:
        r = subprocess.run(
            ["swipl", "-q", "-g", "set_stream(user_output, encoding(utf8))",
             "-g", objetivo, "-t", "halt", BASE],
            capture_output=True, text=True, encoding="utf-8",
        )
    except FileNotFoundError:
        raise SystemExit("Não encontrei o comando swipl. O SWI-Prolog está instalado e no PATH?")
    if r.returncode != 0:
        raise RuntimeError("Erro no Prolog:\n" + r.stderr.strip())
    if r.stderr.strip():
        print("[aviso do Prolog]", r.stderr.strip())
    linhas = [linha for linha in r.stdout.splitlines() if linha.strip()]
    if not variaveis:
        return linhas
    return [dict(zip(variaveis, linha.split("\t"))) for linha in linhas]


def verdade(consulta):
    """True se a consulta tem pelo menos uma solução."""
    return len(consultar(consulta)) > 0


def atomo(texto):
    """Valida o que o usuário digitou antes de colocar na consulta."""
    t = texto.strip().lower().replace(" ", "_")
    if not re.fullmatch(r"[a-z][a-z0-9_]*", t):
        raise ValueError("Digite só letras minúsculas, números e _ (sem acento).")
    return t
