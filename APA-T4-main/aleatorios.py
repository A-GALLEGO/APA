# Cuarta tarea de APA 2023: Generación de números aleatorios

## AGUSTI GALLEGO BETORZ

## Generación de números aleatorios usando el algoritmo LGC

import doctest 
class Aleat:
    """Generador de números aleatorios usando el algoritmo LCG.
    
    Las pruebas unitarias correspondientes:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))   
    ...
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m, self.a, self.c, self.x = m, a, c, x0

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        self.x = x0

### 

def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Descripción del cometido de la función:
    Generador de números aleatorios en el rango (0 <= xn < m).

    Pruebas unitarias correspondientes:   
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m 
        i = (yield x)
        if i : x = i

doctest.testmod()