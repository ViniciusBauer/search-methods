from collections import deque

from busca_em_largura import busca_em_largura           # Busca em largura
from busca_em_profundidade import busca_em_profundidade
from capital import Capital, capitais                   # Lista das capitais + classe capital
from obter_capital import obter_capital                 # Switch case de cada capital (1-27)
import re                                               # Expressões regulares

#Dicionario de cada capital, com seus vizinhos, cada vizinho tem uma distância e um valor de pedágio
aracaju = {
    "aracaju": Capital(0, 0, 0),
    "salvador": Capital(356, 10.10, 277),  # 1
    "maceio": Capital(294, 8.25, 202),  # 2
    "vizinhos": ["salvador", "maceio"],

    # Não vizinhos, mas com distância em linha reta
    "rio_branco": Capital(0, 0, 3361),
    # "macapa": Capital(0, 0, 1968),
    "manaus": Capital(0, 0, 2675),
    "fortaleza": Capital(0, 0, 816),
    "brasilia": Capital(0, 0, 1293),
    "vitoria": Capital(0, 0, 1100),
    "goiania": Capital(0, 0, 1463),
    "sao_luis": Capital(0, 0, 1227),
    "cuiaba": Capital(0, 0, 2123),
    "campo_grande": Capital(0, 0, 2157),
    "belo_horizonte": Capital(0, 0, 1245),
    "belem": Capital(0, 0, 1643),
    "joao_pessoa": Capital(0, 0, 487),
    "curitiba": Capital(0, 0, 2064),
    "recife": Capital(0, 0, 399),
    "teresina": Capital(0, 0, 904),
    "rio_de_janeiro": Capital(0, 0, 1491),
    "natal": Capital(0, 0, 605),
    "porto_alegre": Capital(0, 0, 2582),
    "porto_velho": Capital(0, 0, 2948),
    "boa_vista": Capital(0, 0, 3025),
    "florianopolis": Capital(0, 0, 2209),
    "sao_paulo": Capital(0, 0, 1735),
    "palmas": Capital(0, 0, 1234)
}

belem = {
    "belem": Capital(0, 0, 0),
    "cuiaba": Capital(2941, 110.25, 1780),  # 1
    "palmas": Capital(1283, 55.50, 970),  # 2
    "sao_luis": Capital(806, 25.10, 482),  # 3
    # "macapa": Capital(0, 0, 330),
    "boa_vista": Capital(6083, 515.05, 1434),  # 4
    "manaus": Capital(5298, 485.75, 1294),  # 5
    "vizinhos": ["cuiaba", "palmas", "sao_luis", "boa_vista", "manaus"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1643),
    "salvador": Capital(0, 0, 1689),  
    "maceio": Capital(0, 0, 1682),  
    "rio_branco": Capital(0, 0, 2335),
    "fortaleza": Capital(0, 0, 1135),
    "brasilia": Capital(0, 0, 1595),
    "vitoria": Capital(0, 0, 2277),
    "goiania": Capital(0, 0, 1695),
    "campo_grande": Capital(0, 0, 2215),
    "belo_horizonte": Capital(0, 0, 2116),
    "joao_pessoa": Capital(0, 0, 1638),
    "curitiba": Capital(0, 0, 2669),
    "recife": Capital(0, 0, 1679),
    "teresina": Capital(0, 0, 751),
    "rio_de_janeiro": Capital(0, 0, 2461),
    "natal": Capital(0, 0, 1552),
    "porto_alegre": Capital(0, 0, 3191),
    "porto_velho": Capital(0, 0, 1889),
    "florianopolis": Capital(0, 0, 2907),
    "sao_paulo": Capital(0, 0, 2467),
}

belo_horizonte = {
    "belo_horizonte": Capital(0, 0, 0),
    "sao_paulo": Capital(586, 201.50, 491),  # 1
    "rio_de_janeiro": Capital(434, 196.05, 349),  # 2
    "vitoria": Capital(524, 175.50, 383),  # 3
    "salvador": Capital(1372, 65.10, 966),  # 4
    "brasilia": Capital(716, 38.75, 625),  # 5
    "goiania": Capital(906, 55.25, 667),  # 6
    "vizinhos": ["sao_paulo", "rio_de_janeiro", "vitoria", "salvador", "brasilia", "goiania"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1243),
    "maceio": Capital(0, 0, 1441),  
    "rio_branco": Capital(0, 0, 2788),
    # "macapa": Capital(0, 0, 2351),
    "manaus": Capital(0, 0, 2556),
    "fortaleza": Capital(0, 0, 1895),
    "sao_luis": Capital(0, 0, 1934),
    "cuiaba": Capital(0, 0, 1374),
    "campo_grande": Capital(0, 0, 1120),
    "belem": Capital(0, 0, 2113),
    "joao_pessoa": Capital(0, 0, 1728),
    "curitiba": Capital(0, 0, 823),
    "recife": Capital(0, 0, 1642),
    "teresina": Capital(0, 0, 1654),
    "natal": Capital(0, 0, 1833),
    "porto_alegre": Capital(0, 0, 1343),
    "porto_velho": Capital(0, 0, 2479),
    "boa_vista": Capital(0, 0, 3120),
    "florianopolis": Capital(0, 0, 974),
    "palmas": Capital(0, 0, 1183)
}

