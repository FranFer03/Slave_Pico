import numpy as np

def main(entrada,ventana):
    salida = np.zeros(len(entrada))
    for i in range(len(entrada)):
        inicio = max(0, i - ventana + 1)
        fin = i + 1
        salida[i] = np.mean(entrada[inicio:fin])
    return salida

if __name__ == '__main__':
    pass