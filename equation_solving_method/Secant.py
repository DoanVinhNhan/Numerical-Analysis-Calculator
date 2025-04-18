from math import *
from sympy import *
import pandas as pd
import sympy as sym
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
        self.f1 = sym.lambdify(x, f1, "math");
        self.f2 = sym.lambdify(x, f2, "math");
        self.m1 =  min( abs(self.f1(self.a_0)), abs(self.f1(self.b_0)));
        self.M1 =  max( abs(self.f1(self.a_0)), abs(self.f1(self.b_0)));
        if(self.f2(self.a_0)*self.f(self.a_0) > 0): 
            self.d = a_0 
            self.x_0 = b_0
        else:
            self.x_0 = a_0 
            self.d = b_0
        def __secantMethodEpsilon1(self):
        def __secantMethodEpsilon2(self):
        def __secantMethodDelta1(self):
        def __secantMethodDelta2(self):
        def solve(self):
    