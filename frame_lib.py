import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from sympy import *
import pandas as pd
from equation_solving_method.Bisection import bisection_oop

#Define Basic Frame class
class baseFrame:
    def __init__(self, root):
        self.root = root

    def destroy_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_navigation_buttons(self, home_frame, back_frame):
        tk.Button(self.root, text="Home", command=lambda: home_frame.display()).place(x=700, y=560)
        tk.Button(self.root, text="Quay lại", command=lambda: back_frame.display()).place(x=600, y=560)
        tk.Button(self.root, text="Reset", command=lambda: self.display()).place(x=20, y=560)
        
#Define frame manager
class frameManager:
    def __init__(self, root):
        self.root = root
        self.frames = {}

    def add_frame(self, name, frame):
        self.frames[name] = frame

    def switch_frame(self, name):
        self.frames[name].display()
        
#Define specifically frames
class main_frame(baseFrame):
    def display(self):
        self.destroy_widgets()
        label = ctk.CTkLabel(self.root, text="Máy tính giải tích số", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        source = ctk.CTkLabel(self.root, text="Source by ĐVN", font=ctk.CTkFont(size=12))
        source.place(x=10, y=565)

        ctk.CTkButton(self.root, text="Giải phương trình f(x) = 0", 
                      command=lambda: equation_frame.display(), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self.root, text="Giải hệ phi tuyến", 
                      command=lambda: nonlinear_system_frame.display(), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self.root, text="Giải hệ phương trình AX = B", 
                      command=lambda: matrix_frame.display(), width=400, height=60).place(x=200, y=300)
class equation_frame(baseFrame):
    def display(self):
        self.destroy_widgets()
        label = ctk.CTkLabel(self.root, text="Giải phương trình f(x) = 0", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self.root, text="Phương pháp chia đôi", 
                      command=lambda: bisection_frame.display(), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self.root, text="Phương pháp dây cung", 
                      command=lambda: secant_frame.display(), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self.root, text="Phương pháp tiếp tuyến", 
                      command=lambda: newton1_frame.display(), width=400, height=60).place(x=200, y=300)
        ctk.CTkButton(self.root, text="Phương pháp lặp đơn", 
                      command=lambda: single_loop1_frame.display(), width=400, height=60).place(x=200, y=400)
class nonlinear_system_frame(baseFrame):
    def display(self):
        self.destroy_widgets()
        label = ctk.CTkLabel(self.root, text="Giải hệ phi tuyến", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self.root, text="Phương pháp Newton Raphson", 
                      command=lambda: newton_frame.display(), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self.root, text="Phương pháp Newton Modified", 
                      command=lambda: newton_m_frame.display(), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self.root, text="Phương pháp lặp dơn", 
                      command=lambda: single_loop_frame.display(), width=400, height=60).place(x=200, y=300)
class matrix_frame(baseFrame):
     def display(self):
        self.destroy_widgets()
        label = ctk.CTkLabel(self.root, text="Giải hệ phương trình AX = B", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self.root, text="Phương pháp Gauss", 
                      command=lambda: gauss_frame.display(), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self.root, text="Phương pháp Gauss Jordan", 
                      command=lambda: gauss_jordan_frame.display(), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self.root, text="Phương pháp phân rã LU", 
                      command=lambda: lu_frame.display(), width=400, height=60).place(x=200, y=300)
        ctk.CTkButton(self.root, text="Phương pháp cholesky", 
                      command=lambda: cholesky_frame.display(), width=400, height=60).place(x=200, y=400)

#Define frame form for equation methods
class equationMethodFrame(BaseFrame):
    def __init__(self,title):
        self.f_str = ctk.StringVar()
        self.a_str = ctk.StringVar()
        self.b_str = ctk.StringVar()
        self.selected_option = ctk.StringVar()
        self.option_num_input = ctk.StringVar()
        
        self.title = tk.Label(self.root,text=title, font=ctk.CTkFont(size=30, weight="bold"))
        self.notice_label = tk.Label(self.root)
        self.result_label = tk.Label(self.root)
        self.except_error_label = tk.Label(self.root)

        self.f_label = ctk.CTkLabel(self.root, text = "f(x) = ", font = ("Arial",16))
        self.a_label = ctk.CTkLabel(self.root, text = "a = ", font = ("Arial",16))
        self.b_label = ctk.CTkLabel(self.root, text = "b = ", font = ("Arial",16))
        self.options_label = ctk.CTkLabel(self.root, text = "Option:")
        self.eps_label = ctk.CTkLabel(self.root, text="\u03B5 = ", font = ("Arial", 16))
        self.delta_label = ctk.CTkLabel(self.root, text="\u03B4 = ", font = ("Arial", 16))
        self.n_label = ctk.CTkLabel(self.root, text = "n = ", font = ("Arial", 16))
        
        self.f_input = ctk.CTkEntry(self.root, width=400, height = 30, textvariable=self.f_str)
        self.a_input = ctk.CTkEntry(self.root, width=60, height = 30, textvariable=self.a_str)
        self.b_input = ctk.CTkEntry(self.root, width=60, height = 30, textvariable=self.b_str)
        self.option_num_input = ctk.CTkEntry(self.root, width=60, height = 30)

        self.selected_option = ctk.StringVar()
        self.option = []
        self.option_menu = ctk.CTkOptionMenu(self.root,values=self.options,variable=selected_option,
                                    fg_color="white",
                                    text_color="black",
                                    button_color="lightblue", 
                                    button_hover_color="skyblue")

        self.tree = ttk.Treeview(self.root)
        self.scrollbar_x = tk.Scrollbar(self.root)
        self.scrollbar_y = tk.Scrollbar(self.root)
        
    def displaybase(self):
        self.title.pack(pady=20)
        self.f_label.place(x=30, y = 70)
        self.f_input.place(x=80, y =70)
        self.a_label.place(x=510, y = 70)
        self.a_input.place(x=550, y = 70)
        self.b_label.place(x=630, y =70)
        self.b_input.place(x=670, y =70)
        
#Define specifically method frames of equation
class bisection_frame(equationMethodFrame):
    def display(self):
        self.destroy_widgets()
        self.displaybase()

        self.option = ["Sai số tuyệt đối","Sai số tương đối","Cho trước số lần lặp"]
        self.selected_option = "Sai số tuyệt đối"
        self.options_label.place(x=30, y=120)
        self.option_menu.place(x = 80, y = 120)
        self.eps_label.place(x=260, y =120)
        tk.CTkButton(self.root,text="Giải",command =lambda: bisectionFrame.solve()).pack(pady = 100)
        
    def solve(self):


class secant_frame(equationMethodFrame):
    def display(self):

    def solve(self):
        
class newton1_frame(equationMethodFrame):
    def display(self):

    def solve(self):
        
class single_loop1_frame(equationMethodFrame):
    def display(self):

    def solve(self):  

        
#Define frame form for non linear system methods
class nonLinearSystemMethodsFrame(BaseFrame):
    def __init__(self, title):

    def displaybase(self):

        
#Define specifically method frames of non linear system
class newton_frame(nonLinearSystemMethodsFrame):
    def display(self):

    def solve(self):
        
class newton_m_frame(nonLinearSystemMethodsFrame):
    def display(self):

    def solve(self):

class single_loop_frame(nonLinearSystemMethodsFrame):
    def display(self):

    def solve(self):


#Define frame form for matrix methods
class matrixFrame(BaseFrame):
    def __init__(self, title):

    def displaybase(self):

        
#Define specifically method frames of non linear system    
class gauss_frame(matrixFrame):
    def __init__(self, title):

    def displaybase(self):

class gauss_jordan_frame(matrixFrame):
    def __init__(self, title):

    def displaybase(self):

class lu_frame(matrixFrame):
    def __init__(self, title):

    def displaybase(self):

class cholesky_frame(matrixFrame):
    def __init__(self, title):

    def displaybase(self):

