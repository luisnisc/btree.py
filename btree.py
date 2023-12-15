
def es_arbol(lista):
  
    if isinstance(lista, list) and len(lista) == 3:
        
        for elemento in lista[1:]:
            
            if elemento is not None and not es_arbol(elemento):
                return False
            
        return True
    
    return False
  
if __name__ == "__main__":


    lista = [1, [2, None, None], [3, None, None]]  # Esta es un árbol binario válido
    lista2 = [1, [2, None, None], [3, None, None], 4]  # Esta no es un árbol binario válido
    lista3 = [None,None,None]  # Esta es un árbol binario válido con todos los nodos None
    lista4 = [None,None] # Esta no es un árbol binario válido
    lista5 = [1,2,3] # Esta no es un árbol binario válido


    print(es_arbol(lista))  # True
    print(es_arbol(lista2)) # False  
    print(es_arbol(lista3)) # True
    print(es_arbol(lista4)) # False  
    print(es_arbol(lista5)) # False   