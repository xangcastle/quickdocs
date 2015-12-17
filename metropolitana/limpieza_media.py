# -*- coding: utf-8 -*-
import os


def buscar_carpetas():
    global carpeta_elegida
    carpeta_elegida = raw_input("nIngrese la direccion del directorio al cual usted desea hacerle el analisis (fancy as fuck):n")
    comprobar_existencia(carpeta_elegida)

    global paths
    paths = []
    global dirs
    dirs = []

    for dirpath, dirname, filename in os.walk(carpeta_elegida):
        paths.append(dirpath)
        dirs.append(dirname)
    raw_input("nA continuacion, se borraran las carpetas vacias.nPresione ENTER para continuar")
    borrar_carpetas()


def borrar_carpetas():
    counter = 0
    paths.reverse()
    print "nEliminando las carpetas vacias del directorio elegido.nPor favor, aguarde un momento.n"
    for path in paths:
        try:
            os.rmdir("%s" % (path))
            counter += 1
        except:
            None

    print "Carpetas vacias eliminadas"
    print "Se han eliminado %d carpetas sobre un total de %dn" % (counter, len(dirs) - 1)
    raw_input("Presione ENTER para terminar")
    exit()
    bool = False


def comprobar_existencia(carpeta_elegida):
    if os.path.isdir(carpeta_elegida) != True:
        print "nNo se puede encontrar la direccion o ruta especificada."
        print "Por favor intentelo de nuevo."
        buscar_carpetas()
    else:
        print "Generando base de datos. Por favor espere."


buscar_carpetas()