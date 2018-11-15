def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    while (w != v):
        for ligacoes in arestas:
            if (ligacoes[0] == w):
                if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + arestas[ligacoes]:
                    beta[ligacoes[2]] = beta[w] + arestas[ligacoes]
                    pi[ligacoes[2]] = w


        minimoBeta = float('inf')
        for vertice in vertices:
            if phi[vertice] == 0 and beta[vertice] < float('inf'):
                if beta[vertice] < minimoBeta:
                    minimoBeta = beta[vertice]


        for vertice in vertices:
            if beta[vertice] == minimoBeta:
                phi[vertice] = 1
                w = vertice
    atual = v
    lista = ""
    while atual != u:
        for aaa in pi:
            if aaa == atual:
                lista += atual
                lista += " > "
                atual = pi[atual]

    lista += atual

    return lista[::-1]