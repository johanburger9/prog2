import concurrent.futures as future
from time import perf_counter as pc

import random
import numpy as np
import math

def hypersphere(n_and_d):
    n = n_and_d[0]
    d = n_and_d[1]
    r = 1
    n_inside = 0

    inside_sphere = lambda lis: np.sum([e**2 for e in lis])<r #Funktion som ger true (innanför) eller false (utanför)

    lista = [[random.uniform(-r, r) for j in range(d)] for i in range(n)] #Lista (längd n) med kortinatlistor (längd d)

    n_inside = len(list(filter(inside_sphere, lista))) #Använder funktionen inside_sphere på lista och filtrerar bort alla false. Tar sedan längden.

    V_theo = np.pi**(d/2)*r**d/math.gamma(d/2+1)
    V_approx = n_inside/n*(2*r)**d

    #print('d = '+str(d)+':')
    #print(V_theo)
    #print(V_approx)
    return V_approx

#start1 = pc()
#results = hypersphere([10000000, 11])
#print(results)
#end1 = pc()
#print(f"Runtime: {round(end1-start1, 2)} seconds")

start2 = pc()
with future.ProcessPoolExecutor() as ex:
    results = ex.map(hypersphere, [[1000000, 11]]*10)
end2 = pc()
print(list(results))
print(f"Runtime: {round(end2-start2, 2)} seconds")