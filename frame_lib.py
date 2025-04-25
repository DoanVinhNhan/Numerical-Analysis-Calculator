import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from sympy import *
import pandas as pd
import numpy as np
from PIL import Image
from equationMethods import bisection_oop, secant_oop, newton1_oop, single_loop1_oop

# Function to convert DataFrame to Treeview
def dataframe_to_treeview(df, root):
    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)
    for col in df.columns:
        tree.column(col, width=100)
        tree.heading(col, text=col)
    for i, row in df.iterrows():
        tree.insert("", "end", text=i, values=list(row))
    tree.heading("#0", text="n")
    tree.column("#0", width=30)

    scrollbar_y = tk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbar_x.set)

    return tree, scrollbar_x, scrollbar_y

# Define Basic Frame class
class baseFrame(tk.Frame):
    def __init__(self, root, frame_manager):
        super().__init__(root)
        self.root = root
        self.frame_manager = frame_manager

    def hide(self):
        self.pack_forget()
    def display(self):
        self.pack(fill="both", expand=True)
    def setup_navigation_buttons(self, back_frame):
        tk.Button(self, text="Home", command=lambda: 
                  self.frame_manager.switch_frame("main_frame")).place(x=700, y=560)
        tk.Button(self, text="Quay lại", command=lambda:
                  self.frame_manager.switch_frame(back_frame)).place(x=600, y=560)

# Define frame manager
class frameManager:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        self.current_frame = None

    def add_frame(self, name, frame):
        self.frames[name] = frame

    def switch_frame(self, name):
        if self.current_frame:
            self.current_frame.hide()
            self.root.update_idletasks()
        self.frames[name].display()
        self.root.update_idletasks()
        self.current_frame = self.frames[name]

