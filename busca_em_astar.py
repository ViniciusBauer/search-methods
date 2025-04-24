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
            
            # Calcula os custo de distancia (nó -> vizinho "n"), pedágio e distância em linha reta (nó -> destino)
            custo_no = rotas[raiz][rota].distancia + rotas[raiz][rota].pedagio + rotas[rota][no_destino].distancia_lr 

            dict_vizinhos[rota] = custo_no  # Preenche o vizinho com seu respectivo custo {'vizinho_n': custo_n, ...}
            # print(dict_vizinhos)
        if dict_vizinhos:   # Se o dict existir: calcula o custo mínimo
            melhorCusto = min(dict_vizinhos, key=dict_vizinhos.get)   # Melhor custo é o menor valor entre os caminhos
            print("Caminho até", melhorCusto.upper(), "encontrado! Distância:", dict_vizinhos[melhorCusto])

            # Logo após a verificação de capitais visitadas, adiciona a capital não visitada a lista
            visitados.append(melhorCusto)

            # Acúmulo de custo ao longo do caminho traçado até o destino
            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + dict_vizinhos[melhorCusto]
            else:
                mapaeiaCusto[rota] = dict_vizinhos[melhorCusto]

            if melhorCusto == no_destino:   # Se o nó chegou ao seu destino
                print("\n\nDestino alcançado!!!")
                print("Capitais visitadas:",contador,"\n\n")
                return mapaeiaCusto[rota]   # Soma dos custos ao longo da trajetória
        print("Pressione enter para continuar...")
        input()
        return busca_em_astar(melhorCusto, rotas, no_destino, vizinhos, visitados, contador)    # Recursão até encontrar o destino
    else:
        print("Erro ao traçar rota!")
        return None
