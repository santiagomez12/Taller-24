import csv

mi_archivo=open("serviciosurgenciasambulanciasagosto2020.csv")

mi_lector=csv.reader(mi_archivo,delimiter=";")
#1 
empresas[1]
contador=0
for linea in mi_lector:
    if not (linea[1] in empresas):
        empresas.append (linea[1])
for empresa in empresas:
    print (empresa)

2#
print (mi_lector.linea_num)  
print (contador)
#3
for n in range (mi_lector.linea_num<5):
    contador=n+1
print (mi_lector.linea_num)  
print (contador)
#4 
mi_archivo.seek(0)

direcciones[0]
for linea in mi_lector:
    if linea[1]== "SUBRED INTEGRADA DE SERVICIOS DE SALUD NORTE E.S.E;CALLE":
        if not linea[2] in direcciones:
        direcciones.append (linea[2])
        print(linea[2])
for direccion in direcciones:
    print(direccion)

#5 servicios que contengan la palabra salud
mi_archivo.seek(0)
for intem in mi_lector:
    if "SALUD" in intem[]:
        print (intem)
    else :
        Print(" no hay servicios con la palabra salud")
        
            