# Define specifically frames
class main_frame(baseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager)
        label = ctk.CTkLabel(self, text="Máy tính giải tích số", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        source = ctk.CTkLabel(self, text="Source by ĐVN", font=ctk.CTkFont(size=12))
        source.place(x=10, y=565)

        ctk.CTkButton(self, text="Giải phương trình f(x) = 0",command = lambda:
                      frame_manager.switch_frame("equation_frame"), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self, text="Giải hệ phi tuyến",command = lambda:
                      frame_manager.switch_frame("nonlinear_system_frame"), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self, text="Giải hệ phương trình AX = B",command = lambda:
                      frame_manager.switch_frame("matrix_frame"), width=400, height=60).place(x=200, y=300)
        
class equation_frame(baseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager)
        self.setup_navigation_buttons("main_frame")
        label = ctk.CTkLabel(self, text="Giải phương trình f(x) = 0", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self, text="Phương pháp chia đôi",command = lambda:
                      frame_manager.switch_frame("bisection_frame"), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self, text="Phương pháp dây cung",command = lambda:
                      frame_manager.switch_frame("secant_frame"), width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self, text="Phương pháp tiếp tuyến",command = lambda:
                      frame_manager.switch_frame("newton1_frame"), width=400, height=60).place(x=200, y=300)
        ctk.CTkButton(self, text="Phương pháp lặp đơn",command = lambda:
                      frame_manager.switch_frame("single_loop1_frame"), width=400, height=60).place(x=200, y=400)
class nonlinear_system_frame(baseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager)
        self.setup_navigation_buttons("main_frame")
        label = ctk.CTkLabel(self, text="Giải hệ phi tuyến", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self, text="Phương pháp Newton Raphson",command = lambda:
                      frame_manager.switch_frame("newton_raphson_frame"), width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self, text="Phương pháp Newton Modified", width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self, text="Phương pháp lặp đơn", width=400, height=60).place(x=200, y=300)
class matrix_frame(baseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager)
        self.setup_navigation_buttons("main_frame")
        label = ctk.CTkLabel(self, text="Giải hệ phương trình AX = B", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self, text="Phương pháp Gauss", width=400, height=60).place(x=200, y=100)
        ctk.CTkButton(self, text="Phương pháp Gauss_Jordan", width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self, text="Phương pháp phân rã LU", width=400, height=60).place(x=200, y=300)
        ctk.CTkButton(self, text="Phương pháp Cholesky", width=400, height=60).place(x=200, y=400)

#Define form of equation methods frame
class equationMethodBaseFrame(baseFrame):
    def __init__(self, root, frame_manager, title):
        super().__init__(root, frame_manager)
        self.setup_navigation_buttons("equation_frame")
        self.f_str = ctk.StringVar()
        self.a_str = ctk.StringVar()
        self.b_str = ctk.StringVar()
        self.selected_option = ctk.StringVar()
        self.option_num_input = ctk.StringVar()
        self.options = []

        self.title_label = ctk.CTkLabel(self, text = title, font=ctk.CTkFont(size=30, weight="bold"))
        self.options_label = ctk.CTkLabel(self, text="Option:")
        self.eps_label = ctk.CTkLabel(self, text="\u03B5 = ", font=("Arial", 16))
        self.delta_label = ctk.CTkLabel(self, text="\u03B4 = ", font=("Arial", 16))
        self.n_label = ctk.CTkLabel(self, text="n = ", font=("Arial", 16))

        self.f_label = ctk.CTkLabel(self, text="f(x) = ", font=("Arial", 16))
        self.a_label = ctk.CTkLabel(self, text="a = ", font=("Arial", 16))
        self.b_label = ctk.CTkLabel(self, text="b = ", font=("Arial", 16))
        
        self.f_input = ctk.CTkEntry(self, width=400, height=30, textvariable=self.f_str)
        self.a_input = ctk.CTkEntry(self, width=60, height=30, textvariable=self.a_str)
        self.b_input = ctk.CTkEntry(self, width=60, height=30, textvariable=self.b_str)
        self.option_input = ctk.CTkEntry(self, width=60, height=30, textvariable=self.option_num_input)

        self.option_menu = ctk.CTkOptionMenu(self, values=self.options, variable=self.selected_option,
                                        fg_color="white",
                                        text_color="black",
                                        button_color="lightblue",
                                        button_hover_color="skyblue")

        self.notice_label = ctk.CTkLabel(self)
        self.result_label = ctk.CTkLabel(self)
        self.except_error_label = ctk.CTkLabel(self, text="Lỗi!", text_color="red")
        self.error_input_label = ctk.CTkLabel(self, text="Đầu vào không hợp lệ", text_color="red")
        
        self.tree = ttk.Treeview(self)
        self.scrollbar_x = tk.Scrollbar(self)
        self.scrollbar_y = tk.Scrollbar(self)

        self.selected_option.trace("w", self.on_option_change)
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_fields)
        self.reset_button.place(x=20, y =560)

    def on_option_change(self, *args):
        self.option_input.delete(0, "end")

        self.eps_label.place_forget()
        self.delta_label.place_forget()
        self.n_label.place_forget()
        self.option_input.place_forget()

        selected = self.selected_option.get()
        if selected == "Sai số tuyệt đối":
            self.eps_label.place(x=260, y=120)
            self.option_input.place(x=300, y=120)
        elif selected == "Sai số tương đối":
            self.delta_label.place(x=260, y=120)
            self.option_input.place(x=300, y=120)
        else:
            self.n_label.place(x=260, y=120)
            self.option_input.place(x=300, y=120)
        self.root.update_idletasks()
    def reset_fields(self):
        self.f_str.set("")
        self.a_str.set("")
        self.b_str.set("")
        self.option_num_input.set("")

        self.error_input_label.place_forget()
        self.except_error_label.place_forget()
        self.notice_label.place_forget()
        self.result_label.place_forget()

        if self.tree and self.tree.winfo_exists():
             self.tree.destroy()
        if self.scrollbar_x and self.scrollbar_x.winfo_exists():
             self.scrollbar_x.destroy()
        if self.scrollbar_y and self.scrollbar_y.winfo_exists():
             self.scrollbar_y.destroy()
        self.tree = ttk.Treeview(self)
        self.scrollbar_x = tk.Scrollbar(self)
        self.scrollbar_y = tk.Scrollbar(self)
        self.root.update_idletasks()

    def putwidget(self):
        self.title_label.pack(pady=20)
        self.f_label.place(x=30, y=70)
        self.f_input.place(x=80, y=70)
        self.a_label.place(x=510, y=70)
        self.a_input.place(x=550, y=70)
        self.b_label.place(x=630, y=70)
        self.b_input.place(x=670, y=70)

        self.options_label.place(x=30, y=120)
        self.option_menu.place(x=80, y=120)
        self.eps_label.place(x=260, y=120)
        self.option_input.place(x=300, y=120)
        self.root.update_idletasks()
        
