# Leggere base ed altezza come input intero da testiera
base = int(input("Inserire la base: "))
altezza = int(input("Inserire l'altezza: "))

# Calcolare l'area del triangolo. Se una delle dimensioni è negativa, visualizzare un messaggio di errore
if base > 0 and altezza > 0:
    area_triangolo = (base * altezza) / 2
    print("Area del triangolo: ", area_triangolo)
else:
    print("Impossibile calcolare l'area del triangolo: almeno una delle dimensioni inserite è negativa")