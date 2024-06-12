from geodesics import Geodesics
from body import Body
from utilities.bodyplotter import BodyPlotter

from sympy import *
import matplotlib.patches as patches

# Possible symbols
#τ,t,r,a,b,c,θ,φ,η,ψ,x,y 

def basic(
    s:             Symbol,
    coordinates:   list[Function],
    g_mk:          Matrix,
    initial_pos:   list[float],
    initial_vel:   list[float],
    solver_kwargs: dict = {},
    verbose:       int  = 0
) -> None:

    solver_kwargs.setdefault("time_interval", (0,100)                               )
    solver_kwargs.setdefault("method"       , "Radau"                               )
    solver_kwargs.setdefault("max_step"     , solver_kwargs["time_interval"][1]*1e-3)
    solver_kwargs.setdefault("atol"         , 1e-8                                  )
    solver_kwargs.setdefault("rtol"         , 1e-8                                  )
    solver_kwargs.setdefault("events"       , None                                  )

    print("Calculating geodesics")
    geodesics: Geodesics = Geodesics(s, g_mk, coordinates)
    body = Body(geodesics, initial_pos, initial_vel)

    print("Solving trajectory")
    body.solve_trajectory(**solver_kwargs)

    # Printing
    if verbose == 1:
        print("Geodesic differential equations: ")
        for equation in geodesics._dₛuᵏ:
            pprint(equation)
            print()

        print("Integration result: ")
        print(body.solver_result)

    return body
