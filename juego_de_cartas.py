import random
def generar_mazos(n):
    mazo = []
    k = 1
    while k <= n:
        j = 0
        while j < 4:
            i = 1
            while i <=13:
                mazo.append(i)
                i = i + 1
            j = j + 1
        k = k + 1
    
    random.shuffle(mazo)
    return mazo

def jugar(m):
    puntaje = 0
    while puntaje < 21:
        puntaje = puntaje + m[0]
        m.pop(0)
    return puntaje


def jugar_varios(m, j):
    puntos = []
    i = 0
    while i < j:
        puntos.append(jugar(m))
        i = i + 1
    return puntos
    


def ver_quien_gano(resultados):
    ganadores = []
    j = 0
    while j < len(resultados):
        if j == 21:
            ganadores.append(1)
        else: 
            ganadores.append(0)
        j = j + 1
    return ganadores



mazoNuevo = generar_mazos(1)
print(len(mazoNuevo))
print(mazoNuevo)
jugada = jugar(mazoNuevo)
print(jugada)
resultado = jugar_varios(mazoNuevo,2)
print(resultado)
ganador = ver_quien_gano(resultado)
print(ganador)
        