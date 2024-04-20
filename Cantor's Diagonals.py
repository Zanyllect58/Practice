def cantor(nested_list):
    diagonal_invertida = []  
    for i in range(len(nested_list)):
        elemento = nested_list[i][i]
        if elemento == 1:
            diagonal_invertida.append(0)
        else:
            diagonal_invertida.append(1)
    return diagonal_invertida
pass