boa_vista = {
    "boa_vista": Capital(0, 0, 0),
    "manaus": Capital(785, 75.75, 665),  # 1
    "belem": Capital(6083, 515.05, 1434),  # 2
    "vizinhos": ["manaus", "belem"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 3025),
    "salvador": Capital(0, 0, 3012), 
    "maceio": Capital(0, 0, 3092),  
    "rio_branco": Capital(0, 0, 1628),
    # "macapa": Capital(0, 0, 1112),
    "fortaleza": Capital(0, 0, 2565),
    "brasilia": Capital(0, 0, 2499),
    "vitoria": Capital(0, 0, 3398),
    "goiania": Capital(0, 0, 2505),
    "sao_luis": Capital(0, 0, 1914),
    "cuiaba": Capital(0, 0, 2110),
    "campo_grande": Capital(0, 0, 2669),
    "belo_horizonte": Capital(0, 0, 3122),
    "joao_pessoa": Capital(0, 0, 3070),
    "curitiba": Capital(0, 0, 3374),
    "recife": Capital(0, 0, 3107),
    "teresina": Capital(0, 0, 2172),
    "rio_de_janeiro": Capital(0, 0, 3438),
    "natal": Capital(0, 0, 2986),
    "porto_alegre": Capital(0, 0, 3789),
    "porto_velho": Capital(0, 0, 1337),
    "florianopolis": Capital(0, 0, 3623),
    "sao_paulo": Capital(0, 0, 3304),
    "palmas": Capital(0, 0, 1989)
}

brasilia = {
    "brasilia": Capital(0, 0, 0),
    "belo_horizonte": Capital(716, 38.75, 628),  # 1
    "goiania": Capital(209, 0.50, 174),  # 2
    "vizinhos": ["belo_horizonte", "goiania"],

     # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1293),
    "salvador": Capital(0, 0, 1062), 
    "maceio": Capital(0, 0, 1487),  
    "rio_branco": Capital(0, 0, 2248),
    # "macapa": Capital(0, 0, 1792),
    "manaus": Capital(0, 0, 1932),
    "fortaleza": Capital(0, 0, 1689),
    "vitoria": Capital(0, 0, 950),
    "sao_luis": Capital(0, 0, 1526),
    "cuiaba": Capital(0, 0, 875),
    "campo_grande": Capital(0, 0, 880),
    "belem": Capital(0, 0, 1594),
    "joao_pessoa": Capital(0, 0, 1718),
    "curitiba": Capital(0, 0, 1084),
    "recife": Capital(0, 0, 1659),
    "teresina": Capital(0, 0, 1314), 
    "rio_de_janeiro": Capital(0, 0, 942),
    "natal": Capital(0, 0, 1777),
    "porto_alegre": Capital(0, 0, 1621),
    "porto_velho": Capital(0, 0, 1902),
    "boa_vista": Capital(0, 0, 3025),
    "florianopolis": Capital(0, 0, 2499),
    "sao_paulo": Capital(0, 0, 876),
    "palmas": Capital(0, 0, 626)
}

campo_grande = {
    "campo_grande": Capital(0, 0, 0),
    "curitiba": Capital(991, 125.00, 782),  # 1
    "sao_paulo": Capital(1014, 62.10, 894),  # 2
    "goiania": Capital(935, 25.05, 706),  # 3
    "cuiaba": Capital(694, 120.00, 560),  # 4
    "vizinhos": ["curitiba", "sao_paulo", "goiania", "cuiaba"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2157),
    "salvador": Capital(0, 0, 1908), 
    "maceio": Capital(0, 0, 2355),  
    "rio_branco": Capital(0, 0, 1829),
    # "macapa": Capital(0, 0, 2311),
    "manaus": Capital(0, 0, 2012),
    "fortaleza": Capital(0, 0, 2550),
    "brasilia": Capital(0, 0, 880),
    "vitoria": Capital(0, 0, 1496),
    "sao_luis": Capital(0, 0, 2286),
    "belo_horizonte": Capital(0, 0, 1120),
    "belem": Capital(0, 0, 2215),
    "joao_pessoa": Capital(0, 0, 2596),
    "recife": Capital(0, 0, 2533),
    "teresina": Capital(0, 0, 2134),
    "rio_de_janeiro": Capital(0, 0, 1216),
    "natal": Capital(0, 0, 2656),
    "porto_alegre": Capital(0, 0, 1121),
    "porto_velho": Capital(0, 0, 1636),
    "boa_vista": Capital(0, 0, 2669),
    "florianopolis": Capital(0, 0, 1008),
    "palmas": Capital(0, 0, 1328)
}

