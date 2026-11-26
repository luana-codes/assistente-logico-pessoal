:- encoding(utf8).
:- discontiguous gosta/2.
% =====================================================================
%  meus_dados.pl · Assistente Lógico Pessoal · LPP
%  Base de conhecimento pessoal. Troque os dados de exemplo (da "alex")
%  pelos SEUS dados. Use só letras minúsculas, sem acento e sem espaço
%  nos átomos (ex.: banco_de_dados, the_office).
%  NÃO coloque dados sensíveis: CPF, endereço, telefone, saúde, etc.
% =====================================================================

% ---------- ETAPA 2 · FATOS ----------

% Quem sou eu
eu(luana).
fase(6).
cidade(rio_do_sul).

% Dias e turnos da semana (não altere)
dia(segunda).  dia(terca).  dia(quarta).  dia(quinta).  dia(sexta).  dia(sabado).
turno(manha).  turno(tarde).  turno(noite).

% Disciplinas que curso neste semestre: cursa(Disciplina, Dia, Turno)
cursa(lpp, quarta, noite).
cursa(redes_de_computadores, segunda, noite).
cursa(desenvolvimento_para_plataformas_moveis, terca, noite).
cursa(estrutura_de_dados_ii, quinta, noite).
cursa(administracao_e_sistemas_de_informacao, sexta, noite).

% Outros compromissos: compromisso(Dia, Turno, Atividade)
compromisso(segunda, manha, trabalho).
compromisso(segunda, tarde, trabalho).
compromisso(terca, manha, trabalho).
compromisso(quarta, tarde, trabalho).
compromisso(sabado, manha, dormir).

% Linguagens que sei: sabe(Linguagem, Nivel)   Nivel: basico | intermediario | avancado
sabe(python, intermediario).
sabe(javascript, basico).
sabe(sql, intermediario).

% Do que eu gosto: gosta(Categoria, Item)
gosta(serie, o_mentalista).
gosta(serie, the_office).
gosta(comida, pizza).
gosta(comida, sushi).
gosta(hobby, ler).
gosta(musica, taylor_swift).

% ---------- ETAPA 3 · REGRAS ----------
% R1 · Estou ocupado se tenho aula OU compromisso (duas cláusulas = OU)
ocupado(Dia, Turno) :- cursa(_, Dia, Turno).
ocupado(Dia, Turno) :- compromisso(Dia, Turno, _).

% R2 · Estou livre se NÃO for possível provar que estou ocupado
livre(Dia, Turno) :- dia(Dia), turno(Turno), \+ ocupado(Dia, Turno).

% R3 · O que faço em um dia e turno (aula ou compromisso)
o_que_faco(Dia, Turno, Atividade) :- cursa(Atividade, Dia, Turno).
o_que_faco(Dia, Turno, Atividade) :- compromisso(Dia, Turno, Atividade).

% R4 · Posso ensinar uma linguagem se sei em nível intermediário ou avançado
pode_ensinar(Linguagem) :- sabe(Linguagem, Nivel), member(Nivel, [intermediario, avancado]).

% R5 · Dia cheio: dois turnos ou mais ocupados
dia_cheio(Dia) :- dia(Dia), findall(T, ocupado(Dia, T), Ts), sort(Ts, Unicos), length(Unicos, N), N >= 2.

% R6 · MINHA REGRA: dupla_de_estudo(D)
% D é uma disciplina que curso à noite em um dia em que
% também estou livre à tarde, ou seja, dá para estudar
% com um colega antes da aula.
dupla_de_estudo(D) :- cursa(D, Dia, noite), livre(Dia, tarde).
gosta(filme, interestelar).
gosta(filme, interestelar).