class bisection_frame(equationMethodBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp chia đôi")

        self.options = ["Sai số tuyệt đối", "Sai số tương đối", "Cho trước số lần lặp"]
        self.option_menu.configure(values=self.options)
        self.selected_option.set("Sai số tuyệt đối")
        
        self.putwidget()
        
        def solve(*args):
            self.error_input_label.place_forget()
            self.except_error_label.place_forget()
            self.notice_label.place_forget()
            self.result_label.place_forget()
            self.tree.destroy()
            self.scrollbar_x.destroy()
            self.scrollbar_y.destroy()
            try:
                x = symbols("x")
                expr = self.f_str.get()
                f = lambdify(x, expr, 'math')
                a = sympify(self.a_str.get())
                b = sympify(self.b_str.get())
                option = self.selected_option.get()
                option_num = sympify(self.option_num_input.get())
            
                if (a >= b or f(a) * f(b) > 0 
                or (option == "Cho trước số lần lặp" and (option_num != int(option_num))) or option_num <= 0):
                    self.error_input_label.place(x=30, y=250)
                    return
                uu = bisection_oop(a, b, option, option_num, f)
                df, notice, result = uu.Solve()
                df = df.apply(lambda col: col.map(lambda x: float(x)))
                    
                self.notice_label = ctk.CTkLabel(self, text=f"Phương pháp chia đôi kết thúc sau {notice} lần lặp")
                self.result_label = ctk.CTkLabel(self, text=f"Nghiệm x = {float(result)}")
                self.tree, self.scrollbar_x, self.scrollbar_y = dataframe_to_treeview(df, self)
            
                self.notice_label.place(x=30, y=250)
                self.result_label.place(x=30, y=280)
                self.tree.pack(expand=True, fill="x")
                self.scrollbar_x.pack(side="bottom", fill="x")
                self.scrollbar_y.pack(side="right", fill="y")
            except:
                self.except_error_label.place(x=30, y=250)

        solve_button = tk.Button(self, text="Giải", command=solve)
        solve_button.pack(pady=100)
        
class secant_frame(equationMethodBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp dây cung")
        
        self.stop_conditions = ["|xₙ - x*| ≤ |f(xₙ)| / m₁", "|xₙ - x*| ≤ (M₁ - m₁) |xₙ - xₙ₋₁| / m₁ "]
        self.selected_stop_condition = ctk.StringVar()
        self.selected_stop_condition.set("|xₙ - x*| ≤ |f(xₙ)| / m₁")
        self.stop_condition_label = ctk.CTkLabel(self,text = "Điều kiện dừng: ")
        self.stop_condition_menu = ctk.CTkOptionMenu(self, values=self.stop_conditions,
                                                     variable=self.selected_stop_condition,
                                                     fg_color="white",
                                                     text_color="black",
                                                     button_color="lightblue",
                                                     button_hover_color="skyblue",
                                                     width=120)
        self.m1_M1_label = ctk.CTkLabel(self)
        self.x_0_d_label = ctk.CTkLabel(self)
        self.de0_label = ctk.CTkLabel(self)
        
        self.putwidget()
        
        self.stop_condition_label.place(x=443, y =120)
        self.stop_condition_menu.place(x=550, y =120)

        def solve(*args):
            self.error_input_label.place_forget()
            self.except_error_label.place_forget()
            self.notice_label.place_forget()
            self.m1_M1_label.place_forget()
            self.x_0_d_label.place_forget()
            self.de0_label.place_forget()
            self.result_label.place_forget()
            self.tree.destroy()
            self.scrollbar_x.destroy()
            self.scrollbar_y.destroy()

            try:
                expr = sympify(self.f_str.get())
                a = sympify(self.a_str.get())
                b = sympify(self.b_str.get())
                option = self.selected_option.get()
                option_num = sympify(self.option_num_input.get())
                stop_condition = self.selected_stop_condition.get()
    
                if (a >= b or expr.subs("x",a)*expr.subs("x",b)>0 
                or option_num<=0 or (option == "Cho trước số lần lặp" and option_num!=int(option_num))):
                    self.error_input_label.place(x=30, y=250)
                    return
                uu = secant_oop(a, b, option, option_num, stop_condition, expr)
                de_0, x_0, d, m1, M1, df, notice, result = uu.Solve()
                df = df.apply(lambda col: col.map(lambda x: float(x)))
                    
                if option == "Sai số tuyệt đối": 
                    self.m1_M1_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₁ = {M1}.")
                    self.x_0_d_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}, d = {d}.")
                    self.de0_label =  ctk.CTkLabel(self, text=f"Điều kiện dừng: eps_0 = {de_0}.")
                if option == "Sai số tương đối": 
                    self.m1_M1_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₁ = {M1}.")
                    self.x_0_d_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}, d = {d}.")
                    self.de0_label =  ctk.CTkLabel(self, text=f"Điều kiện dừng: delta_0 = {de_0}.")
                if option == "Cho trước số lần lặp": 
                    self.m1_M1_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₁ = {M1}.")
                    self.x_0_d_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}, d = {d}.")
                self.notice_label = ctk.CTkLabel(self, text=f"Phương pháp dây cung kết thúc sau {notice} lần lặp")
                self.result_label = ctk.CTkLabel(self, text=f"Nghiệm x = {float(result)}.")
                self.tree, self.scrollbar_x, self.scrollbar_y = dataframe_to_treeview(df, self)
    
                self.m1_M1_label.place(x=30, y=200)
                self.x_0_d_label.place(x=30, y=225)
                if option!="Cho trước số lần lặp": self.de0_label.place(x=30, y=250)
                self.notice_label.place(x=30, y=275)
                self.result_label.place(x=30, y=300)
                self.tree.pack(expand=True, fill="x")
                self.scrollbar_x.pack(side="bottom", fill="x")
                self.scrollbar_y.pack(side="right", fill="y")
            except: 
                self.except_error_label.place(x=30, y=250)

        solve_button = tk.Button(self, text="Giải", command=solve)
        solve_button.pack(pady=100)

