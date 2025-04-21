from collections import deque

from busca_em_largura import busca_em_largura
from capital import Capital, capitais
from obter_capital import obter_capital
import re

#Dicionario de cada capital, com seus vizinhos, cada vizinho tem uma distância e um valor de pedágio
#Não sei se vai ser útil, mas inclui a própria capital no dicionário
aracaju = {
    "aracaju": Capital(0, 0),
    "salvador": Capital(356, 10.10),#1
    "maceio": Capital(294, 8.25),#2
    "vizinhos": ["salvador", "maceio"]
}

belem = {
    "belem": Capital(0, 0),
    "cuiaba": Capital(2.941, 110.25),#1
    "palmas": Capital(1.283, 55.50),#2
    "sao_luis": Capital(806, 25.10),#3
    # "macapa": Capital(0, 0),
    "boa_vista": Capital(6.083, 515.05),#4
    "manaus": Capital(5.298, 485.75),#5
    "vizinhos": ["cuiba", "palmas", "sao_luis", "boa_vista", "manaus"]
}

belo_horizonte = {
    "belo_horizonte": Capital(0, 0),
    "sao_paulo": Capital(586, 201.50),#1
    "rio_de_janeiro": Capital(434, 196.05),#2
    "vitoria": Capital(524, 175.50),#3
    "salvador": Capital(1.372, 65.10),#4
    "brasilia": Capital(716, 38.75),#5
    "goiania": Capital(906, 55.25),#6
    "vizinhos": ["sao_paulo", "rio_de_janeiro", "vitoria", "salvador", "brasilia", "goiania"]
}

boa_vista = {
    "boa_vista": Capital(0, 0),
    "manaus": Capital(785, 75.75),#1
    "belem": Capital(6.083, 515.05),#2
    "vizinhos": ["manaus", "belem"]
}

brasilia = {
    "brasilia": Capital(0, 0),
    "belo_horizonte": Capital(716, 38.75),#1
    "goiania": Capital(209, 0.50),#2
    "vizinhos": ["belo_horizonte", "goiania"]
}

campo_grande = {
    "campo_grande": Capital(0, 0),
    "curitiba": Capital(991, 125.00),#1
    "sao_paulo": Capital(1014, 62.10),#2
    "goiania": Capital(935, 25.05),#3
    "cuiaba": Capital(694, 120.00),#4
    "vizinhos": ["curitiba", "sao_paulo", "goiania", "cuiaba"]
}

cuiaba = {
    "cuiaba": Capital(0, 0),
    "campo_grande": Capital(694, 120.00),#1
    "goiania": Capital(934, 120.00),#2
    "palmas": Capital(1784, 123.25),#3
    "belem": Capital(2941, 110.25),#4
    "manaus": Capital(2357, 135.25),#5
    "porto_velho": Capital(1.456, 68.75),#6
    "vizinhos": ["campo_grande", "goiania", "palmas", "belem", "manaus", "porto_velho"]
}

curitiba = {
    "curitiba": Capital(0, 0),
    "florianopolis": Capital(300, 51.10),#1
    "sao_paulo": Capital(408, 99.75),#2
    "campo_grande": Capital(991, 125.00),#3
    "vizinhos": ["florianopolis", "sao_paulo", "campo_grande"]
}

florianopolis = {
    "florianopolis": Capital(0, 0),
    "porto_alegre": Capital(476, 112.25),#1
    "curitiba": Capital(300, 51.10),#2
    "vizinhos": ["porto_alegre", "curitiba"]
}

fortaleza = {
    "fortaleza": Capital(0, 0),
    "recife": Capital(800, 80.00),#1
    "joao_pessoa": Capital(688, 50.00),#2
    "natal": Capital(537, 66.10),#3
    "teresina": Capital(634, 25.05),#4
    "vizinhos": ["recife", "joao_pessoa", "natal", "teresina"]
}

goiania = {
    "goiania": Capital(0, 0),
    "campo_grande": Capital(935, 25.05),#1
    "belo_horizonte": Capital(906, 55.25),#2
    "brasilia": Capital(209, 0.50),#3
    "salvador": Capital(1643, 101.10),#4
    "palmas": Capital(874, 32.10),#5
    "cuiaba": Capital(934, 120.00),#6
    "vizinhos": ["campo_grande", "belo_horizonte", "brasilia", "salvador", "palmas", "cuiba"]
}

