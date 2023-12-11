from newton.newton import newton
from es.es import evo_strat
from es_newton.hybrid import es_newton
from cmaes.cmaes import cma_evo_strat
import numpy as np
from deap import benchmarks


def main():
    x0 = np.array([1, 1])
    x_newton = newton(lambda x: benchmarks.ackley(x)[0], x0)

    x_es = evo_strat(lambda x: benchmarks.ackley(x)[0], 2, children=1000, parents=100, x0=x0, display=False)

    x_es_newton = es_newton(lambda x: benchmarks.ackley(x)[0], 2, children=1000, parents=100, x0=x0, display=False)
    x_cmaes = cma_evo_strat(lambda x: benchmarks.ackley(x)[0], 2, children=1000, parents=100, x0=x0, display=False)
    print(f"Newton's method results: {x_newton}")
    print(f"Evolutionary strategy results: {x_es.x}")
    print(f"Newton-ES hybrid results: {x_es_newton}")
    print(f"CMA-ES results: {x_cmaes.x}")
    

if __name__ == "__main__":
    main()