class newton1_frame(equationMethodBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp tiếp tuyến")
        
        self.stop_conditions = ["|xₙ - x*| ≤ |f(xₙ)| / m₁", "|xₙ - x*| ≤ M₂ |xₙ - xₙ₋₁|² / 2m₁ "]
        self.selected_stop_condition = ctk.StringVar()
        self.selected_stop_condition.set("|xₙ - x*| ≤ |f(xₙ)| / m₁")
        self.stop_condition_label = ctk.CTkLabel(self,text = "Điều kiện dừng: ")
        self.stop_condition_menu = ctk.CTkOptionMenu(self, values=self.stop_conditions,
                                                     variable=self.selected_stop_condition,
                                                     fg_color="white",
                                                     text_color="black",
                                                     button_color="lightblue",
                                                     button_hover_color="skyblue",
                                                     width=120)
        self.m1_M2_label = ctk.CTkLabel(self)
        self.x_0_label = ctk.CTkLabel(self)
        self.de0_label = ctk.CTkLabel(self)
        
        self.putwidget()
        
        self.stop_condition_label.place(x=443, y =120)
        self.stop_condition_menu.place(x=550, y =120)
 
        def solve(*args):
            self.error_input_label.place_forget()
            self.except_error_label.place_forget()
            self.notice_label.place_forget()
            self.m1_M2_label.place_forget()
            self.x_0_label.place_forget()
            self.de0_label.place_forget()
            self.result_label.place_forget()
            self.tree.destroy()
            self.scrollbar_x.destroy()
            self.scrollbar_y.destroy()

            try:
                expr = sympify(self.f_str.get())
                a = sympify(self.a_str.get())
                b = sympify(self.b_str.get())
                option = self.selected_option.get()
                option_num = sympify(self.option_num_input.get())
                stop_condition = self.selected_stop_condition.get()
    
                if (a >= b or expr.subs("x",a)*expr.subs("x",b)>0 
                or option_num<=0 or (option == "Cho trước số lần lặp" and option_num!=int(option_num))):
                    self.error_input_label.place(x=30, y=250)
                    return
                uu = newton1_oop(a, b, option, option_num, stop_condition, expr)
                de_0, x_0, m1, M2, df, notice, result = uu.Solve()
                df = df.apply(lambda col: col.map(lambda x: float(x)))
                    
                if option == "Sai số tuyệt đối": 
                    self.m1_M2_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₂ = {M2}.")
                    self.x_0_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}")
                    self.de0_label =  ctk.CTkLabel(self, text=f"Điều kiện dừng: eps_0 = {de_0}.")
                if option == "Sai số tương đối": 
                    self.m1_M2_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₂ = {M2}.")
                    self.x_0_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}.")
                    self.de0_label =  ctk.CTkLabel(self, text=f"Điều kiện dừng: delta_0 = {de_0}.")
                if option == "Cho trước số lần lặp": 
                    self.m1_M2_label = ctk.CTkLabel(self, text=f"Giá trị các hệ số : m₁ = {m1}, M₂ = {M2}.")
                    self.x_0_label = ctk.CTkLabel(self, text=f"x_0 = {x_0}.")
                self.notice_label = ctk.CTkLabel(self, text=f"Phương pháp tiếp tuyến kết thúc sau {notice} lần lặp")
                self.result_label = ctk.CTkLabel(self, text=f"Nghiệm x = {float(result)}.")
                self.tree, self.scrollbar_x, self.scrollbar_y = dataframe_to_treeview(df, self)
    
                self.m1_M2_label.place(x=30, y=200)
                self.x_0_label.place(x=30, y=225)
                if option!="Cho trước số lần lặp": self.de0_label.place(x=30, y=250)
                self.notice_label.place(x=30, y=275)
                self.result_label.place(x=30, y=300)
                self.tree.pack(expand=True, fill="x")
                self.scrollbar_x.pack(side="bottom", fill="x")
                self.scrollbar_y.pack(side="right", fill="y")
            except: 
                self.except_error_label.place(x=30, y=250)
                
        solve_button = tk.Button(self, text="Giải", command=solve)
        solve_button.pack(pady=100)