cuiaba = {
    "cuiaba": Capital(0, 0, 0),
    "campo_grande": Capital(694, 120.00, 560),  # 1
    "goiania": Capital(934, 120.00, 741),  # 2
    "palmas": Capital(1784, 123.25, 1036),  # 3
    "belem": Capital(2941, 110.25, 1780),  # 4
    "manaus": Capital(2357, 135.25, 1453),  # 5
    "porto_velho": Capital(1456, 68.75, 1139),  # 6
    "vizinhos": ["campo_grande", "goiania", "palmas", "belem", "manaus", "porto_velho"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2123),
    "salvador": Capital(0, 0, 1918), 
    "maceio": Capital(0, 0, 2304),  
    "rio_branco": Capital(0, 0, 1416),
    # "macapa": Capital(0, 0, 1824),
    "fortaleza": Capital(0, 0, 2331),
    "brasilia": Capital(0, 0, 875),
    "vitoria": Capital(0, 0, 1750),
    "sao_luis": Capital(0, 0, 1945),
    "belo_horizonte": Capital(0, 0, 1375),
    "joao_pessoa": Capital(0, 0, 2498),
    "curitiba": Capital(0, 0, 1304),
    "recife": Capital(0, 0, 2456),
    "teresina": Capital(0, 0, 1864),
    "rio_de_janeiro": Capital(0, 0, 1582),
    "natal": Capital(0, 0, 2526),
    "porto_alegre": Capital(0, 0, 1681),
    "boa_vista": Capital(0, 0, 2110),
    "florianopolis": Capital(0, 0, 1545),
    "sao_paulo": Capital(0, 0, 1327)
}

curitiba = {
    "curitiba": Capital(0, 0, 0),
    "florianopolis": Capital(300, 51.10, 251),  # 1
    "sao_paulo": Capital(408, 99.75, 337),  # 2
    "campo_grande": Capital(991, 125.00, 782),  # 3
    "vizinhos": ["florianopolis", "sao_paulo", "campo_grande"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2063),
    "salvador": Capital(0, 0, 1788), 
    "maceio": Capital(0, 0, 2262),  
    "rio_branco": Capital(0, 0, 2604),
    # "macapa": Capital(0, 0, 2838),
    "manaus": Capital(0, 0, 2735),
    "fortaleza": Capital(0, 0, 2673),
    "brasilia": Capital(0, 0, 1084),
    "vitoria": Capital(0, 0, 1082),
    "goiania": Capital(0, 0, 975),
    "sao_luis": Capital(0, 0, 2602),
    "cuiaba": Capital(0, 0, 1304),
    "belo_horizonte": Capital(0, 0, 820),
    "belem": Capital(0, 0, 2669),
    "joao_pessoa": Capital(0, 0, 2547),
    "recife": Capital(0, 0, 2463),
    "teresina": Capital(0, 0, 2365),
    "rio_de_janeiro": Capital(0, 0, 675),
    "natal": Capital(0, 0, 2647),
    "porto_alegre": Capital(0, 0, 546),
    "porto_velho": Capital(0, 0, 2415),
    "boa_vista": Capital(0, 0, 3374),
    "palmas": Capital(0, 0, 1700)
}

florianopolis = {
    "florianopolis": Capital(0, 0, 0),
    "porto_alegre": Capital(476, 112.25, 377),  # 1
    "curitiba": Capital(300, 51.10, 251),  # 2
    "vizinhos": ["porto_alegre", "curitiba"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2209),
    "salvador": Capital(0, 0, 1933), 
    "maceio": Capital(0, 0, 2404),  
    "rio_branco": Capital(0, 0, 2812),
    # "macapa": Capital(0, 0, 3085),
    "manaus": Capital(0, 0, 2982),
    "fortaleza": Capital(0, 0, 2860),
    "brasilia": Capital(0, 0, 1316),
    "vitoria": Capital(0, 0, 1167),
    "goiania": Capital(0, 0, 1217),
    "sao_luis": Capital(0, 0, 2824),
    "cuiaba": Capital(0, 0, 1545),
    "campo_grande": Capital(0, 0, 1008),
    "belo_horizonte": Capital(0, 0, 972),
    "belem": Capital(0, 0, 2907),
    "joao_pessoa": Capital(0, 0, 2696),
    "recife": Capital(0, 0, 2606),
    "teresina": Capital(0, 0, 2576),
    "rio_de_janeiro": Capital(0, 0, 744),
    "natal": Capital(0, 0, 2805),
    "porto_velho": Capital(0, 0, 2643),
    "boa_vista": Capital(0, 0, 3623),
    "sao_paulo": Capital(0, 0, 488),
    "palmas": Capital(0, 0, 1939)
}

fortaleza = {
    "fortaleza": Capital(0, 0, 0),
    "recife": Capital(800, 80.00, 631),  # 1
    "joao_pessoa": Capital(688, 50.00, 556),  # 2
    "natal": Capital(537, 66.10, 436),  # 3
    "teresina": Capital(634, 25.05, 497),  # 4
    "vizinhos": ["recife", "joao_pessoa", "natal", "teresina"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 816),
    "salvador": Capital(0, 0, 1029), 
    "maceio": Capital(0, 0, 731),  
    "rio_branco": Capital(0, 0, 3303),
    # "macapa": Capital(0, 0, 1453),
    "manaus": Capital(0, 0, 2385),
    "brasilia": Capital(0, 0, 1689),
    "vitoria": Capital(0, 0, 1853),
    "goiania": Capital(0, 0, 1857),
    "sao_luis": Capital(0, 0, 654),
    "cuiaba": Capital(0, 0, 2331),
    "campo_grande": Capital(0, 0, 2550),
    "belo_horizonte": Capital(0, 0, 1897),
    "belem": Capital(0, 0, 1135),
    "curitiba": Capital(0, 0, 2674),
    "rio_de_janeiro": Capital(0, 0, 2200),
    "porto_alegre": Capital(0, 0, 3217),
    "porto_velho": Capital(0, 0, 2858),
    "boa_vista": Capital(0, 0, 2565),
    "florianopolis": Capital(0, 0, 2860),
    "sao_paulo": Capital(0, 0, 2373),
    "palmas": Capital(0, 0, 1297)
}

