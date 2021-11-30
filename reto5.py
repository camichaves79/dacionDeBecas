import csv
import numpy as np

bd = []
capital = input()

def listaCapital():
    # leer la información asiciada a la capital y poner los datos útiles en una lista
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            listaTemporal = []
            if row["ciudad"] == capital:
                listaTemporal.append(row["etnia"])
                listaTemporal.append(row["estrato"])
                listaTemporal.append(row["ingresos"])
                listaTemporal.append(row["continua"])
                bd.append(listaTemporal)
    
    return bd

baseDatos = listaCapital()

def continuan():
    conteoContinuan = 0
    for i in range(len(baseDatos)):
        if baseDatos[i][3] == '1':
            conteoContinuan += 1
    return conteoContinuan
     
print(continuan())

def listarIngresos():
    global listaIngresos
    listaIngresos = []
    for i in range(len(baseDatos)):
        if baseDatos[i][3] != "0":
            listaIngresos.append(int(baseDatos[i][2]))

listarIngresos()

def minimoIngreso(lista):
    lista.sort()
    return lista[0]

def maximoIngreso(lista):
    lista.sort()
    return lista[-1]

def promedioIngreso(lista):
    suma= 0
    for i in range(len(lista)):
        suma += lista[i] 
    promedio = suma / len(lista)
    return promedio

print(minimoIngreso(listaIngresos), maximoIngreso(listaIngresos), round(promedioIngreso(listaIngresos),2))

def conteoEtnias(lista):
    sinR = 0
    afro = 0
    indi = 0
    rai = 0
    pale = 0
    gitano = 0
    for i in range(len(lista)):
        if lista[i][3] == "1":
            if lista[i][0] == "sin reconocimiento":
                sinR += 1
            elif lista[i][0] == "afrodescendiente":
                afro += 1
            elif lista[i][0] == "indigena":
                indi +=1
            elif lista[i][0] == "raizal":
                rai += 1
            elif lista[i][0] == "palenquero":
                pale += 1
            elif lista[i][0] == "gitano":
                gitano += 1
    continuanEtno = [afro, gitano, indi, pale, rai, sinR]
    return continuanEtno

listaEtno = ["afrodescendiente","gitano","indigena","palenquero", "raizal", "sin reconocimiento"]
cantidadEtnias = conteoEtnias(baseDatos)

listaEtno.reverse()
cantidadEtnias.reverse()

def ordenamiento(lista1, lista2):
    for j in range(len(lista1) - 1, 0, -1):
        for i in range(j):
            if lista1[i]>lista1[i+1]:
                temp_lista1 = lista1[i]
                temp_lista2 = lista2[i]
                lista1[i] = lista1[i + 1]
                lista2[i] = lista2[i + 1]
                lista1[i+1] = temp_lista1
                lista2[i + 1] = temp_lista2

ordenamiento(cantidadEtnias,listaEtno)

listaEtno.reverse()
cantidadEtnias.reverse()

for i in range(len(listaEtno)):
    if cantidadEtnias[i] != 0:
        print(listaEtno[i], cantidadEtnias[i])   