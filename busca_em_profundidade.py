mapaeiaCusto = dict()

def busca_em_profundidade(raiz, rotas, no_destino, vizinhos, visitados, contador):
    if raiz in rotas:
        print("\nBuscando vizinhos em", raiz.upper())  # Novamente melhor uppercase
        contador += 1 # Cada vez que visita um nó adiciona no contador
        for rota in rotas[raiz]["vizinhos"]:
            if rota in visitados:  # Encontra capitais já visitada
                print("Vizinho", rota.upper(),"já foi encontrado.")
                continue  # Isso evita loop infinito

            # Logo após a verificação de capitais visitadas, adiciona a capital não visitada a lista
            visitados.append(rota)

            # Segue a mesma lógica da Busca em Largura
            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + rotas[raiz][rota].distancia
            else:
                mapaeiaCusto[rota] = rotas[raiz][rota].distancia

            vizinhos.append(rota)  # PILHA de vizinhos (FILO = First In, Last Out)
            print("Caminho até", rota.upper(), "encontrado! Distância:", mapaeiaCusto[rota])
        if rota == no_destino:
            print("\n\nDestino alcançado!!!")
            print("Capitais visitadas:",contador,"\n\n")
            return mapaeiaCusto[rota]
        print("Pressione enter para continuar...")
        input()
        #pop() para PILHA
        return busca_em_profundidade(vizinhos.pop(), rotas, no_destino, vizinhos, visitados, contador)
    else:
        print("Erro ao traçar rota!")
        return None
