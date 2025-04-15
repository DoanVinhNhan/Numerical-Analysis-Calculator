from math import *
from sympy import *
import pandas as pd
class bisection_oop:
    def __init__(self, a_0, b_0, eps, expr):
        x = symbols("x")
        expr = lambdify(x, expr, "numpy")
        self.f = expr
        self.a_0 = a_0
        self.b_0 = b_0
        self.eps = eps

    def __checkInputValidity(self):
        L = self.a_0
        R = self.b_0
        # Check if a < b
        if(L > R or (L == R and self.f(L) != 0)): return 0
        # Check if f(a) * f(b) < 0
        if(self.f(L) * self.f(R) >= 0): return 0
        return 1

    def __bisectionMethod(self):
        nIterations = 0
        left    = self.a_0
        right   = self.b_0
        epsilon = self.eps
        df = pd.DataFrame(columns = ["left", "right", "mid", "left sign" "delta%"])

        # Special case: f(a) = 0 or f(b) = 0
        if(self.f(left) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": left}])
        if(self.f(right) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": right}])
            
        # Evaluation phase
        mid_prev = left
        mid = (left + right) / 2
        lft_sign = 1 if self.f(left) >= 0 else -1
        while abs(mid - mid_prev)/abs(mid) >= epsilon/100:
            
            if (nIterations !=0): mid_prev = mid

            mid = (left + right) / 2            
            new_row = pd.DataFrame([{"left": left, "right": right, "mid": mid, "sign":sign(self.f(mid)), "delta%": abs(mid - left)/abs(mid)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            val = self.f(mid)
            if(val == 0): return df
            if(val * lft_sign < 0):
                right = mid
            else:
                left = mid
            nIterations = nIterations + 1
        result = mid
        return df, nIterations, result

    def Solve(self):
        return self.__bisectionMethod()