joao_pessoa = {
    "joao_pessoa": Capital(0, 0),
    "recife": Capital(120, 20.25),#1
    "natal": Capital(185, 5.00),#2
    "fortaleza": Capital(688, 50.00),#3
    "vizinhos": ["recife", "natal", "fortaleza"]
}

macapa = {
    "macapa": Capital(0, 0),
    #"belem": Capital(0, 0)
    #"vizinhos": ["belem"]
}

maceio = {
    "maceio":  Capital(0, 0),
    "aracaju": Capital(294, 8.25),#1
    "recife":  Capital(285, 18.05),#2
    "salvador": Capital(632, 40.25),#3
    "vizinhos": ["aracaju", "recife", "salvador"]
}

manaus = {
    "manaus": Capital(0, 0),
    "porto_velho": Capital(901,66.10),#1
    "cuiaba": Capital(2.357, 135.25),#2
    "belem": Capital(5298, 485.75),#3
    "boa_vista": Capital(785, 75.75),#4
    "rio_branco": Capital(1445,100.00),#5
    "vizinhos": ["porto_velho", "cuiaba", "boa_vista", "rio_branco"]
}

natal = {
    "natal": Capital(0, 0),
    "joao_pessoa": Capital(185, 5.00),#1
    "fortaleza": Capital(537, 66.10),#2
    "vizinhos": ["joao_pessoa", "fortaleza"]
}

palmas = {
    "palmas": Capital(0, 0),
    "goiania": Capital(874, 32.10),#1
    "salvador": Capital(1454, 106.25),#2
    "teresina": Capital(1401, 102.25),#3
    "sao_luis": Capital(1386, 90.50),#4
    "belem": Capital(1283, 55.50),#5
    "cuiaba": Capital(1784, 123.25),#6
    "vizinhos": ["goiania", "salvador", "teresina", "sao_luis", "belem", "cuiaba"]
}

porto_alegre = {
    "porto_alegre": Capital(0, 0),
    "florianopolis": Capital(476, 112.25),#1
    "vizinhos": ["florianopolis"]
}

porto_velho = {
    "porto_velho": Capital(0, 0),
    "cuiaba": Capital(1456, 68.75),#1
    "manaus": Capital(901,66.10),#2
    "rio_branco": Capital(544,30.50),#3
    "vizinhos": ["cuiaba", "manaus", "rio_branco"]
}

recife = {
    "recife":  Capital(0, 0),
    "maceio": Capital(285, 18.05),#1
    "joao_pessoa": Capital(120, 20.25),#2
    "fortaleza":  Capital(800, 80.00),#3
    "teresina": Capital(1137, 105.05),#4
    "salvador": Capital(839, 45.25),#5
    "vizinhos": ["maceio", "joao_pessoa", "fortaleza", "teresina", "salvador"]
}

rio_branco = {
    "rio_branco": Capital(0, 0),
    "porto_velho": Capital(544,30.50),#1
    "": Capital(1445,100.00),#2
    "vizinhos": ["porto_velho", "manaus"]
}

rio_de_janeiro = {
    "rio_de_janeiro": Capital(0, 0),
    "sao_paulo": Capital(429, 15.05),#1
    "vitoria": Capital(521, 20.0),#2
    "belo_horizonte": Capital(434, 196.05),#3
    "vizinhos": ["sao_paulo", "vitoria", "belo_horizonte"]
}

salvador = {
    "salvador": Capital(0, 0),
    "belo_horizonte": Capital(1372, 65.10),#1
    "vitoria": Capital(1202, 55.50),#2
    "aracaju": Capital(356, 10.10),#3
    "maceio":  Capital(632, 40.25),#4
    "recife": Capital(839, 45.25),#5
    "teresina": Capital(1163, 100.00),#6
    "palmas": Capital(1454, 106.25),#7
    "goiana": Capital(1643, 101.10),#8
    "vizinhos": ["belo_horizonte", "vitoria", "aracaju", "maceio", "recife", "teresina", "palmas", "goiana"]
}

