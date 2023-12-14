# Definimos una función que verifica si una lista dada es un árbol binario
def es_arbol(lista):
    # Verificamos si la lista es de hecho una lista y si tiene exactamente tres elementos
    if isinstance(lista, list) and len(lista) == 3:
        # Iteramos sobre los elementos en los índices 1 y 2 de la lista (los subárboles)
        for elemento in lista[1:]:
            # Si el elemento no es None y no es un árbol válido, retornamos False
            if elemento is not None and not es_arbol(elemento):
                return False
        # Si todos los subárboles son válidos, retornamos True
        return True
    # Si la lista no es una lista o no tiene tres elementos, retornamos False
    return False
if __name__ == "__main__":

# Creamos algunos ejemplos de listas para probar la función
    lista = [1, [2, None, None], [3, None, None]]  # Esta es un árbol binario válido
    lista2 = [1, [2, None, None], [3, None, None], 4]  # Esta no es un árbol binario válido
    lista3 = [None,None,None]  # Esta es un árbol binario válido con todos los nodos None
    lista4 = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], [7, None, None]]] # Esta es un árbol binario válido con varios niveles
    lista5 = [None,None] # Esta no es un árbol binario válido
# Imprimimos los resultados de la función para nuestras listas de prueba
    print(es_arbol(lista))  # Debería imprimir True
    print(es_arbol(lista2))  # Debería imprimir False
    print(es_arbol(lista3))  # Debería imprimir True
    print(es_arbol(lista4))  # Debería imprimir True
    print(es_arbol(lista5))  # Debería imprimir False