class single_loop1_frame(equationMethodBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp lặp đơn")
        self.f_label = ctk.CTkLabel(self, text = "φ(x) = ")
        self.qde_label = ctk.CTkLabel(self)
        self.not_in = ctk.CTkLabel(self, text = "Miền giá trị không đóng!", text_color = "red")
        self.x_0_str = ctk.StringVar()
        self.x_0_label =ctk.CTkLabel(self,text="x0 = ", font = ("Arial",16))
        self.x_0_intput=ctk.CTkEntry(self,width=60, height=30, textvariable=self.x_0_str)

        self.options = ["Sai số tuyệt đối", "Sai số tương đối", "Cho trước số lần lặp"]
        self.option_menu.configure(values=self.options)
        self.selected_option.set("Sai số tuyệt đối")

        self.putwidget()
        self.x_0_label.place(x=510, y =120)
        self.x_0_intput.place(x=550, y =120)
        
        def solve(*args):
            self.error_input_label.place_forget()
            self.except_error_label.place_forget()
            self.notice_label.place_forget()
            self.result_label.place_forget()
            self.qde_label.place_forget()
            self.not_in.place_forget()
            self.tree.destroy()
            self.scrollbar_x.destroy()
            self.scrollbar_y.destroy()
            try:
                expr = sympify(self.f_str.get())
                a = sympify(self.a_str.get())
                b = sympify(self.b_str.get())
                x_0 = sympify(self.x_0_str.get())
                option = self.selected_option.get()
                option_num = sympify(self.option_num_input.get())
            
                if (a >= b or (option == "Cho trước số lần lặp" and (option_num != int(option_num))) or option_num <= 0 or x_0<a or x_0 >b):
                    self.error_input_label.place(x=30, y=250)
                    return
                for x in np.linspace(float(a),float(b),30):
                    if expr.subs("x", x) < a or expr.subs("x", x) >b:
                        self.not_in.place(x=30, y=250)
                        return
                uu = single_loop1_oop(a, b, x_0, option, option_num, expr)
                df, q, de0, notice, result = uu.Solve()
                df = df.apply(lambda col: col.map(lambda x: float(x)))
    
                if option == "Sai số tuyệt đối":
                    self.qde_label = ctk.CTkLabel(self, text=f"Giá trị: max|φ'(x)| = {float(q)}. Điều kiện dừng: eps_0 = {de0}")
                else:
                    self.qde_label = ctk.CTkLabel(self, text=f"Giá trị: max|φ'(x)| = {float(q)}. Điều kiện dừng: delta_0 = {de0}")
                
                self.notice_label = ctk.CTkLabel(self, text=f"Phương pháp lặp đơn kết thúc sau {notice} lần lặp")
                self.result_label = ctk.CTkLabel(self, text=f"Nghiệm x = {float(result)}")
                self.tree, self.scrollbar_x, self.scrollbar_y = dataframe_to_treeview(df, self)
    
                self.qde_label.place(x=30, y =220)
                self.notice_label.place(x=30, y=250)
                self.result_label.place(x=30, y=280)
                self.tree.pack(expand=True, fill="x")
                self.scrollbar_x.pack(side="bottom", fill="x")
                self.scrollbar_y.pack(side="right", fill="y")
            except:
                self.except_error_label.place(x=30, y=250)

        solve_button = tk.Button(self, text="Giải", command=solve)
        solve_button.pack(pady=100)

#Define form of non-linear system methods frame 
class nonLinearSystemMethodsBaseFrame(baseFrame):
    def __init__(self, root, frame_manager, title):
        super().__init__(root, frame_manager)
        self.title_label = ctk.CTkLabel(self, text = title, font=ctk.CTkFont(size=30, weight="bold"))
        self.setup_navigation_buttons("nonlinear_system_frame")
        self.f_str = [ctk.StringVar() for _ in range(5)]
        self.x_left_str = [ctk.StringVar() for _ in range(5)]
        self.x_right_str = [ctk.StringVar() for _ in range(5)]

        self.f_label = []
        self.x_left_label = []
        self.x_right_label = []
        self.f_input = []
        self.x_left_input = []
        self.x_right_input = []

        self.result_frame = ctk.CTkScrollableFrame(
            master=self,
            height = 400
        )
        
        for i in range(5):
            entry = ctk.CTkEntry(self, textvariable=self.f_str[i], width=400, height=25)
            self.f_input.append(entry)
            
            left_entry = ctk.CTkEntry(self, width=60, height=25, textvariable=self.x_left_str[i])
            self.x_left_input.append(left_entry)

            right_entry = ctk.CTkEntry(self, width=60, height=25, textvariable=self.x_right_str[i])
            self.x_right_input.append(right_entry)

            f_label_i = ctk.CTkLabel(self, text = f"f_{i+1}(X) = ")
            self.f_label.append(f_label_i)

            left_label = ctk.CTkLabel(self, text = f"x{i+1}_left = ")
            self.x_left_label.append(left_label)

            right_label = ctk.CTkLabel(self, text = f"x{i+1}_right = ")
            self.x_right_label.append(right_label)
            
    def putwidget(self,n):
        for i in range(5):
            self.f_input[i].place_forget()
            self.f_label[i].place_forget()
            
            self.x_left_input[i].place_forget()
            self.x_left_label[i].place_forget()
            
            self.x_right_input[i].place_forget()
            self.x_right_label[i].place_forget()
        for i in range(n):
            self.f_input[i].place(x=80, y =110 + i*40)
            self.f_label[i].place(x=15, y=110+i*40)
            
            self.x_left_input[i].place(x=565, y =110 + i*40)
            self.x_left_label[i].place(x=490, y =110 +i*40)
            
            self.x_right_input[i].place(x=720, y =110 + i*40)
            self.x_right_label[i].place(x=640, y =110 +i*40)
        self.root.update_idletasks()

class newton_raphson_frame(nonLinearSystemMethodsBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp Newton Raphson")
        self.number_funtion_str = ctk.StringVar(value="3")

        self.number_funtion_label = ctk.CTkLabel(self, text = "Số phương trình:")
        self.number_funtion_menu = ctk.CTkOptionMenu(self, values=["2","3","4","5"],
                                                     variable=self.number_funtion_str,
                                                     command=self._update_widgets_callback,
                                                     fg_color="white",
                                                     text_color="black",
                                                     button_color="lightblue",
                                                     button_hover_color="skyblue",
                                                     width=120, height = 30)
        self.number_funtion_label.place(x=275, y =70)
        self.number_funtion_menu.place(x=395, y =70)
        self.title_label.pack(pady = 20)
        
        self._update_widgets_callback()

    def _update_widgets_callback(self, choice=None):
        num_functions = int(self.number_funtion_str.get())
        self.putwidget(num_functions)
