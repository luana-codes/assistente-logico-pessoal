# Assistente Lógico Pessoal

> Atividade da disciplina Linguagem de Programação e Paradigmas · UNIDAVI · 2026/2

**Aluno(a):** Luana Aparecida Guilherme
**Linguagem do sistema:** Python

## O que é

Uma base de conhecimento em Prolog (`meus_dados.pl`) com fatos e regras sobre mim e um assistente em linha de comando que consulta essa base pela ponte (`prolog.py`).

## Como executar

Requisitos: SWI-Prolog no PATH e Python 3.

```bash
# testar a ponte
python teste_ponte.py      

# executar o assistente
python assistente.py       
```

## Minha base

- Fatos: `eu/1`, `cursa/3`, `compromisso/3`, `sabe/2`, `gosta/2`
- Regras: `ocupado/2`, `livre/2`, `o_que_faco/3`, `pode_ensinar/1`, `dia_cheio/1` e a minha regra abaixo
- Bônus: a opção 9 do menu ("Cadastrar um gosto") acrescenta um fato `gosta/2` ao fim de `meus_dados.pl`.

## Minha regra (R6)

```prolog
% D é uma disciplina que curso à noite em um dia em que
% também estou livre à tarde, ou seja, dá para estudar
% com um colega antes da aula.
dupla_de_estudo(D) :- cursa(D, Dia, noite), livre(Dia, tarde).
```

**O que ela significa:** `dupla_de_estudo(D)` encontra as disciplinas em que dá para estudar com um colega antes da aula. O primeiro subobjetivo, `cursa(D, Dia, noite)`, verifica quais disciplinas eu curso à noite e em que dia. O segundo, `livre(Dia, tarde)`, verifica se, naquele mesmo dia, a tarde está livre (sem aula nem compromisso).

## Saída real do assistente

```text
python assistente.py


=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 1

== Minhas disciplinas ==
  - lpp (quarta, noite)
  - redes_de_computadores (segunda, noite)
  - desenvolvimento_para_plataformas_moveis (terca, noite)
  - estrutura_de_dados_ii (quinta, noite)
  - administracao_e_sistemas_de_informacao (sexta, noite)

=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 4
Dia: sexta
Turno (manha, tarde, noite): noite

Não: sexta de noite está ocupado (ou dia/turno inválido).

=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 8

== Disciplinas para dupla de estudo ==
  - desenvolvimento para plataformas moveis
  - estrutura de dados ii
  - administracao e sistemas de informacao

=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 2
Qual dia? (segunda, terca, quarta, quinta, sexta, sabado): Seg unda!
Ops: Digite só letras minúsculas, números e _ (sem acento).

=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 9
Categoria: filme 
Item: interestelar
Aprendi: você gosta de interestelar (filme).

=== Assistente pessoal de luana ===
1. Minhas disciplinas
2. Agenda de um dia
3. Horários livres
4. Estou livre em...?
5. Linguagens que posso ensinar
6. Meus gostos por categoria
7. Dias cheios
8. Minha regra
9. Cadastrar um gosto
0. Sair
> 0
Até mais!
```
