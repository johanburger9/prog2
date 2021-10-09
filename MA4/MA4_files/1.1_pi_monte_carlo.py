import random
import math
import matplotlib.pyplot as plt
ns  = [1000, 10000, 100000]
for n in ns:
    r = 1
    n_s_x = []
    n_s_y = []
    n_c_x = []
    n_c_y = []
    for i in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 >= r: #blue
            n_s_x.append(x) 
            n_s_y.append(y)
        else:                #red
            n_c_x.append(x) 
            n_c_y.append(y) 
    pi_approx = 4*len(n_c_x)/n

    print(len(n_c_x))
    print(pi_approx)
    print(math.pi)

    plt.figure()
    plt.plot(n_s_x, n_s_y, 'b.')
    plt.plot(n_c_x, n_c_y, 'r.')
plt.show()

ending = input()