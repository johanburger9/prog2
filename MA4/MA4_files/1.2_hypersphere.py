import random
import numpy as np
import math

r = 1
ns_and_ds = [[100000, 2], [100000, 11]]
ds = [2, 11]

for n, d in ns_and_ds[0], ns_and_ds[1]:
    n_inside = 0

    inside_sphere = lambda lista: np.sum([e**2 for e in lista])<r #Funktion som ger true (innanför) eller false (utanför)

    lista = [[random.uniform(-r, r) for j in range(d)] for i in range(n)] #Lista (längd n) med kortinatlistor (längd d)

    n_inside = len(list(filter(inside_sphere, lista))) #Använder funktionen inside_sphere på lista och filtrerar bort alla false. Tar sedan längden.

    V_theo = np.pi**(d/2)*r**d/math.gamma(d/2+1)
    V_approx = n_inside/n*(2*r)**d

    print('d = '+str(d)+':')
    print(V_theo)
    print(V_approx)

