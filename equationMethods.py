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
class secant_oop:
    def __init__(self,a_0, b_0, option, option_num, stop_condition, expr):
        self.a_0 = a_0
        self.b_0 = b_0
        self.option = option
        self.option_num = option_num
        self.stop_condition = stop_condition
        
        x = symbols("x")
        self.f = lambdify(x, expr, "math");
        f1 = expr.diff(x)
        f2 = f1.diff(x)
        self.f1 = lambdify(x, f1, "math");
        self.f2 = lambdify(x, f2, "math");
        self.m1 =  min( abs(self.f1(self.a_0)), abs(self.f1(self.b_0)));
        self.M1 =  max( abs(self.f1(self.a_0)), abs(self.f1(self.b_0)));
        if(self.f2(self.a_0)*self.f(self.a_0) > 0): 
            self.d = a_0 
            self.x_0 = b_0
        else:
            self.x_0 = a_0 
            self.d = b_0
    def __secantMethodEpsilon1(self):
        notice = 0
        epsilon = self.option_num
        de_0 = epsilon*self.m1
        df = pd.DataFrame(columns = ["x_n", "|f(x_n)|"])
        result = self.x_0
        while True:
            new_row = pd.DataFrame([{"x_n": result, "|f(x_n)|": abs(self.f(result))}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            if(abs(self.f(result)) <= self.m1 * epsilon): break
            result = result - (self.f(result)*(result - self.d))/(self.f(result) - self.f(self.d))
            notice +=1
        return de_0, self.x_0, self.d, self.m1, self.M1, df, notice, result
        
    def __secantMethodEpsilon2(self):
        notice = 0
        epsilon = self.option_num
        de_0 = epsilon*self.m1/(self.M1-self.m1)
        df = pd.DataFrame(columns = ["x_n", "|x_n - x_n-1|"])
        result = self.x_0
        result_prev = self.d
        while True:
            new_row = pd.DataFrame([{"x_n": result, 
                                     "|x_n - x_n-1|": abs(result - result_prev)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            if abs(result - result_prev) <= epsilon*self.m1/(self.M1- self.m1): break
            result_prev = result
            result = result - (self.f(result)*(result - self.d))/(self.f(result) - self.f(self.d))
            notice +=1
        return de_0, self.x_0, self.d, self.m1, self.M1, df, notice, result
        
    def __secantMethodDelta1(self):
        notice = 0
        delta = self.option_num
        de_0 = delta*self.m1
        df = pd.DataFrame(columns = ["x_n", "|f(x_n)| / |x_n|"])
        result = self.x_0
        while True:
            new_row = pd.DataFrame([{"x_n": result, "|f(x_n)| / |x_n|": abs(self.f(result)) / abs(result)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            if(abs(self.f(result)) <= self.m1 * delta*abs(result)): break
            result = result - (self.f(result)*(result - self.d))/(self.f(result) - self.f(self.d))
            notice +=1
        return de_0, self.x_0, self.d, self.m1, self.M1, df, notice, result
        
    def __secantMethodDelta2(self):
        notice = 0
        delta = self.option_num
        de_0 = delta*self.m1/(self.M1-self.m1)
        df = pd.DataFrame(columns = ["x_n", "|x_n - x_n-1| / |x_n|"])
        result = self.x_0
        result_prev = self.d
        while True:
            new_row = pd.DataFrame([{"x_n": result, 
                                     "|x_n - x_n-1| / |x_n|": abs(result - result_prev) / abs(result)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            if abs(result - result_prev) <= delta*abs(result)*self.m1/(self.M1- self.m1): break
            result_prev = result
            result = result - (self.f(result)*(result - self.d))/(self.f(result) - self.f(self.d))
            notice +=1
        return de_0, self.x_0, self.d, self.m1, self.M1, df, notice, result

    def __secantMethodN(self):
        notice = self.option_num
        df = pd.DataFrame(columns = ["x_n", "|f(x_n)|", "|x_n - x_n-1|"])
        result = self.x_0
        result_prev = self.d
        for i in range(notice):
            new_row = pd.DataFrame([{"x_n": result, "|f(x_n)|":self.f(result),
                                     "|x_n - x_n-1|": abs(result - result_prev) / abs(result)}])
            if df.empty: df = new_row
            else: df = pd.concat([df, new_row], ignore_index=True)
            if self.f(result) == 0: break
            result_prev = result
            result = result - (self.f(result)*(result - self.d))/(self.f(result) - self.f(self.d))
        return None, self.x_0, self.d, self.m1, self.M1, df, notice, result
        
    def Solve(self):
        if self.option == "Cho trước số lần lặp": return self.__secantMethodN()
        if self.option == "Sai số tuyệt đối":
            if self.stop_condition == "|xₙ - x*| ≤ |f(xₙ)| / m₁":
                return self.__secantMethodEpsilon1()
            else:
                return self.__secantMethodEpsilon2()
        else:
            if self.stop_condition == "|xₙ - x*| ≤ |f(xₙ)| / m₁":
                return self.__secantMethodDelta1()
            else:
                return self.__secantMethodDelta2()
