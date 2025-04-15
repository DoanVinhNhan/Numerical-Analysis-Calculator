import tkinter as tk
import customtkinter as ctk

# Initialize the application
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Numerical Analysis Calculator")
root.geometry("800x600")
root.resizable(False, False)

# Function to switch frames
def switch_frame(new_frame):
    for widget in root.winfo_children():
        widget.destroy()
    new_frame()

# Main frame
def main_frame():
    label = ctk.CTkLabel(root, text="Máy tính giải tích số", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    source = ctk.CTkLabel(root, text="Source by ĐVN", font=ctk.CTkFont(size=12))
    source.place(x=10, y=565)
    feedback = tk.Button(root, text="Feedback")
    feedback.place(x=700, y=560)
    ctk.CTkButton(root, text="Giải phương trình f(x) = 0", command=lambda: switch_frame(equation_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Giải hệ phi tuyến", command=lambda: switch_frame(nonlinear_system_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Giải hệ phương trình AX = B", command=lambda: switch_frame(matrix_frame), width=400, height=60).place(x=200, y=300)

# Problems frame
def equation_frame():
    label = ctk.CTkLabel(root, text="Giải phương trình", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Chia đôi", command=lambda: switch_frame(bisection_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Dây cung", command=lambda: switch_frame(secant_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Tiếp tuyến", command=lambda: switch_frame(newton1_frame), width=400, height=60).place(x=200, y=300)
    ctk.CTkButton(root, text="Phương pháp Lặp đơn", command=lambda: switch_frame(single1_loop_frame), width=400, height=60).place(x=200, y=400)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

def nonlinear_system_frame():
    label = ctk.CTkLabel(root, text="Giải hệ phi tuyến", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Newton Raphson", command=lambda: switch_frame(newton_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Newton Modified", command=lambda: switch_frame(newton_m_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Lặp đơn", command=lambda: switch_frame(single_loop_frame), width=400, height=60).place(x=200, y=300)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

def matrix_frame():
    label = ctk.CTkLabel(root, text="Giải hệ phương trình AX = B", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Gauss", command=lambda: switch_frame(gauss_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Gauss-Jordan", command=lambda: switch_frame(gauss_jordan_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Phân rã LU", command=lambda: switch_frame(lu_frame), width=400, height=60).place(x=200, y=300)
    ctk.CTkButton(root, text="Phương pháp Cholesky", command=lambda: switch_frame(cholesky_frame), width=400, height=60).place(x=200, y=400)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

# Method frame
def bisection_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Chia đôi", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(equation_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(bisection_frame)).place(x=20, y=560)
    f_input = ctk.CTkEntry(root, width=400, height = 30)
    f_label = ctk.CTkLabel(root, text = "f(x) = ", font = ("Arial",16))
    a_input = ctk.CTkEntry(root, width=60, height = 30)
    a_label = ctk.CTkLabel(root, text = "a = ", font = ("Arial",16))
    b_input = ctk.CTkEntry(root, width=60, height = 30)
    b_label = ctk.CTkLabel(root, text = "b = ", font = ("Arial",16))

    selected_option = ctk.StringVar()
    selected_option.set("Sai số tuyệt đối")
    options_label = ctk.CTkLabel(root, text = "Option:")
    options = ["Sai số tuyệt đối", "Sai số tương đối", "Cho trước số lần lặp"]
    option_menu = ctk.CTkOptionMenu(root,values=options,variable=selected_option,
                                    fg_color="white",
                                    text_color="black",
                                    button_color="lightblue", 
                                    button_hover_color="skyblue")
    eps_label = ctk.CTkLabel(root, text="\u03B5 = ", font = ("Arial", 16))
    eps_input = ctk.CTkEntry(root, width=60, height = 30)
    delta_label = ctk.CTkLabel(root, text="\u03B4 = ", font = ("Arial", 16))
    delta_input = ctk.CTkEntry(root, width=60, height = 30)
    n_label = ctk.CTkLabel(root, text = "n = ", font = ("Arial", 16))
    n_input = ctk.CTkEntry(root, width=60, height = 30)
    
    #Change Option
    def on_option_change(*args):
        # Ẩn và xóa nội dung tất cả các input trước khi hiển thị widget mới
        eps_input.place_forget()
        eps_input.delete(0, "end")  # Xóa nội dung của eps_input
    
        delta_input.place_forget()
        delta_input.delete(0, "end")  # Xóa nội dung của delta_input
    
        n_input.place_forget()
        n_input.delete(0, "end")  # Xóa nội dung của n_input
    
        eps_label.place_forget()
        delta_label.place_forget()
        n_label.place_forget()
        xlabel = 260
        xinput = 300
        yplace = 120
        # Hiển thị widget phù hợp
        if selected_option.get() == "Sai số tuyệt đối":
            eps_label.place(x=xlabel, y=yplace)
            eps_input.place(x=xinput, y=yplace)
        elif selected_option.get() == "Sai số tương đối":
            delta_label.place(x=xlabel, y=yplace)
            delta_input.place(x=xinput, y=yplace)
        else:
            n_label.place(x=xlabel, y=yplace)
            n_input.place(x=xinput, y=yplace)
    
        f_label.place(x=30, y = 70)
        f_input.place(x=80, y = 70)
        a_label.place(x=510, y = 70)
        a_input.place(x=550, y = 70)
        b_label.place(x=630, y =70)
        b_input.place(x=670, y =70)
            
    options_label.place(x = 30, y = 120)
    option_menu.place(x = 80, y = 120)
    selected_option.trace("w", on_option_change)
    on_option_change()

def secant_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Dây cung", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(equation_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(secant_frame)).place(x=20, y=560)

def newton1_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Tiếp tuyến", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(equation_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(newton1_frame)).place(x=20, y=560)

def single1_loop_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Lặp đơn", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(equation_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(single1_loop_frame)).place(x=20, y=560)

def newton_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Newton Raphson", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(nonlinear_system_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(newton_frame)).place(x=20, y=560)

def newton_m_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Newton Modify", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(nonlinear_system_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(newton_m_frame)).place(x=20, y=560)

def single_loop_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Lặp đơn", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(nonlinear_system_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(single_loop_frame)).place(x=20, y=560)

def gauss_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Gauss", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(matrix_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(gauss_frame)).place(x=20, y=560)

def gauss_jordan_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Gauss Jordan", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(matrix_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(gauss_jordan_frame)).place(x=20, y=560)

def lu_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Phân rã LU", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(matrix_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(lu_frame)).place(x=20, y=560)

def cholesky_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Cholesky", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    tk.Button(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    tk.Button(root, text="Quay lại", command=lambda: switch_frame(matrix_frame)).place(x=600, y=560)
    tk.Button(root, text="Reset", command=lambda: switch_frame(cholesky_frame)).place(x=20, y=560)


# Initialize with the main frame
main_frame()

# Start the main event loop
root.mainloop()
