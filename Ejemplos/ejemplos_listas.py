Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Operaciones con listas
>>> lista =["hello",7,"Josselyn",[1,2,3,4,5,6,7]]
>>> 

>>> 
>>> print(lista)
['hello', 7, 'Josselyn', [1, 2, 3, 4, 5, 6, 7]]
>>> print(lista[0])
hello
>>> print(lista[0,3])

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(lista[0,3])
TypeError: list indices must be integers, not tuple
>>> print(lista[3])
[1, 2, 3, 4, 5, 6, 7]
>>> nombres=["Josselyn","Carolina","Sindi","Nahomi"]
>>> print(nombres[-1])
Nahomi
>>> print(nombres[1])
Carolina
>>> #particionado
>>> print(nombres[1:4])
['Carolina', 'Sindi', 'Nahomi']
>>> #añadir objeto al final de la lista
>>> numeros=[1,2,3]
>>> numeros.append(4)
>>> print(numeros)
[1, 2, 3, 4]
>>> #count que devuelve el numero de veces que se encontro valor
>>> numeros.append(4)
>>> numeros.count(4)
2
>>> #extend
>>> numeros.extend([7,8,9,10,11,12])
>>> print(numeros)
[1, 2, 3, 4, 4, 7, 8, 9, 10, 11, 12]
>>> 
