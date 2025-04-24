capitais = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador",
    "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís",
    "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa",
    "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal",
    "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo",
    "Aracaju", "Palmas"
]

class Capital:
    def __init__(self, distancia, pedagio, distancia_lr):
        self.distancia = distancia # Distância rodoviária
        self.pedagio = pedagio # Valor em R$ do pedágio
        self.distancia_lr = distancia_lr #Distância aérea (linha reta)
        self.vizinhos = None