def agregar_articulo(articulo):
    archivo_lista = open("lista.txt","a")
    archivo_lista.write("{}\n".format(articulo))
    archivo_lista.close()




agregar_articulo(input("Articulo que quieres agregar: "))
