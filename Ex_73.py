#073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 'Atletico Mineiro', 'Fortaleza', 'São Paulo', 'América Fc SAF', 'Botafogo', 'Santos', 'Goiás', 'Bragantino','Coritiba','Cuiaba Saf', 'Ceará', 'Atlético GO', 'Avaí', 'Juventude')
print(brasileirao[0:5])
print(brasileirao[-4:])
print(sorted(brasileirao))
if 'Chapecoense' in brasileirao:
    pos = brasileirao.index('Chapecoense',0)
    print(pos)
else:
    print('Chapecoense não está na lista')