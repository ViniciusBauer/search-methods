mapaeiaCusto = dict()


def busca_em_largura(raiz, rotas, no_destino, vizinhos, visitados):
    if raiz in rotas:  # Essa validação ficou desnecessário, mas enfim... Melhor pecar por excesso
        print("\nBuscando vizinhos em", raiz.upper())  # Deixei Uppercase para ficar bem visível
        for rota in rotas[raiz]["vizinhos"]:
            if rota in visitados:  # Encontra capitais já visitada
                print("Vizinho", rota.upper(),"já foi encontrado.")
                continue  # Se a capital já foi visitada não itera, senão pode dar loop infinito

            # Logo após a verificação de capitais visitadas, adiciona a capital não visitada a lista
            visitados.append(rota)

            if raiz in mapaeiaCusto:
                mapaeiaCusto[rota] = mapaeiaCusto[raiz] + rotas[raiz][rota].distancia
            else:
                mapaeiaCusto[rota] = rotas[raiz][rota].distancia

            vizinhos.append(rota)  # FILA de vizinhos (FIFO = First In, First Out)
            print("Caminho até", rota.upper(), "encontrado! Distância:", mapaeiaCusto[rota])
            if rota == no_destino:
                print("\n\nDestino alcançado!!!\n\n")
                return mapaeiaCusto[rota]
        print("Pressione enter para continuar...")
        input()

        return busca_em_largura(vizinhos.popleft(), rotas, no_destino, vizinhos, visitados)
    else:
        print("Erro ao traçar rota!")
