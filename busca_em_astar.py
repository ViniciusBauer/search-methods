mapaeiaCusto = dict()

def busca_em_astar(raiz, rotas, no_destino, vizinhos, visitados, contador):
    if raiz in rotas:
        print("\nBuscando vizinhos em", raiz.upper())  
        contador += 1   # Cada vez que visita um nó adiciona no contador
        dict_vizinhos = {}  # Dict para armazenar os vizinhos de cada nó e pegar o mínimo custo a cada iteração

        for rota in rotas[raiz]["vizinhos"]:    # Faz a varredura das capitais vizinhas
            if rota in visitados:  # Encontra capitais já visitada
                print("Vizinho", rota.upper(),"já foi encontrado.")
                continue  # Se a capital já foi visitada não itera, senão pode dar loop infinito
            
            # Calcula os custo de distância (nó -> vizinho "n"), pedágio e distância em linha reta (nó -> destino)
            # Preenche o vizinho com seu respectivo custo {'vizinho_n': custo_n, ...}
            dict_vizinhos[rota] = rotas[raiz][rota].distancia + rotas[raiz][rota].pedagio + rotas[rota][no_destino].distancia_lr**2
            # A distância em linha reta é o que tem mais importância, por isso ela é elevada ao quadrado
            # Dá para dizer que a distância rodoviária é a mais importante, daí é só trocar a base

            # Segundo meus testes se deixar fora do FOR ele vai voltar para capital já descoberta, podendo andar em círculos,
            # Por isso é melhor deixar assim, existe uma chance de ele se perder e cair em uma rota sem nenhum caminho disponível
            # Mas desse jeito ainda fica mais correto, se deixar fora, outra lógica adicional precisaria ser implementada,
            # usando pilha ou fila talvez, mas ficaria bem complexo e mesmo assim não sei se resolveria o problema
            visitados.append(rota)

            # Precisa mapear o custo mesmo que não sejo o melhor caminho
            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + rotas[raiz][rota].distancia
                print("Caminho até", rota.upper(), "encontrado! Distância entre as duas capitais:", rotas[raiz][rota].distancia)
            else:
                mapaeiaCusto[rota] = rotas[raiz][rota].distancia
                print("Caminho até", rota.upper(), "encontrado! Distância entre as duas capitais:", rotas[raiz][rota].distancia)

            if rota == no_destino:   # Se o nó chegou ao seu destino
                print("\n\nDestino alcançado!!!")
                print("Capitais visitadas:",contador,"\n\n")
                return mapaeiaCusto[rota]   # Soma dos custos ao longo da trajetória

        melhor_custo = ""#só para não dar alert na recursividade

        if dict_vizinhos:   # Se o dict existir: calcula o custo mínimo
            # Usa o .get para dizer que são os valores a serem ordenados? Estranho...
            melhor_custo = min(dict_vizinhos, key=dict_vizinhos.get)   # Melhor custo é o menor valor entre os caminhos

            # Usando items() ficaria mais claro, porém o código fica mais poluído
            # melhor_custo = min(dict_vizinhos.items(), key=lambda item:item[1])
            # o item pega os pares, como se fosse uma lista, e o lambda faz a comparação pelo especificado.
            # Se especificar item[1] significa os valores, se trocar para item[0] significa as chaves.
            # Pelo menos assim seria usando a lógica do Kotlin/Java, mas o importante é que o que foi feito funciona

            #Mudei um pouco o print, ficou mais claro agora
            print("\tMelhor caminho encontrado", melhor_custo.upper(), "! Distância já percorida:", mapaeiaCusto[melhor_custo])

        print("Pressione enter para continuar...")
        input()
        return busca_em_astar(melhor_custo, rotas, no_destino, vizinhos, visitados, contador)    # Recursão até encontrar o destino
    else:
        print("Erro ao traçar rota!")
        return None