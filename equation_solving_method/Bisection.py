from math import *
from sympy import *
import pandas as pd
class bisection_oop:
    def __init__(self, a_0, b_0,option, option_num, expr):
        self.f = expr
        self.a_0 = a_0
        self.b_0 = b_0
        self.option = option
        self.option_num = option_num

    def __bisectionEpsilonMethod(self):
        nIterations = 0
        left    = self.a_0
        right   = self.b_0
        epsilon = self.option_num
        df = pd.DataFrame(columns = ["left", "right", "mid", "left sign" "Absolute error"])

        # Special case: f(a) = 0 or f(b) = 0
        if(self.f(left) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": left}]), 0, left
        if(self.f(right) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": right}]), 0, right
            
        # Evaluation phase
        mid_prev = left
        mid = (left + right) / 2
        lft_sign = 1 if self.f(left) >= 0 else -1
        while abs(mid - mid_prev) >= epsilon:
            
            if (nIterations !=0): mid_prev = mid

            mid = (left + right) / 2            
            new_row = pd.DataFrame([{"left": left, "right": right, "mid": mid, "sign":sign(self.f(mid)),
                                     "Absolute error": abs(mid - mid_prev)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            val = self.f(mid)
            if(val == 0): return df, nIterations, mid
            if(val * lft_sign < 0):
                right = mid
            else:
                left = mid
            nIterations = nIterations + 1
        result = mid
        return df, nIterations, result
        
    def __bisectionDeltaMethod(self):
        nIterations = 0
        left    = self.a_0
        right   = self.b_0
        delta = self.option_num
        df = pd.DataFrame(columns = ["left", "right", "mid", "left sign" "Relative error"])

        # Special case: f(a) = 0 or f(b) = 0
        if(self.f(left) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": left}]), 0, left
        if(self.f(right) == 0): return pd.DataFrame([{"left": left, "right": right, "solution": right}]), 0, right
            
        # Evaluation phase
        mid_prev = left
        mid = (left + right) / 2
        lft_sign = 1 if self.f(left) >= 0 else -1
        check = abs(mid - mid_prev)/abs(mid) if mid!=0 else delta+1
        while check >= delta:
            
            if (nIterations !=0): mid_prev = mid

            mid = (left + right) / 2            
            new_row = pd.DataFrame([{"left": left, "right": right, "mid": mid, "sign":sign(self.f(mid)),
                                     "Relative error": abs(mid - mid_prev)/abs(mid) if mid!=0 else "NaN"}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            val = self.f(mid)
            if(val == 0): return df, nIterations, mid
            if(val * lft_sign < 0):
                right = mid
            else:
                left = mid
            nIterations = nIterations + 1
            check = abs(mid - mid_prev)/abs(mid) if mid!=0 else delta+1
        result = mid
        return df, nIterations, result
        
    def __bisectionNumMethod(self):
        left    = self.a_0
        right   = self.b_0
        n = self.option_num
        df = pd.DataFrame(columns = ["left", "right", "mid", "left sign" "Absolute error"])
        mid = left
        lft_sign = 1 if self.f(left) >= 0 else -1
        if(self.f(left) == 0): 
            return pd.DataFrame([{"left": left, "right": right, "solution": left}]), 0, left
        if(self.f(right) == 0): 
            return pd.DataFrame([{"left": left, "right": right, "solution": right}]), 0, right
        for i in range(n):
            mid_prev = mid
            mid = (left+right)/2
            new_row = pd.DataFrame([{"left": left, "right": right, "mid": mid, "sign":sign(self.f(mid)),
                                     "Absolute error": abs(mid - mid_prev)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            val = self.f(mid)
            if(val == 0): return df, i, mid
            if(val * lft_sign < 0):
                right = mid
            else:
                left = mid
        result = mid
        return df, n, result    
    def Solve(self):
        option = self.option
        if option == "Sai số tuyệt đối":
            return self.__bisectionEpsilonMethod()
        elif option == "Sai số tương đối":
            return self.__bisectionDeltaMethod()
        else:
            return self.__bisectionNumMethod()
