
NUM = int(input("CUANTAS TABLAS: "))

T = 1
while T <= NUM:
    I = 10
    while I >= 1:
        RESUL = T * I
        print(f"{T}*{I}={RESUL}")
        I = I - 1
    input("Pulse una Tecla:")
    T = T + 1
