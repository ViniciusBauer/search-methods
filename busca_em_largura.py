mapaeiaCusto = dict()

def busca_em_largura(raiz, rotas, no_destino, vizinhos, visitados, contador):
    if raiz in rotas:  # Essa validação ficou desnecessário, mas enfim... Melhor pecar por excesso
        print("\nBuscando vizinhos em", raiz.upper())  # Deixei Uppercase para ficar bem visível
        contador += 1 # Cada vez que visita um nó adiciona no contador
        if raiz in mapaeiaCusto:# Só imprime se a raiz já foi mapeada, isso acontece depois da primeira iteração do FOR
            print("\tDistância total já percorrida:", mapaeiaCusto[raiz])
        for rota in rotas[raiz]["vizinhos"]:
            if rota in visitados:  # Encontra capitais já visitada
                print("Vizinho", rota.upper(),"já foi encontrado.")
                continue  # Se a capital já foi visitada não itera, senão pode dar loop infinito

            # Logo após a verificação de capitais visitadas, adiciona a capital não visitada a lista
            visitados.append(rota)

            # Map para salvar a distância entre cada rota
            # a rota atual pega a distância da rota anterior (raiz) e soma a rota nova, e assim vai...
            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + rotas[raiz][rota].distancia
            else:
                mapaeiaCusto[rota] = rotas[raiz][rota].distancia

            vizinhos.append(rota)  # FILA de vizinhos (FIFO = First In, First Out)
            print("Caminho até", rota.upper(), "encontrado! Distância entre as duas capitais:", rotas[raiz][rota].distancia)
            if rota == no_destino:
                print("\n\nDestino alcançado!!!")
                print("Capitais visitadas:",contador,"\n\n")
                return mapaeiaCusto[rota]
        print("Pressione enter para continuar...")
        input()
        #popleft() para FILA
        return busca_em_largura(vizinhos.popleft(), rotas, no_destino, vizinhos, visitados, contador)
    else:
        print("Erro ao traçar rota!")
        return None