goiania = {
    "goiania": Capital(0, 0, 0),
    "campo_grande": Capital(935, 25.05, 706),  # 1
    "belo_horizonte": Capital(906, 55.25, 671),  # 2
    "brasilia": Capital(209, 0.50, 174),  # 3
    "salvador": Capital(1643, 101.10, 1228),  # 4
    "palmas": Capital(874, 32.10, 731),  # 5
    "cuiaba": Capital(934, 120.00, 739),  # 6
    "vizinhos": ["campo_grande", "belo_horizonte", "brasilia", "salvador", "palmas", "cuiaba"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1463),
    "maceio": Capital(0, 0, 1659),  
    "rio_branco": Capital(0, 0, 2140),
    # "macapa": Capital(0, 0, 1869),
    "manaus": Capital(0, 0, 1912),
    "fortaleza": Capital(0, 0, 1857),
    "vitoria": Capital(0, 0, 1027),
    "sao_luis": Capital(0, 0, 1664),
    "belem": Capital(0, 0, 1695),
    "joao_pessoa": Capital(0, 0, 1893),
    "curitiba": Capital(0, 0, 975),
    "recife": Capital(0, 0, 1833),
    "teresina": Capital(0, 0, 1469),
    "rio_de_janeiro": Capital(0, 0, 946),
    "natal": Capital(0, 0, 1951),
    "porto_alegre": Capital(0, 0, 1499),
    "porto_velho": Capital(0, 0, 1815),
    "boa_vista": Capital(0, 0, 2504),
    "florianopolis": Capital(0, 0, 1217),
    "sao_paulo": Capital(0, 0, 813)
}

joao_pessoa = {
    "joao_pessoa": Capital(0, 0, 0),
    "recife": Capital(120, 20.25, 105),  # 1
    "natal": Capital(185, 5.00, 152),  # 2
    "fortaleza": Capital(688, 50.00, 556),  # 3
    "vizinhos": ["recife", "natal", "fortaleza"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 487),
    "salvador": Capital(0, 0, 764), 
    "maceio": Capital(0, 0, 300),  
    "rio_branco": Capital(0, 0, 3636),
    # "macapa": Capital(0, 0, 1966),
    "manaus": Capital(0, 0, 2821),
    "brasilia": Capital(0, 0, 1718),
    "vitoria": Capital(0, 0, 1579),
    "goiania": Capital(0, 0, 1892),
    "sao_luis": Capital(0, 0, 1164),
    "cuiaba": Capital(0, 0, 2498),
    "campo_grande": Capital(0, 0, 2596),
    "belo_horizonte": Capital(0, 0, 1730),
    "belem": Capital(0, 0, 1638),
    "curitiba": Capital(0, 0, 2549),
    "teresina": Capital(0, 0, 907),
    "rio_de_janeiro": Capital(0, 0, 1977),
    "porto_alegre": Capital(0, 0, 3069),
    "porto_velho": Capital(0, 0, 3203),
    "boa_vista": Capital(0, 0, 3070),
    "florianopolis": Capital(0, 0, 2696),
    "sao_paulo": Capital(0, 0, 2221),
    "palmas": Capital(0, 0, 1520)
}

macapa = {
    "macapa": Capital(0, 0, 0),
    # "belem": Capital(0, 0)
    # "vizinhos": ["belem"]
}

maceio = {
    "maceio": Capital(0, 0, 0),
    "aracaju": Capital(294, 8.25, 202),  # 1
    "recife": Capital(285, 18.05, 203),  # 2
    "salvador": Capital(632, 40.25, 476),  # 3
    "vizinhos": ["aracaju", "recife", "salvador"],

    # Não vizinhos, mas com distância em linha reta
    "rio_branco": Capital(0, 0, 3513),
    # "macapa": Capital(0, 0, 2011),
    "manaus": Capital(0, 0, 2779),
    "fortaleza": Capital(0, 0, 731),
    "brasilia": Capital(0, 0, 1487),
    "vitoria": Capital(0, 0, 1280),
    "goiania": Capital(0, 0, 1658),
    "sao_luis": Capital(0, 0, 1236),
    "cuiaba": Capital(0, 0, 2304),
    "campo_grande": Capital(0, 0, 2355),
    "belo_horizonte": Capital(0, 0, 1443),
    "belem": Capital(0, 0, 1682),
    "joao_pessoa": Capital(0, 0, 300),
    "curitiba": Capital(0, 0, 2263),
    "teresina": Capital(0, 0, 931),
    "rio_de_janeiro": Capital(0, 0, 1680),
    "natal": Capital(0, 0, 435),
    "porto_alegre": Capital(0, 0, 2778),
    "porto_velho": Capital(0, 0, 3093),
    "boa_vista": Capital(0, 0, 3092),
    "florianopolis": Capital(0, 0, 2404),
    "sao_paulo": Capital(0, 0, 1933),
    "palmas": Capital(0, 0, 1381)
}

