def reina (solucion, posi, nreinas)
    if posi >= nreinas:
        return False

    tdb = False

#for/while true
    if solucion[posi] < nreinas:
        solucion[posi] = solucion[posi]+1