sao_luis = {
    "sao_luis": Capital(0, 0),
    "palmas": Capital(1386, 90.50),#1
    "teresina": Capital(446, 12.05),#2
    "belem": Capital(806, 25.10),#3
    "vizinhos": ["palmas", "teresina", "belem"]
}

sao_paulo = {
    "sao_paulo": Capital(0, 0),
    "curitiba":  Capital(408, 99.75),#1
    "rio_de_janeiro": Capital(429, 15.05),#2
    "belo_horizonte": Capital(586, 201.50),#3
    "campo_grande": Capital(1014, 62.10),#4
    "vizinhos": ["curitiba", "rio_de_janeiro", "belo_horizonte", "campo_grande"]
}

teresina = {
    "teresina": Capital(0, 0),
    "salvador": Capital(1163, 100.00),#1
    "recife": Capital(1137, 105.05),#2
    "fortaleza": Capital(634, 25.05),#3
    "sao_luis": Capital(446, 12.05),#4
    "palmas": Capital(1401, 102.25),#5
    "vizinhos": ["salvador", "recife", "fortaleza", "sao_luis", "palmas"]
}

vitoria = {
    "vitoria": 0,
    "rio_de_janeiro": Capital(521, 20.0),#1
    "belo_horizonte": Capital(524, 175.50),#2
    "salvador": Capital(1202, 55.50),#3
    "vizinhos": ["rio_de_janeiro", "belo_horizonte", "salvador"]
}

#Outro dicionário de dicionários (redundante? Talvez...)
#Assim conseguimos percorrer as rotas conforme a origem/destino do usuário
rotas = {
    "aracaju" : aracaju,
    "belem": belem,
    "belo_horizonte": belo_horizonte,
    "boa_vista": boa_vista,
    "brasilia": brasilia,
    "campo_grande": campo_grande,
    "cuiaba": cuiaba,
    "curitiba": curitiba,
    "florianopolis": florianopolis,
    "fortaleza": fortaleza,
    "goiania": goiania,
    "joao_pessoa": joao_pessoa,
    "macapa": macapa,
    "maceio": maceio,
    "manaus": manaus,
    "natal": natal,
    "palmas": palmas,
    "porto_alegre": porto_alegre,
    "porto_velho": porto_velho,
    "recife": recife,
    "rio_branco": rio_branco,
    "rio_de_janeiro": rio_de_janeiro,
    "salvador": salvador,
    "sao_luis": sao_luis,
    "sao_paulo": sao_paulo,
    "teresina": teresina,
    "vitoria": vitoria
}

regex = r"^(?:[1-9]|1[0-9]|2[0-7])$"#regex para digitar somente número válidos
flag = True #se não passar no regex não deixa chamar a busca
raiz = ""#nó do qual irá iniciar a busca
no_destino = ""#nó que precisa ser alcançado

print("Capitais do Brasil:")
i = 1
for capital in sorted(capitais):
    print(f"- {i} - {capital}")
    i += 1

origem = input("Escolha uma capital de origem (de 1 a 27): ")
if re.match(regex, origem):
    raiz = obter_capital(int(origem))  # guardei numa variável para ficar mais legível
    print(raiz)
else:
    print("Entrada inválida!")
    flag = False

destino = input("Escolha uma capital destino (de 1 a 27): ")
if re.match(regex, destino):
    no_destino = obter_capital(int(destino))#'no' de nó da árvore, mas ficou 'NO' porque não vai acento
    print(no_destino,"\n")
else:
    print("Entrada inválida!")
    flag = False


custo = 0.0
vizinhos = deque() #um FIFO resolve o problema de validar todos na largura, melhor coisa do mundo!
if flag:
    visitados = [raiz] #essa lista será preenchida conforme as capitais expandidas
    #no caso a origem já deve estar na lista, teoricamente ela já foi visitada
    if raiz == no_destino:#da maneira que foi implentado a busca não consegue achar se a origem é o destino
        print("\n\nDestino alcançado!!!\n\n")#essa é a solução para contornar esse problema
    else:
        print("Iniciando a Busca em Largura!\n")
        custo = busca_em_largura(raiz, rotas, no_destino, vizinhos, visitados)
else:
    print("\nHouve um problema na leitura da origem/destino")
print("\nCusto da viagem: ", custo)