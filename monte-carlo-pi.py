import random

# config
N = int(1e9)            # number of iterations/samples
r = 1                   # radius of the circle
seed = 0                # seed for random number generator
checkpoint = int(1e6)   # checkpoint interval

def main():
    print('Estimating pi using Monte Carlo method...')
    random.seed(seed)
    mu = 0
    M2 = 0
    i = 1
    try:
        while i <= N:
            x = random.uniform(-r, r)
            y = random.uniform(-r, r)
            f = 1 if x**2 + y**2 <= r**2 else 0

            if i == 1:
                mu = f
                M2 = 0
            else:
                d1 = f - mu
                mu += d1 / i
                d2 = f - mu
                M2 += d1 * d2

            pi = 4*r**2 * mu
            var = (4*r**2)**2 * M2/i
            std_err = (var / i)**0.5

            if i % checkpoint == 0:
                print(f'Iteration {i} -> pi={pi:.10f}, std_err={std_err:.10f}')
            i += 1
        print('\n\nDone!\n\n')
    
    except KeyboardInterrupt:
        print(f'\n\nInterrupted!\n\n')
        pass
    
    print(f'Final iteration {i} -> pi={pi:.10f}, std_err={std_err:.10f}')
    print(f'pi={pi:.60f}')

if __name__ == '__main__':
    main()