manaus = {
    "manaus": Capital(0, 0, 0),
    "porto_velho": Capital(901, 66.10, 760),  # 1
    "cuiaba": Capital(2357, 135.25, 1455),  # 2
    "belem": Capital(5298, 485.75, 1294),  # 3
    "boa_vista": Capital(785, 75.75, 663),  # 4
    "rio_branco": Capital(1445, 100.00, 1149),  # 5
    "vizinhos": ["porto_velho", "cuiaba", "boa_vista", "rio_branco"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2676),
    "salvador": Capital(0, 0, 2607), 
    "maceio": Capital(0, 0, 2780),  
    # "macapa": Capital(0, 0, 1056),
    "fortaleza": Capital(0, 0, 2386),
    "brasilia": Capital(0, 0, 1932),
    "vitoria": Capital(0, 0, 2868),
    "goiania": Capital(0, 0, 1912),
    "sao_luis": Capital(0, 0, 1747),
    "campo_grande": Capital(0, 0, 2012),
    "belo_horizonte": Capital(0, 0, 2561),
    "belem": Capital(0, 0, 1294),
    "joao_pessoa": Capital(0, 0, 2822),
    "curitiba": Capital(0, 0, 2735),
    "recife": Capital(0, 0, 2837),
    "teresina": Capital(0, 0, 1923),
    "rio_de_janeiro": Capital(0, 0, 2858),
    "natal": Capital(0, 0, 2766),
    "porto_alegre": Capital(0, 0, 3135),
    "florianopolis": Capital(0, 0, 2982),
    "sao_paulo": Capital(0, 0, 2691),
    "palmas": Capital(0, 0, 1510)
}

natal = {
    "natal": Capital(0, 0, 0),
    "joao_pessoa": Capital(185, 5.00, 152),  # 1
    "fortaleza": Capital(537, 66.10, 436),  # 2
    "vizinhos": ["joao_pessoa", "fortaleza"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 605),
    "salvador": Capital(0, 0, 876), 
    "maceio": Capital(0, 0, 435),  
    "rio_branco": Capital(0, 0, 3619),
    # "macapa": Capital(0, 0, 1876),
    "manaus": Capital(0, 0, 2766),
    "brasilia": Capital(0, 0, 1777),
    "vitoria": Capital(0, 0, 1704),
    "goiania": Capital(0, 0, 1951),
    "sao_luis": Capital(0, 0, 1072),
    "cuiaba": Capital(0, 0, 2526),
    "campo_grande": Capital(0, 0, 2656),
    "belo_horizonte": Capital(0, 0, 1833),
    "belem": Capital(0, 0, 1552),
    "curitiba": Capital(0, 0, 2647),
    "recife": Capital(0, 0, 255),
    "teresina": Capital(0, 0, 844),
    "rio_de_janeiro": Capital(0, 0, 2094),
    "porto_alegre": Capital(0, 0, 3175),
    "porto_velho": Capital(0, 0, 3181),
    "boa_vista": Capital(0, 0, 2986),
    "florianopolis": Capital(0, 0, 2805),
    "sao_paulo": Capital(0, 0, 2325),
    "palmas": Capital(0, 0, 1525)
}

palmas = {
    "palmas": Capital(0, 0, 0),
    "goiania": Capital(874, 32.10, 731),  # 1
    "salvador": Capital(1454, 106.25, 1115),  # 2
    "teresina": Capital(1401, 102.25, 831),  # 3
    "sao_luis": Capital(1386, 90.50, 959),  # 4
    "belem": Capital(1283, 55.50, 970),  # 5
    "cuiaba": Capital(1784, 123.25, 1036),  # 6
    "vizinhos": ["goiania", "salvador", "teresina", "sao_luis", "belem", "cuiaba"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1234),
    "maceio": Capital(0, 0, 1381),  
    "rio_branco": Capital(0, 0, 2133),
    # "macapa": Capital(0, 0, 1175),
    "manaus": Capital(0, 0, 1510),
    "fortaleza": Capital(0, 0, 1297),
    "brasilia": Capital(0, 0, 626),
    "vitoria": Capital(0, 0, 1417),
    "campo_grande": Capital(0, 0, 1328),
    "belo_horizonte": Capital(0, 0, 1186),
    "joao_pessoa": Capital(0, 0, 1519),
    "curitiba": Capital(0, 0, 1702),
    "recife": Capital(0, 0, 1497),
    "rio_de_janeiro": Capital(0, 0, 1526),
    "natal": Capital(0, 0, 1524),
    "porto_alegre": Capital(0, 0, 2230),
    "porto_velho": Capital(0, 0, 1715),
    "boa_vista": Capital(0, 0, 1989),
    "florianopolis": Capital(0, 0, 1939),
    "sao_paulo": Capital(0, 0, 1500)
}

porto_alegre = {
    "porto_alegre": Capital(0, 0, 0),
    "florianopolis": Capital(476, 112.25, 377),  # 1
    "vizinhos": ["florianopolis"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2582),
    "salvador": Capital(0, 0, 2306), 
    "maceio": Capital(0, 0, 2778),  
    "rio_branco": Capital(0, 0, 2817),
    # "macapa": Capital(0, 0, 3344),
    "manaus": Capital(0, 0, 3133),
    "fortaleza": Capital(0, 0, 3216),
    "brasilia": Capital(0, 0, 1621),
    "vitoria": Capital(0, 0, 1542),
    "goiania": Capital(0, 0, 1499),
    "sao_luis": Capital(0, 0, 3145),
    "cuiaba": Capital(0, 0, 1681),
    "campo_grande": Capital(0, 0, 1121),
    "belo_horizonte": Capital(0, 0, 1341),
    "belem": Capital(0, 0, 3191),
    "joao_pessoa": Capital(0, 0, 3069),
    "curitiba": Capital(0, 0, 546),
    "recife": Capital(0, 0, 2980),
    "teresina": Capital(0, 0, 2912),
    "rio_de_janeiro": Capital(0, 0, 1120),
    "natal": Capital(0, 0, 3175),
    "porto_velho": Capital(0, 0, 2709),
    "boa_vista": Capital(0, 0, 3789),
    "sao_paulo": Capital(0, 0, 851),
    "palmas": Capital(0, 0, 2230)
}

