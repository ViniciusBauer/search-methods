mapaeiaCusto = dict()

def busca_em_astar(raiz, rotas, no_destino, vizinhos, visitados, contador):
    if raiz in rotas:  # Essa validação ficou desnecessário, mas enfim... Melhor pecar por excesso
        print("\nBuscando vizinhos em", raiz.upper())  # Deixei Uppercase para ficar bem visível
        contador += 1 # Cada vez que visita um nó adiciona no contador
        dict_vizinhos = {} # Diciinário para armazenar os vizinhos de cada nó e pegar o mínimo custo a cada iteração

        for rota in rotas[raiz]["vizinhos"]:
            if rota in visitados:  # Encontra capitais já visitada
                print("Vizinho", rota.upper(),"já foi encontrado.")
                continue  # Se a capital já foi visitada não itera, senão pode dar loop infinito
            
            custo_no = rotas[raiz][rota].distancia + rotas[raiz][rota].pedagio + rotas[raiz][no_destino].distancia_lr # Calcula os custo de distancias mais os dois custos baseados em heuristica

            dict_vizinhos[rota] = custo_no  # Preenche o vizinho com seu respectivo custo 'vizinho_n': custo_n

        if dict_vizinhos:   # Se o dict existir: calcula o custo mínimo
            melhorCusto = min(dict_vizinhos, key=dict_vizinhos.get())   # Melhor custo baseado na soma dos custos

            print("Caminho até", melhorCusto.upper(), "encontrado! Distância:", dict_vizinhos[melhorCusto])

            # Logo após a verificação de capitais visitadas, adiciona a capital não visitada a lista
            visitados.append(melhorCusto)

            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + dict_vizinhos[melhorCusto]
            else:
                mapaeiaCusto[rota] = dict_vizinhos[melhorCusto]

            if melhorCusto == no_destino:
                print("\n\nDestino alcançado!!!")
                print("Capitais visitadas:",contador,"\n\n")
                return mapaeiaCusto[rota]
        print("Pressione enter para continuar...")
        input()
        return busca_em_astar(melhorCusto, rotas, no_destino, vizinhos, visitados, contador)
    else:
        print("Erro ao traçar rota!")
        return None
