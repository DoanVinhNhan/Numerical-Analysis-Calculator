import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from sympy import *
import pandas as pd
from equation_solving_method.Bisection import bisection_oop

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
        ctk.CTkButton(self, text="Phương pháp dây cung", width=400, height=60).place(x=200, y=200)
        ctk.CTkButton(self, text="Phương pháp tiếp tuyến", width=400, height=60).place(x=200, y=300)
        ctk.CTkButton(self, text="Phương pháp lặp đơn", width=400, height=60).place(x=200, y=400)
class nonlinear_system_frame(baseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager)
        self.setup_navigation_buttons("main_frame")
        label = ctk.CTkLabel(self, text="Giải hệ phi tuyến", font=ctk.CTkFont(size=30, weight="bold"))
        label.pack(pady=20)

        ctk.CTkButton(self, text="Phương pháp Newton Raphson", width=400, height=60).place(x=200, y=100)
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

        self.notice_label = tk.Label(self)
        self.result_label = tk.Label(self)
        self.except_error_label = ctk.CTkLabel(self, text="Lỗi!", text_color="red")
        self.error_input_label = ctk.CTkLabel(self, text="Đầu vào không hợp lệ", text_color="red")
        
        self.tree = ttk.Treeview(self)
        self.scrollbar_x = tk.Scrollbar(self)
        self.scrollbar_y = tk.Scrollbar(self)
        
class bisection_frame(equationMethodBaseFrame):
    def __init__(self, root, frame_manager):
        super().__init__(root, frame_manager, "Phương pháp chia đôi")

        self.options = ["Sai số tuyệt đối", "Sai số tương đối", "Cho trước số lần lặp"]
        self.option_menu.configure(values=self.options)
        self.selected_option.set("Sai số tuyệt đối")
        
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

        def on_option_change(*args):
            self.option_input.delete(0, "end")

            self.eps_label.place_forget()
            self.delta_label.place_forget()
            self.n_label.place_forget()

            if self.selected_option.get() == "Sai số tuyệt đối":
                self.eps_label.place(x=260, y=120)
            elif self.selected_option.get() == "Sai số tương đối":
                self.delta_label.place(x=260, y=120)
            else:
                self.n_label.place(x=260, y=120)
            self.option_input.place(x=300, y=120)
        self.selected_option.trace("w", on_option_change)
        on_option_change()
        
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
            
                if a >= b or f(a) * f(b) > 0 or (option == "Cho trước số lần lặp" and (option_num != int(option_num) or option_num <= 0)):
                    self.error_input_label.place(x=30, y=250)
                    return
                uu = bisection_oop(a, b, option, option_num, f)
                df, notice, result = uu.Solve()
                df = df.apply(lambda col: col.map(lambda x: float(x)))
                    
                self.notice_label = ctk.CTkLabel(self, text=f"Phương pháp Chia đôi kết thúc sau {notice} lần lặp")
                self.result_label = ctk.CTkLabel(self, text=f"Nghiệm x = {float(result)}")
                self.tree, self.scrollbar_x, self.scrollbar_y = dataframe_to_treeview(df, self)
            
                self.notice_label.place(x=30, y=250)
                self.result_label.place(x=30, y=280)
                self.tree.pack(expand=True, fill="x")
                self.scrollbar_x.pack(side="bottom", fill="x")
                self.scrollbar_y.pack(side="right", fill="y")
            except:
                self.except_error_label.place(x=30, y=250)
        
        on_option_change()
        solve_button = tk.Button(self, text="Giải", command=solve)
        solve_button.pack(pady=100)
        
        def reset_fields():
            self.f_str.set("")
            self.a_str.set("")
            self.b_str.set("")
            self.option_num_input.set("")
            self.error_input_label.place_forget()
            self.except_error_label.place_forget()
            self.notice_label.place_forget()
            self.result_label.place_forget()
            self.tree.destroy()
            self.scrollbar_x.destroy()
            self.scrollbar_y.destroy()

        reset_button = tk.Button(self, text="Reset", command=reset_fields)
        reset_button.place(x=20, y =560)


        