porto_velho = {
    "porto_velho": Capital(0, 0, 0),
    "cuiaba": Capital(1456, 68.75, 1139),  # 1
    "manaus": Capital(901, 66.10, 760),  # 2
    "rio_branco": Capital(544, 30.50, 450),  # 3
    "vizinhos": ["cuiaba", "manaus", "rio_branco"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 2948),
    "salvador": Capital(0, 0, 2812), 
    "maceio": Capital(0, 0, 3093),  
    # "macapa": Capital(0, 0, 1726),
    "fortaleza": Capital(0, 0, 2858),
    "brasilia": Capital(0, 0, 1902),
    "vitoria": Capital(0, 0, 2841),
    "goiania": Capital(0, 0, 1815),
    "sao_luis": Capital(0, 0, 2276),
    "campo_grande": Capital(0, 0, 1636),
    "belo_horizonte": Capital(0, 0, 2481),
    "belem": Capital(0, 0, 1889),
    "joao_pessoa": Capital(0, 0, 3203),
    "curitiba": Capital(0, 0, 2415),
    "recife": Capital(0, 0, 3194),
    "teresina": Capital(0, 0, 2365),
    "rio_de_janeiro": Capital(0, 0, 2715),
    "natal": Capital(0, 0, 3181),
    "porto_alegre": Capital(0, 0, 2708),
    "boa_vista": Capital(0, 0, 1337),
    "florianopolis": Capital(0, 0, 2643),
    "sao_paulo": Capital(0, 0, 2465),
    "palmas": Capital(0, 0, 1715)
}

recife = {
    "recife": Capital(0, 0, 0),
    "maceio": Capital(285, 18.05, 203),  # 1
    "joao_pessoa": Capital(120, 20.25, 105),  # 2
    "fortaleza": Capital(800, 80.00, 630),  # 3
    "teresina": Capital(1137, 105.05, 935),  # 4
    "salvador": Capital(839, 45.25, 675),  # 5
    "vizinhos": ["maceio", "joao_pessoa", "fortaleza", "teresina", "salvador"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 399),
    "rio_branco": Capital(0, 0, 3621),
    # "macapa": Capital(0, 0, 2007),
    "manaus": Capital(0, 0, 2835),
    "brasilia": Capital(0, 0, 1658),
    "vitoria": Capital(0, 0, 1481),
    "goiania": Capital(0, 0, 1831),
    "sao_luis": Capital(0, 0, 1211),
    "cuiaba": Capital(0, 0, 2455),
    "campo_grande": Capital(0, 0, 2533),
    "belo_horizonte": Capital(0, 0, 1643),
    "belem": Capital(0, 0, 1678),
    "curitiba": Capital(0, 0, 2463),
    "rio_de_janeiro": Capital(0, 0, 1882),
    "natal": Capital(0, 0, 254),
    "porto_alegre": Capital(0, 0, 2979),
    "porto_velho": Capital(0, 0, 3193),
    "boa_vista": Capital(0, 0, 3106),
    "florianopolis": Capital(0, 0, 2606),
    "sao_paulo": Capital(0, 0, 2133),
    "palmas": Capital(0, 0, 1496)
}

rio_branco = {
    "rio_branco": Capital(0, 0, 0),
    "porto_velho": Capital(544, 30.50, 450),  # 1
    "manaus": Capital(1445, 100.00, 1149),  # 2
    "vizinhos": ["porto_velho", "manaus"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 3361),
    "salvador": Capital(0, 0, 3209), 
    "maceio": Capital(0, 0, 3513),  
    # "macapa": Capital(0, 0, 2161),
    "fortaleza": Capital(0, 0, 3303),
    "brasilia": Capital(0, 0, 2248),
    "vitoria": Capital(0, 0, 3162),
    "goiania": Capital(0, 0, 2140),
    "sao_luis": Capital(0, 0, 2725),
    "cuiaba": Capital(0, 0, 1416),
    "campo_grande": Capital(0, 0, 1829),
    "belo_horizonte": Capital(0, 0, 2790),
    "belem": Capital(0, 0, 3235),
    "joao_pessoa": Capital(0, 0, 3636),
    "curitiba": Capital(0, 0, 2603),
    "recife": Capital(0, 0, 3622),
    "teresina": Capital(0, 0, 2809),
    "rio_de_janeiro": Capital(0, 0, 2989),
    "natal": Capital(0, 0, 3619),
    "porto_alegre": Capital(0, 0, 2817),
    "boa_vista": Capital(0, 0, 1628),
    "florianopolis": Capital(0, 0, 2812),
    "sao_paulo": Capital(0, 0, 2706),
    "palmas": Capital(0, 0, 2133)
}

