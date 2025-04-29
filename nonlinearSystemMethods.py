from math import *
from sympy import *
import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
def find_global_maximum_on_box(func, variables, bounds, **kwargs):
    objective_func = lambda x: -func(*np.asarray(x))
    try:
        result = differential_evolution(objective_func, bounds, **kwargs)
        if result.success:
            return -result.fun
        else:
            return -np.inf
    except Exception as e:
        return -np.inf
        
class newton_raphson_oop:
    def __init__(self, n, x_0, option, option_num, expr):
        self.n = n
        self.variables = [symbols(f"x{i}") for i in range(1,n+1)]
        self.x_0 = x_0
        self.option = option
        self.option_num = option_num
        self.F = expr
    def __jacobiMatrix(self):
        jacobi = []
        for i in range(self.n):
            row = [(self.F[i].diff(self.variables[j])) for j in range(self.n)]
            jacobi.append(row)
        jacobi = Matrix(jacobi)
        return jacobi
    def __newtonRaphsonMethodEpsilon(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
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
        result = X
        return J,notice,result,df
    def __newtonRaphsonMethodDelta(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        delta = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        while True:
            notice +=1
            X_prev = X
            X = X - J.subs({self.variables[i]: X[i] for i in range(n)}).evalf().inv()*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev|| / ||X||": abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))}])
            df = pd.concat([df, new_row], ignore_index=True)
    
            check = abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))
            if check<delta: break
        result = X
        return J,notice,result,df
    def __newtonRaphsonMethodN(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        time = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        for i in range(time-1):
            notice +=1
            X_prev = X
            X = X - J.subs({self.variables[i]: X[i] for i in range(n)}).evalf().inv()*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev||": abs(max(list(X_prev-X),key=abs)), "||X-X_prev|| / ||X||": abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))}])
            df = pd.concat([df, new_row], ignore_index=True)
        result = X
        return J,notice,result,df
        
    def Solve(self):
        option = self.option
        if option == "Sai số tuyệt đối":
            return self.__newtonRaphsonMethodEpsilon()
        elif option == "Sai số tương đối":
            return self.__newtonRaphsonMethodDelta()
        else:
            return self.__newtonRaphsonMethodN()


class newton_modified_oop:
    def __init__(self, n, x_0, option, option_num, expr):
        self.n = n
        self.variables = [symbols(f"x{i}") for i in range(1,n+1)]
        self.x_0 = x_0
        self.option = option
        self.option_num = option_num
        self.F = expr
    def __jacobiMatrix(self):
        jacobi = []
        for i in range(self.n):
            row = [(self.F[i].diff(self.variables[j])) for j in range(self.n)]
            jacobi.append(row)
        jacobi = Matrix(jacobi)
        return jacobi
    def __newtonModifiedMethodEpsilon(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        J0 = J.subs({self.variables[i]: self.x_0[i] for i in range(n)}).evalf()
        if J0.det() == 0: return J,J0,None,None,None,None,0,0
        J0inv = J0.inv().evalf()
        eps = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        while True:
            notice +=1
            X_prev = X
            X = X - J0inv*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev||": abs(max(list(X_prev-X),key=abs))}])
            df = pd.concat([df, new_row], ignore_index=True)

            if 'check' in locals(): 
                check_prev = check
            check = abs(max(list(X_prev-X),key=abs))
            if 'check_prev' in locals():
                if check_prev<check:return J,J0,J0inv,None,None,None,0,1
            if check<eps: break
        result = X
        return J,J0,J0inv,notice,result,df,1,1
    def __newtonModifiedMethodDelta(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        J0 = J.subs({self.variables[i]: self.x_0[i] for i in range(n)}).evalf()
        if J0.det() == 0: return J,J0,None,None,None,None,0,0
        J0inv = J0.inv().evalf()
        delta = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        while True:
            notice +=1
            X_prev = X
            X = X - J0inv*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev|| / ||X||": abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))}])
            df = pd.concat([df, new_row], ignore_index=True)

            if 'check' in locals(): 
                check_prev = check
            check = abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))
            if 'check_prev' in locals():
                if check_prev<check:return J,J0,J0inv,None,None,None,0,1
            if check<delta: break
        result = X
        return J,J0,J0inv,notice,result,df,1,1
    def __newtonModifiedMethodN(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        J0 = J.subs({self.variables[i]: self.x_0[i] for i in range(n)}).evalf()
        if J0.det() == 0: return J,J0,None,None,None,None,0,0
        J0inv = J0.inv().evalf()
        time = self.option_num
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        for i in range(time-1):
            notice +=1
            X_prev = X
            X = X - J0inv*self.F.subs({self.variables[i]: X[i] for i in range(n)}).evalf()
            
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev||": abs(max(list(X_prev-X),key=abs)), "||X-X_prev|| / ||X||": abs(max(list(X_prev-X),key=abs)) / abs(max(list(X), key = abs))}])
            df = pd.concat([df, new_row], ignore_index=True)
        result = X
        return J,J0,J0inv,notice,result,df,1,1
        
    def Solve(self):
        option = self.option
        if option == "Sai số tuyệt đối":
            return self.__newtonModifiedMethodEpsilon()
        elif option == "Sai số tương đối":
            return self.__newtonModifiedMethodDelta()
        else:
            return self.__newtonModifiedMethodN()

class single_loop_oop:
    def __init__(self, n, x_0, a_0, b_0, option, option_num, expr):
        self.n = n
        self.variables = [symbols(f"x{i}") for i in range(1,n+1)]
        self.x_0 = x_0
        self.a_0 = a_0
        self.b_0 = b_0
        self.option = option
        self.option_num = option_num
        self.phi = expr
    def __jacobiMatrix(self):
        jacobi = []
        for i in range(self.n):
            row = [(self.phi[i].diff(self.variables[j])) for j in range(self.n)]
            jacobi.append(row)
        jacobi = Matrix(jacobi)
        return jacobi
    def __jacobiMaximumMatrix(self):
        jacobi_matrix = self.__jacobiMatrix()
        jacobi_list = [lambdify(self.variables,jacobi_matrix[i, j],"numpy") for i in range(self.n) for j in range(self.n)]
        bounds = [(self.a_0[i], self.b_0[i]) for i in range(self.n)]
        maximumList = [find_global_maximum_on_box(func, self.variables, bounds) for func in jacobi_list]
        return Matrix(np.array(maximumList).reshape((self.n,self.n))) 
    def __singleLoopMethodEpsilon(self):
        notice = 1
        n = self.n
        J = self.__jacobiMatrix()
        JMaximum = self.__jacobiMaximumMatrix()
        max_row = max([sum(abs(x) for x in list(JMaximum[i,:])) for i in range(n)])
        max_col = max([sum(abs(x) for x in list(JMaximum[:,i])) for i in range(n)])
        K = max(max_row, max_col)
        eps = self.option_num
        eps0 = eps*(1-K)/K
        X = self.x_0
        df = pd.DataFrame([{f"x{i}_k":X[i-1] for i in range(1,n+1)}])
        while True:
            notice +=1
            X_prev = X
            X = self.phi.subs({self.variables[i]: X[i] for i in range(n)})
            new_row = pd.DataFrame([{**{f"x{i}_k":X[i-1] for i in range(1,n+1)},
                             "||X-X_prev||": abs(max(list(X_prev-X),key=abs))}])
            df = pd.concat([df, new_row], ignore_index=True)
    
            check = abs(max(list(X_prev-X),key=abs))
            if check<eps0: break
        result = X
        return J, JMaximum, max_row, max_col, K, eps0, notice, result, df
        
