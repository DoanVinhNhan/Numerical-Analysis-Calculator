from math import *
from sympy import *
import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
class newton_raphson_oop:
    def __init__(self, n, x_0, option, option_num, expr):
        self.n = n
        self.variables = [symbols(f"x{i}") for i in range(1,n+1)]
        self.x_0 = x_0
        self.option = option
        self.option_num = option_num
        self.F = expr
    def jacobiMatrix(self):
        jacobi = []
        for i in range(self.n):
            row = [(self.F[i].diff(self.variables[j])) for j in range(self.n)]
            jacobi.append(row)
        jacobi = Matrix(jacobi)
        return jacobi
    def newtonRaphsonMethodEpsilon(self):
        notice = 1
        n = self.n
        J = self.jacobiMatrix()
        eps = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        while True:
            notice +=1
            X_prev = X
            X = X - J.subs({self.variables[i]: X[i] for i in range(n)}).evalf().inv()*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev||": abs(max(list(X_prev-X),key=abs))}])
            df = pd.concat([df, new_row], ignore_index=True)
    
            check = abs(max(list(X_prev-X),key=abs))
            if check<eps: break
        return J,notice,df
    def newtonRaphsonMethodDelta(self):
        