rio_de_janeiro = {
    "rio_de_janeiro": Capital(0, 0, 0),
    "sao_paulo": Capital(429, 15.05, 360),  # 1
    "vitoria": Capital(521, 20.0, 418),  # 2
    "belo_horizonte": Capital(434, 196.05, 338),  # 3
    "vizinhos": ["sao_paulo", "vitoria", "belo_horizonte"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 0),
    "salvador": Capital(0, 0, 277), 
    "maceio": Capital(0, 0, 202),  
    "rio_branco": Capital(0, 0, 3361),
    # "macapa": Capital(0, 0, 1968),
    "manaus": Capital(0, 0, 1485),
    "fortaleza": Capital(0, 0, 2192),
    "brasilia": Capital(0, 0, 935),
    "goiania": Capital(0, 0, 938),
    "sao_luis": Capital(0, 0, 2269),
    "cuiaba": Capital(0, 0, 1577),
    "campo_grande": Capital(0, 0, 1213),
    "belem": Capital(0, 0, 2453),
    "joao_pessoa": Capital(0, 0, 1970),
    "curitiba": Capital(0, 0, 677),
    "recife": Capital(0, 0, 1876),
    "teresina": Capital(0, 0, 1982),
    "natal": Capital(0, 0, 2087),
    "porto_alegre": Capital(0, 0, 1125),
    "porto_velho": Capital(0, 0, 2709),
    "boa_vista": Capital(0, 0, 3431),
    "florianopolis": Capital(0, 0, 749),
    "palmas": Capital(0, 0, 1518)
}

salvador = {
    "salvador": Capital(0, 0, 0),
    "belo_horizonte": Capital(1372, 65.10, 968),  # 1
    "vitoria": Capital(1202, 55.50, 837),  # 2
    "aracaju": Capital(356, 10.10, 277),  # 3
    "maceio": Capital(632, 40.25, 476),  # 4
    "recife": Capital(839, 45.25, 676),  # 5
    "teresina": Capital(1163, 100.00, 996),  # 6
    "palmas": Capital(1454, 106.25, 1115),  # 7
    "goiania": Capital(1643, 101.10, 1227),  # 8
    "vizinhos": ["belo_horizonte", "vitoria", "aracaju", "maceio", "recife", "teresina", "palmas", "goiania"],

    # Não vizinhos, mas com distância em linha reta
    "rio_branco": Capital(0, 0, 3209),
    # "macapa": Capital(0, 0, 2003),
    "manaus": Capital(0, 0, 2607),
    "fortaleza": Capital(0, 0, 1029),
    "brasilia": Capital(0, 0, 1062),
    "sao_luis": Capital(0, 0, 1325),
    "cuiaba": Capital(0, 0, 1918),
    "campo_grande": Capital(0, 0, 1908),
    "belem": Capital(0, 0, 1689),
    "joao_pessoa": Capital(0, 0, 764),
    "curitiba": Capital(0, 0, 1788),
    "rio_de_janeiro": Capital(0, 0, 1218),
    "natal": Capital(0, 0, 876),
    "porto_alegre": Capital(0, 0, 2306),
    "porto_velho": Capital(0, 0, 2812),
    "boa_vista": Capital(0, 0, 3012),
    "florianopolis": Capital(0, 0, 1933),
    "sao_paulo": Capital(0, 0, 1458)
}

sao_luis = {
    "sao_luis": Capital(0, 0, 0),
    "palmas": Capital(1386, 90.50, 959),  # 1
    "teresina": Capital(446, 12.05, 330),  # 2
    "belem": Capital(806, 25.10, 482),  # 3
    "vizinhos": ["palmas", "teresina", "belem"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1227),
    "salvador": Capital(0, 0, 1325), 
    "maceio": Capital(0, 0, 1236),  
    "rio_branco": Capital(0, 0, 2725),
    # "macapa": Capital(0, 0, 804),
    "manaus": Capital(0, 0, 1747),
    "fortaleza": Capital(0, 0, 654),
    "brasilia": Capital(0, 0, 1526),
    "vitoria": Capital(0, 0, 2023),
    "goiania": Capital(0, 0, 1664),
    "cuiaba": Capital(0, 0, 1944),
    "campo_grande": Capital(0, 0, 2286),
    "belo_horizonte": Capital(0, 0, 1937),
    "joao_pessoa": Capital(0, 0, 1164),
    "curitiba": Capital(0, 0, 2603),
    "recife": Capital(0, 0, 1212),
    "rio_de_janeiro": Capital(0, 0, 2277),
    "natal": Capital(0, 0, 1072),
    "porto_alegre": Capital(0, 0, 3145),
    "porto_velho": Capital(0, 0, 2276),
    "boa_vista": Capital(0, 0, 1914),
    "florianopolis": Capital(0, 0, 2824),
    "sao_paulo": Capital(0, 0, 2353)
}

