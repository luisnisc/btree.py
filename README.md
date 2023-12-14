# Verificador de Árbol Binario

Este proyecto contiene una función `es_arbol` que verifica si una lista dada representa un árbol binario válido.

## Código

El código principal se encuentra en el archivo `btree.py`. La función `es_arbol` toma una lista como argumento y verifica si representa un árbol binario válido.

Un árbol binario se representa como una lista de tres elementos: [valor, subárbol_izquierdo, subárbol_derecho]. Por lo tanto, la función verifica si la lista tiene exactamente tres elementos. Luego, para cada subárbol (los elementos en los índices 1 y 2 de la lista), si el subárbol no es `None`, la función verifica si es un árbol binario válido llamándose a sí misma recursivamente.

Si todos los subárboles son válidos, la función retorna `True`. Si cualquier subárbol no es válido, la función retorna `False`. Si la lista no es una lista o no tiene tres elementos, la función también retorna `False`.

## Ejemplos

El archivo `btree.py` también contiene algunos ejemplos de listas que representan árboles binarios válidos e inválidos. Puedes ejecutar este archivo para ver los resultados de la función `es_arbol` para estas listas de prueba.

## Uso

Para verificar si una lista representa un árbol binario válido, simplemente llama a la función `es_arbol` con la lista como argumento. Por ejemplo:

```python
resultado = es_arbol([1, [2, None, None], [3, None, None]])
print(resultado)  # Imprime: True
