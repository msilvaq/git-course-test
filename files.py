import re

def abrirArchivo():
    archivo = open("sample.txt",encoding="utf-8")
    informacion = archivo.read()
    archivo.close()
    return informacion

#busca solo en la primer linea match

def comparar():    
    contenido = abrirArchivo()
    return re.match(r"abcdefghijklmnopqrstuvwxyz",contenido)

#busca sen todas las lineas search
#\+\d-\(\d\d\d\)-\(\d\d\d\)-\(\d\d\d\d\)
#\+\d-\(?\d{3}\)?-\(?\d{3}\)?-\(?\d{4}\)?
def buscar():    
    contenido = abrirArchivo()
    return re.search(r"\+\d-\(?\d{3}\)?-\(?\d{3}\)?-\(?\d{4}\)?",contenido)