sao_paulo = {
    "sao_paulo": Capital(0, 0, 0),
    "curitiba": Capital(408, 99.75, 338),  # 1
    "rio_de_janeiro": Capital(429, 15.05, 360),  # 2
    "belo_horizonte": Capital(586, 201.50, 491),  # 3
    "campo_grande": Capital(1014, 62.10, 894),  # 4
    "vizinhos": ["curitiba", "rio_de_janeiro", "belo_horizonte", "campo_grande"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1735),
    "salvador": Capital(0, 0, 1458), 
    "maceio": Capital(0, 0, 1933),  
    "rio_branco": Capital(0, 0, 2706),
    # "macapa": Capital(0, 0, 2667),
    "manaus": Capital(0, 0, 2689),
    "fortaleza": Capital(0, 0, 2373),
    "brasilia": Capital(0, 0, 876),
    "vitoria": Capital(0, 0, 750),
    "goiania": Capital(0, 0, 813),
    "sao_luis": Capital(0, 0, 2353),
    "cuiaba": Capital(0, 0, 1327),
    "belem": Capital(0, 0, 2467),
    "joao_pessoa": Capital(0, 0, 2221),
    "recife": Capital(0, 0, 2134),
    "teresina": Capital(0, 0, 2096),
    "natal": Capital(0, 0, 2325),
    "porto_alegre": Capital(0, 0, 851),
    "porto_velho": Capital(0, 0, 2465),
    "boa_vista": Capital(0, 0, 3304),
    "florianopolis": Capital(0, 0, 488),
    "palmas": Capital(0, 0, 1500)
}

teresina = {
    "teresina": Capital(0, 0, 0),
    "salvador": Capital(1163, 100.00, 996),  # 1
    "recife": Capital(1137, 105.05, 936),  # 2
    "fortaleza": Capital(634, 25.05, 497),  # 3
    "sao_luis": Capital(446, 12.05, 330),  # 4
    "palmas": Capital(1401, 102.25, 831),  # 5
    "vizinhos": ["salvador", "recife", "fortaleza", "sao_luis", "palmas"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 904),
    "maceio": Capital(0, 0, 931),  
    "rio_branco": Capital(0, 0, 2809),
    # "macapa": Capital(0, 0, 1081),
    "manaus": Capital(0, 0, 1923),
    "brasilia": Capital(0, 0, 1314),
    "vitoria": Capital(0, 0, 1713),
    "goiania": Capital(0, 0, 1469),
    "cuiaba": Capital(0, 0, 1864),
    "campo_grande": Capital(0, 0, 2134),
    "belo_horizonte": Capital(0, 0, 1657),
    "belem": Capital(0, 0, 751),
    "joao_pessoa": Capital(0, 0, 907),
    "curitiba": Capital(0, 0, 2366),
    "rio_de_janeiro": Capital(0, 0, 1990),
    "natal": Capital(0, 0, 844),
    "porto_alegre": Capital(0, 0, 2912),
    "porto_velho": Capital(0, 0, 2365),
    "boa_vista": Capital(0, 0, 2172),
    "florianopolis": Capital(0, 0, 2576),
    "sao_paulo": Capital(0, 0, 2096)
}

vitoria = {
    "vitoria": Capital(0, 0, 0),
    "rio_de_janeiro": Capital(521, 20.0, 423),  # 1
    "belo_horizonte": Capital(524, 175.50, 382),  # 2
    "salvador": Capital(1202, 55.50, 839),  # 3
    "vizinhos": ["rio_de_janeiro", "belo_horizonte", "salvador"],

    # Não vizinhos, mas com distância em linha reta
    "aracaju": Capital(0, 0, 1102),
    "maceio": Capital(0, 0, 1282),  
    "rio_branco": Capital(0, 0, 3162),
    # "macapa": Capital(0, 0, 2548),
    "manaus": Capital(0, 0, 2868),
    "fortaleza": Capital(0, 0, 1856),
    "brasilia": Capital(0, 0, 951),
    "goiania": Capital(0, 0, 1027),
    "sao_luis": Capital(0, 0, 2025),
    "cuiaba": Capital(0, 0, 1750),
    "campo_grande": Capital(0, 0, 1495),
    "belem": Capital(0, 0, 2279),
    "joao_pessoa": Capital(0, 0, 1581),
    "curitiba": Capital(0, 0, 1082),
    "recife": Capital(0, 0, 1484),
    "teresina": Capital(0, 0, 1715),
    "natal": Capital(0, 0, 1706),
    "porto_alegre": Capital(0, 0, 1540),
    "porto_velho": Capital(0, 0, 2841),
    "boa_vista": Capital(0, 0, 3400),
    "florianopolis": Capital(0, 0, 1165),
    "sao_paulo": Capital(0, 0, 1419),
    "palmas": Capital(0, 0, 1234)
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
    print("\n1- Busca em Largura")
    print("2- Busca em Profundidade")
    print("3- Busca A* (heurística)")
    busca = input("Selecione um método de busca: ")
    visitados = [raiz]  # Essa lista será preenchida conforme as capitais expandidas
    # No caso a origem já deve estar na lista, teoricamente ela já foi visitada
    if raiz == no_destino:  # Da maneira que foi implentado a busca, não dá para achar se a origem é o destino
        print("\n\nDestino alcançado!!!\n\n")  # Esse IF é a solução para contornar esse problema
    else:
        print("Iniciando a Busca em Largura!\n")
        match int(busca):
            case 1:
                custo = busca_em_largura(raiz, rotas, no_destino, vizinhos, visitados)
            case 2:
                custo = busca_em_profundidade(raiz, rotas, no_destino, vizinhos, visitados)
            case 3:
                print("Em construção...")
            case _:
                print("Se é loko não compensa...")

else:
    print("\nHouve um problema na leitura da origem/destino")

print("\nCusto da viagem: ", custo)
#FAZER CONTAGEM DE VISITAS